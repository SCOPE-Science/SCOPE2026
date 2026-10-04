#!/usr/bin/env python3
import cmath
import math
from math import comb

def residue_weights(N, k):
    p = [0.0] * N
    for j in range(k + 1):
        p[j % N] += comb(k, j) / (2.0 ** k)
    return p

def gram(N, k):
    return [[(math.cos(math.pi * (a-b) / N) ** k) / N
             for b in range(N)] for a in range(N)]

def character(N, k, r):
    return [cmath.exp(1j * (k - 2*r) * math.pi * a / N) for a in range(N)]

def matvec(A, v):
    return [sum(A[a][b] * v[b] for b in range(len(v))) for a in range(len(A))]

def success(p):
    N = len(p)
    return sum(math.sqrt(max(0.0, x)) for x in p) ** 2 / N

def main():
    for N in range(3, 9):
        for k in (1, 2, 3, 4, 5, 8, 11, 14):
            p = residue_weights(N, k)
            A = gram(N, k)
            # The gauge-shifted cyclic characters are exact eigenvectors.
            for r in range(N):
                v = character(N, k, r)
                Av = matvec(A, v)
                residual = max(abs(Av[a] - p[r] * v[a]) for a in range(N))
                assert residual < 5e-11, (N, k, r, residual)
            assert abs(sum(p) - 1.0) < 2e-14
            P = success(p)
            assert 1.0/N - 1e-13 <= P <= 1.0 + 1e-13
    for N in (3, 4, 5, 6, 8, 10):
        c = math.cos(math.pi / N)
        k = 18 if N <= 4 else 40
        P = success(residue_weights(N, k))
        ratio = (1.0 - P) / (c ** (2*k))
        assert abs(ratio - 0.5) < (0.03 if N <= 4 else 0.08), (N, k, ratio)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
