"""Exact rational finite-horizon check of the skew-map covariance theorem.
This supplements, but does not replace, the analytic proof.
"""
from fractions import Fraction as Q


def exact_check(b, N):
    t = 1 / (2 - b)
    a = t
    rho_low = (2 - b) / 2
    rho_high = (2 - b) / (2 * (1 - b))
    mean = (1 + 2 * t) / 4
    q = b * (2 - b)
    lam = 1 - 2 * q
    # affine itineraries: initial interval, F^n(x)=mx+c, initial density
    pieces = [(Q(0), t, Q(1), Q(0), rho_low),
              (t, Q(1), Q(1), Q(0), rho_high)]
    count = 0
    for n in range(N + 1):
        val = Q(0)
        for lo, hi, m, c, density in pieces:
            val += density * (
                m * (hi**3 - lo**3) / 3
                + (c - mean - m * mean) * (hi**2 - lo**2) / 2
                - mean * (c - mean) * (hi - lo)
            )
        if n % 2 == 0:
            expected = Q(1, 16) + (t*t + (1-t)**2) * lam**(n//2) / 24
        else:
            expected = -Q(1, 16) + t * (1-t) * (q-1) * lam**(n//2) / 12
        assert val == expected, (b, n, val, expected)
        count += 1
        if n == N:
            break
        nxt = []
        for lo, hi, m, c, density in pieces:
            cut = (b-c)/m
            div = [lo, hi]
            if lo < cut < hi:
                div = [lo, cut, hi]
            for l, r in zip(div[:-1], div[1:]):
                if m*(l+r)/2+c < b:
                    slope, intercept = (1-a)/b, a
                else:
                    slope, intercept = -1/(1-b), 1/(1-b)
                nxt.append((l, r, slope*m, slope*c+intercept, density))
        pieces = nxt
    return count


def main():
    bs = [Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(3, 4)]
    n = sum(exact_check(b, 10) for b in bs)
    print('PASS: {} exact rational covariance identities; 5 rational parameters, 11 horizons each'.format(n))


if __name__ == '__main__':
    main()
