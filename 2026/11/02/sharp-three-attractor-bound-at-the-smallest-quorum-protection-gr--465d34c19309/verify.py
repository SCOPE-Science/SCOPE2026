#!/usr/bin/env python3
"""Exact-rational checks for the three-person quorum-protection replicator theorem.

Only the Python standard library is required. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)


def independent_payoffs(x, z, c, r, loss, rho, operating, efficacy):
    y = ONE - x - z
    probs = {'C': x, 'D': y, 'S': z}
    result = {}
    for focal in 'CDS':
        total = ZERO
        for u, v in product('CDS', repeat=2):
            group = (focal, u, v)
            contrib = sum(t != 'D' for t in group)
            defect = 3 - contrib
            protect = sum(t == 'S' for t in group)
            benefit = r * c * contrib / 3
            cost = (c if focal != 'D' else ZERO) + (operating if focal == 'S' else ZERO)
            failure = (ONE - rho ** defect) * (ONE - efficacy if protect >= 2 else ONE)
            total += probs[u] * probs[v] * (benefit - cost - loss * failure)
        result[focal] = total
    return result


def gradients(x, z, c, r, loss, rho, operating, efficacy):
    h = ONE - rho
    C = loss * h
    q = rho + h * (x + z)
    a = r * c / 3 - c
    A = a + C * (q * q - efficacy * z * z)
    B = A - operating + 2 * C * efficacy * z * (ONE - x - z)
    return A, B


def jacobian_at_payoff_equality(x, z, loss, rho, efficacy):
    y = ONE - x - z
    h = ONE - rho
    C = loss * h
    q = ONE - h * y
    Ax = 2 * C * h * q
    Az = 2 * C * (h * q - efficacy * z)
    Bx = Ax - 2 * C * efficacy * z
    Bz = Az + 2 * C * efficacy * (y - z)
    j11 = x * ((ONE - x) * Ax - z * Bx)
    j12 = x * ((ONE - x) * Az - z * Bz)
    j21 = z * ((ONE - z) * Bx - x * Ax)
    j22 = z * ((ONE - z) * Bz - x * Az)
    return j11 + j22, j11 * j22 - j12 * j21


def verify():
    count = 0
    for rho, efficacy, r, cost in product(
            (F(1,4), F(1,2), F(3,4)),
            (ZERO, F(1,4), F(3,4), ONE),
            (F(4,3), F(5,2)),
            (F(1,10), F(4,5))):
        loss, c = F(2), ONE
        for i in range(1, 8):
            for j in range(1, 9 - i):
                x, z = F(i, 9), F(j, 9)
                vals = independent_payoffs(x, z, c, r, loss, rho, cost, efficacy)
                A, B = gradients(x, z, c, r, loss, rho, cost, efficacy)
                assert A == vals['C'] - vals['D']
                assert B == vals['S'] - vals['D']
                h, C, y = ONE - rho, loss * (ONE - rho), ONE - x - z
                q = ONE - h * y
                tr, det = jacobian_at_payoff_equality(x, z, loss, rho, efficacy)
                assert tr == 2 * C * y * (h * q * (x + z) + efficacy * z * (ONE - 3*z))
                assert det == 4 * x * y * z * C*C * efficacy * (h * q * y - efficacy * z*z)
                if det >= 0:
                    assert tr > 0
                count += 1

    # An entirely rational, parameter-admissible witness.
    c, r, loss, rho, cost, efficacy = ONE, F(33, 20), F(2), F(1,2), F(3,25), F(3,4)
    A_D, B_D = gradients(ZERO, ZERO, c, r, loss, rho, cost, efficacy)
    A_C, _ = gradients(ONE, ZERO, c, r, loss, rho, cost, efficacy)
    assert (A_D, B_D, A_C) == (F(-1,5), F(-8,25), F(11,20))
    for j in range(0, 101):
        z = F(j, 100)
        _, B = gradients(ZERO, z, c, r, loss, rho, cost, efficacy)
        assert B == -2 * (z - F(1,5)) * (z - F(4,5))
    for z, transverse, tangent in ((F(1,5), F(-3,25), F(24,125)),
                                   (F(4,5), F(-3,25), F(-24,125))):
        A, B = gradients(ZERO, z, c, r, loss, rho, cost, efficacy)
        assert B == 0 and A == transverse
        deriv = 2 - 4*z
        assert z * (ONE-z)*deriv == tangent
    print(f'PASS: {count} exact rational payoff and Jacobian checks;')
    print('PASS: 101 exact polynomial identity checks; exact three-attractor witness.')

if __name__ == '__main__':
    verify()
