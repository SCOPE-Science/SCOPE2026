"""Exact independent finite checks for a clique with one incompletely connected vertex.

Run with: python verify_projection.py
Only the symbolic argument in the accompanying proof establishes all-size claims.
"""
from fractions import Fraction as F
from collections import defaultdict


def inverse(a):
    n = len(a)
    m = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        j = next(i for i in range(k, n) if m[i][k] != 0)
        m[k], m[j] = m[j], m[k]
        z = m[k][k]
        m[k] = [v / z for v in m[k]]
        for i in range(n):
            if i != k:
                z = m[i][k]
                if z:
                    m[i] = [v - z * w for v, w in zip(m[i], m[k])]
    return [row[n:] for row in m]


def sample(r, h):
    n = r + h + 1
    c = 0
    fverts = range(1, r+1)
    hverts = range(r+1, n)
    edges = [(i, j) for i in range(1, n) for j in range(i+1, n)] + [(c, j) for j in hverts]
    lap = [[F(0) for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        lap[i][i] += 1
        lap[j][j] += 1
        lap[i][j] -= 1
        lap[j][i] -= 1
    l_reg = [[lap[i][j] + F(1,n) for j in range(n)] for i in range(n)]
    g = inverse(l_reg)
    group = defaultdict(list)
    for ai,aj in edges:
        p = [g[i][ai]-g[i][aj] for i in range(n)]
        val = sum(abs(p[bi]-p[bj]) for bi,bj in edges)
        if ai == 0: label='C'
        elif ai in fverts and aj in fverts: label='A'
        elif ai in hverts and aj in hverts: label='D'
        else: label='B'
        group[label].append(val)
    for v in group.values():
        assert all(x == v[0] for x in v)
    nn = F(n)
    expected = {
        'A':F(2*(n-2),n-1),
        'B':F(2*h*h*h+4*h*h*r+h*h+2*h*r*r+2*h*r-3*h-2*r, h*(h+r)*(h+r+1)),
        'C':F(2*h*h+3*h*r-2*r,h*(h+r+1)),
        'D':F(2*(n-1),n)
    }
    count=0
    for typ, vals in group.items():
        assert vals[0] == expected[typ], (r,h,typ,vals[0],expected[typ])
        count += len(vals)
    predicted = (F(2*r,r+1) if h == 1 else
                 F((r+1)*(2*r+7),(r+2)*(r+3)) if h == 2 else
                 F(2*h*h+3*h*r-2*r,h*(h+r+1)))
    assert max(vals[0] for vals in group.values()) == predicted
    assert (predicted > 2) == (h >= 3 and r*(h-2) > 2*h)
    return count+2


def main():
    assertions = 0
    for r in range(2, 9):
        for h in range(1, 9):
            assertions += sample(r,h)
    print(f'PASS: {assertions} exact-rational row and threshold comparisons for 56 graphs.')


if __name__ == '__main__':
    main()
