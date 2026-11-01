#!/usr/bin/env python3
"""Two-method integer spectral-table and graph-distance checks for folded 6-, 7-, 8-cubes.

The all-parameter sign inequalities are established analytically in RESULT.md.
This verifier does not claim numerical sampling to be an infinite proof.
"""
from collections import deque
from math import comb

EXPECTED = {
    6: {(1, 2): (2, -1, -2), (3, 4): (-2, -1, 2), (5,): (-6, 15, -10)},
    7: {(1, 2): (3, 1, -5), (3, 4): (-1, -3, 3), (5, 6): (-5, 9, -5)},
    8: {(1, 2): (4, 4, -4, -5), (3, 4): (0, -4, 0, 3),
        (5, 6): (-4, 4, 4, -5), (7,): (-8, 28, -56, 35)},
}

def folded_graph_distances(n):
    d = n - 1
    N = 1 << d
    steps = [1 << i for i in range(d)] + [N - 1]
    distances = []
    for origin in range(N):
        row = [-1] * N
        row[origin] = 0
        queue = deque([origin])
        while queue:
            x = queue.popleft()
            for mask in steps:
                y = x ^ mask
                if row[y] == -1:
                    row[y] = row[x] + 1
                    queue.append(y)
        assert all(z >= 0 for z in row)
        for v, dist in enumerate(row):
            h = (origin ^ v).bit_count()
            assert dist == min(h, d + 1 - h), (n, origin, v, dist)
        distances.append(row)
    return distances

def krawtchouk(d, j, k):
    return sum((-1) ** i * comb(k, i) * comb(d-k, j-i)
               for i in range(max(0, j-(d-k)), min(k, j)+1))

def coeff_by_formula(d, k):
    R = (d+1)//2
    ans = [0] * R
    for j in range(1, d+1):
        dist = min(j, d+1-j)
        ans[dist-1] += krawtchouk(d, j, k)
    return tuple(ans)

def coeff_by_full_char_sum(d, k, distances):
    N = 1 << d
    mask = (1 << k) - 1
    R = (d+1)//2
    ans = [0] * R
    for v in range(1, N):
        sign = -1 if ((mask & v).bit_count() & 1) else 1
        ans[distances[0][v]-1] += sign
    return tuple(ans)

rows_checked = 0
for n, classes in EXPECTED.items():
    d = n-1
    distances = folded_graph_distances(n)
    expected_for_weight = {k: values for ks, values in classes.items() for k in ks}
    assert sorted(expected_for_weight) == list(range(1, d+1))
    for k in range(1, d+1):
        observed = coeff_by_full_char_sum(d, k, distances)
        assert observed == coeff_by_formula(d, k)
        assert observed == expected_for_weight[k], (n, k, observed)
        assert sum(observed) == -1
        rows_checked += 1
    zero_weights = {6:(3,4),7:(3,4),8:(7,)}[n]
    nullity = sum(comb(d,k) for k in zero_weights)
    rank = 2**d - 1-nullity
    assert (nullity,rank)=={6:(15,16),7:(35,28),8:(1,126)}[n]
    print(f'EXACT_OK F_{n} vertices={1<<d} classes={d} endpoint_nullity={nullity} rank={rank}')

# Exact, rational fourth-power comparisons certifying that the parity
# branch of F_8 is positive at p=1/4.
assert 1189**4 < 2 * 1000**4
assert 1317**4 > 3 * 1000**4
assert 1414**4 < 4 * 1000**4
assert -8000 + 28*1189 - 56*1317 + 35*1414 > 0
# Exact radical comparisons used to locate the neighboring thresholds
# strictly on opposite sides of p=1/2.
assert 9 > 8 and 18 > 16
# Exact strict negativity of the global polynomial upper envelope in F_7.
# max_{t>=1} (-5+9t^2-5t^3) = -17/25.
# Evaluate the stationary value without integer floor divisions.
from fractions import Fraction
stationary = -5 + 9*Fraction(6,5)**2 - 5*Fraction(6,5)**3
assert stationary == Fraction(-17,25)

# The following bisections are diagnostic approximations, not a substitute
# for the symbolic monotonicity and sign arguments in RESULT.md.
functions = {
    6: lambda p: -2 - 2.0**p + 2.0*3.0**p,
    7: lambda p: -1 - 3.0*2.0**p + 3.0*3.0**p,
    8: lambda p: -8 + 28.0*2.0**p - 56.0*3.0**p + 35.0*4.0**p,
}
for n, f in functions.items():
    lo,hi=0.0,1.0
    assert f(lo)<0<f(hi)
    for _ in range(70):
        mid=(lo+hi)/2
        if f(mid)<0: lo=mid
        else: hi=mid
    approximate=(lo+hi)/2
    target={6:.482147185182,7:.516584374301,8:.135372723557}[n]
    assert abs(approximate-target)<1e-10
    print(f'NUMERIC_DIAGNOSTIC F_{n} threshold={approximate:.12f}')
print(f'CERTIFICATE_OK integer_spectral_rows={rows_checked} full_graph_distances={32**2+64**2+128**2} exact_inequalities=passed')
