"""Finite numerical stress checks for the phase-centred two-mode concentration law.

These sampled checks corroborate formulas but are not proofs of inequalities for
all measurable weights. Only Python's standard library is required.
"""
import cmath
import math
import random

pi = math.pi
rng = random.Random(26072026)
N = 8192
dt = 2*pi/N
t = [-pi+(j+.5)*dt for j in range(N)]

for a in (0.3, 0.75, 1.55, 2.3, 2.85):
    for trial in range(80):
        # A discretized mask with exactly the prescribed total angular mass.
        order = list(range(N))
        rng.shuffle(order)
        q = 2*a/dt
        k = int(q)
        weight = [0.0]*N
        for j in order[:k]:
            weight[j] = 1.0
        weight[order[k]] = q-k
        z = dt*sum((weight[j]*cmath.exp(1j*t[j]) for j in range(N)))
        phase = cmath.phase(z)
        mismatch = dt*sum((1-weight[j]) for j in range(N)
                          if abs((t[j]-phase+pi)%(2*pi)-pi) < a)
        gap = (math.sin(a)-abs(z)/2)/pi
        rhs = 2*math.sin(a)*(1-math.cos(mismatch/2))/pi
        assert gap + 0.002 >= rhs, (a, trial, gap, rhs)

for a in (0.3, 0.75, 1.55, 2.3, 2.85):
    for fraction in (0, .1, .37, .8, 1.):
        cap = min(2*a, 2*(pi-a), 2*pi/3)
        m = fraction*cap
        if m >= 2*pi/3:
            continue
        z = 2*math.sin(a-m/2)+2*(math.sin(a+m/2)-math.sin(a))
        formula = 2*math.sin(a)*(2*math.cos(m/2)-1)
        assert z > 0 and abs(z-formula) < 1e-12
        deficit = (2*math.sin(a)-z)/(2*pi)
        rhs = 2*math.sin(a)*(1-math.cos(m/2))/pi
        assert abs(deficit-rhs)<1e-12
print('Finite grid stress tests and exact-formula evaluations passed.')
