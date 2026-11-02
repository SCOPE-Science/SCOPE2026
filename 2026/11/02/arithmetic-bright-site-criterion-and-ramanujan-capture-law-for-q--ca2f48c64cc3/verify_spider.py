#!/usr/bin/env python3
"""Numerically compare exact site-resolved hub-trap survival on spider graphs.

Only the standard library and NumPy are required. The direct calculation forms
spectral projectors of the real symmetric adjacency matrix and subtracts the
hub-visible direction in each eigenspace; no arithmetic formulas are used in it.
"""
import itertools
from math import gcd, lcm
import numpy as np


def mobius(n):
    if n == 1:
        return 1
    p = 2
    parity = 0
    while p * p <= n:
        if n % p == 0:
            n //= p
            parity += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        parity += 1
    return -1 if parity % 2 else 1


def totient(q):
    return sum(gcd(q, k) == 1 for k in range(1, q + 1))


def ramanujan(q, t):
    g = gcd(q, t)
    return sum(d * mobius(q // d) for d in range(1, g + 1) if g % d == 0)


def exact_survival(arms):
    L = [a + 1 for a in arms]
    values = [0.0]
    for i, Li in enumerate(L):
        for t in range(1, Li):
            s = 0.0
            for q in range(2, Li + 1):
                if Li % q:
                    continue
                sharing = [Lk for Lk in L if Lk % q == 0]
                count = len(sharing)
                if count < 2:
                    continue
                attenuation = 1.0 - (1 / Li) / sum(1 / Lk for Lk in sharing)
                s += (totient(q) - ramanujan(q, t)) * attenuation / Li
            values.append(s)
    ds = sum(totient(q) * (sum(Li % q == 0 for Li in L) - 1)
             for q in range(2, max(L) + 1)
             if sum(Li % q == 0 for Li in L) >= 2)
    return np.array(values), ds


def adjacency(arms):
    n = 1 + sum(arms)
    A = np.zeros((n, n))
    k = 1
    for a in arms:
        A[0, k] = A[k, 0] = 1
        for t in range(a - 1):
            A[k + t, k + t + 1] = A[k + t + 1, k + t] = 1
        k += a
    return A


def spectral_survival(arms):
    A = adjacency(arms)
    w, U = np.linalg.eigh(A)
    D = np.zeros_like(A)
    a = 0
    while a < len(w):
        b = a + 1
        while b < len(w) and abs(w[b] - w[a]) < 1e-7:
            b += 1
        V = U[:, a:b]
        P = V @ V.T
        bnorm = P[0, 0]
        if bnorm > 1e-8:
            root_col = P[:, 0]
            D += P - np.outer(root_col, root_col) / bnorm
        else:
            D += P
        a = b
    return np.diag(D), np.trace(D)


def criterion(arms):
    L = [a + 1 for a in arms]
    result = [True]
    for i, Li in enumerate(L):
        G = 1
        for j, Lj in enumerate(L):
            if i != j:
                G = lcm(G, gcd(Li, Lj))
        result.extend(t % G == 0 for t in range(1, Li))
    return result


def run():
    cases = 0
    positions = 0
    max_difference = 0.0
    for k in [3, 4, 5]:
        limit = 6 if k == 3 else (4 if k == 4 else 3)
        for arms in itertools.product(range(1, limit + 1), repeat=k):
            s, d = exact_survival(arms)
            direct, direct_d = spectral_survival(arms)
            error = float(np.max(np.abs(s - direct)))
            max_difference = max(error, max_difference)
            assert error < 1e-8, (arms, error, s, direct)
            assert abs(d - direct_d) < 1e-8, (arms, d, direct_d)
            assert all((abs(v) < 1e-8) == pred for v,pred in zip(s, criterion(arms))), (arms, s)
            assert abs(s.sum() - d) < 1e-8, (arms, s.sum(), d)
            cases += 1
            positions += len(s)
    arms = (1,3,5)
    s, d = exact_survival(arms)
    print('Exact-vs-direct spectral-projector cases:', cases)
    print('Checked site amplitudes:', positions)
    print('Max absolute difference:', f'{max_difference:.3g}')
    print('Example arm lengths:', arms)
    print('Example exact dark dimension:', d)
    print('Example site survival probabilities:', np.round(s, 12).tolist())
    try:
        from scipy.linalg import expm
    except ImportError:
        print('Finite-time absorbing evolution skipped: SciPy unavailable')
    else:
        decay_error = 0.0
        for arms in [(1, 3, 5), (1, 2, 4), (2, 2, 2), (3, 6, 9)]:
            A = adjacency(arms)
            P = np.zeros_like(A)
            P[0, 0] = 1
            U = expm(-1j * (A - .5j * P) * 12000)
            survival_at_t = np.sum(np.abs(U)**2, axis=0)
            expected, _ = exact_survival(arms)
            decay_error = max(decay_error, float(np.max(np.abs(survival_at_t - expected))))
        assert decay_error < 1e-8, decay_error
        print('Absorbing semigroup samples:', 4)
        print('Max finite-time vs infinite-limit difference at t=12000:', f'{decay_error:.3g}')
    print('VERIFIED')

if __name__ == '__main__':
    run()
