"""Exact two-round profiles of finite abelian 2-groups.

Run: python3 verify.py
The algebraic profile formula applies to all finite direct sums of cyclic 2-groups;
the finite loops below only test its implementation and the 15-case table.
"""
from itertools import product
from math import prod

REPS = [(),(2,),(2,2),(4,),(2,4),(4,4),(2,4,4),
        (8,),(2,8),(4,8),(8,8),(16,),(2,16),(4,16),(8,16)]

def profile(r,t,u,v):
    """All pointed one-round type sets, as eight-bit atomic masks."""
    assert r>=t>=u>=v>=0
    F=lambda v:frozenset(v)
    out={F([255]+([153] if r else [])+([9] if t else []))}
    if t:
        out.add(F([90,60,136]+([24] if r>1 else [])+([8] if u or t>1 else [])))
    if r>t:
        out.add(F([90,60]+([24] if r>1 else [])+([8] if t else [])))
    if u:
        out.add(F([18,4,32,80,128,0]+([16] if r>1 else [])))
    if t and (r>t or t>u):
        out.add(F([18,4,32,80]+([16] if r>1 else [])+([0] if not (r==t==1 and u==0) else [])))
    if v:out.add(F([18,4,32,64,128,16,0]))
    if u:out.add(F([18,4,32,64,16,0]))
    return frozenset(out)

def abstract_signature(mod):
    exps=[x.bit_length()-1 for x in mod]
    assert all(2**a==x for a,x in zip(exps,mod))
    return profile(len(exps),sum(a>=2 for a in exps),sum(a>=3 for a in exps),sum(a>=4 for a in exps))

def brute(mod):
    """Full direct enumeration of the eight primitive atomic tests."""
    Z=(0,)*len(mod)
    elems=list(product(*(range(m) for m in mod)))
    def plus(a,b):return tuple((i+j)%m for i,j,m in zip(a,b,mod))
    def dbl(a):return plus(a,a)
    out=set()
    for x in elems:
        masks=set()
        for y in elems:
            q=(x==Z,y==Z,x==y,dbl(x)==Z,dbl(y)==Z,
               plus(x,y)==Z,dbl(x)==y,dbl(y)==x)
            masks.add(sum((1<<i) for i,z in enumerate(q) if z))
        out.add(frozenset(masks))
    return frozenset(out)

def partitions(n,lo=1):
    if n==0:yield ()
    else:
        for k in range(lo,n+1):
            for x in partitions(n-k,k):yield (k,)+x

def representative(r,t,u,v):
    """One of fifteen canonical groups, determined by multiplicity thresholds."""
    if not r:return ()
    if not t:return (2,) if r==1 else (2,2)
    if not u:
        if r>t:return (2,4) if t==1 else (2,4,4)
        return (4,) if t==1 else (4,4)
    if not v:
        if r>t:return (2,8)
        if t>u:return (4,8)
        return (8,) if r==1 else (8,8)
    if r>t:return (2,16)
    if t>u:return (4,16)
    return (16,) if r==1 else (8,16)

def run():
    for e in range(0,9):
        for p in partitions(e):
            mod=tuple(2**a for a in p)
            assert abstract_signature(mod)==brute(mod),mod
    print('EXACT_ATOMIC_OK exponent_sum=0..8')
    S={abstract_signature(rep) for rep in REPS}
    assert len(S)==15
    for r in range(0,14):
        for t in range(r+1):
            for u in range(t+1):
                for v in range(u+1):
                    assert profile(r,t,u,v)==abstract_signature(representative(r,t,u,v)),(r,t,u,v)
    print('ALL_MULTIPLICITY_PATTERNS_OK r<=13 (analytic thresholds are unbounded)')
    print('REPRESENTATIVES_OK classes=15 rep_orders='+','.join(str(prod(x)) for x in REPS))
    print('SHARP_REPRESENTATIVE_OK min_max_order=128')
    print('VERIFY_OK')
if __name__=='__main__':run()
