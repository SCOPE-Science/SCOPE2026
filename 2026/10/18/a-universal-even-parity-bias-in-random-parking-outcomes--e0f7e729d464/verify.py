#!/usr/bin/env python3
"""Independent exact checks for signed parity of classical parking outcomes.

Runs with Python 3 standard library only. All calculations are integer or rational.
"""
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


def qbinom_at_minus_one(m, k):
    if not (0 <= k <= m):
        return 0
    if m % 2 == 0 and k % 2 == 1:
        return 0
    return comb(m // 2, k // 2)


def signed_vacancy_recurrence(nmax):
    ans = [1]
    for n in range(1, nmax + 1):
        cur = sum((k + 1) * (-1) ** (n - 1 - k)
                  * qbinom_at_minus_one(n - 1, k)
                  * ans[k] * ans[n - 1 - k]
                  for k in range(n))
        ans.append(cur)
    return ans


def mul(a, b, max_degree):
    out = [Fraction(0) for _ in range(max_degree + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= max_degree:
                out[i + j] += x * y
    return out


def signed_from_positive_ode(nmax):
    # E'(z) = E(z)^3 + 8 z E(z)^2 E'(z) + 4 z^2 E(z)^2 E''(z)
    # E(z) = sum_{m>=0} T_(2m) z^m/m!.
    mmax = nmax // 2
    E = [Fraction(1)]
    for m in range(mmax):
        E2 = mul(E, E, m)
        E3 = mul(E2, E, m)
        E1 = [(i + 1) * E[i + 1] for i in range(len(E) - 1)]
        E22 = [(i + 2) * (i + 1) * E[i + 2]
               for i in range(len(E) - 2)]
        rhs = E3[m]
        if m >= 1:
            rhs += 8 * mul(E2, E1, m - 1)[m - 1]
        if m >= 2:
            rhs += 4 * mul(E2, E22, m - 2)[m - 2]
        E.append(rhs / (m + 1))
    out = [None] * (nmax + 1)
    for m in range(mmax + 1):
        out[2 * m] = E[m] * factorial(m)
        assert out[2 * m].denominator == 1
        out[2 * m] = int(out[2 * m])
        if 2 * m + 1 <= nmax:
            sq = mul(E, E, m)
            val = (m + 1) * sq[m] * factorial(m)
            assert val.denominator == 1
            out[2 * m + 1] = int(val)
    return out


def outcome_sign(positions):
    inversions = sum(positions[i] > positions[j]
                     for i in range(len(positions))
                     for j in range(i + 1, len(positions)))
    return -1 if inversions % 2 else 1


def signed_from_preferences(n):
    total = 0
    signed = 0
    for wants in product(range(n), repeat=n):
        occupied = [False] * n
        positions = []
        for want in wants:
            j = want
            while j < n and occupied[j]:
                j += 1
            if j == n:
                break
            occupied[j] = True
            positions.append(j)
        else:
            total += 1
            signed += outcome_sign(positions)
    return total, signed


def signed_from_subset_dp(n):
    dp = [0] * (1 << n)
    dp[0] = 1
    for mask in range((1 << n) - 1):
        if dp[mask] == 0:
            continue
        for j in range(n):
            if (mask >> j) & 1:
                continue
            choices = 1
            k = j - 1
            while k >= 0 and ((mask >> k) & 1):
                choices += 1
                k -= 1
            inv = (mask >> (j + 1)).bit_count()
            dp[mask | (1 << j)] += dp[mask] * choices * (-1 if inv % 2 else 1)
    return dp[-1]


def signed_shuffle_direct(m, k):
    result = 0
    for left in combinations(range(m), k):
        ls = set(left)
        inversions = sum(1 for i in range(m) if i not in ls
                         for j in range(i + 1, m) if j in ls)
        result += (-1) ** inversions
    return result


def main():
    checks = 0
    for m in range(0, 10):
        for k in range(m + 1):
            assert signed_shuffle_direct(m, k) == qbinom_at_minus_one(m, k)
            checks += 1
    nmax = 24
    vacancy = signed_vacancy_recurrence(nmax)
    ode = signed_from_positive_ode(nmax)
    for n in range(nmax + 1):
        assert vacancy[n] == ode[n], (n, vacancy[n], ode[n])
        assert vacancy[n] > 0
        checks += 2
    for n in range(1, 14):
        assert signed_from_subset_dp(n) == vacancy[n]
        checks += 1
    for n in range(1, 7):
        total, signed = signed_from_preferences(n)
        assert total == (n + 1) ** (n - 1)
        assert signed == vacancy[n]
        checks += 2
    assert vacancy[:11] == [1, 1, 1, 4, 11, 72, 335, 2944, 19449, 211520, 1815089]
    checks += 1
    print(f'PASS {checks} assertions; direct parking preferences through n=6; '
          'subset DP through n=13; two algebraically independent recurrences through n=24.')
    print('T_n (n=1..14):', vacancy[1:15])


if __name__ == '__main__':
    main()
