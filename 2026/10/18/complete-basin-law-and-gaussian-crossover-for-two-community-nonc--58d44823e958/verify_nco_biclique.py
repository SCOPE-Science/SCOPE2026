"""Exact checks for the finite two-community synchronous binary opinion theorem.
Only Python standard library is required; execute `python verify_nco_biclique.py`.
The proof is analytic; these checks independently test finite cases and combinatorial formulas.
"""
from fractions import Fraction
from itertools import product
from math import comb


def thresholds(k):
    assert k >= 2
    return (k - 2) // 2, (k + 1) // 2 + 1


def label(k, plus):
    low, high = thresholds(k)
    return 'L' if plus <= low else 'H' if plus >= high else 'G'


def category(m, n, plus_left, plus_right):
    a, b = label(m, plus_left), label(n, plus_right)
    if a == b == 'G':
        return 'frozen'
    if (a, b) in (('L', 'H'), ('H', 'L')):
        return 'swap'
    if a == 'L' or b == 'L':
        return 'minus'
    return 'plus'


def one_step(state, m, n):
    """Direct source update with 1+epsilon=3/2 and values -1/+1."""
    left, right = state[:m], state[m:]
    a = sum(left)
    b = sum(right)
    return tuple(1 if 3*s+2*b > 0 else -1 for s in left) + tuple(
        1 if 3*s+2*a > 0 else -1 for s in right
    )


def actual_outcome(state, m, n):
    path = [state]
    s = state
    for _ in range(4):
        s = one_step(s, m, n)
        if s in path:
            period = len(path) - path.index(s)
            if period == 2:
                assert s[:m] in ((-1,)*m, (1,)*m)
                assert s[m:] in ((-1,)*n, (1,)*n)
                assert s[0] == -s[m]
                return 'swap'
            assert period == 1
            if all(x == 1 for x in s):
                return 'plus'
            if all(x == -1 for x in s):
                return 'minus'
            assert s == state
            return 'frozen'
        path.append(s)
    raise AssertionError('A trajectory has not entered an orbit by two updates')


def partition_probabilities(k, p):
    lo, hi = thresholds(k)
    a = sum(Fraction(comb(k,j)) * p**j * (1-p)**(k-j)
            for j in range(lo+1))
    b = sum(Fraction(comb(k,j)) * p**j * (1-p)**(k-j)
            for j in range(hi, k+1))
    return a, b, 1-a-b


def claimed_probs(m, n, p):
    lm, hm, gm = partition_probabilities(m, p)
    ln, hn, gn = partition_probabilities(n, p)
    return {'swap':lm*hn+hm*ln, 'frozen':gm*gn,
            'plus':hm*hn+hm*gn+gm*hn,
            'minus':lm*ln+lm*gn+gm*ln}


def check():
    total = 0
    for m in range(2, 8):
        for n in range(2, 8):
            exact_count = {k:0 for k in ('swap', 'frozen', 'plus', 'minus')}
            weighted = {k:Fraction(0) for k in exact_count}
            p = Fraction(2, 5)
            for s in product((-1,1), repeat=m+n):
                a, b = sum(x==1 for x in s[:m]), sum(x==1 for x in s[m:])
                expected = category(m, n, a, b)
                actual = actual_outcome(s, m, n)
                assert actual == expected, (m, n, s, actual, expected)
                exact_count[actual] += 1
                weighted[actual] += p**(a+b)*(1-p)**(m+n-a-b)
                total += 1
            formulas = claimed_probs(m, n, p)
            assert weighted == formulas, (m,n, weighted, formulas)
            assert sum(exact_count.values()) == 2**(m+n)
            assert sum(formulas.values()) == 1
            assert claimed_probs(m,n,Fraction(1,2))['swap'] == Fraction(
                (2**m - central(m))*(2**n - central(n)), 2**(m+n+1))
    print(f'PASS: {total} full-state dynamics tests on all m,n from 2 to 7;')
    print('36 exact rational (p=2/5) basin-distribution identities;')
    print('36 unbiased swap-probability and 36 normalization identities.')


def central(k):
    return comb(k,k//2) * (2 if k%2 else 1)


if __name__ == '__main__':
    check()
