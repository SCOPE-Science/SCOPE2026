"""Numerical checks of the sharp negative-type threshold on pentagonal edge books.

Requires Python 3 and NumPy. Finite-dimensional numerical tests supplement the proof.
"""
import math
from collections import deque
import numpy as np

def distances(pages):
    count = 2 + 3 * pages
    adj = [[] for _ in range(count)]
    edges = [(0, 1)]
    for j in range(pages):
        x, y, z = 2 + 3*j, 3 + 3*j, 4 + 3*j
        edges += [(0, x), (x, y), (y, z), (z, 1)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    out = np.zeros((count, count), dtype=int)
    for source in range(count):
        ds = [-1] * count
        ds[source] = 0
        q = deque([source])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if ds[y] < 0:
                    ds[y] = ds[x] + 1
                    q.append(y)
        assert all(d >= 0 for d in ds)
        out[source, :] = ds
    return out

def sector(pages, exponent):
    r = pages
    a, b, c = (2**exponent, 3**exponent, 4**exponent)
    return np.array([
        [-2*a*r+2*b*r-2*b-2*r, -3*a*r+2*b*r-2*b+2],
        [-3*a*r+2*b*r-2*b+2, -2*a*r+c*r-c+r/2]
    ], dtype=float)

def determinant(r, p):
    e = sector(r, p)
    return float(np.linalg.det(e))

def threshold(r):
    stop = 1.2 if r == 2 else 1.0
    assert determinant(r, 0) > 0 > determinant(r, stop)
    low, high = 0.0, stop
    for _ in range(75):
        middle = (low + high) / 2
        if determinant(r, middle) > 0:
            low = middle
        else:
            high = middle
    return (low + high) / 2

def projected_spectrum(ds, p):
    n = ds.shape[0]
    matrix = ds.astype(float)**p
    q, _ = np.linalg.qr(np.eye(n)[:, :-1] - np.eye(n)[:, [-1]])
    return np.linalg.eigvalsh(q.T @ matrix @ q)

def check():
    num = 0
    for r in (2, 3, 4, 5, 8, 12, 30):
        ds = distances(r)
        assert ds.shape == (2 + 3*r, 2 + 3*r)
        assert np.array_equal(ds, ds.T)
        assert np.max(ds) == 4
        p_star = threshold(r)
        assert (1 < p_star < 1.2) if r == 2 else (0 < p_star < 1)
        assert abs(determinant(r, p_star)) < 1e-7
        for p in (p_star/2, p_star, p_star + 0.03):
            ev = projected_spectrum(ds, p)
            maximum = ev[-1]
            if p < p_star - 1e-5:
                assert maximum < -1e-5, (r, p, maximum)
            elif p > p_star + 1e-5:
                assert maximum > 1e-5, (r, p, maximum)
            else:
                assert abs(maximum) < 1e-7, (r, maximum)
                assert ev[-2] < -1e-5, (r, ev[-2])
            num += 2
        for p in (0.1, min(1.0, p_star)):
            matrix = ds.astype(float)**p
            even = np.zeros((2 + 3*r, 2))
            even[:2, 0] = -r
            even[:2, 1] = -r/2
            for j in range(r):
                even[2 + 3*j, 0] = even[4 + 3*j, 0] = 1
                even[3 + 3*j, 1] = 1
            assert np.linalg.norm(even.T @ matrix @ even - r*sector(r, p)) < 1e-7
            num += 1
    # This is an asymptotic trend check, not an infinite proof.
    kappa = 3/math.log(32/27)
    for r in (300, 1000, 3000):
        assert abs(r*threshold(r)-kappa) < 3.0
        num += 1
    print('CHECK_OK', num)

if __name__ == '__main__':
    check()
