#!/usr/bin/env python3
"""Exact independent checks for the stated polynomial-copula formulas.
Standard-library fractions only; numerical experimentation does not certify universal claims.
"""
from fractions import Fraction as Q
from math import factorial, comb


def beta_integral(k):
    return Q(4 ** (2*k) * factorial(2*k)**2, factorial(4*k+1))


def polynomial_integral(k):
    return 4**(2*k) * sum(((-1)**j) * Q(comb(2*k, j), 2*k+j+1) for j in range(2*k+1))


def source_copula(u, v, k, eps):
    return u*v + eps*u*(1-u)*(4*v*(1-v))**k


def checkerboard_xi_by_cells(k, eps):
    h = Q(1, 2)
    intervals = (Q(0), h, Q(1))
    delta = [
        [source_copula(intervals[i+1], intervals[j+1], k, eps)
         -source_copula(intervals[i], intervals[j+1], k, eps)
         -source_copula(intervals[i+1], intervals[j], k, eps)
         +source_copula(intervals[i], intervals[j], k, eps)
         for j in range(2)]
        for i in range(2)]
    assert all(sum(row) == h for row in delta)
    assert all(sum(delta[i][j] for i in range(2)) == h for j in range(2))
    integral = Q(0)
    for i in range(2):
        running = Q(0)
        for j in range(2):
            density = 4*delta[i][j]
            integral += h*(h*running*running + h*h*running*density + h*h*h*density*density/Q(3))
            running += h*density
        assert running == 1
    return 6*integral - 2, delta


runs = 0
for k in range(1, 17):
    eps = Q(1, 8*k)
    I = beta_integral(k)
    assert I == polynomial_integral(k)
    xi_original = 2*eps*eps*I
    xi_cb, delta = checkerboard_xi_by_cells(k, eps)
    assert xi_cb == eps*eps/Q(2)
    assert xi_original > 0
    assert xi_cb/xi_original == Q(1, 4*I)
    assert delta == [[Q(1,4)+eps/Q(4),Q(1,4)-eps/Q(4)],
                     [Q(1,4)-eps/Q(4),Q(1,4)+eps/Q(4)]]
    if k < 6:
        assert xi_cb < xi_original
    else:
        assert xi_cb > xi_original
    runs+=1

assert beta_integral(5) == Q(262144, 969969)
assert beta_integral(6) == Q(4194304, 16900975)
assert Q(4)*beta_integral(6) < 1
assert Q(4)*beta_integral(5) > 1
print(f"PASS: {runs} independent rational binomial expansions, finite grid integrations, threshold comparisons")
print(f"k=6: I={beta_integral(6)}, xi_CB/xi={Q(1,4*beta_integral(6))}")
print(f"k=16: I={beta_integral(16)}, xi_CB/xi={Q(1,4*beta_integral(16))}")
print("Analytic SI/density bounds and k→infinity asymptotics require the manuscript proof.")
