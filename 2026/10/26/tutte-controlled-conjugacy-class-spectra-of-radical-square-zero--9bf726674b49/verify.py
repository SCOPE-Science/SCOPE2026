#!/usr/bin/env python3
"""Independent finite-group conjugacy verification for a graph-indexed unit group.

The algebra is the radical-square-zero quiver algebra over GF(q):
D(t)+N(u), with edges allowed to repeat or be loops.  Group orbits are
computed from explicit multiplication; graph-polynomial counts are
computed separately from deletion/contraction subset ranks.
"""
from itertools import product
from collections import Counter


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def neg(x, q):
    return x if q == 4 else (-x) % q


def mul(x, y, q):
    if q != 4:
        return x * y % q
    a = 0
    while y:
        if y & 1:
            a ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7
    return a


def inv(x, q):
    assert x
    return next(y for y in range(1, q) if mul(x, y, q) == 1)


def group_mul(g, h, q, edges):
    t, u = g
    s, v = h
    d = tuple(mul(x, y, q) for x, y in zip(t, s))
    w = tuple(add(mul(t[i], v[k], q), mul(u[k], s[j], q), q)
              for k, (i, j) in enumerate(edges))
    return d, w


def group_inv(g, q, edges):
    t, u = g
    v = tuple(inv(x, q) for x in t)
    z = tuple(neg(mul(mul(v[i], x, q), v[j], q), q)
              for (i, j), x in zip(edges, u))
    return v, z


def poly_class_count(n, edges, q):
    # Independent graph-subset computation, without using group multiplication.
    t = q - 1
    total = 0
    for bits in product((0, 1), repeat=len(edges)):
        roots = list(range(n))
        def root(x):
            while roots[x] != x:
                x = roots[x]
            return x
        for bit, (i, j) in zip(bits, edges):
            if bit:
                ri, rj = root(i), root(j)
                roots[ri] = rj
        c = len({root(x) for x in range(n)})
        exponent = sum(bits) - n + 2*c
        assert exponent >= 0
        total += t ** exponent
    return total


def brute_class_count(n, edges, q):
    nonzero = tuple(range(1, q))
    elements = list(product(product(nonzero, repeat=n), product(range(q), repeat=len(edges))))
    inverses = [(h, group_inv(h, q, edges)) for h in elements]
    unseen = set(elements)
    sizes = Counter()
    classes = 0
    while unseen:
        g = next(iter(unseen))
        orbit = {group_mul(group_mul(h, g, q, edges), hi, q, edges) for h, hi in inverses}
        assert orbit <= unseen  # distinct conjugacy orbits partition the group
        classes += 1
        sizes[len(orbit)] += 1
        unseen.difference_update(orbit)
    assert sum(k*v for k,v in sizes.items()) == len(elements)
    return classes, dict(sorted(sizes.items()))


def predicted_class_spectrum(n, edges, q):
    """Conjugacy prediction by diagonal equality strata, not group multiplication."""
    t = q - 1
    count = Counter()
    for colors in product(range(1, q), repeat=n):
        same = [e for e,(i,j) in enumerate(edges) if colors[i] == colors[j]]
        for bits in product((0,1), repeat=len(same)):
            roots=list(range(n))
            def root(x):
                while roots[x]!=x:
                    x=roots[x]
                return x
            s=0
            for bit,k in zip(bits,same):
                if bit:
                    s+=1
                    i,j=edges[k]
                    a,b=root(i),root(j)
                    roots[a]=b
            components=len({root(v) for v in range(n)})
            r=n-components
            beta=s-r
            assert beta >= 0
            size = q**(len(edges)-len(same)) * t**r
            count[size]+=t**beta
    return dict(sorted(count.items()))


def poly_add(a,b):
    out=Counter(a)
    for key,val in b.items(): out[key]+=val
    return {k:v for k,v in out.items() if v}


def poly_mul(a,b):
    out=Counter()
    for (i,j),v in a.items():
        for (k,l),w in b.items():out[(i+k,j+l)]+=v*w
    return {k:v for k,v in out.items() if v}


def poly_pow(a,n):
    out={(0,0):1}
    for _ in range(n):out=poly_mul(out,a)
    return out


def predict_forest(n,m,c,q):
    t=q-1
    p=poly_pow({(0,0):1,(0,1):1,(1,0):t-1},m)
    counts=Counter()
    for (a,b),coef in p.items():counts[q**a*t**b]+=t**c*coef
    return dict(sorted((k,v) for k,v in counts.items() if v))


def predict_cycle(ell,q):
    t=q-1
    plus={(0,0):1,(1,0):t-1,(0,1):1}
    minus={(0,0):1,(1,0):-1,(0,1):1}
    terms=poly_add(poly_pow(plus,ell),{k:(t-1)*v for k,v in poly_pow(minus,ell).items()})
    terms=poly_add(terms,{(0,ell):-t,(0,ell-1):t*t})
    counts=Counter()
    for (a,b),coef in terms.items():counts[q**a*t**b]+=coef
    return dict(sorted((k,v) for k,v in counts.items() if v))


def run():
    cases = [
        (2, [], 2),
        (2, [(0,1)], 2),
        (2, [(0,1)], 3),
        (2, [(0,1),(0,1)], 3),
        (2, [(0,0),(0,1)], 3),
        (3, [(0,1),(1,2)], 3),
        (3, [(0,1),(0,2)], 3),
        (3, [(0,1),(1,2),(2,0)], 3),
        (3, [(0,1),(0,1),(1,2)], 3),
        (3, [(0,0),(1,1),(0,1)], 2),
        (4, [(0,1),(1,2),(2,3)], 3),
        (4, [(0,1),(0,2),(0,3)], 3),
        (4, [(0,2),(0,3),(1,2),(1,3)], 3),
        (4, [(0,1),(1,2),(2,3),(3,0)], 2),
        (2, [(0,1),(1,0)], 4),
        (3, [(0,1),(1,2)], 4),
        (3, [(0,1),(1,2),(2,0)], 4),
    ]
    for idx,(n,edges,q) in enumerate(cases,1):
        expected=poly_class_count(n,edges,q)
        actual,hist=brute_class_count(n,edges,q)
        assert expected==actual, (n,edges,q,expected,actual)
        independent_spectrum=predicted_class_spectrum(n,edges,q)
        assert hist==independent_spectrum, (n,edges,q,hist,independent_spectrum)
        print('PASS',idx,'q',q,'vertices',n,'edges',repr(edges),
              'classes',actual,'class_sizes',repr(hist))
    # Structural corollaries checked independently of full-group orbit enumeration.
    for n,edges,q in [(3,[(0,1),(1,2)],3),
                       (4,[(0,1),(1,2),(2,3)],3),
                       (4,[(0,1),(0,2),(0,3)],3)]:
        counts=predicted_class_spectrum(n,edges,q)
        assert counts==predict_forest(n,len(edges),n-len(edges),q)
    for ell,q in [(1,2),(1,3),(2,3),(2,4),(3,3),(3,4),(4,2),(4,3)]:
        edges=[(i,(i+1)%ell) for i in range(ell)]
        assert predict_cycle(ell,q)==predicted_class_spectrum(ell,edges,q), (ell,q)
    print('ALL_QUIVER_UNIT_TUTTE_CLASS_AND_SPECTRUM_CHECKS_PASSED',len(cases),
          'forest_3','cycle_8')

if __name__=='__main__':
    run()
