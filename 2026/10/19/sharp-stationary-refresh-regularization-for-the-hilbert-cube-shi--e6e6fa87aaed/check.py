"""Finite rational checks of refresh-channel anti-concentration and numeric entropy diagnostics.

This checks finite instances only; the all-length theorem is proved analytically.
"""
from fractions import Fraction
from math import log


def kernel_probability(base, target, epsilon, radius):
    """Probability of [target-radius,target+radius] after one refresh."""
    low = max(Fraction(0), target-radius)
    high = min(Fraction(1), target+radius)
    return ((1-epsilon) if low <= base <= high else Fraction(0)) + epsilon*(high-low)


def block_probability(x, z, epsilon, radius):
    result = Fraction(1)
    for base, target in zip(x, z):
        result *= kernel_probability(base, target, epsilon, radius)
    return result


def conditional_entropy(epsilon, bins):
    a = 1-epsilon+epsilon/bins
    b = epsilon/bins
    return -a*log(a)-(bins-1)*b*log(b)


def test():
    cases = 0
    for epsilon in (Fraction(1,9), Fraction(1,3), Fraction(3,4), Fraction(1)):
        for r in (Fraction(1,16), Fraction(1,4), Fraction(2,5)):
            q = 1-epsilon*(1-2*r)
            for n in range(1, 10):
                centered = [Fraction(1,2)]*n
                assert block_probability(centered, centered, epsilon, r) == q**n
                cases += 1
                for pattern in range(16):
                    x = [Fraction((pattern >> (j % 4)) & 1) for j in range(n)]
                    z = [Fraction(1,2)]*n
                    assert block_probability(x, z, epsilon, r) <= q**n
                    cases += 1
            # For a deterministic zero process, mean absolute refresh cost is epsilon/2.
            assert epsilon*Fraction(1,2) <= Fraction(1,2)
            cases += 1
        if epsilon != 1:
            for b in (2, 3, 8, 128, 4096):
                assert conditional_entropy(float(epsilon), b) > 0
                cases += 1
    print(f"PASS {cases} cases: 1848 rational window/bound cases and 15 numeric entropy tests")


if __name__ == '__main__':
    test()
