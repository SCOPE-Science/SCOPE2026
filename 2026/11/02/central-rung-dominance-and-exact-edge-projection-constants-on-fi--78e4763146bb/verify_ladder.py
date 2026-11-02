#!/usr/bin/env python3
"""Exact rational checks of the electrical-projection norm on finite ladders.
Run: python3 verify_ladder.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import acosh, cosh, sinh


def inverse(M):
    n = len(M)
    a = [[F(M[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if a[i][k])
        a[k], a[p] = a[p], a[k]
        z = a[k][k]
        a[k] = [v / z for v in a[k]]
        for i in range(n):
            if i != k and a[i][k]:
                z = a[i][k]
                a[i] = [a[i][j] - z * a[k][j] for j in range(2*n)]
    return [row[n:] for row in a]


def closed(n):
    def seq(t0, t1, k):
        if k == 0: return t0
        a, b = t0, t1
        for _ in range(1, k): a, b = b, 4*b-a
        return b
    if n % 2:
        m = (n-1)//2
        c, s = seq(1, 3, m), seq(1, 5, m)
        return F(1) + F(2*(c-1), s)
    m = n//2
    a, b = seq(1, 2, m), seq(0, 1, m)
    return F(1) + F((2*a-1)*(a-1), 3*a*b)


def edges(n):
    e = []
    for j in range(n-1):
        e.extend((('top', j, j+1), ('bottom', n+j, n+j+1)))
    e.extend(('rung', j, n+j) for j in range(n))
    return e


def graph_ground_inverse(n):
    v = 2*n
    L = [[0]*v for _ in range(v)]
    for _, a, b in edges(n):
        L[a][a] += 1; L[b][b] += 1
        L[a][b] -= 1; L[b][a] -= 1
    return inverse([row[:-1] for row in L[:-1]])


def green(n):
    D = [[4 if i == j else (-1 if abs(i-j) == 1 else 0)
          for j in range(n)] for i in range(n)]
    D[0][0] = D[-1][-1] = 3 if n > 1 else 2
    return inverse(D)


def main():
    checks = 0
    for n in range(2, 15):
        inv = graph_ground_inverse(n)
        E = edges(n)
        rows = []
        for name, a, b in E:
            s = [F(0)]*(2*n-1)
            if a != 2*n-1: s[a] += 1
            if b != 2*n-1: s[b] -= 1
            u = [sum(inv[i][j]*s[j] for j in range(2*n-1)) for i in range(2*n-1)] + [F(0)]
            currents = [u[x]-u[y] for _, x, y in E]
            rows.append((name, a, b, currents, sum(map(abs, currents))))
        G = green(n)
        center = [(n-1)//2, n//2] if n%2==0 else [n//2]
        winner_rows = []
        for name, a, b, currents, norm in rows:
            k = a if name=='rung' else a % n
            if name == 'rung':
                expected = F(1)+2*(2*G[k][k]-G[0][k]-G[n-1][k])
            else:
                expected = 2 - (G[0][k]-G[0][k+1]) + (G[n-1][k]-G[n-1][k+1])
                assert expected < 2
            assert norm == expected, (n, name, k, norm, expected)
            checks += 1
        maximum = max(r[-1] for r in rows)
        predicted = closed(n)
        assert maximum == predicted, (n, maximum, predicted)
        winners = [(name, a) for name, a, b, cs, v in rows if v == maximum]
        if n == 2:
            assert len(winners) == 4, (n, winners)
        else:
            assert winners == [('rung', k) for k in center], (n, winners, center)
        checks += 1
        if n <= 9:
            for i, row in enumerate(rows):
                for j, other in enumerate(rows):
                    assert row[3][j] == other[3][i]
                    assert sum(row[3][k]*rows[k][3][j] for k in range(len(rows))) == row[3][j]
                    checks += 2
    gamma = acosh(2)
    for n in range(2, 31):
        Y, A = cosh(n*gamma/2), cosh(gamma/2)
        if n%2:
            expect = 1 + 2*(Y-A)/(sinh(gamma)*sinh(n*gamma/2))
        else:
            expect = 1 + (2*Y-1)*(Y-1)/(sinh(gamma)*Y*sinh(n*gamma/2))
        assert abs(expect-float(closed(n)))<1e-12
        checks += 1
    for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        print('n=%2d norm=%s  decimal=%.12f' % (n, closed(n), float(closed(n))))
    print('VERIFY_OK exact and hyperbolic checks:', checks)


if __name__=='__main__': main()
