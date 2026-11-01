#!/usr/bin/env python3
"""Exact-rational independent vertex-enumeration checks for a quadrilateral covering index.

Requires only Python's standard library. Finite tests supplement, not replace,
the universal analytic proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def solve3(rows, rhs):
    m = [[F(v) for v in r] + [F(b)] for r, b in zip(rows, rhs)]
    for c in range(3):
        pivot = next((r for r in range(c, 3) if m[r][c]), None)
        if pivot is None:
            return None
        m[c], m[pivot] = m[pivot], m[c]
        t = m[c][c]
        m[c] = [u/t for u in m[c]]
        for r in range(3):
            if r != c:
                t = m[r][c]
                if t:
                    m[r] = [m[r][j]-t*m[c][j] for j in range(4)]
    return tuple(m[i][3] for i in range(3))


def estimate(p, q):
    k = p + q - 1
    assert p > 0 and q > 0 and k > 0
    # Each affine weight c0+c1*x+c2*y gives c1*x+c2*y-z <= -c0.
    abc = [(1, -1, (p-1)/q), (0, 1, -p/q), (0, 0, 1/q)]
    acd = [(1, (q-1)/p, -1), (0, 1/p, 0), (0, -q/p, 1)]
    abd = [(1, -1, -1), (0, 1, 0), (0, 0, 1)]
    bcd = [(p/k, 1-p/k, -p/k), (-1/k, 1/k, 1/k),
           (q/k, -q/k, 1-q/k)]
    sectors = [
        ('A', abc+abd, [((1,1,0), 1), ((-q,p,0),0), ((0,-1,0),0)]),
        ('B', abc+bcd, [((-1,-1,0), -1), ((-q,p,0),0), ((q,1-p,0),q)]),
        ('C', acd+bcd, [((-1,-1,0), -1), ((q,-p,0),0), ((1-q,p,0),p)]),
        ('D', acd+abd, [((1,1,0), 1), ((q,-p,0),0), ((-1,0,0),0)]),
    ]
    minima = {}
    for label, forms, triangle in sectors:
        constraints = [((cx,cy,-1), -constant) for constant,cx,cy in forms]
        constraints += triangle
        best = None
        for indices in combinations(range(len(constraints)), 3):
            a = [constraints[i][0] for i in indices]
            b = [constraints[i][1] for i in indices]
            sol = solve3(a, b)
            if sol is None:
                continue
            if all(sum(u*v for u,v in zip(row,sol)) <= bound
                   for row,bound in constraints):
                if best is None or sol[2] < best:
                    best = sol[2]
        assert best is not None, (label,p,q)
        minima[label] = best
    return minima


def proposed(p, q):
    small, large = sorted((p, q))
    k = p+q-1
    if large <= 1:
        return 1/(3-small)
    if small <= 1:
        if p+q <= 2:
            return large/(2*large+1-small)
        return large/(3*large-1)
    return k/(2*(p+q)-3+large)


def run():
    values = [F(1,8),F(1,4),F(1,3),F(2,5),F(1,2),F(3,5),
              F(2,3),F(3,4),F(7,8),F(1),F(9,8),F(5,4),
              F(3,2),F(7,4),F(2),F(5,2),F(3),F(5)]
    pairs = [(p,q) for p in values for q in values if p+q>1]
    # Force checks on all phase boundaries and close to the triangle limit.
    pairs += [(F(1,100),F(101,100)), (F(100,1),F(101,1)),
              (F(1,100),F(3,2)), (F(99,100),F(101,100)),
              (F(1,1),F(1,1)), (F(2,3),F(4,3))]
    # A deterministic exact-arithmetic subset with symmetric representatives.
    pairs = pairs[::3] + pairs[-6:]
    n = 0
    for p,q in pairs:
        result = estimate(p,q)
        target = proposed(p,q)
        assert min(result.values()) == target, (p,q,result,target)
        n += 1
    print('VERIFY_OK: %d exact rational quadrilateral systems; four-sector LP vertex enumeration' % n)


if __name__ == '__main__':
    run()
