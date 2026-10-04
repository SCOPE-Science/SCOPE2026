from itertools import product
from math import comb

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q
    def add(self,a,b):
        return a ^ b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        if self.q in (2,4):
            return a
        return (-a)%self.q
    def sub(self,a,b):
        return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:
            return (a*b)%self.q
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0 | (c1<<1)
    def inv(self,a):
        assert a!=0
        for b in range(1,self.q):
            if self.mul(a,b)==1:
                return b
        raise AssertionError

def rank(F,A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]!=0),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        inv=F.inv(A[r][c])
        A[r]=[F.mul(inv,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                a=A[i][c]
                A[i]=[F.sub(x,F.mul(a,y)) for x,y in zip(A[i],A[r])]
        r+=1
        if r==m:
            break
    return r

def cycle_matrix(F,n,y):
    A=[[0]*n for _ in range(n)]
    for i,w in enumerate(y):
        j=(i+1)%n
        A[i][j]=F.add(A[i][j],w)
        A[j][i]=F.add(A[j][i],F.neg(w))
    return A

def Acoef(n,j):
    return n*comb(n-j,j)//(n-j)

def predicted(n,q):
    Q=q*(q-1)
    m=n//2
    rho={}
    if n%2:
        for i in range(m):
            rho[i]=Acoef(n,i)*(Q**i)
        rho[m]=Acoef(n,m)*(Q**m)+(q-1)**n
    else:
        for i in range(m-1):
            rho[i]=Acoef(n,i)*(Q**i)
        rho[m-1]=Acoef(n,m-1)*(Q**(m-1))+(q-1)**(n-1)
        rho[m]=2*(Q**m)-q*(q-1)**(n-1)
    return [rho.get(i,0) for i in range(m+1)]

def brute(n,q):
    F=Field(q)
    counts=[0]*(n//2+1)
    for y in product(range(q),repeat=n):
        r=rank(F,cycle_matrix(F,n,y))
        assert r%2==0
        counts[r//2]+=1
    return counts

cases=[(5,2),(5,3),(6,3),(7,3),(8,2),(6,4),(5,5)]
expected_vectors={
    (5,2):[1,10,21],
    (5,3):[1,30,212],
    (6,3):[1,36,356,336],
    (7,3):[1,42,504,1640],
    (8,2):[1,16,80,129,30],
    (6,4):[1,72,1539,2484],
    (5,5):[1,100,3024],
}

for n,q in cases:
    b=brute(n,q)
    p=predicted(n,q)
    assert b==p==(expected_vectors[(n,q)]), (n,q,b,p)
    assert sum(b)==q**n
    if q%2==1:
        # ch_i = q^(n-2i) rho_i, and sum ch_i*(q^i)^2 = |G| = q^(2n)
        chars=[q**(n-2*i)*b[i] for i in range(len(b))]
        assert sum(chars[i]*(q**i)**2 for i in range(len(chars)))==q**(2*n)
    print((n,q),b)

# Check Lucas coefficient recurrence symbolically as coefficient lists for n<=12.
Qtag=7
L0=[2]
L1=[1]
def add_poly(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return c
def shift_scale(a,c):
    return [0]+[c*x for x in a]
Ls=[L0,L1]
for n in range(2,13):
    Ls.append(add_poly(Ls[-1],shift_scale(Ls[-2],Qtag)))
for n in range(1,13):
    explicit=[Acoef(n,j)*(Qtag**j) for j in range(n//2+1)]
    assert Ls[n]==explicit,(n,Ls[n],explicit)

print("VERIFY_OK")
