"""Exact finite-field crosschecks for the binomial Artin--Schreier bound.
Run: python verify.py. No third-party dependencies.
"""
from math import gcd

class F:
    def __init__(self,k,coeffs):
        self.k=k; self.mod=coeffs; self.q=3**k
    def vec(self,x):
        v=[]
        for _ in range(self.k):v.append(x%3);x//=3
        return v
    def fromvec(self,v):
        return sum((a%3)*3**i for i,a in enumerate(v))
    def add(self,a,b):return self.fromvec([(x+y)%3 for x,y in zip(self.vec(a),self.vec(b))])
    def neg(self,a):return self.fromvec([-x for x in self.vec(a)])
    def mul(self,a,b):
        av=self.vec(a);bv=self.vec(b);arr=[0]*(2*self.k-1)
        for i,u in enumerate(av):
            for j,v in enumerate(bv):arr[i+j]+=u*v
        for i in range(2*self.k-2,self.k-1,-1):
            coeff=arr[i]%3
            for j,c in enumerate(self.mod):arr[i-self.k+j]-=coeff*c
        return self.fromvec(arr[:self.k])
    def power(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n>>=1
        return out
    def frob(self,x,h):
        for _ in range(h):x=self.power(x,3)
        return x
    def trace(self,x):
        total=0
        for _ in range(self.k):total=self.add(total,x);x=self.frob(x,1)
        assert total<3
        return total

def rank(M):
    arr=[list(row) for row in M];n=len(arr);m=len(arr[0]);i=0
    for j in range(m):
        piv=next((r for r in range(i,n) if arr[r][j]%3),None)
        if piv is None:continue
        arr[i],arr[piv]=arr[piv],arr[i]
        d=pow(arr[i][j],-1,3)
        arr[i]=[(x*d)%3 for x in arr[i]]
        for r in range(n):
            if r!=i:
                a=arr[r][j]
                arr[r]=[(x-a*y)%3 for x,y in zip(arr[r],arr[i])]
        i+=1
        if i==n:break
    return i

def check(k,h,a,b,full_count=False):
    poly={6:[2,1,0,1,0,0],8:[1,2,2,1,0,0,0,0],10:[2,1,0,1,0,0,0,0,0,0]}[k]
    Fld=F(k,poly); assert k%2==0 and 1<=h<=k//2 and a*b!=0
    # radical equation L(x) = a*x^(3^h) + a^(3^(k-h))*x^(3^(k-h))+2b*x
    a_dual=Fld.frob(a,k-h)
    def L(x):
        z=Fld.mul(a,Fld.frob(x,h))
        z=Fld.add(z,Fld.mul(a_dual,Fld.frob(x,k-h)))
        z=Fld.add(z,Fld.mul(Fld.add(b,b),x))
        return z
    cols=[Fld.vec(L(3**i)) for i in range(k)]
    r=k-rank([[cols[j][i] for j in range(k)] for i in range(k)])
    d=gcd(h,k)
    assert r<=2*d,(k,h,a,b,r,d)
    if full_count:
        zeros=0
        for x in range(Fld.q):
            quad=Fld.add(Fld.mul(a,Fld.mul(x,Fld.frob(x,h))), Fld.mul(b,Fld.mul(x,x)))
            if Fld.trace(quad)==0:zeros+=1
        N=1+3*zeros; delta=abs(N-(Fld.q+1))
        assert delta<=2*3**(k//2+d),(k,h,a,b,N,delta)
        print('q=%d h=%d a=%d b=%d radical_dim=%d gcd=%d point_count=%d delta=%d bound=%d'%(Fld.q,h,a,b,r,d,N,delta,2*3**(k//2+d)))
    else:
        print('q=%d h=%d a=%d b=%d radical_dim=%d gcd=%d radical_bound=%d'%(Fld.q,h,a,b,r,d,2*d))
    return r

if __name__=='__main__':
    check(6,2,1,1,True)
    check(8,3,1,1,True)
    check(8,3,1,2,True)
    check(10,4,1,1)
    check(10,4,2,1)
    print('VERIFY_OK binomial_artin_schreier_exact_finite_field_rank_and_points')
