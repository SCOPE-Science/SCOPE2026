#!/usr/bin/env python3
"""Exact finite-field checks for a characteristic-five genus-four family.

Uses only the Python standard library. The polynomial and Cartier proofs
are provided separately in the accompanying mathematical note.
"""
from itertools import product

P = 5


def coeff_matrix():
    # Sparse expansion of (x^10+x^7+a*x^4+b*x)^2 over F_5[a,b,x].
    terms = [(10, 0, 0, 1), (7, 0, 0, 1), (4, 1, 0, 1), (1, 0, 1, 1)]
    coeffs = {}
    for e, a, b, c in terms:
        for f, d, h, v in terms:
            key = (e + f, a + d, b + h)
            coeffs[key] = (coeffs.get(key, 0) + c * v) % 5
    def at(k):
        return { (a,b):v for (e,a,b),v in coeffs.items() if e==k and v }
    M = [[at(5*i-j) for j in range(1,5)] for i in range(1,5)]
    zero, one, two = {}, {(0,0):1}, {(0,0):2}
    expect = [
        [zero,zero,{(0,2):1},zero],
        [zero,{(2,0):1,(0,1):2},zero,zero],
        [{(1,0):2,(0,0):1},zero,zero,{(1,0):2,(0,1):2}],
        [zero,zero,two,zero],
    ]
    assert M == expect, (M,expect)
    return M


def rank(mat):
    A = [[x % 5 for x in row] for row in mat]
    n,m = len(A),len(A[0]);r=0
    for j in range(m):
        pivot = next((i for i in range(r,n) if A[i][j]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        u=pow(A[r][j],-1,5)
        A[r]=[(z*u)%5 for z in A[r]]
        for i in range(n):
            if i!=r and A[i][j]:
                t=A[i][j]
                A[i]=[(A[i][k]-t*A[r][k])%5 for k in range(m)]
        r+=1
    return r


def mmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%5
             for j in range(len(B[0]))] for i in range(len(A))]


def check_small_base_field():
    observed={(i,j):0 for i in (0,1) for j in (0,1)}
    for a,b in product(range(5),repeat=2):
        delta=(-4*a**3+a*a+18*a*b-27*b*b-4*b)%5
        if b==0 or delta==0: continue
        h=(a*a+2*b)%5
        d=(b*b*(2*pow(a,5,5)+1)+4*pow(a,5,5)+4*pow(b,5,5))%5
        M=[[0,0,b*b%5,0], [0,h,0,0], [(2*a+1)%5,0,0,2*(a+b)%5],
           [0,0,2,0]]
        expected_a=1+(h==0)
        expected_rank=(h!=0)+2*(d!=0)
        assert rank(M)==4-expected_a
        stable=M
        for _ in range(3):stable=mmul(stable,M)
        assert rank(stable)==expected_rank, (a,b,expected_rank,rank(stable))
        observed[(h==0,d==0)]+=1
    assert observed=={(0,0):12,(0,1):2,(1,0):2,(1,1):1},observed
    print('F5_PARAMETER_CENSUS',observed)


def remainder(f,g):
    arr=list(f)
    while len(arr)>1 and arr[-1]%5==0:arr.pop()
    while len(arr)>=len(g) and any(arr):
        c=arr[-1]*pow(g[-1],-1,5)%5
        offset=len(arr)-len(g)
        for i,b in enumerate(g):arr[offset+i]=(arr[offset+i]-c*b)%5
        while arr and arr[-1]==0:arr.pop()
    return arr or [0]


def irreducible(poly):
    n=len(poly)-1
    for degree in range(1,n//2+1):
        for c in product(range(5),repeat=degree):
            if remainder(poly,list(c)+[1]) == [0]: return False
    return True


class Field:
    def __init__(self,n,poly):
        self.n,self.poly=n,poly
        assert len(poly)==n+1 and poly[-1]==1 and (n==1 or irreducible(poly))
        self.q=5**n
        self.digits=[]
        for x in range(self.q):
            ds=[]
            for _ in range(n):ds.append(x%5);x//=5
            self.digits.append(ds)
    def encode(self,ds):return sum((v%5)*5**j for j,v in enumerate(ds))
    def add(self,a,b):
        return self.encode([(self.digits[a][i]+self.digits[b][i])%5 for i in range(self.n)])
    def mul(self,a,b):
        if self.n==1:return a*b%5
        ds,dt=self.digits[a],self.digits[b]
        c=[0]*(2*self.n-1)
        for i in range(self.n):
            for j in range(self.n):c[i+j]+=ds[i]*dt[j]
        for k in range(2*self.n-2,self.n-1,-1):
            val=c[k]%5
            for j in range(self.n): c[k-self.n+j]-=val*self.poly[j]
        return self.encode(c[:self.n])
    def exp(self,a,n):
        y=1
        while n:
            if n&1:y=self.mul(y,a)
            a=self.mul(a,a);n>>=1
        return y


def count_curve(n,mod):
    K=Field(n,mod)
    count=2  # Two F_(5^n)-rational points above infinity: monic degree ten.
    for x in range(K.q):
        x2=K.mul(x,x)
        x3=K.mul(x2,x)
        x4=K.mul(x2,x2)
        x7=K.mul(x3,x4)
        x10=K.mul(x3,x7)
        fx=K.add(K.add(x10,x7),K.add(K.mul(4,x4),K.mul(2,x)))
        count+=1 if fx==0 else 2 if K.exp(fx,(K.q-1)//2)==1 else 0
    return count


def convolution(f,g):
    a=[0]*(len(f)+len(g)-1)
    for i,v in enumerate(f):
        for j,w in enumerate(g):a[i+j]+=v*w
    return a


def main():
    coeff_matrix()
    check_small_base_field()
    mods={1:[0,1],2:[2,0,1],3:[1,1,0,1],4:[1,1,1,0,1]}
    observed=[]
    for n in range(1,5):
        N=count_curve(n,mods[n]); observed.append(N)
    assert observed==[6,36,126,576], observed
    q=5
    traces=[None]+[q**i+1-observed[i-1] for i in range(1,5)]
    coeff=[1]
    for n in range(1,5):
        numerator=-sum(coeff[n-i]*traces[i] for i in range(1,n+1))
        assert numerator%n==0
        coeff.append(numerator//n)
    coeff+= [q*coeff[3],q**2*coeff[2],q**3*coeff[1],q**4*coeff[0]]
    assert coeff==[1,0,5,0,0,0,125,0,625],coeff
    p1=convolution([1,0,5],[1,0,5])
    p2=[1,0,-5,0,25]
    assert convolution(p1,p2)==coeff
    print('POINT_COUNTS_F5_TO_F625',observed)
    print('ZETA_NUMERATOR_COEFFICIENTS',coeff)
    print('VERIFY_OK')


if __name__=='__main__':main()
