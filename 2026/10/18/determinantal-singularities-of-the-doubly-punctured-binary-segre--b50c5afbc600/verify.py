#!/usr/bin/env python3
"""Finite cross-checks for toric charts of a two-coordinate Segre projection.

Only finite dimension instances are checked; the uniform proof is in RESULT.md.
Requires Python 3 standard library. An optional NumPy/SciPy section checks volumes.
"""
from itertools import product
from math import factorial
from collections import Counter


def vertices(d):
    return [v for v in product((0, 1), repeat=d) if 0 < sum(v) < d]


def difference(u, v):
    return tuple(a-b for a, b in zip(u, v))


def expected_rays(d, v):
    # Basic neighbors of central vertex, otherwise matrix semigroup generators.
    k=sum(v)
    if 1 < k < d-1:
        return [tuple((1-2*v[i]) if j==i else 0 for j in range(d)) for i in range(d)]
    # By complement symmetry reduce to singleton base vertex.
    if k == d-1:
        w=tuple(1-x for x in v)
        return [tuple(-x for x in q) for q in expected_rays(d,w)]
    pivot=v.index(1)
    out=[]
    for i in range(d):
        if i==pivot: continue
        b=[0]*d; b[i]=1
        a=list(b); a[pivot]=-1
        out.extend([tuple(a),tuple(b)])
    return out


def decompose(d, v, u, gens):
    """Construct a nonnegative decomposition of each actual chart monomial."""
    k=sum(v)
    dv=difference(u,v)
    if 1 < k < d-1:
        out=[]
        for i in range(d):
            if u[i] != v[i]:
                out.append(i)
        assert tuple(sum(gens[i][j] for i in out) for j in range(d))==dv
        return len(out)
    # By complement symmetry, flip all components for high-weight vertex.
    if k==d-1:
        v=tuple(1-x for x in v);u=tuple(1-x for x in u)
        dv=difference(u,v)
        gens=[tuple(-x for x in g) for g in gens]
    p=v.index(1)
    cols=[i for i in range(d) if i!=p]
    if u[p]:
        terms=[gens[2*cols.index(i)+1] for i in cols if u[i]]
    else:
        q=next(i for i in cols if u[i])
        terms=[gens[2*cols.index(q)]]+[gens[2*cols.index(i)+1] for i in cols if u[i] and i!=q]
    assert tuple(sum(term[j] for term in terms) for j in range(d))==dv
    return len(terms)


def main():
    total_charts=total_monomials=0
    for d in range(3,8):
        vv=vertices(d)
        counts=Counter()
        for v in vv:
            gens=expected_rays(d,v)
            k=sum(v)
            counts['determinantal' if k in (1,d-1) else 'smooth']+=1
            assert len(gens)==(2*(d-1) if k in (1,d-1) else d)
            for u in vv:
                decompose(d,v,u,gens)
                total_monomials+=1
            total_charts+=1
        assert counts['determinantal']==2*d
        assert counts['smooth']==2**d-2-2*d
        print(f'd={d}: vertices={len(vv)}, determinantal={counts["determinantal"]}, smooth={counts["smooth"]}; all vertex differences decomposed')
        # The 2 by (d-1) generator relation uses a_i+b_j=a_j+b_i.
        for v in vv:
            if sum(v)!=1: continue
            gg=expected_rays(d,v)
            m=d-1
            for i in range(m):
                for j in range(i+1,m):
                    assert tuple(gg[2*i][k]+gg[2*j+1][k] for k in range(d))==tuple(gg[2*j][k]+gg[2*i+1][k] for k in range(d))
        assert factorial(d)-2 > 0
    print(f'PASS: {total_charts} vertex charts and {total_monomials} exponent differences, with pairwise rank-one relations.')
    try:
        import numpy as np
        from scipy.spatial import ConvexHull
        for d in range(3,6):
            vv=np.array(vertices(d),dtype=float)
            degree=factorial(d)*ConvexHull(vv).volume
            expected=factorial(d)-2
            assert abs(degree-expected)<1e-7,(d,degree,expected)
            print(f'd={d}: numerical normalized volume={degree:.8f}, predicted={expected}')
    except ImportError:
        print('Optional convex-hull volume test skipped (NumPy/SciPy missing).')

if __name__=='__main__':main()
