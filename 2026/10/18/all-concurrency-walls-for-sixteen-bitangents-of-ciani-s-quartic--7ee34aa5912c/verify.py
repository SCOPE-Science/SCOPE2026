#!/usr/bin/env python3
"""Exact, standard-library incidence certificate for the Ciani 16-bitangent subarrangement.
Run: python3 verify.py
All arithmetic uses integer polynomials in s; no numerical tolerance or extension-field cutoff.
"""
from itertools import combinations, product
from collections import Counter

# Integer polynomials, coefficients in ascending order.
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return tuple(a)
def add(a,b):
    return trim([ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b))) ])
def neg(a): return tuple(-v for v in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): out[i+j]+=v*w
    return trim(out)
def zero(a): return all(v==0 for v in a)
def rem(a,p):
    # p is a monic polynomial. Works integrally.
    a=list(trim(a));p=trim(p)
    assert p[-1]==1
    while len(a)>=len(p) and any(a):
        d=len(a)-len(p);c=a[-1]
        for k,v in enumerate(p):a[d+k]-=c*v
        a=list(trim(a))
    return trim(a)
def vanishes(a,p): return zero(a if p is None else rem(a,p))
S=(0,1); ONE=(1,); NEG=(-1,)
lines=[(ONE,(b,),(c,)) for b,c in product((-1,1),repeat=2)]
for pos in range(3):
    for b,c in product((-1,1),repeat=2):
        v=[(b,),(c,)];v.insert(pos,S)
        lines.append(tuple(v))
assert len(lines)==16

def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):
    r=(0,)
    for x,y in zip(a,b): r=add(r,mul(x,y))
    return r

# A complete exact list of possible zeros of a nonzero 3-line determinant.
linear=[(0,1),(-1,1),(1,1),(-2,1),(2,1),(-3,1),(3,1)]
quadratic=[(1,0,1),(3,0,1),(2,1,1),(2,-1,1)]
factors=linear+quadratic

def factor_test(poly):
    if zero(poly):return []
    x=poly
    used=[]
    for f in factors:
        while len(x)>=len(f) and zero(rem(x,f)):
            # Exact quotient by monic f using integer arithmetic.
            a=list(x);q=[0]*(len(a)-len(f)+1)
            while len(a)>=len(f):
                d=len(a)-len(f);c=a[-1];q[d]=c
                for i,v in enumerate(f):a[d+i]-=c*v
                a=list(trim(a))
            assert zero(a)
            x=trim(q)
            used.append(f)
    assert len(x)==1, ('unlisted irreducible determinant factor',poly,x)
    return used

minors=[]
for ids in combinations(range(16),3):
    det=dot(lines[ids[0]],cross(lines[ids[1]],lines[ids[2]]))
    factor_test(det)
    minors.append(det)
assert len(minors)==560
assert sum(zero(m) for m in minors)==24

# Pairwise distinctness is guaranteed away from s=0, +1, -1.
for i,j in combinations(range(16),2):
    P=cross(lines[i],lines[j])
    assert not all(zero(t) for t in P)
    # A common root of all three cross components must be 0, 1, or -1.
    lists=[set(factor_test(t)) for t in P if not zero(t)]
    common=set.intersection(*lists)
    assert common.issubset({(0,1),(-1,1),(1,1)}),(i,j,common)

# Every intersection point is encoded by its complete, exact set of lines.
def profile(p):
    points=set()
    for i,j in combinations(range(16),2):
        P=cross(lines[i],lines[j])
        assert not all(vanishes(u,p) for u in P), ('duplicate lines',p,i,j)
        containing=frozenset(k for k in range(16)
                             if vanishes(dot(lines[k],P),p))
        assert i in containing and j in containing
        points.add(containing)
    ans=Counter(map(len,points))
    assert sum(v*(v-1)//2*n for v,n in ans.items())==120
    assert max(ans)==4
    return dict(sorted(ans.items()))

expected={
    'generic':{2:84,4:6},
    'fermat':{2:48,4:12},
    'minus-five':{2:72,3:4,4:6},
    'minus-ten':{2:48,3:12,4:6},
    'quadratic-wall':{2:48,3:12,4:6},
}
checks=[('generic',None),('fermat',(1,0,1)),
        ('minus-five',(-2,1)),('minus-five',(2,1)),
        ('minus-ten',(-3,1)),('minus-ten',(3,1)),
        ('quadratic-wall',(2,1,1)),('quadratic-wall',(2,-1,1))]
for name,p in checks:
    got=profile(p)
    assert got==expected[name],(name,p,got)
    print(name, 'parameter polynomial:',p, 'incidence profile:',got)
print('PASS: all pairs distinct for smooth fibers; 560 minors factor in the listed exact set; 24 identically zero;')
print('PASS: all eight generic/special exact profiles and 120 pair incidences each.')
