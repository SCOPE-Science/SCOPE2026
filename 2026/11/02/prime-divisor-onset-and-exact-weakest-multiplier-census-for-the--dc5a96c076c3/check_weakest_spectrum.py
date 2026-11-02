"""Exact finite checks for the twisted baker weakest-multiplier census.

Only Python's standard library is used. Finite tests are not a proof of
statements quantified over arbitrary dimensions and return lengths.
"""
from collections import Counter
from itertools import product
from math import comb, gcd


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def period_jacobian_cycles(M, word):
    """Return (length, base-two exponent, sign) for each monomial cycle."""
    perm, signs, powers = list(range(M)), [1] * M, [0] * M
    for branch in word:
        new_perm, new_signs, new_powers = [], [], []
        for j in range(M):
            k, s, a = perm[j], signs[j], powers[j]
            if branch == 'L':
                if k == 0:
                    a += 1
            else:
                if k == M - 1:
                    k, s, a = 0, -s, a + 1
                else:
                    k += 1
            new_perm.append(k)
            new_signs.append(s)
            new_powers.append(a)
        perm, signs, powers = new_perm, new_signs, new_powers

    cycles, seen = [], set()
    for first in range(M):
        if first in seen:
            continue
        j, power, sign, length = first, 0, 1, 0
        while j not in seen:
            seen.add(j)
            power += powers[j]
            sign *= signs[j]
            length += 1
            j = perm[j]
        assert j == first
        cycles.append((length, power, sign))
    return cycles


def compositions(k, total):
    if k == 1:
        yield (total,)
    else:
        for v in range(total + 1):
            for tail in compositions(k - 1, total - v):
                yield (v,) + tail


def histogram_formula(M, n, t):
    g = gcd(M, t)
    s, L = t // g, n - t
    result = Counter()
    for vec in compositions(g, L):
        ways = comb(vec[0] + s, s)
        for v in vec[1:]:
            ways *= comb(v + s - 1, s - 1)
        result[t + g * min(vec)] += ways
    return result


def is_primitive(word):
    n = len(word)
    return all(word != word[:d] * (n // d)
               for d in range(1, n) if n % d == 0)


def test():
    tested = 0
    for M in range(2, 10):
        p = next(d for d in range(2, M + 1) if M % d == 0)
        for n in range(1, 10):
            counts = {t: Counter() for t in range(1, n + 1)}
            all_min = []
            for word in product('LR', repeat=n):
                t = word.count('R')
                if t == 0:
                    continue
                cycles = period_jacobian_cycles(M, word)
                g, s = gcd(M, t), t // gcd(M, t)
                assert len(cycles) == g
                assert all(length == M // g and sign == (-1) ** s
                           and power >= s for length, power, sign in cycles)
                assert sum(power for _, power, _ in cycles) == n
                # Each cycle gives eigenvalues of modulus 2**(power/length).
                exponents = [power * g for _, power, _ in cycles]
                e = min(exponents)
                counts[t][e] += 1
                all_min.append(e)
                tested += 1
            for t in range(1, n + 1):
                assert counts[t] == histogram_formula(M, n, t)
                assert sum(counts[t].values()) == comb(n, t)
            assert min(all_min) == min(n, p)
            multiplicity = all_min.count(min(n, p))
            expected = ((1 << n) - 1 if n <= p else
                        choose(n, p) - choose(n - p, p) -
                        choose(n - p - 1, p - 1))
            assert multiplicity == expected
            witness = ('R' + 'L' * (n - 1) if n <= p else
                       'R' * p + 'L' * (n - p))
            assert is_primitive(witness)
            wc = period_jacobian_cycles(M, witness)
            assert min(power * len(wc) for _, power, _ in wc) == min(n, p)
    print('CHECK_OK', tested, 'signed-monomial words checked')


if __name__ == '__main__':
    test()
