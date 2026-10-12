#!/usr/bin/env python3
import math, random

pi = math.pi
bias = 1.0 - 2.0/pi
classical_win = 1.0 - 1.0/pi
quantum_win = 0.75
gap = 1.0/pi - 0.25
assert abs(classical_win - (0.5 + 0.5*bias)) < 1e-15
assert abs(quantum_win - classical_win - gap) < 1e-15
assert gap > 0.0

# Midpoint quadrature of the hemisphere transform h(z)=(2/pi) asin(z),
# where z is uniform on [-1,1]. This is a regression check only; the proof
# in RESULT.md is analytic and uses spherical isoperimetry.
N = 200000
s = 0.0
for k in range(N):
    z = -1.0 + 2.0*(k + 0.5)/N
    s += abs((2.0/pi)*math.asin(z))
quad_bias = s/N
assert abs(quad_bias - bias) < 2e-8

# Fixed-seed Monte Carlo stress check of the displayed hemisphere and singlet
# strategies for the third game. This does not certify optimality.
rng = random.Random(20261006)
M = 200000
cw = 0
qw = 0.0
for _ in range(M):
    # For two independent uniform directions on S^2, their dot product is
    # uniform on [-1,1]. Rotate the first direction to the north pole.
    z = 2.0*rng.random() - 1.0
    # Conditional singlet winning probability is (1+|z|)/2.
    qw += (1.0 + abs(z))/2.0
    # For the classical hemisphere strategy, use a separate random pair in a
    # rotation-invariant coordinate system and evaluate the exact sign rule.
    # Generate two directions by normalized Gaussians.
    def unit():
        while True:
            v = [rng.gauss(0.0,1.0) for _ in range(3)]
            n = math.sqrt(sum(t*t for t in v))
            if n > 0:
                return [t/n for t in v]
    x = unit(); y = unit()
    dot = sum(x[i]*y[i] for i in range(3))
    a = 1 if x[2] >= 0 else -1
    b = -1 if y[2] >= 0 else 1
    target = 1 if dot < 0 else -1
    cw += (a*b == target)
mc_classical = cw/M
mc_quantum = qw/M
assert abs(mc_classical - classical_win) < 0.004
assert abs(mc_quantum - quantum_win) < 0.002
print('VERIFY_OK')
print(f'classical_bias={bias:.15f}')
print(f'classical_win={classical_win:.15f}')
print(f'quantum_win={quantum_win:.15f}')
print(f'gap={gap:.15f}')
print(f'quadrature_bias={quad_bias:.15f}')
print(f'mc_classical={mc_classical:.6f}')
print(f'mc_quantum={mc_quantum:.6f}')
