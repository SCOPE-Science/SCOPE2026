#!/usr/bin/env python3
"""Exact independent finite checks of pair-type moments in uniform matchings.

Uses recursive matching enumeration, no symbolic moment formulas for the data.
"""
from fractions import Fraction as F
from itertools import permutations
from math import comb


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j] + vertices[j + 1:]
        for tail in matchings(rest):
            yield ((a, b),) + tail


def pair_type(a, b):
    (u, v), (w, z) = a, b
    if u < w < v < z or w < u < z < v:
        return 0
    if u < w < z < v or w < u < v < z:
        return 1
    return 2


def moments(n):
    total = 0
    sums = [0] * 3
    products = [[0] * 3 for _ in range(3)]
    for pairs in matchings(tuple(range(2 * n))):
        z = [0] * 3
        for i in range(n):
            for j in range(i + 1, n):
                z[pair_type(pairs[i], pairs[j])] += 1
        total += 1
        for i in range(3):
            sums[i] += z[i]
            for j in range(3):
                products[i][j] += z[i] * z[j]
    assert total == (1 if n == 1 else __import__('math').prod(range(1, 2*n, 2)))
    means = [F(s, total) for s in sums]
    cov = [[F(products[i][j], total) - means[i]*means[j] for j in range(3)] for i in range(3)]
    m = F(comb(n, 2), 3)
    vc = F(n*(n-1)*(n+3), 45)
    vd = F(n*(n-1)*(2*n+1), 45)
    cn = -F(n*(n-1), 18)
    cd = -F(n*(n-1)*(2*n+1), 90)
    expected = [[vc, cn, cd], [cn, vc, cd], [cd, cd, vd]]
    assert means == [m]*3, (n,means,m)
    assert cov == expected,(n,cov,expected)
    return total, 9+3


def conditional_pattern_counts():
    counts = [[0]*3 for _ in range(3)]
    seen=set()
    for word in permutations('AABBCC'):
        if word in seen:
            continue
        seen.add(word)
        arcs=[]
        for label in 'ABC':
            ends=[i for i,t in enumerate(word) if t==label]
            arcs.append(tuple(ends))
        counts[pair_type(arcs[0], arcs[1])][pair_type(arcs[0], arcs[2])] += 1
    assert len(seen)==90
    # Exact probabilities for one shared chord; 0=cross, 1=nest, 2=alignment.
    assert counts == [[12,10,8],[10,12,8],[8,8,14]],counts
    return len(seen)


def projection_integrals():
    import sympy as sp
    a,b=sp.symbols('a b')
    L=b-a
    q=[2*L*(1-L),L**2+2*a*(1-b),a*a+(1-b)**2]
    def E(f):
        return sp.integrate(2*sp.integrate(sp.expand(f),(b,a,1)),(a,0,1))
    mu=[sp.Rational(1,3)]*3
    sigma=[[sp.factor(E(q[i]*q[j])-mu[i]*mu[j]) for j in range(3)] for i in range(3)]
    exp=sp.Matrix([[sp.Rational(1,45),0,-sp.Rational(1,45)],
                   [0,sp.Rational(1,45),-sp.Rational(1,45)],
                   [-sp.Rational(1,45),-sp.Rational(1,45),sp.Rational(2,45)]])
    assert sp.Matrix(sigma)==exp,(sigma,exp)
    return sigma

if __name__ == '__main__':
    p=conditional_pattern_counts()
    print('three-labeled-chord interleavings',p)
    tests=0
    instances=0
    for n in range(1,8):
        v,c=moments(n)
        instances += v
        tests += c
        print('n',n,'matchings',v,'checks',c)
    x=projection_integrals()
    print('projection matrix',x)
    print('VERIFY_OK',instances,tests)
