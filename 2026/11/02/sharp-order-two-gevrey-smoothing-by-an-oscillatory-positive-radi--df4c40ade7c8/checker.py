#!/usr/bin/env python3
"""Independent numerical probes of exact radial moment identities and leading asymptotics.

Requires mpmath (pip install mpmath).  Finite probes do not establish any asymptotic theorem.
"""
import mpmath as mp

mp.mp.dps = 60


def normalized_complex_moment(n, alpha, eta):
    # Exact special-function representation after a unit-interval substitution.
    return (mp.exp(1j * eta) * mp.gamma(n + alpha + 2)
            * mp.hyperu(n + 1, -alpha, -1j * eta) / mp.gamma(alpha + 1))


def predicted_complex_moment(n, alpha, eta):
    z = -1j * eta
    return (mp.sqrt(mp.pi) / mp.gamma(alpha + 1)
            * z ** ((2 * alpha + 1) / 4)
            * n ** ((2 * alpha + 1) / 4)
            * mp.exp(1j * eta / 2 - 2 * mp.sqrt(n * z)))


def perturbation_coefficient(n, alpha, eta, eps):
    l = normalized_complex_moment(n, alpha, eta)
    moment0_inverse = mp.gamma(n + alpha + 2) / (mp.gamma(alpha + 2) * mp.gamma(n + 1))
    return moment0_inverse * (-eps * mp.re(l)) / (1 + eps * mp.re(l))


def predicted_real_coefficient(n, alpha, eta, eps):
    c = -eps * mp.sqrt(mp.pi) * eta ** ((2 * alpha + 1) / 4) / (mp.gamma(alpha + 1) * mp.gamma(alpha + 2))
    power = (6 * alpha + 5) / 4
    phase = mp.sqrt(2 * eta * n) + eta / 2 - mp.pi * (2 * alpha + 1) / 8
    return c * n ** power * mp.exp(-mp.sqrt(2 * eta * n)) * mp.cos(phase)


checks = 0
for alpha, eta, eps in [(mp.mpf(0), mp.mpf('0.5'), mp.mpf('0.3')),
                        (mp.mpf(1), mp.mpf(2), mp.mpf('-0.25')),
                        (mp.mpf('-0.5'), mp.mpf('0.5'), mp.mpf('0.6'))]:
    for n in [60, 130, 260, 410]:
        exact = normalized_complex_moment(n, alpha, eta)
        leading = predicted_complex_moment(n, alpha, eta)
        relerr = abs(exact / leading - 1)
        assert relerr < mp.mpf('2.5') / mp.sqrt(n), (alpha, eta, n, relerr)
        checks += 1
        assert abs(mp.re(exact)) <= 1 + mp.mpf('1e-25')
        checks += 1
        coeff = perturbation_coefficient(n, alpha, eta, eps)
        target = predicted_real_coefficient(n, alpha, eta, eps)
        full_envelope = abs(eps) * mp.sqrt(mp.pi) * eta ** ((2 * alpha + 1) / 4) / (mp.gamma(alpha + 1) * mp.gamma(alpha + 2)) * n ** ((6 * alpha + 5) / 4) * mp.exp(-mp.sqrt(2 * eta * n))
        assert abs(coeff - target) < full_envelope * mp.mpf('2.9') / mp.sqrt(n), (alpha, eta, n)
        checks += 1

    # Verify steepest-phase subsequence approaching cosine +1, without treating it as a proof.
    shift = eta/2 - mp.pi*(2*alpha + 1)/8
    for j in [10, 15, 20]:
        nn = int(mp.nint((2*mp.pi*j-shift)**2/(2*eta)))
        ph = mp.sqrt(2*eta*nn) + shift
        assert mp.cos(ph) > mp.mpf('0.99')
        checks += 1
print(f'PASS: {checks} supplementary numerical assertions (three parameter families).')
