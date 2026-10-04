from itertools import combinations
from fractions import Fraction
from functools import lru_cache
import math

N=12
ZERO=(Fraction(0),)*4
ONE=(Fraction(1),Fraction(0),Fraction(0),Fraction(0))
ZETA=(Fraction(0),Fraction(1),Fraction(0),Fraction(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def mul(a,b):
    c=[Fraction(0) for _ in range(7)]
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: c[i+j]+=x*y
    for d in range(6,3,-1):
        x=c[d]
        if x:
            c[d]=0
            c[d-2]+=x
            c[d-4]-=x
    return tuple(c[:4])

@lru_cache(None)
def inv(a):
    if a==ZERO: raise ZeroDivisionError
    basis=[ONE,ZETA,mul(ZETA,ZETA),mul(mul(ZETA,ZETA),ZETA)]
    M=[[mul(a,basis[j])[i] for j in range(4)] for i in range(4)]
    aug=[M[i]+[Fraction(1 if i==0 else 0)] for i in range(4)]
    r=0
    for c in range(4):
        piv=next(i for i in range(r,4) if aug[i][c])
        aug[r],aug[piv]=aug[piv],aug[r]
        q=aug[r][c]
        aug[r]=[x/q for x in aug[r]]
        for i in range(4):
            if i!=r and aug[i][c]:
                q=aug[i][c]
                aug[i]=[aug[i][j]-q*aug[r][j] for j in range(5)]
        r+=1
    return tuple(aug[i][4] for i in range(4))

ZP=[ONE]
for _ in range(1,12): ZP.append(mul(ZP[-1],ZETA))
assert mul(ZP[11],ZETA)==ONE

def rref_exact(rows,cols):
    A=[[ZP[(r*c)%12] for c in cols] for r in rows]
    m=len(A); n=len(cols); rr=0; pivots=[]
    for cc in range(n):
        piv=next((i for i in range(rr,m) if A[i][cc]!=ZERO),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        iv=inv(A[rr][cc])
        A[rr]=[mul(x,iv) for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][cc]!=ZERO:
                fac=A[i][cc]
                A[i]=[sub(A[i][j],mul(fac,A[rr][j])) for j in range(n)]
        pivots.append(cc); rr+=1
        if rr==m: break
    return rr,pivots,A

def has_full_support_kernel_exact(rows,cols):
    rank,piv,A=rref_exact(rows,cols)
    n=len(cols)
    if rank==n: return False,rank
    free=[j for j in range(n) if j not in piv]
    coord_possible=[False]*n
    for f in free:
        coord_possible[f]=True
        for ri,p in enumerate(piv):
            if A[ri][f]!=ZERO: coord_possible[p]=True
    return all(coord_possible),rank

def primitive_root12_mod(p):
    for g in range(2,p):
        if pow(g,12,p)==1 and pow(g,6,p)!=1 and pow(g,4,p)!=1:
            return g
    raise RuntimeError

def rank_mod(rows,cols,p,w):
    A=[[pow(w,(r*c)%12,p) for c in cols] for r in rows]
    m=len(A); n=len(cols); rr=0
    for cc in range(n):
        piv=next((i for i in range(rr,m) if A[i][cc]%p),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        iv=pow(A[rr][cc],p-2,p)
        for j in range(cc,n): A[rr][j]=(A[rr][j]*iv)%p
        for i in range(rr+1,m):
            if A[i][cc]%p:
                q=A[i][cc]
                for j in range(cc,n): A[i][j]=(A[i][j]-q*A[rr][j])%p
        rr+=1
        if rr==n: break
    return rr

PRIMES=(13,37,61)
ROOTS={p:primitive_root12_mod(p) for p in PRIMES}

def certify_no_exact_support_with_fourier_at_most3(k):
    total=0; ambiguous=[]
    for S in combinations(range(12),k):
        for Zrows in combinations(range(12),9):
            total+=1
            full=False
            for p in PRIMES:
                if rank_mod(Zrows,S,p,ROOTS[p])==k:
                    full=True; break
            if not full: ambiguous.append((S,Zrows))
    exact_rank_counts={}
    for S,Zrows in ambiguous:
        ok,r=has_full_support_kernel_exact(Zrows,S)
        if ok:
            raise AssertionError((k,S,Zrows,r))
        exact_rank_counts[r]=exact_rank_counts.get(r,0)+1
    return total,len(ambiguous),exact_rank_counts

def ft_of_sparse(S,coeffs):
    out=[]
    for r in range(12):
        s=ZERO
        for c,a in zip(S,coeffs): s=add(s,mul(a,ZP[(r*c)%12]))
        out.append(s)
    return out

def support_count(v): return sum(x!=ZERO for x in v)

def E(a,b,c,d): return (Fraction(a),Fraction(b),Fraction(c),Fraction(d))

# Explicit witnesses for exact support k and claimed Fourier support mu(k).
witnesses={
1: ((0,), [ONE]),
2: ((0,6), [ONE,ONE]),
3: ((0,4,8), [ONE,ONE,ONE]),
4: ((0,3,6,9), [ONE,ONE,ONE,ONE]),
5: ((0,2,4,6,8), [E(1,0,0,0),E(-1,0,2,0),E(-2,0,0,0),E(1,0,-2,0),E(1,0,0,0)]),
6: ((1,3,5,7,9,11), [ONE]*6),
7: ((0,1,2,5,6,8,9), [E(1,2,-2,-1),E(0,0,4,0),E(-1,-1,-1,2),E(-2,0,2,0),E(1,-2,-2,1),E(-1,1,-1,-2),E(2,0,0,0)]),
}
# For k=8..11 use inverse transform of two frequencies 0,d: f(x)=1-zeta^{-d x}.
for k,d in [(8,4),(9,3),(10,2),(11,1)]:
    S=[]; C=[]
    for x in range(12):
        a=sub(ONE,ZP[(-d*x)%12])
        if a!=ZERO: S.append(x); C.append(a)
    witnesses[k]=(tuple(S),C)
witnesses[12]=(tuple(range(12)),[ONE]*12)

MU=[None,12,6,4,3,4,2,4,2,2,2,2,1]
for k in range(1,13):
    S,C=witnesses[k]
    assert len(S)==k and all(a!=ZERO for a in C)
    out=ft_of_sparse(S,C)
    assert support_count(out)==MU[k], (k,support_count(out))

# Delvaux--Van Barel Hamming/Meshulam profile for <=k, computed from Theorem 20 candidates.
def isprime(p): return p>=2 and all(p%q for q in range(2,int(p**0.5)+1))
def hamming(n,l):
    vals=[]
    for d in range(1,n+1):
        if n%d: continue
        for p in range(2,n+1):
            if not isprime(p) or n%(p*d): continue
            for c in range(1,p+1):
                if c*d<=l: vals.append((p+1-c)*n//(p*d))
    if l>=n: vals.append(1)
    return min(vals)
THETA=[None]+[hamming(12,k) for k in range(1,13)]
assert THETA[1:]==[12,6,4,3,3,2,2,2,2,2,2,1]
for k in range(1,13): assert MU[k]>=THETA[k]

c5=certify_no_exact_support_with_fourier_at_most3(5)
c7=certify_no_exact_support_with_fourier_at_most3(7)
assert c5==(174240,96,{4:96}), c5
assert c7==(174240,1680,{6:1680}), c7
print('MU',MU[1:])
print('THETA',THETA[1:])
print('k=5 exhaustive',c5)
print('k=7 exhaustive',c7)
print('VERIFY_OK')
