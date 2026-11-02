"""Independent small-dimension checks for weighted-permutation evolution algebras.

Run: python3 verify.py
Only the Python standard library is required.
"""
from itertools import permutations, product
from fractions import Fraction
from math import factorial, gcd


def multiply(q, a, b):
    if q not in (4, 8):
        return a * b % q
    degree = 2 if q == 4 else 3
    modulus = 0b111 if q == 4 else 0b1011
    raw = 0
    for shift in range(degree):
        if (b >> shift) & 1:
            raw ^= a << shift
    for shift in range(2 * degree - 2, degree - 1, -1):
        if (raw >> shift) & 1:
            raw ^= modulus << (shift - degree)
    return raw


def cycle_sizes(sigma):
    seen = set()
    out = []
    for i in range(len(sigma)):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = sigma[j]
        out.append(size)
    return out


def number_of_idempotents_bruteforce(q, sigma, a):
    square = [multiply(q, x, x) for x in range(q)]
    total = 0
    for x in product(range(q), repeat=len(sigma)):
        out = [0] * len(sigma)
        for i, j in enumerate(sigma):
            out[j] = multiply(q, a[i], square[x[i]])
        if tuple(out) == x:
            total += 1
    return total


def moments_by_cycle_index(q, N, r):
    g = [0] + [gcd(2 ** k - 1, q - 1) for k in range(1, N + 1)]
    h = [Fraction(0)] + [Fraction((1 + d) ** r - 1, d) + 1 for d in g[1:]]
    vals = [Fraction(1)]
    for n in range(1, N + 1):
        vals.append(sum(h[k] * vals[n - k] for k in range(1, n + 1)) / n)
    return vals


def verify():
    for q in (2, 3, 4, 5, 7, 8):
        for n in range(1, 5 if q in (2, 3, 4) else 4):
            total, sum1, sum2, zero_only = 0, 0, 0, 0
            for sigma in permutations(range(n)):
                # Keep cycle structure separate from the direct multiplication check.
                sizes = cycle_sizes(sigma)
                for weights in product(range(1, q), repeat=n):
                    count = number_of_idempotents_bruteforce(q, sigma, weights)
                    total += 1
                    sum1 += count
                    sum2 += count * count
                    zero_only += (count == 1)
                    assert count >= 1
                    allowed_factors = [{1, 1 + gcd(2 ** k - 1, q - 1)} for k in sizes]
                    possible = {1}
                    for choices in allowed_factors:
                        possible = {a * b for a in possible for b in choices}
                    assert count in possible, (q, n, sigma, weights, count, possible)
            assert total == factorial(n) * (q - 1) ** n
            exact1 = Fraction(sum1, total)
            exact2 = Fraction(sum2, total)
            assert exact1 == n + 1
            assert exact1 == moments_by_cycle_index(q, n, 1)[n]
            assert exact2 == moments_by_cycle_index(q, n, 2)[n]
            if q in (4, 7):
                prob_zero = Fraction(zero_only, total)
                if n % 2:
                    assert prob_zero == 0
                else:
                    k = n // 2
                    val = Fraction(1)
                    for j in range(k):
                        val *= Fraction(3 * j + 1, 3 * (j + 1))
                    assert prob_zero == val, (n, prob_zero, val)
            print(f"FINITE_FIELD_OK q={q} n={n} E1={exact1} E2={exact2}")
    print("VERIFY_OK")


if __name__ == '__main__':
    verify()
