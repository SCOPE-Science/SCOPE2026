"""Exact rational-algebra consistency checks for a periodic nilpotent-Jacobian map.

Run: python3 CHECK.py. No external packages are required.
The ring is Q[T]/(T^3-T^2-2), not a numerical approximation.
"""
from fractions import Fraction as Q


class R:
    def __init__(self, coeffs):
        v = [Q(x) for x in coeffs] + [Q(0)] * max(0, 3 - len(coeffs))
        for k in range(len(v) - 1, 2, -1):
            ck = v[k]
            v[k - 1] += ck
            v[k - 3] += 2 * ck
        self.c = tuple(v[:3])

    @staticmethod
    def lift(x):
        return x if isinstance(x, R) else R([x])

    def __add__(self, other):
        b = self.lift(other)
        return R([self.c[i] + b.c[i] for i in range(3)])

    __radd__ = __add__

    def __neg__(self):
        return R([-v for v in self.c])

    def __sub__(self, other):
        return self + (-self.lift(other))

    def __rsub__(self, other):
        return self.lift(other) - self

    def __mul__(self, other):
        b = self.lift(other)
        c = [Q(0)] * 5
        for i in range(3):
            for j in range(3):
                c[i + j] += self.c[i] * b.c[j]
        return R(c)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        assert isinstance(scalar, int) and scalar != 0
        return R([a / scalar for a in self.c])

    def __pow__(self, power):
        assert isinstance(power, int) and power >= 0
        answer, a = R([1]), self
        while power:
            if power % 2:
                answer = answer * a
            a = a * a
            power //= 2
        return answer

    def __eq__(self, other):
        return self.c == self.lift(other).c

    def __repr__(self):
        return repr(self.c)


ZERO = R([0]); ONE = R([1]); T = R([0, 1]); SIGMA = T**2 + (T - 1)**2


def P(u):
    return (T**2 * u * (SIGMA - u)) / 4


def G(state):
    _, y, z = state
    delta = P(y) - P(z)
    return (delta, z, delta**2)


def main():
    assert T**3 == T**2 + 2
    assert 1 < 1.69562076955986 < 2
    assert P(0) == 0
    assert P(1) == T
    assert P(T**2) == 1
    assert P((T - 1)**2) == 1
    states = [
        (ZERO, (T - 1)**2, ZERO),
        (ONE, ZERO, ONE),
        (-T, ONE, T**2),
        (T - 1, T**2, (T - 1)**2),
    ]
    for k, state in enumerate(states):
        assert G(state) == states[(k + 1) % 4], (k, G(state))
    assert len({str(z.c) for _, _, z in states}) == 4
    print('CHECK_OK exact polynomial ring, four distinct states, four transitions')


if __name__ == '__main__':
    main()
