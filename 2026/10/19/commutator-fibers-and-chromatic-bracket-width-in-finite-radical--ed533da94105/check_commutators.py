#!/usr/bin/env python3
"""Exhaustive finite-field enumeration of commutator fibers in square-zero quiver algebras."""
from itertools import product
from collections import Counter

def count_theoretical(q, n, arrows, target):
    m = len(arrows)
    nonloops = [(k,u,v) for k,(u,v) in enumerate(arrows) if u != v]
    loop_indices=[k for k,(u,v) in enumerate(arrows) if u==v]
    loops = len(loop_indices)
    if any(target[k] for k in loop_indices): return 0
    total = 0
    for colors in product(range(q), repeat=2*n):
        exponent = 2*loops
        ok = True
        for k,u,v in nonloops:
            equal = colors[u]==colors[v] and colors[n+u]==colors[n+v]
            if equal and target[k]!=0: ok=False; break
            exponent += 2 if equal else 1
        if ok: total += q**exponent
    return total

def run_case(q, n, arrows):
    m=len(arrows)
    dim=n+m
    if q**(2*dim)>100000:
        raise ValueError('test would be too large')
    def multiply(a,b):
        diag=[a[i]*b[i]%q for i in range(n)]
        radical=[(a[u]*b[n+k]+a[n+k]*b[v])%q for k,(u,v) in enumerate(arrows)]
        return diag+radical
    seen=Counter()
    for x in product(range(q),repeat=dim):
        for y in product(range(q),repeat=dim):
            xy=multiply(x,y)
            yx=multiply(y,x)
            comm=[(a-b)%q for a,b in zip(xy,yx)]
            assert all(a==0 for a in comm[:n])
            seen[tuple(comm[n:])]+=1
    assert sum(seen.values())==q**(2*dim)
    all_vectors=product(range(q),repeat=m)
    for z in all_vectors:
        expected=count_theoretical(q,n,arrows,z)
        assert seen[z]==expected, (q,n,arrows,z,seen[z],expected)
    print('PASS', 'q',q,'vertices',n,'arrows',arrows,'pairs',q**(2*dim),'image',len(seen))

for q,n,arrows in [
 (2,2,[(0,1)]),
 (2,2,[(0,1),(0,1)]),
 (3,2,[(0,1)]),
 (2,3,[(0,1),(1,2),(2,0)]),
 (2,3,[(0,1),(1,2),(0,0)]),
 (3,2,[(0,0),(0,1)]),
 (2,2,[(0,0),(1,1),(0,1)])
]: run_case(q,n,arrows)

# Exhaustive chromatic-check by assigning q^(2r) colors to graphs.
def colorable(n,edges,k):
    return any(all(c[u]!=c[v] for u,v in edges) for c in product(range(k),repeat=n))
for n,edges in [(5,[(i,j) for i in range(5) for j in range(i+1,5)]),
                (4,[(i,j) for i in range(4) for j in range(i+1,4)]),
                (5,[(i,(i+1)%5) for i in range(5)])]:
    chi=next(k for k in range(1,n+1) if colorable(n,edges,k))
    predicted=0 if not edges else next(r for r in range(1,4) if colorable(n,edges,4**r))
    assert predicted==(0 if chi==1 else next(r for r in range(1,4) if 4**r>=chi))
    print('PASS_CHROMATIC','n',n,'chi',chi,'width_over_F2',predicted)
print('ALL_COMMUTATOR_FIBER_AND_WIDTH_CHECKS_PASSED')
