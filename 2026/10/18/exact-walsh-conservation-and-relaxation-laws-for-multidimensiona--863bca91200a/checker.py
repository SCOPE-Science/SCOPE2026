#!/usr/bin/env python3
"""Independent rational checks for a Boolean opinion ODE and its Walsh spectrum.

Run: python3 checker.py  (only Python standard library required).
The finite checks supplement, but do not replace, the arbitrary-dimensional proof.
"""
from fractions import Fraction as F
from itertools import combinations


def transition(n, weights, lower, upper, rate):
    q = 1 << n
    kernel = []
    for i in range(n):
        ki = []
        for d in range(q):
            similarity = sum(weights[j] for j in range(n) if not (d >> j) & 1)
            different = bool((d >> i) & 1)
            ki.append(int((different and similarity > upper)
                          or ((not different) and similarity < lower)))
        kernel.append(ki)

    def derivative(x):
        # Direct ordered focal/target event rates, not a Fourier routine.
        output = [F(0)] * q
        for focal in range(q):
            for target in range(q):
                rel = focal ^ target
                for i in range(n):
                    if kernel[i][rel]:
                        flux = rate[i] * x[focal] * x[target] / n
                        output[focal] -= flux
                        output[focal ^ (1 << i)] += flux
        return output
    return kernel, derivative


def spectral_values(n, kernel, rate):
    q = 1 << n
    return {
        a: -F(4, n * q) * sum(
            rate[i] * sum(kernel[i][d]
                          for d in range(q) if (a & d).bit_count() % 2 == 0)
            for i in range(n) if a & (1 << i))
        for a in range(1, q)
    }


def check_case(n, weights, lower, upper, rate):
    q = 1 << n
    kernel, rhs = transition(n, weights, lower, upper, rate)
    u = [F(1, q)] * q
    assert rhs(u) == [F(0)] * q
    vals = spectral_values(n, kernel, rate)
    step = F(1, 13)
    jac = [[F(0) for _ in range(q)] for _ in range(q)]
    for col in range(q):
        xp = u.copy(); xm = u.copy()
        xp[col] += step; xm[col] -= step
        yp, ym = rhs(xp), rhs(xm)
        for row in range(q):
            jac[row][col] = (yp[row] - ym[row]) / (2 * step)
    for a, lam in vals.items():
        chi = [(-1) ** ((s & a).bit_count()) for s in range(q)]
        for row in range(q):
            assert sum(jac[row][col] * chi[col] for col in range(q)) == lam * chi[row]
        assert lam <= 0

    # Directly test all zero-mode conservation identities on an arbitrary
    # non-uniform probability vector; no Walsh formula enters derivative.
    x = [F(s + 1, q * (q + 1) // 2) for s in range(q)]
    dx = rhs(x)
    for a, lam in vals.items():
        if lam == 0:
            assert sum(((-1) ** ((a & s).bit_count())) * dx[s]
                       for s in range(q)) == 0
    return len(vals)


def main():
    checks = 0
    for n in range(2, 6):
        weights = [F(1 << j, (1 << n) - 1) for j in range(n)]
        rate = [F(j + 1, n + 1) for j in range(n)]
        for lower, upper in [(F(0), F(1)), (F(1, 10), F(1, 10)),
                             (F(1, 5), F(3, 5)), (F(2, 5), F(2, 5)),
                             (F(3, 5), F(4, 5)), (F(9, 10), F(9, 10)),
                             (F(1), F(1))]:
            checks += check_case(n, weights, lower, upper, rate)
        # The high-threshold formula has a fully explicit exact check.
        lower = upper = F(1) - min(weights) / 2
        kernel, _ = transition(n, weights, lower, upper, rate)
        vals = spectral_values(n, kernel, rate)
        for a, lam in vals.items():
            active = [i for i in range(n) if a & (1 << i)]
            if len(active) == 1:
                expected = -F(2, n) * (1 - F(1, 1 << (n - 1))) * rate[active[0]]
            else:
                expected = -F(1, n) * (1 - F(1, 1 << (n - 2))) * sum(rate[i] for i in active)
            assert lam == expected
            checks += 1
    # For two issues the parity character is conserved at ALL admissible
    # confidence thresholds (not only the high-threshold special case).
    for a in [F(0), F(1, 5), F(1, 2), F(4, 5), F(1)]:
        k, f = transition(2, [F(1, 3), F(2, 3)], a, a, [F(2), F(5)])
        assert spectral_values(2, k, [F(2), F(5)])[3] == 0
        checks += 1
    print(f"PASS: {checks} exact rational eigenmode/parity assertions; n=2,3,4,5")


if __name__ == '__main__':
    main()
