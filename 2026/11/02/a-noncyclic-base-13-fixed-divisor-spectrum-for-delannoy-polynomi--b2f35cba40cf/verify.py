"""Exact arithmetic checks for digit spectra of Delannoy-polynomial fixed divisors.

Requires only Python 3 standard library. These checks are finite; the accompanying
mathematical proof supplies the universal statements.
"""
from collections import defaultdict
from math import comb, gcd, factorial

PRIMES = (3, 5, 7, 11, 13)
EXPECTED = {
    3: ((0, 2), 1),
    5: ((0, 2, 4), 4),
    7: ((0, 2, 4, 6), 6),
    11: ((0, 4, 6, 10), 10),
    13: ((0, 4, 6, 8, 12), 144),
}


def direct(n, x, p):
    return sum(comb(n, j) * comb(n + j, j) * pow(x, j, p)
               for j in range(n + 1)) % p


def factored(n, x, p):
    ans = 1
    while n:
        ans = ans * direct(n % p, x, p) % p
        n //= p
    return ans


def vector(p, d):
    return tuple(direct(d, x, p) for x in range(p))


def multiply(p, a, b):
    return tuple((u*v) % p for u, v in zip(a, b))


def generated_group(p, vectors):
    one = (1,) * p
    group = {one}
    todo = [one]
    while todo:
        g = todo.pop()
        for h in vectors:
            nxt = multiply(p, g, h)
            if nxt not in group:
                group.add(nxt)
                todo.append(nxt)
    return group


def exact_count(k):
    acc = 0
    for a in range(0, k + 1, 12):
        for b in range(0, k - a + 1, 12):
            acc += comb(k, a)*comb(k-a, b)*(2 ** (k - b))
    return acc


def verify():
    digit_cells = 0
    full_polynomial_checks = 0
    for p in PRIMES:
        vectors = [vector(p, d) for d in range(p)]
        digit_cells += p*p
        good = tuple(d for d in range(p) if all(vectors[d]))
        assert good == EXPECTED[p][0], (p, good)
        group = generated_group(p, [vectors[d] for d in good])
        assert len(group) == EXPECTED[p][1], (p, len(group))
        assert vectors[0] == vectors[p-1] == (1,) * p
        # Coefficient-sum implementation versus independent digit reduction.
        for n in range(105):
            for x in range(p):
                assert direct(n, x, p) == factored(n, x, p), (p, n, x)
                full_polynomial_checks += 1

    p = 13
    f4, f6, f8 = vector(p, 4), vector(p, 6), vector(p, 8)
    assert f4 == f8
    assert (f4[1], f6[1], f4[5], f6[5]) == (9, 6, 5, 2)
    logs = {pow(2, k, p): k for k in range(12)}
    assert len(logs) == 12
    determinant = (logs[f4[1]] * logs[f6[5]]
                   - logs[f6[1]] * logs[f4[5]])
    assert determinant == -37 and gcd(determinant, 12) == 1
    assert vector(13, 2)[1] == vector(13, 10)[1] == 0
    for d in (1, 3, 5, 7, 9, 11):
        assert vector(13, d)[6] == 0

    # Independent dynamic-programming count on the 12 x 12 residue group.
    counts = {(0, 0): 1}
    checked = 0
    for k in range(33):
        assert counts.get((0, 0), 0) == exact_count(k), k
        checked += 1
        nxt = defaultdict(int)
        for (a, b), value in counts.items():
            nxt[a, b] += 2*value
            nxt[(a+1) % 12, b] += 2*value
            nxt[a, (b+1) % 12] += value
        counts = nxt

    # Brute finite index checks, independently evaluating every residue x.
    finite_indices = 0
    for n in range(600):
        a = b = 0
        t = n
        permissible = True
        while t:
            d = t % 13
            if d not in EXPECTED[13][0]:
                permissible = False
            if d in (4, 8): a += 1
            if d == 6: b += 1
            t //= 13
        criterion = permissible and (a % 12 == b % 12 == 0)
        observed = all(direct(n, x, 13) == 1 for x in range(13))
        assert criterion == observed, n
        finite_indices += 1
    print('VERIFY_OK digit_cells=%d direct_vs_digits=%d exact_group_counts=%d '
          'index_congruences=%d group_order_13=144 determinant=%d' %
          (digit_cells, full_polynomial_checks, checked,
           finite_indices, determinant))


if __name__ == '__main__':
    verify()
