"""Exact-arithmetic finite verification of a panhandle matroid polytope formula.
Uses only Python's standard library. The infinite statement requires its separate proof.
"""
from fractions import Fraction as Q
from itertools import combinations


def data(p, t, r):
    assert 3 <= r <= p and t >= 2
    n = p + t
    rho = max(Q(t), Q(n-r, r), Q(r, p-r+1))
    v = max(Q(t), Q((rho+1)*r-p*rho))
    z = [((rho+1)*r-v)/p]*p + [v/t]*t
    assert all(1 <= u <= rho for u in z)
    assert sum(z) == (rho+1)*r
    assert sum(z[p:]) <= rho
    c = [u/(rho+1) for u in z]
    return rho, z, c


def run():
    instances = vertices = inequalities = 0
    regimes = set()
    for p in range(3, 10):
        for r in range(3, p+1):
            for t in range(2, 7):
                n = p+t
                rho, z, c = data(p, t, r)
                lower = Q(n-r,r)
                upper = Q(r,p-r+1)
                dom = ('tail' if rho == t else 'lower' if rho == lower else 'upper')
                regimes.add(dom)
                V = []
                for I in combinations(range(p), r):
                    V.append(set(I))
                for I in combinations(range(p), r-1):
                    for j in range(p, n):
                        V.append(set(I) | {j})
                assert V and len(V) == len(set(map(frozenset,V)))
                # Full supporting extrema: every coordinate has both zero and one,
                # and the tail sum achieves both zero and one.
                for j in range(n):
                    assert any(j in B for B in V)
                    assert any(j not in B for B in V)
                assert any(all(j < p for j in B) for B in V)
                assert any(any(j >= p for j in B) for B in V)
                inequalities += 2*n + 2
                for B in V:
                    x = [Q(int(j in B)) for j in range(n)]
                    y = [c[j] + (c[j]-x[j])/rho for j in range(n)]
                    assert sum(y) == r
                    assert all(0 <= yi <= 1 for yi in y)
                    assert sum(y[p:]) <= 1
                    vertices += 1
                    inequalities += 2*n + 1
                # Every lower bound is necessary for all centers, and the
                # constructed center simultaneously attains the derived upper bound.
                assert rho >= t
                assert (rho+1)*r >= n
                assert (rho+1)*r <= (p+1)*rho
                if rho == t and rho > lower and rho > upper:
                    assert all(z[j] == 1 for j in range(p, n))
                    assert all(1 < z[j] < rho for j in range(p))
                if rho == lower and rho > t:
                    assert all(zi == 1 for zi in z)
                if rho == upper and rho > t:
                    assert all(z[j] == rho for j in range(p))
                    assert sum(z[p:]) == rho
                    assert all(1 < z[j] < rho for j in range(p,n))
                instances += 1
    assert regimes == {'tail', 'lower', 'upper'}
    print('EXACT_VERIFY_OK', 'instances', instances, 'base_vertices', vertices,
          'facet_and_containment_checks', inequalities,
          'strict_regimes', ','.join(sorted(regimes)))

if __name__ == '__main__':
    run()
