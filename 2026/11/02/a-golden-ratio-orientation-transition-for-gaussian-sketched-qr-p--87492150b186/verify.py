"""Independent finite checks for the exact two-row Gaussian QR pivot-regret law.

This is a check of algebra and numerical examples, not a substitute for the
analytical probability and optimization arguments in RESULT.md.
"""
from decimal import Decimal, getcontext
import math
import random


def exact_regret(L, delta):
    assert L > 1 and 0 <= delta <= L - 1
    return delta * (1 - delta / math.sqrt(delta * delta + 4 * L)) / 2


def theoretical_max(L):
    s = (math.sqrt(5) - 1) / 2
    if L <= 2 + math.sqrt(5):
        return (L - 1) / (L + 1), L - 1
    return s ** 2.5 * math.sqrt(L), 2 * math.sqrt(s * L)


def simulate(L, delta, N, seed):
    # M^T M is a rotation of diag(L,1), with norm gap delta.
    theta = 0.5 * math.acos(delta / (L - 1))
    c, s = math.cos(theta), math.sin(theta)
    a, b = L * c * c + s * s, L * s * s + c * c
    assert abs((a - b) - delta) <= 1e-10 * L
    rng = random.Random(seed)
    wrong = 0
    for _ in range(N):
        a_sq = b_sq = 0.0
        for row in range(2):
            g, h = rng.gauss(0, 1), rng.gauss(0, 1)
            y_a = math.sqrt(L) * c * g - s * h
            y_b = math.sqrt(L) * s * g + c * h
            a_sq += y_a * y_a
            b_sq += y_b * y_b
        wrong += b_sq > a_sq
    return delta * wrong / N


def check():
    getcontext().prec = 70
    five = Decimal(5).sqrt()
    phi_inverse = (five - Decimal(1)) / Decimal(2)
    L_critical = Decimal(2) + five
    # The derivative of h(u)=u^2(1-u)/(1+u) is
    # 2u(1-u-u^2)/(1+u)^2; its unique positive critical point is s.
    assert abs(phi_inverse * phi_inverse + phi_inverse - 1) < Decimal('1e-65')
    assert abs((L_critical - 1) / (L_critical + 1) - phi_inverse) < Decimal('1e-65')
    assert abs((L_critical - 1)**2 - 4 * phi_inverse * L_critical) < Decimal('1e-65')

    cases = [1.1, 2, 4, 2 + math.sqrt(5), 5, 10, 100]
    checks = 0
    for L in cases:
        peak, optimum = theoretical_max(L)
        assert 0 <= optimum <= L - 1 + 1e-12 * L
        assert math.isclose(exact_regret(L, min(optimum, L-1)), peak,
                            rel_tol=1e-11, abs_tol=1e-11)
        assert math.isclose(exact_regret(L, L-1), (L-1)/(L+1),
                            rel_tol=1e-11)
        for j in range(2001):
            delta = (L - 1) * j / 2000
            assert exact_regret(L, delta) <= peak + 1e-11
            checks += 1
    # Cross-check the probability calculation independently using the
    # χ²_2 exponential density integral and Simpson quadrature.
    for L in [2., 5., 10., 100.]:
        for r in [0.1, 0.5, 0.9, 1.0]:
            delta = (L-1)*r
            root = math.sqrt(delta*delta+4*L)
            alpha, beta = (root+delta)/2, (root-delta)/2
            exact_p = (root-delta)/(2*root)
            # Transform the conditional-integral variable via z=
            # (alpha+beta)*x/(2*beta). The transformed density is
            # (beta/(alpha+beta))*exp(-z).
            steps, T = 4000, 30.0
            h = T/steps
            f = lambda z: beta/(alpha+beta)*math.exp(-z)
            integral = h/3*(f(0)+f(T)+4*sum(f(h*i) for i in range(1,steps,2))
                             +2*sum(f(h*i) for i in range(2,steps,2)))
            assert abs(integral-exact_p) < 3e-11
            checks += 1
    # Stochastic check uses independent simulation from the matrix entries.
    for j,L in enumerate([2., 5., 10., 100.]):
        peak, delta = theoretical_max(L)
        estimate = simulate(L, min(delta,L-1), 90000, 913113+j)
        assert abs(estimate - peak) < 0.035 * math.sqrt(L)
        checks += 1
    print('VERIFY_OK', checks, 'deterministic bounds / integral / sampling checks')


if __name__ == '__main__':
    check()
