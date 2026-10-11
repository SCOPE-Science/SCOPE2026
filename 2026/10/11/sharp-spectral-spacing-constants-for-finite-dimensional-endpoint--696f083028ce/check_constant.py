#!/usr/bin/env python3
"""Illustrative numerical quadrature of a convergent endpoint kernel coefficient."""
from math import exp, log, sqrt

def coefficient(r=2.0, b=2.0, kmax=55, mesh=100000):
    # Finite truncation and quadrature illustrate, but do not certify, the theorem.
    if not (r >= 1.0 and b > 1.0 and mesh % 2 == 0):
        raise ValueError("Require r >= 1, b > 1 and even mesh")
    def f(u):
        return sum((b ** k * exp(-(b ** k) * u)) ** r
                   for k in range(-kmax, kmax + 1)) ** (1.0 / r)
    step = (b - 1.0) / mesh
    value = f(1.0) + f(b)
    for j in range(1, mesh):
        value += (4 if j % 2 else 2) * f(1.0 + j * step)
    return step * value / 3.0

if __name__ == "__main__":
    print("Approximate kappa_2(2) =", format(coefficient(), ".15f"))
    print("Jensen upper bound =", format(sqrt(log(2.0)) / 2.0, ".15f"))
