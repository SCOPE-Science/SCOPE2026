#!/usr/bin/env python3
"""Exact bounded checks for fixed-prime-support square-perimeter Pythagorean triples."""
from itertools import product
from math import gcd, isqrt, log, comb, factorial


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def classify_square_pair(m, n):
    P = 2 * m * (m + n)
    r = isqrt(P)
    if r * r != P:
        return None
    if m % 2:
        return False
    U2 = m // 2
    U = isqrt(U2)
    V = isqrt(m + n)
    if U * U != U2 or V * V != m + n:
        return False
    if V % 2 == 0 or gcd(U, V) != 1:
        return False
    if not (2 * U * U < V * V < 4 * U * U):
        return False
    # Exact prime-support decomposition.
    fU, fV = factor(U), factor(V)
    if set(fU).intersection(fV):
        return False
    if any(p == 2 for p in fV):
        return False
    return set(factor(P)) == ({2} | set(fU) | set(fV))


def choose_a(Uodd, V):
    if V <= Uodd:
        return None
    a = 0
    while (1 << (a + 1)) * Uodd <= V:
        a += 1
    return a


def predicted_tuple(primes, A_mask, exponents):
    Uodd = 1
    V = 1
    for i, (p, e) in enumerate(zip(primes, exponents)):
        if A_mask >> i & 1:
            V *= p ** e
        else:
            Uodd *= p ** e
    a = choose_a(Uodd, V)
    if a is None:
        return None
    U = (1 << a) * Uodd
    # This is exactly {L_A}>1/2 after a=floor(L_A).
    if V * V <= 2 * U * U:
        return None
    if V >= 2 * U:
        return None
    m = 2 * U * U
    n = V * V - 2 * U * U
    x, y, z = m * m - n * n, 2 * m * n, m * m + n * n
    P = x + y + z
    return (m, n, x, y, z, P)


def count_fixed_support(primes, logX):
    # Enumerate a safe exponent box. Since P>V^4, every exponent on V is bounded
    # by logX/(4 log p); exponents on Uodd are then bounded by V/Uodd>sqrt(2).
    r = len(primes)
    bounds = [int(logX / (4 * log(p))) + 3 for p in primes]
    total = 0
    for mask in range(1, 1 << r):
        for exps in product(*[range(1, B + 1) for B in bounds]):
            data = predicted_tuple(primes, mask, exps)
            if data is None:
                continue
            if log(data[-1]) <= logX + 1e-12:
                total += 1
    return total


def main():
    primitive_pairs = square_cases = bad = 0
    for m in range(2, 2501):
        for n in range(1, m):
            if gcd(m, n) != 1 or ((m - n) & 1) == 0:
                continue
            primitive_pairs += 1
            P = 2 * m * (m + n)
            rP = isqrt(P)
            if rP * rP != P:
                continue
            square_cases += 1
            if classify_square_pair(m, n) is not True:
                bad += 1

    constructed = failures = 0
    for primes in ([3], [3, 5], [3, 5, 7]):
        r = len(primes)
        for mask in range(1, 1 << r):
            for exps in product(range(1, 5), repeat=r):
                data = predicted_tuple(primes, mask, exps)
                if data is None:
                    continue
                constructed += 1
                m, n, x, y, z, P = data
                expected_support = {2, *primes}
                if not (0 < n < m and gcd(m, n) == 1 and ((m - n) & 1) == 1 and
                        x * x + y * y == z * z and factor(P).keys() == expected_support):
                    failures += 1

    print(f"primitive Euclid pairs checked: {primitive_pairs}")
    print(f"square-perimeter cases checked: {square_cases}")
    print(f"normal-form/support mismatches: {bad}")
    print(f"fixed-support constructions checked: {constructed}")
    print(f"construction failures: {failures}")

    print("asymptotic spot checks (count / leading prediction):")
    for primes, decimal_exponents in [([3], [40, 80, 120]), ([3, 5], [40, 80, 120]), ([3, 5, 7], [20, 40])]:
        r = len(primes)
        C = comb(2*r - 1, r) / (2 * (4 ** r) * factorial(r))
        C /= __import__('math').prod(log(p) for p in primes)
        vals = []
        for D in decimal_exponents:
            LX = D * log(10)
            exact = count_fixed_support(primes, LX)
            pred = C * (LX ** r)
            vals.append(f"10^{D}: {exact}/{pred:.3f}={exact/pred:.4f}")
        print(f"  S={primes}: " + "; ".join(vals))

    if bad or failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
