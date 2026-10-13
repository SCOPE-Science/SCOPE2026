#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, gamma, sqrt, pi, log

def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))

def mean_root_exact(n):
    # m_2=1 and m_{n+1}/m_n=(2n-1)/(2n-2)
    m = Fraction(1)
    for k in range(2, n):
        m *= Fraction(2 * k - 1, 2 * k - 2)
    return m

def B_sum(n):
    return Fraction(2*n-1, 2) * sum(
        (harmonic(k-1) / ((2*k-1)*(2*k+1)) for k in range(2, n)),
        Fraction(0),
    )

def B_closed(n):
    return (
        Fraction(2*n-1, 2) *
        (1 + harmonic(n-2) - harmonic(2*n-3))
        - Fraction(1, 4) * harmonic(n-2)
    )

def enumerate_weighted(n):
    # states are (parent tuple, probability)
    states = [((), Fraction(1))]
    for new_vertex in range(3, n + 1):
        next_states = []
        old_n = new_vertex - 1
        for parents, prob in states:
            # vertices are indexed 0..old_n-1; initial edge is 0--1.
            deg = [0] * old_n
            deg[0] += 1
            deg[1] += 1
            for child_zero, par in enumerate(parents, start=2):
                deg[child_zero] += 1
                deg[par] += 1
            total_deg = 2 * (old_n - 1)
            for par, d in enumerate(deg):
                next_states.append((parents + (par,), prob * Fraction(d, total_deg)))
        states = next_states

    ER = EP = ERP = Fraction(0)
    for parents, prob in states:
        deg = [0] * n
        depth = [0] * n
        deg[0] += 1
        deg[1] += 1
        depth[1] = 1
        for child_zero, par in enumerate(parents, start=2):
            deg[child_zero] += 1
            deg[par] += 1
            depth[child_zero] = depth[par] + 1
        R = deg[0]
        P = sum(depth)
        ER += prob * R
        EP += prob * P
        ERP += prob * R * P
    return len(states), ER, EP, ERP - ER * EP

def run():
    history_checks = 0
    total_histories = 0
    finite_formula_checks = 0

    for n in range(2, 10):
        count, ER, EP, COV = enumerate_weighted(n)
        assert count == factorial(n-1)
        total_histories += count
        history_checks += 1

        assert ER == mean_root_exact(n)
        assert EP == Fraction(n-1, 2) * (harmonic(n-1) + 1)
        finite_formula_checks += 2

        if n == 2:
            assert COV == 0
        else:
            assert B_sum(n) == B_closed(n)
            assert COV == -ER * B_closed(n)
            finite_formula_checks += 2

    recurrence_checks = 0
    c = Fraction(0)
    m = Fraction(1)
    for n in range(2, 300):
        H = harmonic(n-1)
        c_next = Fraction(2*n+1, 2*n-2) * c - m * H / (4*(n-1))
        m_next = m * Fraction(2*n-1, 2*n-2)
        if n + 1 >= 3:
            assert c_next == -m_next * B_closed(n+1)
            assert B_sum(n+1) == B_closed(n+1)
            assert B_closed(n+1) > 0
            recurrence_checks += 3
        c, m = c_next, m_next

    asymptotic_checks = 0
    target = -2 * (1 - log(2)) / sqrt(pi)
    for n in (100, 1000, 10000):
        # Closed form in floating point, independent of enumerator.
        H1 = sum(1.0/k for k in range(1, n-1))
        H2 = sum(1.0/k for k in range(1, 2*n-2))
        B = (2*n-1)/2 * (1 + H1 - H2) - H1/4
        logm = (
            log(2.0) + math_lgamma(n-0.5)
            - 0.5*log(pi) - math_lgamma(n-1)
        )
        m_float = math_exp(logm)
        ratio = -(m_float * B) / (n ** 1.5)
        assert ratio < 0
        if n == 10000:
            assert abs(ratio - target) < 0.002
        asymptotic_checks += 1

    print(
        "VERIFY_OK "
        f"sizes=8 "
        f"weighted_histories={total_histories} "
        f"history_checks={history_checks} "
        f"finite_formula_checks={finite_formula_checks} "
        f"recurrence_checks={recurrence_checks} "
        f"asymptotic_checks={asymptotic_checks}"
    )

from math import lgamma as math_lgamma, exp as math_exp

if __name__ == "__main__":
    run()
