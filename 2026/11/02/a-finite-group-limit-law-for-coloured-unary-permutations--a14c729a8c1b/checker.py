"""Independent finite checks for coloured-permutation automorphism counts.

Run with Python 3: python checker.py. Exhaustive computations at small sizes
corroborate, but do not replace, the arbitrary-size proofs in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def mobius(n):
    factors = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            factors += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors += 1
    return -1 if factors % 2 else 1


def necklace_count(q, d):
    return sum(mobius(k) * q ** (d // k)
               for k in range(1, d + 1) if d % k == 0) // d


def egf_coefficients(q, N):
    """Coefficients T_q: exact rational EGF; independently of enumeration."""
    rigid = [1, q] + [(q - 1) * q ** (n - 1) for n in range(2, N + 1)]
    twice_b = [0] * (N + 1)
    for d in range(1, N // 2 + 1):
        p = necklace_count(q, d)
        for k in range(2, N // d + 1):
            twice_b[k * d] += p * (2 if k == 2 else (1 if k % 2 == 0 else -1))
    return [Fraction(sum(rigid[j] * twice_b[n-j] for j in range(n+1)), 2)
            for n in range(N+1)]


def cycles_of(f):
    seen = set()
    for v in range(len(f)):
        if v in seen:
            continue
        cycle = []
        u = v
        while u not in seen:
            seen.add(u)
            cycle.append(u)
            u = f[u]
        assert u == v
        yield cycle


def necklace(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def group_order_from_cycle_types(f, colors):
    typemults = Counter()
    for cyc in cycles_of(f):
        s = tuple(colors[v] for v in cyc)
        canon = necklace(s)
        length = len(s)
        rotations = sum(1 for i in range(length) if s[i:] + s[:i] == s)
        typemults[(length, canon, rotations)] += 1
    g = 1
    for (length, canon, rotations), m in typemults.items():
        g *= rotations ** m * factorial(m)
    return g


def brute_group_order(f, colors):
    n = len(f)
    return sum(all(colors[g[v]] == colors[v] and
                   f[g[v]] == g[f[v]] for v in range(n))
               for g in permutations(range(n)))


def test_counts():
    for q, max_n in ((1, 5), (2, 5), (3, 4)):
        coeff = egf_coefficients(q, max_n)
        for n in range(1, max_n + 1):
            order2 = rigid = total = 0
            for f in permutations(range(n)):
                for colors in product(range(q), repeat=n):
                    structural = group_order_from_cycle_types(f, colors)
                    brute = brute_group_order(f, colors)
                    assert structural == brute, (q, n, f, colors, structural, brute)
                    order2 += brute == 2
                    rigid += brute == 1
                    total += 1
            assert total == factorial(n) * q ** n
            assert order2 == coeff[n] * factorial(n), (q,n,order2,coeff[n])
            target_rigid = (q if n == 1 else (q - 1) * q ** (n - 1)) * factorial(n)
            assert rigid == target_rigid, (q,n,rigid,target_rigid)
            print(f'q={q},n={n},rigid={rigid},order_two={order2}')
    assert [int(c * factorial(n)) for n,c in enumerate(egf_coefficients(2,6))][2:] == [4,18,96,1080,11880]


def test_necklaces():
    for q in (1, 2, 3):
        for d in range(1, 7):
            primitive = set()
            for word in product(range(q), repeat=d):
                if all(word != word[i:] + word[:i] for i in range(1, d)):
                    primitive.add(necklace(word))
            assert len(primitive) == necklace_count(q, d)


def test_limit_numeric():
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 50
        q = 2
        Q = Decimal(q)
        b = sum((Decimal(necklace_count(q, d)) * Q ** (-2 * d) / 2 *
                 (1 + 1 / (1 + Q ** (-d)))) for d in range(1, 81))
        limit = (1 - 1 / Q) * b
        print('observed limit', limit)
        assert abs(limit - Decimal('0.261848236423527184')) < Decimal('0.000000000000000001')
        # For d>80, p_d <= q^d/d and (1+1/(1+q^-d))/2 <= 1.
        tail_bound = (1 - 1/Q) * Q ** (-81) / (Decimal(81) * (1 - 1/Q))
        print('limit_C2_q2=', limit, 'tail_bound=', tail_bound)
        assert tail_bound < Decimal('1e-25')

if __name__ == '__main__':
    test_necklaces()
    test_counts()
    test_limit_numeric()
    print('ALL_CHECKS_OK')
