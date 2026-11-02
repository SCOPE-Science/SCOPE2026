"""Independent finite-field census for idempotents in weighted permutation evolution algebras.

Run: python3 verify.py
Only Python's standard library is required. The census tests x^2=x directly;
probability/moment predictions come from cycle-length arithmetic and a recurrence.
"""
from fractions import Fraction
from itertools import permutations, product
from math import factorial, gcd


def field(q):
    """Products for prime fields and GF(4), GF(8) using fixed irreducibles."""
    if q in (2, 3, 5, 7, 11):
        return [[(a * b) % q for b in range(q)] for a in range(q)]
    if q not in (4, 8):
        raise ValueError(q)
    degree = 2 if q == 4 else 3
    polynomial = 0b111 if q == 4 else 0b1011  # t^2+t+1; t^3+t+1
    tab = []
    for a in range(q):
        row = []
        for b in range(q):
            z = 0
            aa, bb = a, b
            while bb:
                if bb & 1:
                    z ^= aa
                bb >>= 1
                aa <<= 1
                if aa & (1 << degree):
                    aa ^= polynomial
            row.append(z)
        tab.append(row)
    return tab


def predicted(q, n):
    d = {j: gcd(q - 1, 2 ** j - 1) for j in range(1, n + 1)}
    a0 = {j: Fraction(d[j] - 1, d[j]) for j in d}
    a1 = {j: Fraction(2) for j in d}
    a2 = {j: Fraction(d[j] + 3) for j in d}

    def coeffs(a):
        v = [Fraction(1)]
        for size in range(1, n + 1):
            v.append(sum(a[j] * v[size - j]
                         for j in range(1, size + 1)) / size)
        return v
    return (coeffs(a0)[n], coeffs(a1)[n], coeffs(a2)[n])


def census(q, n):
    mult = field(q)
    square = [mult[x][x] for x in range(q)]
    vs = list(product(range(q), repeat=n))
    perms = list(permutations(range(n)))
    coeffs = list(product(range(1, q), repeat=n))
    zero = total_m = total_m2 = 0
    size = len(perms) * len(coeffs)
    for perm in perms:
        for weights in coeffs:
            count = 0
            for v in vs:
                if all(v[perm[i]] == mult[weights[i]][square[v[i]]]
                       for i in range(n)):
                    count += 1
            assert count >= 1  # zero always idempotent
            zero += int(count == 1)
            total_m += count
            total_m2 += count * count
    return size, (Fraction(zero, size),
                  Fraction(total_m, size), Fraction(total_m2, size))


def semigroup_support(q, limit):
    # Exact semigroup of attainable positive dimensions for characteristic q.
    def prime_divisors(m):
        d, p = [], 2
        while p * p <= m:
            if m % p == 0:
                d.append(p)
                while m % p == 0:
                    m //= p
            p += 1
        if m > 1:
            d.append(m)
        return d
    generators = []
    for p in prime_divisors(q - 1):
        if p == 2:
            continue
        k, z = 1, 2 % p
        while z != 1:
            k += 1
            z = 2 * z % p
        generators.append(k)
    reachable = [False] * (limit + 1)
    reachable[0] = True
    for k in range(1, limit + 1):
        reachable[k] = any(k >= h and reachable[k - h] for h in generators)
    return generators, reachable


def main():
    cases = [(q, n) for q in (2, 3, 4, 5, 7, 8) for n in (1, 2, 3)]
    cases += [(q, 4) for q in (2, 3, 4)]
    for q, n in cases:
        size, actual = census(q, n)
        predicted_values = predicted(q, n)
        assert actual == predicted_values, (q, n, actual, predicted_values)
        generators, reachable = semigroup_support(q, n)
        assert (actual[0] > 0) == reachable[n], (q, n, generators)
        assert actual[1] == n + 1
        print(f'q={q:2d} n={n}: models={size:6d}; '
              f'Pr(N=0)={actual[0]}; E[N]={actual[1]-1}; '
              f'Var(N)={actual[2]-actual[1]**2}; support={generators}; PASS')
    # Extra exact recurrence on dimensions beyond feasible brute force.
    for q in (4, 7, 8, 11):
        orders, reachable = semigroup_support(q, 22)
        for n in range(1, 23):
            p0, _, _ = predicted(q, n)
            assert (p0 > 0) == reachable[n]
        print(f'q={q:2d}: support law through dimension 22 PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
