"""Exact rational replay of the initial BCZ cusp run; Python 3 standard library."""
from fractions import Fraction as F
from math import ceil


def bcz_digits(a, b, steps):
    out = []
    for _ in range(steps):
        index = (1 + a) // b
        out.append(int(index))
        a, b = b, index*b - a
    return out


def expected(k, t, s):
    R = (F(k) + s - 3*t - 6) / 4
    return -((-R.numerator) // R.denominator)


def allowed_lengths(k):
    q, r = divmod(k, 4)
    return [{q-2, q-1}, {q-1}, {q-1, q}, {q-1, q}][r]


def run_test():
    tested = 0
    for k in range(12, 80):
        for ti in range(1, 11):
            for si in range(1, 13):
                t, s = F(ti, 11), F(si, 13)
                den = k+t+s
                a, b = (k+t-s)/den, F(2)/den
                ds = bcz_digits(a, b, 60)
                assert ds[0] == k and ds[1] == 1
                actual = 0
                for d in ds[2:]:
                    if d != 2:
                        break
                    actual += 1
                assert actual == expected(k, t, s)
                assert actual in allowed_lengths(k)
                tested += 1
    print('EXACT_RATIONAL_REPLAY_OK', tested)


if __name__ == '__main__':
    run_test()
