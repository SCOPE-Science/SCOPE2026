"""Exact arithmetic diagnostic for rational-data finite parabola zero rigidity."""
from itertools import product
from random import Random

def zero_by_cyclotomic(f,p,a,b):
    c=[0]*p
    for x,v in enumerate(f):
        c[(a*x*x+b*x)%p]+=v
    return all(t==c[0] for t in c)

def expected(f,p):
    if not any(f): return None
    if len(set(f))==1: return p-1
    centers=[s for s in range(p) if all(f[x]+f[(s-x)%p]==0 for x in range(p))]
    if centers:
        assert len(centers)==1
        return p
    return int(sum(f)==0)

def run():
    totals={}
    for p in (5,7):
        counts={0:0,1:0,p-1:0,p:0}
        for f in product((-1,0,1),repeat=p):
            e=expected(f,p)
            if e is None: continue
            got=sum(zero_by_cyclotomic(f,p,a,b) for a in range(p) for b in range(p))
            assert got==e,(p,f,got,e)
            counts[e]+=1
        totals[p]=counts
    p=11; rng=Random(146273)
    for trial in range(10000):
        f=tuple(rng.choice((-3,-2,-1,0,1,2,3)) for _ in range(p))
        e=expected(f,p)
        if e is None: continue
        got=sum(zero_by_cyclotomic(f,p,a,b) for a in range(p) for b in range(p))
        assert got==e,(p,f,got,e)
    print('EXACT DIAGNOSTICS PASSED: ternary exhaustive p=5,7; 10000 seeded p=11 samples')
    print('CATEGORY COUNTS:',totals)
if __name__=='__main__':run()
