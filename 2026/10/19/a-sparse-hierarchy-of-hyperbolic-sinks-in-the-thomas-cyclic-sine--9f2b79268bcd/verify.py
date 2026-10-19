"""Numerical sanity checks of explicit Thomas sine-ring formulas.

The accompanying RESULT.md contains the analytic proof for all integer indices;
finite calculations here illustrate rather than establish its infinitary claims.
"""
import math


def bisect(f, left, right, n=90):
    fl, fr = f(left), f(right)
    if not fl * fr < 0:
        raise AssertionError(('nonbracketed root', left, right, fl, fr))
    for _ in range(n):
        mid = (left + right) / 2
        fm = f(mid)
        if fm == 0:
            return mid
        if (fl < 0) == (fm < 0):
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return (left + right) / 2


def thresholds(k):
    v = (2*k + 0.5) * math.pi
    if k == 0:
        uf, bf = 0.0, 1.0
    else:
        uf = bisect(lambda u: math.sin(u) - u*math.cos(u),
                    2*k*math.pi, v)
        bf = 1 / math.sqrt(1 + uf*uf)
    uh = bisect(lambda u: math.sin(u) + 0.5*u*math.cos(u),
                v, (2*k + 1)*math.pi)
    bh = 1 / math.sqrt(4 + uh*uh)
    return uf, uh, bf, bh, v


if __name__ == '__main__':
    last_h = float('inf')
    print(' k    beta_H          beta_F         width         scaled_width')
    for k in range(12):
        uf, uh, bf, bh, v = thresholds(k)
        assert 0 < bh < bf <= 1
        assert bf < last_h or k == 0
        last_h = bh
        assert abs(math.sin(uh)/uh - bh) < 1e-13
        assert abs(math.cos(uh) + 2*bh) < 1e-13
        assert abs(-1 - uh*uh/6) > 1
        if k:
            assert abs(math.sin(uf)/uf - bf) < 1e-13
            assert abs(math.cos(uf) - bf) < 1e-13
        b = (bf + bh) / 2
        u = bisect(lambda x: math.sin(x) - b*x,
                   max(uf + 1e-7, 1e-7), (2*k + 1)*math.pi)
        c = math.cos(u)
        assert abs(math.sin(u)-b*u) < 1e-12
        assert c-b < 0 and -b-c/2 < 0  # three-dimensional sink
        print(f'{k:2d} {bh: .12f} {bf: .12f} {bf-bh: .12f} '
              f'{(bf-bh)*v**3: .8f}')
    for k in (20, 100, 400):
        uf, uh, bf, bh, v = thresholds(k)
        scaled = (bf-bh)*v**3
        assert abs(scaled - 4.5) < 0.15
        print(f'k={k}: width*v^3={scaled:.12f}, limit=4.5')
    print('PASS: finite threshold, eigenvalue, separation and asymptotic checks.')
