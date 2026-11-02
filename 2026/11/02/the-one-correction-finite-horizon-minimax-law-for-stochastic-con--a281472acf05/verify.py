#!/usr/bin/env python3
"""Exact finite-family checks of the stochastic consensus theorem.

Uses only Python's standard library. These checks supplement the proof; no
finite enumeration is presented as a proof of the infinite graph family.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks = 0

def require(condition, description="check failed"):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def optimum(degree, gap, rounds):
    assert degree >= 2 and F(0) < gap <= degree and rounds >= 1
    h = F(gap, 2 * degree)
    rho = 1 - 2 * h
    a = rho ** (rounds - 1)
    beta = a * (1 - h) / (1 + h * a)
    return beta, (1 + beta) / (2 * degree)

def spectrum_factor(eigenvalue, steps):
    value = F(1)
    for t in steps:
        value *= 1 - eigenvalue * t
    return value

def verify_spectrum(degree, gap, spectrum, rounds):
    beta, correction = optimum(degree, gap, rounds)
    steps = [F(1, degree)] * (rounds - 1) + [correction]
    require(F(0) <= correction <= F(1, degree))
    require(abs(spectrum_factor(gap, steps)) == beta)
    require(abs(spectrum_factor(2 * degree, steps)) == beta)
    for eig in spectrum:
        if eig:
            require(abs(spectrum_factor(eig, steps)) <= beta,
                    f"degree={degree}, gap={gap}, rounds={rounds}, eigenvalue={eig}")
    # Pair compression is exact, with strictness away from endpoints.
    h = F(gap, 2 * degree)
    for u, v in product([F(i, 10) for i in range(11)], repeat=2):
        slow = lambda z: 1 - h * (1 + z)
        surplus = slow(u) * slow(v) - slow(1) * slow(u * v)
        require(surplus == h * (1 - h) * (1 - u) * (1 - v))
        require(surplus >= 0)
        if u != 1 and v != 1:
            require(surplus > 0)
    # Check all rational grids of 1--4 rounds; none beats the certified value.
    if rounds <= 4:
        choices = [F(i, 2 * degree * 4) for i in range(9)]
        for seq in product(choices, repeat=rounds):
            low = abs(spectrum_factor(gap, seq))
            high = abs(spectrum_factor(2 * degree, seq))
            require(max(low, high) >= beta)

def graph_cycle(n):
    return [[1 if (j - i) % n in (1, n - 1) else 0 for j in range(n)] for i in range(n)]

def graph_cube(d):
    return [[int((i ^ j).bit_count() == 1) for j in range(1 << d)] for i in range(1 << d)]

def graph_complete_bipartite(n):
    return [[int((i < n) != (j < n)) for j in range(2 * n)] for i in range(2 * n)]

def graph_crown(n):
    return [[int((i < n) != (j < n) and (i % n) != (j % n))
             for j in range(2 * n)] for i in range(2 * n)]

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def characteristic_coefficients(L):
    n = len(L)
    B = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    coeff = [F(1)]
    for k in range(1, n + 1):
        B = matmul(L, B)
        c = -sum(B[i][i] for i in range(n)) / k
        coeff.append(c)
        for i in range(n):
            B[i][i] += c
    return coeff

def polynomial_from_roots(roots):
    coeff = [F(1)]
    for lam in roots:
        next_coeff = [F(0)] * (len(coeff) + 1)
        for i, c in enumerate(coeff):
            next_coeff[i] += c
            next_coeff[i + 1] -= c * lam
        coeff = next_coeff
    return coeff

def verify_graph(adjacency, degree, spectrum, gap):
    n = len(adjacency)
    require(n > 2)
    for i in range(n):
        require(sum(adjacency[i]) == degree)
        require(adjacency[i][i] == 0)
        for j in range(n):
            require(adjacency[i][j] == adjacency[j][i])
    L = [[F(degree * int(i == j) - adjacency[i][j]) for j in range(n)]
         for i in range(n)]
    require(characteristic_coefficients(L) == polynomial_from_roots(spectrum))
    require(min(lam for lam in spectrum if lam > 0) == gap)
    require(max(spectrum) == 2 * degree)
    for rounds in (1, 2, 3, 5):
        beta, correction = optimum(degree, gap, rounds)
        seq = [F(1, degree)] * (rounds - 1) + [correction]
        H = [[F(int(i == j)) for j in range(n)] for i in range(n)]
        for t in seq:
            P = [[F(int(i == j)) - t * L[i][j] for j in range(n)] for i in range(n)]
            for row in P:
                require(all(x >= 0 for x in row))
                require(sum(row) == 1)
            H = matmul(P, H)
        for row in H:
            require(sum(row) == 1)
            require(all(x >= 0 for x in row))
        if beta == 0:
            require(all(H[i][j] == F(1, n) for i in range(n) for j in range(n)))

def run():
    # Rational spectral families with multiplicity and exact matrices.
    verify_graph(graph_cycle(6), 2, [0, 1, 1, 3, 3, 4], F(1))
    verify_graph(graph_cube(3), 3, [0] + [2]*3 + [4]*3 + [6], F(2))
    verify_graph(graph_complete_bipartite(3), 3, [0] + [3]*4 + [6], F(3))
    verify_graph(graph_crown(4), 3, [0] + [2]*3 + [4]*3 + [6], F(2))
    for d in range(2, 17):
        spectrum = [F(2 * k) for k in range(d + 1)]
        for rounds in (1, 2, 3, 4, 5, 8, 12):
            verify_spectrum(d, F(2), spectrum, rounds)
    for d in range(2, 17):
        for rounds in (1, 2, 3, 4, 5, 9):
            verify_spectrum(d, F(d), [0, d, 2 * d], rounds)
    # Crown graphs: degree=d=n-1, positive eigenvalues n-2, n, 2(n-1).
    for n in range(4, 18):
        d = n - 1
        for rounds in (1, 2, 3, 5, 9):
            verify_spectrum(d, F(n - 2), [0, n-2, n, 2*d], rounds)
    print('ALL_CHECKS_PASSED', checks)

if __name__ == '__main__':
    run()
