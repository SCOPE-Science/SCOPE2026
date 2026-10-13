"""Finite Heyting-chain power generation: independent direct closure and exact census."""
from itertools import product
from math import comb, factorial

def implication(a,b,k):
    return k-1 if a<=b else b

def generated(k,n,generators):
    zero=(0,)*n; one=(k-1,)*n
    seen={zero,one,*generators}
    while True:
        before=len(seen)
        items=list(seen)
        for a in items:
            for b in items:
                seen.add(tuple(min(x,y) for x,y in zip(a,b)))
                seen.add(tuple(max(x,y) for x,y in zip(a,b)))
                seen.add(tuple(implication(x,y,k) for x,y in zip(a,b)))
        if len(seen)==before:
            return len(seen)==k**n

def criterion(k,n,generators):
    sig=[]
    for i in range(n):
        vals=[g[i] for g in generators]
        if not set(range(1,k-1)).issubset(vals): return False
        sig.append(tuple(x>0 for x in vals))
    return len(set(sig))==n

def predicted(k,n,r):
    # coefficient of z^n in prod_{s=0}^r(1+z h_s)^C(r,s)
    coeff=[1]+[0]*n
    for s in range(r+1):
        h=sum((-1)**j*comb(k-2,j)*(k-1-j)**s for j in range(k-1))
        for _ in range(comb(r,s)):
            for t in range(n,0,-1): coeff[t]+=h*coeff[t-1]
    return factorial(n)*coeff[n]

def rmin(k,n):
    for r in range(24):
        admissible=sum(comb(r,s) for s in range(k-2,r+1))
        if admissible>=n: return r
    raise RuntimeError

cases=0; tested=0
for k,n,max_r in [(2,1,4),(2,2,4),(2,3,3),(3,1,3),(3,2,3),(3,3,2),(4,1,3),(4,2,3),(4,3,2)]:
    for r in range(max_r+1):
        total_good=0
        for flat in product(range(k),repeat=n*r):
            gens=[tuple(flat[j*n:(j+1)*n]) for j in range(r)]
            c=criterion(k,n,gens)
            d=generated(k,n,gens)
            assert c==d, (k,n,r,gens,c,d)
            total_good+=c
            tested+=1
        exp=predicted(k,n,r)
        assert total_good==exp,(k,n,r,total_good,exp)
        cases+=1
rchecks=0
for k in range(2,9):
    for n in range(1,100):
        r=rmin(k,n)
        assert sum(comb(r,s) for s in range(k-2,r+1))>=n
        if r>0: assert sum(comb(r-1,s) for s in range(k-2,r))<n
        rchecks+=1
print('VERIFY_OK direct_term_closures',tested,'census_parameter_cases',cases,'rank_boundary_checks',rchecks)
