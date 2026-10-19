#!/usr/bin/env python3
"""Direct finite-field matrix enumeration for cross-checking a general formula."""
from collections import Counter
from itertools import product

class Field:
    def __init__(self,q):
        assert q in (2,3,4,5)
        self.q=q; self.p=2 if q==4 else q
    def add(self,a,b):
        return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):
        return a if self.q==4 else (-a)%self.q
    def mul(self,a,b):
        if self.q!=4:return a*b%self.q
        r=0
        while b:
            if b&1:r^=a
            b>>=1; a<<=1
            if a&4:a^=7
        return r
    def inv(self,a):
        assert a
        for b in range(1,self.q):
            if self.mul(a,b)==1:return b
        raise ValueError('no inverse')

def rank(M,n,F):
    rows=[list(M[i*n:(i+1)*n]) for i in range(n)]
    pivot=0
    for j in range(n):
        i=next((i for i in range(pivot,n) if rows[i][j]),None)
        if i is None:continue
        rows[i],rows[pivot]=rows[pivot],rows[i]
        inv=F.inv(rows[pivot][j]); rows[pivot]=[F.mul(inv,v) for v in rows[pivot]]
        for i in range(n):
            if i==pivot or not rows[i][j]:continue
            t=rows[i][j]
            rows[i]=[F.add(v,F.neg(F.mul(t,w))) for v,w in zip(rows[i],rows[pivot])]
        pivot+=1
        if pivot==n:break
    return pivot

def mulmat(A,B,n,F):
    return tuple(sumfield((F.mul(A[i*n+k],B[k*n+j]) for k in range(n)),F) for i in range(n) for j in range(n))

def sumfield(elems,F):
    ans=0
    for x in elems:ans=F.add(ans,x)
    return ans

def vec_mat(M,v,n,F):
    return tuple(sumfield((F.mul(M[i*n+j],v[j]) for j in range(n)),F) for i in range(n))

def projective(V,F):
    pts=set()
    for v in V:
        if not any(v):continue
        j=next(i for i,a in enumerate(v) if a)
        t=F.inv(v[j]); pts.add(tuple(F.mul(t,x) for x in v))
    return pts

def nilpotent_rank_one(n,F):
    V=list(product(range(F.q),repeat=n)); M=set()
    for u in V:
        if not any(u):continue
        for phi in V:
            if not any(phi):continue
            if sumfield((F.mul(a,b) for a,b in zip(u,phi)),F):continue
            M.add(tuple(F.mul(u[i],phi[j]) for i in range(n) for j in range(n)))
    return sorted(M)

def predicted(S,n,F):
    r=rank(S,n,F)
    H=(F.q**n-1)*(F.q**(n-1)-1)//(F.q-1)
    if r==0:return H
    tr=sumfield((S[i*n+i] for i in range(n)),F)
    if tr:return 0
    if r==1:return 2*F.q**(n-1)-F.q-2
    if r>2:return 0
    S2=mulmat(S,S,n,F); r2=rank(S2,n,F)
    if r2==0:return F.q*(F.q+1)
    if r2==1:return 2*F.q
    if r2!=2:return 0
    # Count invariant projective lines within the two-dimensional image of S.
    W=[]
    cols=[tuple(S[i*n+j] for i in range(n)) for j in range(n)]
    for v in product(range(F.q),repeat=n):
        W.append(tuple(sumfield((F.mul(v[j],cols[j][i]) for j in range(n)),F) for i in range(n)))
    pts=projective(set(W),F); e=0
    for v in pts:
        Sv=vec_mat(S,v,n,F)
        if not any(Sv): continue
        j=next(j for j,t in enumerate(v) if t)
        lam=Sv[j]
        if all(Sv[i]==F.mul(lam,v[i]) for i in range(n)):e+=1
    return F.q+1-e

def test(n,q):
    F=Field(q); M=nilpotent_rank_one(n,F)
    H=(q**n-1)*(q**(n-1)-1)//(q-1)
    assert len(M)==H,(n,q,len(M),H)
    counts=Counter()
    for idx,A in enumerate(M):
        for B in M:
            S=tuple(F.add(x,y) for x,y in zip(A,B))
            counts[S]+=1
    # Check ALL possible n*n targets, not only reachable ones where feasible.
    if q**(n*n)<=500000:
        allS=product(range(q),repeat=n*n)
    else:
        allS=counts.keys()
    tested=0; examples=Counter()
    for S in allS:
        observed=counts[S]; expect=predicted(S,n,F)
        assert observed==expect,(n,q,S,observed,expect)
        if observed: examples[(rank(S,n,F),rank(mulmat(S,S,n,F),n,F))]+=1
        tested+=1
    assert sum(counts.values())==H**2
    print(f'PASS n={n} q={q} minimal_orbit={H} pairs={H**2} targets_tested={tested} nonzero_fibers={len(counts)} classes={dict(sorted(examples.items()))}',flush=True)

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)]:test(n,q)
    print('ALL_EXACT_CHECKS_PASSED')
