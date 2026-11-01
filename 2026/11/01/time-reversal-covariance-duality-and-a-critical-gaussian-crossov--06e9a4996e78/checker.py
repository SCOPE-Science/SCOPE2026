"""Exact-rational finite checks for an expanding/inverse-branch interval process.

Run with Python 3.9+: python checker.py
The symbolic argument in the accompanying proof establishes the infinite statements.
"""
from collections import defaultdict
from fractions import Fraction as F


def fourier_covariances(b, p, horizon):
    r = F(1, b)
    q = 1 - p
    t = p / r + q * r
    alpha = F(1)
    beta = {}
    values = []
    for n in range(horizon + 1):
        values.append(F(1, 12) * (alpha + (1 - r * r) *
                                   sum((r ** k) * value for k, value in beta.items())))
        nxt = defaultdict(F)
        nxt[0] -= alpha * p / r
        for k, weight in beta.items():
            nxt[k + 1] += p * weight
            if k:
                nxt[k - 1] += q * weight
        alpha *= t
        beta = {k: v for k, v in nxt.items() if v}
    return values


def segment_covariance(b, p, horizon):
    """Integrate original random compositions exactly over uniform x."""
    q = 1 - p
    # Piece: (left,right,image_slope,image_intercept,probability).
    pieces = [(F(0), F(1), F(1), F(0), F(1))]
    values = []
    for n in range(horizon + 1):
        total = F(0)
        for left, right, slope, intercept, weight in pieces:
            dx1 = right - left
            dx2 = right * right - left * left
            dx3 = right ** 3 - left ** 3
            integral = slope * dx3 / 3 + (intercept - F(1, 2) - slope / 2) * dx2 / 2
            integral -= (intercept - F(1, 2)) * dx1 / 2
            total += weight * integral
        values.append(total)
        if n == horizon:
            break
        next_pieces = []
        for left, right, slope, intercept, weight in pieces:
            for digit in range(b):
                next_pieces.append((left, right, slope / b,
                                    (intercept + digit) / b, weight * q / b))
                cut_left = max(left, (F(digit, b) - intercept) / slope)
                cut_right = min(right, (F(digit + 1, b) - intercept) / slope)
                if cut_left < cut_right:
                    next_pieces.append((cut_left, cut_right, b * slope,
                                        b * intercept - digit, weight * p))
        pieces = next_pieces
    return values


def main():
    checks = 0
    for b, horizon, probs in (
        (2, 6, (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))),
        (3, 5, (F(1, 5), F(1, 2), F(4, 5))),
        (4, 4, (F(1, 3), F(1, 2), F(2, 3))),
    ):
        for p in probs:
            from_operator = fourier_covariances(b, p, horizon)
            from_integrals = segment_covariance(b, p, horizon)
            for n, (a, c) in enumerate(zip(from_operator, from_integrals)):
                assert a == c, (b, p, n, a, c)
                assert a == fourier_covariances(b, 1 - p, horizon)[n]
                checks += 2
            assert from_operator[0] == F(1, 12)
            assert from_operator[1] == F(1, 12 * b)
            checks += 2
            print('exact branch and Fourier agreement:', 'b', b, 'p', p,
                  'lags', horizon + 1)
    print('PASS; exact rational identities checked:', checks)


if __name__ == '__main__':
    main()
