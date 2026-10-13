from fractions import Fraction
from math import sqrt


def b_value(N, eta):
    return Fraction((eta + 1) * (N + 2), N + eta + 2)


def variance(N, eta, lam, probs):
    b = float(b_value(N, eta))
    S = sum(p / (j + 1) for j, p in enumerate(probs))
    p0 = probs[0]
    return b * (1.0 / lam + S / (1.0 - lam)) - p0


def check_case(N, eta, probs):
    S = sum(p / (j + 1) for j, p in enumerate(probs))
    b = float(b_value(N, eta))
    lam = 1.0 / (1.0 + sqrt(S))
    vopt = variance(N, eta, lam, probs)
    veq = variance(N, eta, 0.5, probs)
    gain = b * (1.0 - sqrt(S)) ** 2
    assert abs((veq - vopt) - gain) < 1e-12
    for trial_lam in (0.1, 0.25, 0.4, 0.5, 0.7, 0.9):
        assert vopt <= variance(N, eta, trial_lam, probs) + 1e-12


for N in range(1, 9):
    for eta in range(1, N + 1):
        J = min(eta, N - eta)
        probs = [0.0] * (eta + 1)
        if J == 0:
            probs[0] = 1.0
        else:
            weights = [j + 1 for j in range(J + 1)]
            total = sum(weights)
            for j, w in enumerate(weights):
                probs[j] = w / total
        check_case(N, eta, probs)
        b = float(b_value(N, eta))
        same = [1.0] + [0.0] * eta
        for lam in (0.2, 0.35, 0.5, 0.65, 0.8):
            witness = variance(N, eta, lam, same)
            assert witness + 1e-12 >= 4.0 * b - 1.0
        assert abs(variance(N, eta, 0.5, same) - (4.0 * b - 1.0)) < 1e-12

print('VERIFY_OK')
