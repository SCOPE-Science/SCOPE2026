"""Finite exact-incidence and floating spectral checks for affine-plane Gaussian thresholds.

Run: python checker.py (requires numpy). This supports, but cannot replace,
the all-orders analytic theorem in RESULT.md.
"""
from collections import deque
from math import log2, log
import numpy as np


def field(q):
    if q in (2, 3, 5, 7):
        return lambda a, b: (a + b) % q, lambda a, b: (a * b) % q
    if q == 4:
        # F_4 = F_2[t] / (t^2+t+1), with 2=t and 3=t+1.
        def multiply(a, b):
            z = 0
            for i in range(2):
                if (a >> i) & 1:
                    z ^= b << i
            if (z >> 2) & 1:
                z ^= 7
            return z
        return lambda a, b: a ^ b, multiply
    raise ValueError(q)


def affine_matrices(q):
    add, mul = field(q)
    points = [(x, y) for x in range(q) for y in range(q)]
    lines = [({(x, add(mul(a, x), b)) for x in range(q)}, a)
             for a in range(q) for b in range(q)]
    lines += [({(b, y) for y in range(q)}, q) for b in range(q)]
    B = np.array([[int(point in L) for L, _ in lines] for point in points], dtype=int)
    H = np.array([[int(i != j and lines[i][1] == lines[j][1])
                   for j in range(len(lines))] for i in range(len(lines))], dtype=int)
    return B, H


def graph_distances(B):
    m, n = B.shape
    adj = [[] for _ in range(m+n)]
    for i, j in zip(*np.where(B)):
        adj[int(i)].append(int(m+j)); adj[int(m+j)].append(int(i))
    D = np.full((m+n, m+n), -1, dtype=int)
    for start in range(m+n):
        D[start, start] = 0
        queue = deque([start])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if D[start, y] == -1:
                    D[start, y] = D[start, x] + 1
                    queue.append(y)
    assert np.min(D) >= 0
    return D


def powered_distance(q, p, B, H):
    m, n = B.shape
    a, b, c = 2**p, 4**p, 3**p
    upper = a*(np.ones((m, m))-np.eye(m))
    lower = a*(np.ones((n, n))-np.eye(n))+(b-a)*H
    cross = c*np.ones((m, n))+(1-c)*B
    return np.block([[upper, cross], [cross.T, lower]])


def analytic_sectors(q, p):
    a, b, c = 2**p, 4**p, 3**p
    line = (q-1)*b-q*a
    det = a*b-q*(c-1)**2
    E = a*(q*q-1)+q/(q+1)*((q-1)*b+q*q*a) \
        -2*q/(q+1)*((q+1)+(q*q-1)*c)
    return line, det, E


def main():
    checks = 0
    for q in (2, 3, 4, 5, 7):
        B, H = affine_matrices(q)
        m, n = B.shape
        Jm, Jn = np.ones((m,m), dtype=int), np.ones((n,n), dtype=int)
        Im, In = np.eye(m,dtype=int), np.eye(n,dtype=int)
        assert np.array_equal(B@B.T, q*Im+Jm)
        assert np.array_equal(B.T@B, (q-1)*In+Jn-H)
        assert np.array_equal(H@H, (q-2)*H+(q-1)*In)
        checks += 3
        if q <= 5:
            paths = graph_distances(B)
            D1 = powered_distance(q, 1, B, H)
            assert np.array_equal(paths, D1), (q, paths-D1)
            checks += 1
        alpha = log2(q/(q-1))
        N = m+n
        center = np.eye(N)-np.ones((N,N))/N
        # Check each sector against full, directly diagonalized distance matrix.
        for p in (0.0, alpha/3, alpha*0.8, alpha, alpha+0.025):
            D = powered_distance(q,p,B,H)
            vals = np.linalg.eigvalsh(center@D@center)
            line, det, E = analytic_sectors(q,p)
            boundary = abs(p-alpha)<1e-12
            if p < alpha-1e-10:
                assert vals[-1] <= 5e-9
                assert np.count_nonzero(abs(vals)<5e-9) == 1
            elif boundary:
                assert vals[-1] <= 5e-9
                assert np.count_nonzero(abs(vals)<5e-9)-1 == (5 if q==2 else q)
                assert abs(line)<1e-11
                assert det>=-1e-11
            else:
                assert vals[-1]>1e-7
                assert line>1e-7
            assert E < -1e-9
            if p<=alpha+1e-11:
                assert det>-1e-9
            checks += 6
        print(f'q={q}: vertices={N}; threshold={alpha:.9f}; '
              f'critical nullity={5 if q==2 else q}; tests OK')
    print(f'PASS ({checks} independent assertion groups, including BFS distances for q<=5)')


if __name__ == '__main__':
    main()
