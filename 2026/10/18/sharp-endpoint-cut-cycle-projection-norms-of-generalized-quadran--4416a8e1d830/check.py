"""Exact-rational checks for incidence-graph cut/cycle projection norms.

Standard-library-only computation for the symplectic generalized quadrangles
W(3,2) and W(3,3). Construct projective points and totally isotropic lines
from the standard symplectic form, then independently invert the reduced
incidence-graph Laplacian over Q and check every edge column.

Usage: python check.py
"""
from fractions import Fraction
from itertools import product


def canonical(v, p):
    for x in v:
        if x % p:
            s = pow(x, -1, p)
            return tuple((a * s) % p for a in v)
    raise ValueError('zero vector')


def symp(u, v, p):
    return (u[0]*v[2] + u[1]*v[3] - u[2]*v[0] - u[3]*v[1]) % p


def symplectic_graph(p):
    points = sorted({canonical(v, p) for v in product(range(p), repeat=4)
                     if any(v)})
    index = {x: i for i, x in enumerate(points)}
    line_sets = set()
    for a, u in enumerate(points):
        for v in points[a+1:]:
            if symp(u, v, p) != 0:
                continue
            line = frozenset(index[canonical(tuple((s*x+t*y)%p
                                        for x, y in zip(u, v)), p)]
                             for s, t in product(range(p), repeat=2)
                             if s or t)
            assert len(line) == p + 1
            line_sets.add(line)
    lines = sorted(line_sets, key=lambda s: tuple(sorted(s)))
    edges = [(point, len(points)+j) for j, line in enumerate(lines)
             for point in sorted(line)]
    n = len(points) + len(lines)
    assert len(points) == (p+1)*(p*p+1)
    assert len(lines) == len(points)
    assert len(edges) == len(points)*(p+1)
    return n, edges


def inverse_integer_matrix(a):
    n = len(a)
    aug = [[Fraction(x) for x in row] +
           [Fraction(int(i == j)) for j in range(n)]
           for i, row in enumerate(a)]
    for i in range(n):
        k = next(k for k in range(i, n) if aug[k][i])
        aug[i], aug[k] = aug[k], aug[i]
        fac = aug[i][i]
        aug[i] = [v/fac for v in aug[i]]
        for k in range(n):
            if k == i or not aug[k][i]:
                continue
            fac = aug[k][i]
            aug[k] = [v-fac*w for v,w in zip(aug[k], aug[i])]
    return [row[n:] for row in aug]


def main():
    for q in (2, 3):
        n, edges = symplectic_graph(q)
        L = [[0]*n for _ in range(n)]
        for x, y in edges:
            L[x][x] += 1
            L[y][y] += 1
            L[x][y] -= 1
            L[y][x] -= 1
        # Ground the last vertex. Voltage differences and therefore
        # transfer-current entries are independent of this choice.
        inv = inverse_integer_matrix([row[:-1] for row in L[:-1]])
        def green(x, y):
            return inv[x][y] if x < n-1 and y < n-1 else Fraction(0)
        H = (q+1)**2*(q*q+1)
        expectQ = Fraction(7*q**4 + 2*q**3 + 2*q*q + 2*q + 1, H)
        expectC = Fraction(8*q**4, H)
        expectDiag = Fraction(2*q**3 + 2*q*q + 2*q + 1, H)
        for e, (p,l) in enumerate(edges):
            col = [green(x,p)-green(x,l)-green(y,p)+green(y,l)
                   for x,y in edges]
            assert col[e] == expectDiag, (q,e,col[e],expectDiag)
            assert sum(map(abs, col)) == expectQ, (q,e,'Q')
            assert sum(abs(Fraction(int(j == e)) - v)
                       for j, v in enumerate(col)) == expectC, (q,e,'C')
        print(f'q={q}: {n} vertices, {len(edges)} edges, '
              f'Q={expectQ}, C={expectC}, all edge columns PASS')
    print('ALL EXACT-RATIONAL CHECKS PASS')


if __name__ == '__main__':
    main()
