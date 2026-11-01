#!/usr/bin/env python3
"""Finite, reproducible checks of a log-periodic Bergman boundary-kernel law.

This checks numerical consequences of the theorem, not its all-phase proof.
"""
import mpmath as mp

mp.mp.dps = 32
alpha = mp.mpf('0.25')
epsilon = mp.mpf('0.55')
omega = mp.mpf('1.3')
p = alpha + 2
T = 2 * mp.pi / omega
a = mp.gamma(alpha + 1)
b = mp.gamma(alpha + 1 - 1j * omega)


def h(x):
    return 1 + epsilon * mp.cos(omega * x)


def A(x):
    return a + epsilon * mp.re(b * mp.exp(1j * omega * x))


def moment(n):
    return mp.beta(n + 1, alpha + 1) + epsilon * mp.re(
        mp.beta(n + 1, alpha + 1 - 1j * omega))


def limit_kernel(theta, zeta):
    return mp.quad(lambda t: mp.exp(-zeta * t) * t**(alpha + 1) /
                   A(theta + mp.log(t)), [0, 1, mp.inf])


def finite_kernel(N, zeta):
    total = 1 / moment(0)
    for n in range(1, 16*N + 1):
        total += mp.exp(-zeta * n / N) / moment(n)
    return total / mp.power(N, p)


# The Mellin convolution has the exact complex-Gamma first harmonic.
for x in [mp.mpf('0'), mp.mpf('0.4'), mp.mpf('1.3')]:
    direct = mp.quad(lambda v: mp.exp(-v) * v**alpha *
                     h(x - mp.log(v)), [0, 1, mp.inf])
    assert abs(direct - A(x)) < mp.mpf('1e-19')
assert abs(A(0) - A(T)) < mp.mpf('1e-19')

# Scalar tangent profiles depend on their phase, even after normalization.
zeta = mp.mpc('1.35', '0.4')
r0 = limit_kernel(0, zeta) / limit_kernel(0, 1)
r1 = limit_kernel(T/2, zeta) / limit_kernel(T/2, 1)
separation = abs(r0 - r1)
assert separation > mp.mpf('0.004'), separation

# Independent finite-sum comparisons for the exact beta moments.
for N in (120, 360):
    theta = mp.log(N)
    predicted = limit_kernel(theta, zeta)
    actual = finite_kernel(N, zeta)
    relative_error = abs(actual - predicted) / abs(predicted)
    assert relative_error < mp.mpf('0.04'), (N, relative_error)
    print('N={} relative scaling error={}'.format(N, mp.nstr(relative_error, 8)))
print('normalized phase separation={}'.format(mp.nstr(separation, 8)))
print('CHECK_OK: exact Mellin/Fourier specialization, finite moments, two phase profiles')
