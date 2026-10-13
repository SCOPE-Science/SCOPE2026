#!/usr/bin/env python3
"""Exact-arithmetic checks for quantum mixing on anisotropically weighted cubes.

No external packages required. Finite checks corroborate, but do not replace,
the symbolic argument for all dimensions and admissible couplings.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from collections import defaultdict
from math import gcd, pi, cos, sin
from functools import reduce


def signed_zero_count(weights):
    n = len(weights)
    out = []
    for mask in range(1 << n):
        sub = [weights[j] for j in range(n) if mask >> j & 1]
        cnt = sum(sum(e * a for e, a in zip(signs, sub)) == 0
                  for signs in product((-1, 1), repeat=len(sub)))
        out.append(Q(cnt, 1 << len(sub)))
    return out


def spectral_projector_average(weights):
    n = len(weights)
    N = 1 << n
    eigs = defaultdict(list)
    for z in range(N):
        eigs[sum(((-1) ** (z >> j & 1)) * weights[j] for j in range(n))].append(z)
    M = [[Q(0) for y in range(N)] for x in range(N)]
    for z_group in eigs.values():
        for x in range(N):
            for y in range(N):
                parity = x ^ y
                proj = Q(sum(-1 if (z & parity).bit_count() % 2 else 1
                             for z in z_group), N)
                M[x][y] += proj * proj
    return M


def walsh_average(modes):
    N = len(modes)
    return [[sum(((-v if (S & (x ^ y)).bit_count() % 2 else v)
                   for S, v in enumerate(modes)), Q(0)) / N
             for y in range(N)] for x in range(N)]


def rank_exact(matrix):
    mat = [row[:] for row in matrix]
    R = len(mat)
    cols = len(mat[0])
    rank = 0
    for c in range(cols):
        piv = next((r for r in range(rank, R) if mat[r][c]), None)
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pivot = mat[rank][c]
        for r in range(rank+1, R):
            if not mat[r][c]:
                continue
            factor = mat[r][c] / pivot
            mat[r][c:] = [a - factor*b for a,b in zip(mat[r][c:], mat[rank][c:])]
        rank += 1
        if rank == R:
            break
    return rank


def distinct_sums(weights):
    ss = {0}
    for w in weights:
        ss |= {x + w for x in ss}
    return len(ss) == (1 << len(weights))


def basic_checks():
    profiles = [
        (1,), (1, 1), (1, 2), (1, 3), (2, 6),
        (1, 1, 1), (1, 2, 4), (1, 3, 5), (2, 3, 4),
        (1, 1, 2), (1, 2, 3), (2, 2, 2),
        (1, 1, 1, 1), (1, 2, 3, 4), (1, 2, 4, 8),
        (1, 3, 5, 11), (1, 1, 2, 3), (2, 4, 6, 8),
        (1, 2, 4, 8, 16), (1, 1, 2, 2, 3),
        (1, 3, 5, 11, 23),
    ]
    entries = 0
    for w in profiles:
        modes = signed_zero_count(w)
        direct = spectral_projector_average(w)
        other = walsh_average(modes)
        assert direct == other, ('spectral/mode disagreement', w)
        N = len(direct)
        assert all(sum(row) == 1 for row in direct), w
        assert rank_exact(direct) == sum(v != 0 for v in modes), w
        assert (all(direct[x][y] == Q(1,N) for x in range(N) for y in range(N))
                == distinct_sums(w)), w
        entries += N*N
    return len(profiles), entries


def budget_checks():
    nlists = 0
    for d in range(1, 6):
        B = (1 << d) - 1
        solutions = []
        for w in combinations_with_replacement(range(1, B+1), d):
            if sum(w) > B:
                continue
            nlists += 1
            if distinct_sums(w):
                solutions.append(w)
        assert solutions == [tuple(1 << j for j in range(d))], (d, solutions)
    return nlists


def finite_window_checks():
    profiles = [(1,2,4), (1,3,5), (2,4,8), (1,1,2), (2,3,4),
                (1,2,4,8), (1,1,1,1), (1,3,5,11)]
    max_error = 0.0
    tested = 0
    for w in profiles:
        g = reduce(gcd, w)
        T = pi/(2*g)
        N_steps = 8192
        coeffs = signed_zero_count(w)
        for mask in range(1 << len(w)):
            coords = [j for j in range(len(w)) if mask >> j & 1]
            actual = 0.0
            for k in range(N_steps):
                t = T*(k+0.5)/N_steps
                p = 1.0
                for j in coords:
                    p *= cos(2*w[j]*t)
                actual += p
            actual /= N_steps
            err = abs(actual - float(coeffs[mask]))
            max_error = max(max_error, err)
            assert err < 2e-12, (w, mask, err)
            tested += 1
        same_2adic = len({(a & -a) for a in w}) == 1
        v_min = min(a & -a for a in w)
        t_instant = pi/(4*v_min)
        actual_uniform = all(abs(cos(2*a*t_instant)) < 1e-12 for a in w)
        assert same_2adic == actual_uniform, w
    return tested, max_error


if __name__ == '__main__':
    p, e = basic_checks()
    budgets = budget_checks()
    finite, error = finite_window_checks()
    print(f'VERIFY_OK exact_profiles={p} exact_entries={e} '
          f'integer_budget_profiles={budgets} finite_window_modes={finite} '
          f'max_midpoint_error={error:.3e}')
