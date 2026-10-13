"""Direct finite-dimensional tests of a photon-cutoff parity envelope.

Standard-library only. The analytic proof is separate from these tests.
"""
import math
import cmath
import random


def wigner_origin_from_kraus(psi, eta):
    """Apply all vacuum-loss Kraus operators to a normalized pure vector."""
    kmax = len(psi) - 1
    diagonal = [0.0] * (kmax + 1)
    for lost in range(kmax + 1):
        for n in range(lost, kmax + 1):
            amp = (math.sqrt(math.comb(n, lost)) *
                   eta ** ((n - lost) / 2) *
                   (1 - eta) ** (lost / 2) * psi[n])
            diagonal[n - lost] += abs(amp) ** 2
    assert abs(sum(diagonal) - 1) < 2e-12
    return 2 / math.pi * sum((-1) ** n * p for n, p in enumerate(diagonal))


def wigner_origin_binomial(psi, eta):
    x = 1 - 2 * eta
    return 2 / math.pi * sum(abs(a) ** 2 * x ** n for n, a in enumerate(psi))


def bound_for_cutoff(K):
    m = K // 2
    r = (2 * m) ** (-1 / (2 * m - 1))
    return -(2 * m - 1) / (2 * m * math.pi) * r, (1 + r) / 2


def random_admissible_state(K, rng):
    weights = [rng.expovariate(1) for _ in range(K + 1)]
    odds = [j for j in range(K + 1) if j % 2]
    evens = [j for j in range(K + 1) if not j % 2]
    odd_weight = rng.uniform(0, .5)
    odd_sum = sum(weights[j] for j in odds)
    even_sum = sum(weights[j] for j in evens)
    for j in odds:
        weights[j] *= odd_weight / odd_sum
    for j in evens:
        weights[j] *= (1 - odd_weight) / even_sum
    psi = [math.sqrt(p) * cmath.exp(1j * rng.uniform(0, 2 * math.pi))
           for p in weights]
    assert sum((-1) ** j * weights[j] for j in range(K + 1)) >= -1e-12
    return psi


def radial_wigner_polynomial(a, eta, y):
    p2 = 1 - a
    q2 = eta * eta * p2
    q1 = eta * (a + 2 * (1 - eta) * p2)
    return 1 - 2 * q1 + (q1 - 2 * q2) * y + q2 * y * y / 2


def verify():
    rng = random.Random(435309)
    samples = 0
    for K in range(2, 12):
        sharp, eta_star = bound_for_cutoff(K)
        m = K // 2
        psi = [0j] * (K + 1)
        psi[1] = math.sqrt(.5)
        psi[2 * m] = 1j * math.sqrt(.5)
        assert abs(wigner_origin_from_kraus(psi, eta_star) - sharp) < 2e-12
        assert abs(wigner_origin_binomial(psi, eta_star) - sharp) < 2e-12
        for _ in range(80):
            psi = random_admissible_state(K, rng)
            for eta in (0.0, 0.24, 0.5, 0.625, 0.75, 0.9, 1.0):
                kraus_value = wigner_origin_from_kraus(psi, eta)
                direct_value = wigner_origin_binomial(psi, eta)
                assert abs(kraus_value - direct_value) < 3e-12
                assert direct_value + 3e-12 >= sharp
                if eta <= .5:
                    assert direct_value >= -3e-12
                samples += 1
        if K % 2 == 1:
            sharp0, eta0 = bound_for_cutoff(K - 1)
            assert abs(sharp - sharp0) < 1e-15
            assert abs(eta_star - eta0) < 1e-15
    sharp_list = [bound_for_cutoff(2 * m)[0] for m in range(1, 60)]
    assert all(sharp_list[i+1] < sharp_list[i] for i in range(len(sharp_list)-1))
    assert abs(sharp_list[0] + 1 / (4 * math.pi)) < 1e-15
    assert -1 / math.pi < sharp_list[-1] < -.9 / math.pi

    # The exact one/two-photon diagonal illustration: annulus -> disk -> none.
    a = .3
    crossing = 1 / (2 * (1 - a))
    assert .5 < crossing < 1
    for eta, expected in ((.95, "annulus"), (.6, "disk"), (.49, "none")):
        values = [radial_wigner_polynomial(a, eta, j / 200) for j in range(1500)]
        negative = [j for j, v in enumerate(values) if v < -1e-10]
        observed = "none" if not negative else "disk" if values[0] < 0 else "annulus"
        assert observed == expected, (eta, observed)
    assert abs(radial_wigner_polynomial(a, crossing, 0)) < 2e-15
    assert abs(radial_wigner_polynomial(a, .5, 0)) < 2e-15
    print("VERIFY_OK pure_loss_kraus_cases=%d exact_sharp_cutoffs=10 odd_cutoff_plateau=passed radial_transition=passed" % samples)


if __name__ == "__main__":
    verify()
