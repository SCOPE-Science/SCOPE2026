"""Reproducible finite checks for a scalar full-averaging local-gradient theorem.

Only standard-library arithmetic is used. Infinite-range claims require the
analytic arguments in the accompanying proof, not these finite computations.
"""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from math import isclose, log

getcontext().prec = 80
CHECKS = 0


def check(condition, message):
    global CHECKS
    if not condition:
        raise AssertionError(message)
    CHECKS += 1


def local_step(z, h, c, alpha):
    return z - alpha * h * (z - c)


def direct_round(z, curvatures, centers, alpha, epochs):
    states = [z for _ in curvatures]
    for _ in range(epochs):
        states = [local_step(x, h, c, alpha)
                  for x, h, c in zip(states, curvatures, centers)]
    return sum(states, Q(0)) / len(states)


def exact_round(z, curvatures, centers, alpha, epochs):
    terms = [(Q(1) - alpha * h) ** epochs
             for h in curvatures]
    return (sum(terms, Q(0)) * z
            + sum(((Q(1) - r) * c for r, c in zip(terms, centers)), Q(0))) / len(terms)


def fixed_point(curvatures, centers, alpha, epochs):
    ws = [Q(1) - (Q(1) - alpha * h) ** epochs
          for h in curvatures]
    return sum((w * c for w, c in zip(ws, centers)), Q(0)) / sum(ws, Q(0))


def global_minimizer(curvatures, centers):
    return sum((h * c for h, c in zip(curvatures, centers)), Q(0)) / sum(curvatures, Q(0))


def F(epochs, z):
    # Dimensionless curvature distortion, stable on (0,2).
    return Decimal(1) + sum(((Decimal(1) - z) ** j for j in range(1, epochs)), Decimal(0))


def tuned_alpha(epochs, a, b):
    assert epochs >= 3 and epochs % 2 and Decimal(1) < b / a < Decimal(2)
    lo, hi = Decimal(1) / a, Decimal(2) / b
    check(F(epochs, lo * a) - F(epochs, lo * b) > 0, 'left sign')
    check(F(epochs, hi * a) - F(epochs, hi * b) < 0, 'right sign')
    for _ in range(255):
        md = (lo + hi) / 2
        gap = F(epochs, md * a) - F(epochs, md * b)
        if gap > 0:
            lo = md
        else:
            hi = md
    return (lo + hi) / 2


def run():
    a, b = Q(1), Q(3, 2)
    alpha = Q(6, 5)
    centers = [Q(0), Q(1)]
    hs = [a, b]
    true_min = Q(3, 5)
    check(global_minimizer(hs, centers) == true_min, 'global optimum')
    check(fixed_point(hs, centers, alpha, 3) == true_min, 'E=3 exact fixed point')
    check(fixed_point(hs, centers, alpha, 2) == Q(3, 11), 'E=2 biased fixed point')
    check(fixed_point(hs, centers, alpha, 1) == true_min, 'E=1 exact')
    check(((1 - alpha * a) ** 3 + (1 - alpha * b) ** 3) / 2 == Q(-13, 50),
          'alternating contraction')
    check(alpha == Q(3) / (a + b), 'cubic closed tuning')
    for hs2, cs2, alph2 in [
        ([Q(1), Q(3, 2)], [Q(-3), Q(2)], Q(6, 5)),
        ([Q(2), Q(3)], [Q(2), Q(-4)], Q(3, 5)),
        ([Q(1), Q(1), Q(3, 2)], [Q(-1), Q(2), Q(7)], Q(6, 5)),
        ([Q(1), Q(7, 5), Q(3, 2)], [Q(-1), Q(2), Q(7)], Q(6, 5)),
    ]:
        for epochs in range(1, 13):
            for j in range(-10, 11):
                z = Q(j, 3)
                check(direct_round(z, hs2, cs2, alph2, epochs)
                      == exact_round(z, hs2, cs2, alph2, epochs),
                      'direct multi-local-step equals affine closed map')
            zp = fixed_point(hs2, cs2, alph2, epochs)
            check(exact_round(zp, hs2, cs2, alph2, epochs) == zp,
                  'fixed point invariance')

    # Exact verification that equality is independent of arbitrary centers.
    for epoch in [3, 5, 7, 9, 11, 21]:
        for a0, b0 in [(Q(1), Q(3, 2)), (Q(1), Q(7, 4))]:
            dA, dB = Decimal(a0.numerator) / Decimal(a0.denominator), Decimal(b0.numerator) / Decimal(b0.denominator)
            best = tuned_alpha(epoch, dA, dB)
            gap = abs(F(epoch, best * dA) - F(epoch, best * dB))
            check(gap < Decimal('1e-68'), 'equalized curvatures')
            check(Decimal(1) / dA < best < Decimal(2) / dB,
                  'tuned step strict interval')
            if epoch == 3:
                check(abs(best - Decimal(3) / (dA + dB)) < Decimal('1e-68'),
                      'cubic closed form')
            # Direct two-point uniqueness probes on either side.
            left = (Decimal(1) / dA + best) / 2
            right = (Decimal(2) / dB + best) / 2
            check(F(epoch, left * dA) > F(epoch, left * dB), 'one crossing, left')
            check(F(epoch, right * dA) < F(epoch, right * dB), 'one crossing, right')

    ratio = Decimal(3) / Decimal(2)
    for epochs in [101, 501, 1001]:
        best = tuned_alpha(epochs, Decimal(1), ratio)
        s = Decimal(epochs) * (Decimal(2) - best * ratio)
        asymptotic_limit = -Decimal(str(log(0.5)))
        check(abs(s - asymptotic_limit) < Decimal('0.1'), 'large odd E boundary layer')
        t0, t1 = best - Decimal(1), best * ratio - Decimal(1)
        check(abs(t1 ** epochs - (ratio - 1 + ratio * t0 ** epochs)) < Decimal('1e-67'),
              'high precision critical-power identity')
    print('VERIFIED checks=', CHECKS)
    print('Cubic tuned alpha=6/5; odd E=3 synchronized multiplier=-13/50')
    print('E=3 common optimum=3/5; E=2 biased point=3/11')
    print('Analytic proof, not this finite test, establishes uniqueness/parity/infinite-E.')


if __name__ == '__main__':
    run()
