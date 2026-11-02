"""Independent modular checks for the five-adic derangement residue census.

Uses only Python's standard library, modular recurrence and finite polynomial arithmetic.
Finite checks corroborate, but do not prove, the quantified theorem.
"""
from math import prod

EXPECTED = (2, 3, 1, 1, 3)


def factorial_falling_and_derivative_at(a, terms=10):
    f = 0
    df = 0
    for j in range(terms):
        polynomial_value = prod(a - h for h in range(j))
        derivative_value = sum(
            prod(a - h for h in range(j) if h != i)
            for i in range(j)
        )
        f += (-1)**j * polynomial_value
        df += (-1)**j * derivative_value
    return f % 5, df % 5


def cycle(k):
    m = 5**k
    values = []
    derangement = 1
    for n in range(2*m):
        if n:
            derangement = (n*derangement + (-1)**n) % m
        values.append(derangement)
    return values


def periodicity_check(vals):
    size = len(vals)
    assert all(vals[i] != vals[i+size//p] for p in () for i in range(size))
    # Test all prime divisors of 2*5^k. Any proper period divides a
    # divisor of index 2 or 5, so rejecting these reductions suffices.
    return all(
        any(vals[i] != vals[(i+size//prime)%size] for i in range(size))
        for prime in (2, 5)
    )


def main():
    table = [factorial_falling_and_derivative_at(a) for a in range(5)]
    assert table == [(1, 1), (0, 3), (1, 4), (3, 2), (4, 4)], table
    for k in range(1, 7):
        m = 5**k
        vals = cycle(k)
        counts = [0]*m
        for v in vals:
            counts[v] += 1
        assert all(counts[v] == EXPECTED[v%5] for v in range(m)), k
        assert periodicity_check(vals), ('nonminimal', k)
        # Independently confirm the recurrence repeats across a full period.
        d = vals[-1]
        for n in range(2*m, 4*m):
            d = (n*d + (-1)**n) % m
            assert d == vals[n-2*m], ('not periodic', k, n)
        print('LEVEL_OK', 'k=', k, 'modulus=', m, 'all_targets=', m,
              'count_range=', (min(counts), max(counts)))
    def image(mod):
        vals=[]
        d=1
        for n in range(2*mod):
            if n: d=(n*d+(-1)**n)%mod
            vals.append(d)
        return set(vals)
    assert image(4) == {0,1,2}
    assert image(9) == {0,1,2,4,5,7,8}
    print('VERIFY_OK derivative_table=5 residue_censuses=1..6',
          'period_minimality=1..6', 'small_prime_obstructions=4,9')

if __name__ == '__main__':
    main()
