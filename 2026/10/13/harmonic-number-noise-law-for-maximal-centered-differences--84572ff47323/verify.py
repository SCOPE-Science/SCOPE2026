from fractions import Fraction
from math import factorial


def alpha(m, j):
    sign = 1 if j % 2 == 1 else -1
    return Fraction(sign * factorial(m) ** 2,
                    j * factorial(m-j) * factorial(m+j))


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m+1)), Fraction(0))


def weights(m):
    w = {0: Fraction(0)}
    for j in range(1, m+1):
        a = alpha(m, j)
        w[j] = a
        w[-j] = -a
    return w


for m in range(1, 21):
    w = weights(m)
    # The derivative of every polynomial of degree <= 2m is reproduced at zero.
    for q in range(0, 2*m + 1):
        moment = sum((c * (j ** q) for j, c in w.items()), Fraction(0))
        target = Fraction(1) if q == 1 else Fraction(0)
        assert moment == target, (m, q, moment, target)
    absolute_sum = sum((abs(c) for c in w.values()), Fraction(0))
    assert absolute_sum == harmonic(m), (m, absolute_sum, harmonic(m))

print("VERIFY_OK")
