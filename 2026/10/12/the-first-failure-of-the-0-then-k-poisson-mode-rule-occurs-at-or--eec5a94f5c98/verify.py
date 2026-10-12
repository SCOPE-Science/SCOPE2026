"""Exact rational certificate for initial global modes of Poisson laws of order 2--15.
Run: python3 verify.py.  Standard library only.
The infinite-tail bound and monotone-root argument are explained in RESULT.md.
"""
from fractions import Fraction
from math import factorial

# Rational upper endpoints, written as integers in millionths.
# For k=2,...,14 the candidate is n=k; for k=15 it is n=25.
BRACKET_UPPER = (
    732051, 601680, 520352, 463330, 420487, 386782, 359378,
    336537, 317127, 300374, 285728, 272786, 261245, 250228,
)
SCALE = 1000000
TAIL_UPPER = Fraction(2 * 4**41, factorial(41))
assert TAIL_UPPER < 1


def coefficients(k, lam, max_n):
    """Coefficient a_n=[z^n] exp(lam*(z+...+z^k))."""
    a = [Fraction(1)]
    for n in range(1, max_n + 1):
        a.append(lam * sum(j * a[n-j] for j in range(1, min(k,n)+1)) / n)
    return a


def main():
    assert len(BRACKET_UPPER) == 14
    for k in range(2, 16):
        target = k if k <= 14 else 25
        hi = Fraction(BRACKET_UPPER[k-2], SCALE)
        lo = hi - Fraction(1, SCALE)
        assert k * hi < 4

        # Direct exact rational tests for every n in 1,...,40*k.
        a = coefficients(k, hi, 40*k)
        assert a[target] > 1, (k, target, 'target at upper endpoint')
        competitors = [(a[n],n) for n in range(1,40*k+1) if n != target]
        highest_other, other_idx = max(competitors)
        assert highest_other < 1, (k,other_idx,'competitor at upper endpoint')

        # Root lower endpoint. All coefficient functions strictly increase.
        lower = coefficients(k, lo, target)
        assert lower[target] < 1, (k,target,'root lower endpoint')

        # A_n <= sum_{m>=ceil(n/k)} (k*hi)^m/m! for n>40*k.
        # Since k*hi<4, it is < 2*4^41/41! < 1.
        assert TAIL_UPPER < 1
        print('k=%2d, first index=%2d, root interval=(%d,%d)/1000000, '
              'highest alternate index=%2d, gap=%.9g' %
              (k,target,BRACKET_UPPER[k-2]-1,BRACKET_UPPER[k-2],
               other_idx,float(1-highest_other)))
    print('VERIFY_OK: 14 rational brackets, complete finite prefixes and global tails')


if __name__ == '__main__':
    main()
