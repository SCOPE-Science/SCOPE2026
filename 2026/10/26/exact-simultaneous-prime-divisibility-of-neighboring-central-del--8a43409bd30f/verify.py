#!/usr/bin/env python3
"""Independent exact-arithmetic checks for a central-Delannoy neighbor theorem."""
from math import comb


def delannoy_row(max_index):
    """Compute exact coefficients using a recurrence, not a digit formula."""
    arr = [1, 3]
    for n in range(1, max_index):
        numerator = 3 * (2*n + 1) * arr[n] - n * arr[n-1]
        assert numerator % (n+1) == 0
        arr.append(numerator // (n+1))
    return arr[:max_index+1]


def predicted_count(p, L, d):
    forbidden = {i for i in range(p) if d[i] % p == 0}
    assert 0 not in forbidden and 1 not in forbidden and p-1 not in forbidden
    a = p - len(forbidden)
    c = sum(i not in forbidden and i+1 not in forbidden for i in range(p-1))
    return p**L - 2 * a**L + 1 + c*((a**L-1)//(a-1)), a, c, forbidden


def run():
    pairs = [(7,1),(7,2),(7,3),(7,4),(11,1),(11,2),(11,3),
             (13,1),(13,2),(17,1),(17,2),(19,1),(19,2),(23,1),
             (23,2),(31,1),(31,2),(43,1),(43,2)]
    max_n = max(p**L for p,L in pairs)
    d = delannoy_row(max_n)
    for n in range(45):
        independent = sum(comb(n, k)**2 * 2**k for k in range(n+1))
        assert independent == d[n], (n, independent, d[n])
    for p, L in pairs:
        predicted, a, c, z = predicted_count(p, L, d)
        actual = sum(d[n] % p == 0 and d[n+1] % p == 0 for n in range(p**L))
        assert actual == predicted, (p, L, actual, predicted)
        # Independently check digit factorization, including carries and endpoints.
        for n in range(p**L + 1):
            rem, prod = n, 1
            while rem:
                rem, digit = divmod(rem, p)
                prod = (prod * (d[digit] % p)) % p
            assert d[n] % p == prod, (p, L, n)
    for p in range(7, 201, 4):
        # Check only prime p=3 mod4 via exact trial division and independent formula.
        if any(p % q == 0 for q in range(2, int(p**.5)+1)):
            continue
        m=(p-1)//2
        assert sum(comb(m,k)**2 * pow(2,k,p) for k in range(m+1))%p==0,p
    print('VERIFY_OK: 45 independent binomial-square identities; 19 complete consecutive-pair blocks; full Lucas checks; prime-3-mod-4 midpoint checks through 199.')
    for p, L in [(7,2),(7,3),(7,4),(11,2),(13,2)]:
        value, a, c, z = predicted_count(p, L, d)
        print(f'  p={p} L={L}: forbidden={sorted(z)}, allowed={a}, adjacent={c}, both-divisible={value}')


if __name__ == '__main__':
    run()
