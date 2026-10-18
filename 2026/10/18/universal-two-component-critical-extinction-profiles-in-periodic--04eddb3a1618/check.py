"""Independent finite-trajectory checks for a critical cooperative Lotka--Volterra example.

Python 3 standard library only. Numerical checks illustrate, but do not prove,
the global theorem in RESULT.md.
"""
from math import sin, cos, exp, pi
from fractions import Fraction

sigma0 = Fraction(4, 5)
tau0 = Fraction(11, 10)
d10 = Fraction(2)
d20 = Fraction(3)
p0 = sigma0 / d20
k0 = d10 - p0 * tau0
assert sigma0 - p0 * d20 == 0
assert -d10 + p0 * tau0 == -k0
assert k0 == Fraction(128, 75)

sigma, tau, d1, d2 = map(float, (sigma0, tau0, d10, d20))
p, k = float(p0), float(k0)
T = 2 * pi
N = 512
step = T / N
phase_index = 52


def a2(t):
    return 1.4 + 0.5 * cos(t) + 0.3 * sin(2 * t)


def a1(t):
    return -p * 1.4 + 0.6 * sin(t) - 0.25 * cos(2 * t)


def B(t):
    return 1.4 * t + 0.5 * sin(t) + 0.15 * (1 - cos(2 * t))


def G(t):
    return p * 0.5 * sin(t) + p * 0.15 * (1 - cos(2 * t)) + 0.6 * (1 - cos(t)) - 0.125 * sin(2 * t)


def simpson(values, h):
    assert len(values) % 2 == 1
    return h / 3 * (values[0] + values[-1] + 4 * sum(values[1:-1:2]) + 2 * sum(values[2:-1:2]))


def rk4(t, state, h, f):
    k1 = f(t, state)
    k2 = f(t + h / 2, tuple(v + h * u / 2 for v, u in zip(state, k1)))
    k3 = f(t + h / 2, tuple(v + h * u / 2 for v, u in zip(state, k2)))
    k4 = f(t + h, tuple(v + h * u for v, u in zip(state, k3)))
    return tuple(v + h * (u1 + 2 * u2 + 2 * u3 + u4) / 6
                 for v, u1, u2, u3, u4 in zip(state, k1, k2, k3, k4))


def resident_rhs(t, state):
    y, = state
    return (y * (a2(t) - d2 * y),)


J = simpson([exp(B(i * step)) for i in range(N + 1)], step)
z0 = d2 * J / (exp(B(T)) - 1)
Y0 = 1 / z0
Ys = [Y0]
for i in range(N):
    Ys.append(rk4(i * step, (Ys[-1],), step, resident_rhs)[0])
assert abs(Ys[-1] - Y0) < 2e-7, (Ys[-1], Y0)

Qs = [exp(G(i * step)) * Ys[i] ** (-p) for i in range(N + 1)]
I = simpson(Qs, step) / T
fs = [q / (k * I) for q in Qs]
assert abs(simpson(fs, step) / T - 1 / k) < 1e-9

Es = [exp(B(i * step)) * Y0 / Ys[i] for i in range(N + 1)]
J_H = simpson([E * f for E, f in zip(Es, fs)], step)
H0 = tau * J_H / (Es[-1] - 1)
j = phase_index
t_phase = j * step
H_phase = (H0 + tau * simpson([Es[i] * fs[i] for i in range(j + 1)], step)) / Es[j]
Z_phase = Ys[j] * H_phase


def rhs(t, state):
    x, y = state
    return (x * (a1(t) - d1 * x + sigma * y),
            y * (a2(t) + tau * x - d2 * y))

for x0, y0 in ((0.2, 0.5), (10., 2.)):
    x, y = x0, y0
    steps = 320 * N + phase_index
    for i in range(steps):
        x, y = rk4(i * step, (x, y), step, rhs)
    now = steps * step
    assert abs(now * x / fs[j] - 1) < .007, (x0, now * x, fs[j])
    assert abs(now * (y - Ys[j]) - Z_phase) < .005, (y0, now * (y - Ys[j]), Z_phase)
    print('initial=', (x0, y0), 't*x=', now * x, 'profile=', fs[j],
          't*(y-Y)=', now * (y - Ys[j]), 'profile=', Z_phase)
print('checks passed; k=', k, 'mean critical coefficient=', 1 / k)
