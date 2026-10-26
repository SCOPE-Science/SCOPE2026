"""Exact checks for the triangle/four-cycle covariance identity.
Requires Python >=3.9 and SymPy. No random sampling is used.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from sympy import symbols, prod, together, cancel, factor, simplify


def falling(x, k):
    out = 1
    for i in range(k):
        out *= x - i
    return out


def hypergeom(n, m, j):
    edge_total = comb(n, 2)
    if j > m:
        return Fraction(0)
    return Fraction(falling(m, j), falling(edge_total, j))


def covariance_formula(n, m):
    M = comb(n, 2)
    L = m * (n*n - 2*n - 7) - 4*(n*n-n-4)
    return Fraction(4 * falling(m, 4) * (M-m) * (M-m-1) * L,
                    (n+1)**2 * (n+2) * (n+3) * (M-5) * (M-4) * (M-2)**2)


def overlap_formula(n, m):
    c3 = comb(n, 3)
    c4 = 3 * comb(n, 4)
    p3, p4, p5, p6, p7 = [hypergeom(n, m, j) for j in (3,4,5,6,7)]
    return c4*(c3*(p7-p3*p4)+4*(n-4)*(p6-p7)+4*(p5-p7))


def graph_motifs(n):
    edgelist = list(combinations(range(n), 2))
    eid = {e:i for i,e in enumerate(edgelist)}
    triangles = []
    cycles = []
    for vs in combinations(range(n), 3):
        triangles.append(sum(1<<eid[e] for e in combinations(vs, 2)))
    for vs in combinations(range(n), 4):
        K4 = [tuple(e) for e in combinations(vs, 2)]
        complete_mask = sum(1<<eid[e] for e in K4)
        # Each pair of disjoint removed diagonals determines a 4-cycle.
        for e in K4:
            for f in K4:
                if e < f and len(set(e+f)) == 4:
                    cycles.append(complete_mask^(1<<eid[e])^(1<<eid[f]))
    assert len(triangles) == comb(n,3)
    assert len(set(cycles)) == 3*comb(n,4)
    return edgelist, triangles, cycles


def exhaustive_checks(n):
    edges, triangles, cycles = graph_motifs(n)
    hist = [Counter() for _ in range(len(edges)+1)]
    for mask in range(1 << len(edges)):
        x = sum((mask&t)==t for t in triangles)
        y = sum((mask&c)==c for c in cycles)
        hist[mask.bit_count()][(x,y)] += 1
    assertions = 0
    for m, joint in enumerate(hist):
        total = sum(joint.values())
        assert total == comb(len(edges),m)
        ex = Fraction(sum(x*v for (x,y),v in joint.items()),total)
        ey = Fraction(sum(y*v for (x,y),v in joint.items()),total)
        exy = Fraction(sum(x*y*v for (x,y),v in joint.items()),total)
        value = exy-ex*ey
        assert value == overlap_formula(n,m) == covariance_formula(n,m), (n,m,value,overlap_formula(n,m))
        assert ex == comb(n,3)*hypergeom(n,m,3)
        assert ey == 3*comb(n,4)*hypergeom(n,m,4)
        assertions += 4
    return assertions


def symbolic_check():
    n,m = symbols('n m')
    M = n*(n-1)/2
    def h(k):
        return falling(m,k)/falling(M,k)
    overlap = 3*n*(n-1)*(n-2)*(n-3)/24 * (
        n*(n-1)*(n-2)/6*(h(7)-h(3)*h(4))
        +4*(n-4)*(h(6)-h(7))+4*(h(5)-h(7)))
    closed = 4*falling(m,4)*(M-m)*(M-m-1)*(
        m*(n*n-2*n-7)-4*(n*n-n-4))/(
        (n+1)**2*(n+2)*(n+3)*(M-5)*(M-4)*(M-2)**2)
    assert cancel(overlap-closed)==0
    assert factor(closed)==factor(overlap)
    return 2

if __name__ == '__main__':
    ntests=sum(exhaustive_checks(n) for n in (4,5,6))
    ntests+=symbolic_check()
    print('PASS', ntests, 'exact checks; fully enumerated graphs: ',sum(2**comb(n,2) for n in (4,5,6)))
    for n in range(4,51):
        M=comb(n,2)
        for m in range(M+1):
            c=covariance_formula(n,m)
            L=m*(n*n-2*n-7)-4*(n*n-n-4)
            if 4<=m<=M-2:
                assert (c>0)-(c<0)==(L>0)-(L<0)
            else:
                assert c==0
    print('PASS finite sign crosschecks for n<=50 (supplements exact sign proof)')
