"""Finite exact checks for the dyadic-holding tent-map Cesaro theorem.

Every computation uses rational arithmetic. The accompanying proof, not these
finite examples, establishes the infinite statements.
"""
from fractions import Fraction as F


def tent(x):
    return 2 * x if x <= F(1, 2) else 2 - 2 * x


def phi(x):
    return F(4, 5) - x / 5


checks = 0
for denominator in (2, 3, 4, 5, 7, 11, 13, 17):
    for numerator in range(denominator + 1):
        x = F(numerator, denominator)
        y = x
        summation = F(0)
        count = 0
        for block in range(10):
            for _ in range(2 ** block):
                # Exact recurrence solution has 2**block repeats of T**block(x).
                summation += y
                count += 1
                assert 5 * summation <= 4 * count + x
                checks += 1
            assert count == 2 ** (block + 1) - 1
            y = tent(y)

# The affine Bellman inequality is checked on a dense rational test grid;
# the accompanying proof checks its two affine pieces symbolically.
for denominator in (11, 17, 29, 101):
    for numerator in range(denominator + 1):
        x = F(numerator, denominator)
        assert x + phi(x) <= 2 * phi(tent(x))
        checks += 1

# Right-branch inverse orbit and the exact finite truncation of its
# discounted orbit sum; the infinite sum is evaluated geometrically in proof.
z = F(0)
weighted = F(0)
for k in range(1, 25):
    predecessor = 1 - z / 2
    assert tent(predecessor) == z
    z = predecessor
    weighted += z / (2 ** k)
    expected = F(2, 3) * (
        (1 - F(1, 2) ** k)
        + F(1, 5) * (1 - F(-1, 4) ** k)
    )
    # sum 2^-j (2/3)[1-(-1/2)^j], j=1...k.
    assert weighted == expected
    assert weighted <= F(4, 5)
    checks += 3
print(f"PASS: {checks} exact rational consistency checks")
