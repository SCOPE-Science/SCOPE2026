from itertools import product
from math import comb

class PrimeField:
    def __init__(self,p): self.q=p
    def add(self,a,b): return (a+b)%self.q
    def sub(self,a,b): return (a-b)%self.q
    def mul(self,a,b): return (a*b)%self.q
    def inv(self,a):
        assert a%self.q
        return pow(a,self.q-2,self.q)

class GF4:
    # F2[a]/(a^2+a+1), elements low-bit + high-bit*a.
    q=4
    def add(self,x,y): return x^y
    sub=add
    def mul(self,x,y):
        a0,a1=x&1,(x>>1)&1
        b0,b1=y&1,(y>>1)&1
        c0=(a0*b0) ^ (a1*b1)       # a^2 = a+1 contributes to constant
        c1=(a0*b1) ^ (a1*b0) ^ (a1*b1)
        return c0 | (c1<<1)
    def inv(self,x):
        assert x
        for y in range(1,4):
            if self.mul(x,y)==1: return y
        raise AssertionError

def rank(M,F):
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]!=0),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=F.inv(A[r][c])
        A[r]=[F.mul(z,x) for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                t=A[i][c]
                A[i]=[F.sub(A[i][j],F.mul(t,A[r][j])) for j in range(n)]
        r+=1
        if r==m: break
    return r

def mm(A,B,F):
    n=len(A)
    return [[sum_field((F.mul(A[i][k],B[k][j]) for k in range(n)),F) for j in range(n)] for i in range(n)]

def sum_field(vals,F):
    s=0
    for v in vals: s=F.add(s,v)
    return s

def upper_from_tuple(n,t):
    A=[[0]*n for _ in range(n)]
    k=0
    for i in range(n):
        for j in range(i,n):
            A[i][j]=t[k]; k+=1
    return A

def formula(n,r,q):
    return comb(n,r)*(q-1)**r*q**(n*(n-1)//2-(n-r)*(n-r-1)//2)

def check_field(F,max_n):
    q=F.q
    out=[]
    for n in range(1,max_n+1):
        counts=[0]*(n+1)
        for t in product(range(q), repeat=n*(n+1)//2):
            A=upper_from_tuple(n,t)
            r=rank(A,F)
            if rank(mm(A,A,F),F)==r:
                counts[r]+=1
        expect=[formula(n,r,q) for r in range(n+1)]
        assert counts==expect,(q,n,counts,expect)
        out.append((n,counts))
    return out

def check_pattern_formula(q,nmax=12):
    # Recurrences for a fixed zero/nonzero diagonal pattern imply dependence only on k.
    f={(0,0):1}
    for n in range(1,nmax+1):
        for k in range(n+1):
            # closed form; verify both possible terminal recurrences when applicable
            val=q**(n*(n-1)//2-k*(k-1)//2)
            if k<=n-1:
                assert val==q**(n-1)*q**((n-1)*(n-2)//2-k*(k-1)//2)
            if k>=1:
                assert val==q**(n-k)*q**((n-1)*(n-2)//2-(k-1)*(k-2)//2)
            f[(n,k)]=val
    return True

checks=[]
checks += [(2,x) for x in check_field(PrimeField(2),5)]
checks += [(3,x) for x in check_field(PrimeField(3),4)]
checks += [(4,x) for x in check_field(GF4(),3)]
checks += [(5,x) for x in check_field(PrimeField(5),3)]
for q in (2,3,4,5,7,11): check_pattern_formula(q)
print('VERIFY_OK')
for q,(n,counts) in checks:
    print(f'q={q} n={n} counts={counts}')
