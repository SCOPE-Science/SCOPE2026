from fractions import Fraction
from math import factorial

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

def baseline(d):
    return d - d.bit_count()

N = 4000
H = [1, 0]
for d in range(1, N):
    H.append(d * (H[d] + 2 * H[d - 1]))

# Exact coefficient formula, checked independently with rational arithmetic.
for d in range(2, 101):
    A = sum(
        (Fraction((d - j + 1) * ((-2) ** j), factorial(j)) for j in range(d + 1)),
        Fraction(0, 1),
    )
    value = Fraction(factorial(d), 1) * A
    assert value.denominator == 1
    assert value.numerator == H[d]

# The dyadic phase law.
for d in range(2, N + 1):
    val = v2(H[d])
    b = baseline(d)
    if d % 2 == 0:
        assert val == b
    elif d % 4 == 3:
        assert val == b + 1
    else:
        assert val >= b + 2

assert H[2:10] == [2, 4, 24, 128, 880, 6816, 60032, 589312]
assert [v2(H[d]) - baseline(d) for d in range(2, 10)] == [0, 1, 0, 4, 0, 1, 0, 2]

print("VERIFY_OK", N - 1, 99)
