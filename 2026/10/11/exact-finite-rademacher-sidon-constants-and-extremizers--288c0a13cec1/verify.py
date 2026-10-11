#!/usr/bin/env python3
import cmath
import itertools
import math
import random

TOL = 2e-11

def sign_max(coeffs):
    best = 0.0
    for eps in itertools.product((-1.0, 1.0), repeat=len(coeffs)):
        z = sum(e*a for e, a in zip(eps, coeffs))
        best = max(best, abs(z))
    return best

def ratio(coeffs):
    return sum(abs(a) for a in coeffs) / sign_max(coeffs)

extremizers = 0
for n in range(5, 13):
    target = n * math.sin(math.pi / (2*n))
    for phase in (0.0, 0.137, 1.111):
        r = 0.7 + n/20.0
        coeffs = [r * cmath.exp(1j*(phase + j*math.pi/n)) for j in range(n)]
        got = ratio(coeffs)
        if abs(got-target) > TOL:
            raise SystemExit(f'extremizer mismatch n={n}: {got} vs {target}')
        extremizers += 1

rng = random.Random(271005)
random_cases = 0
worst_slack = float('inf')
for n in range(5, 10):
    target = n * math.sin(math.pi / (2*n))
    for _ in range(180):
        coeffs=[]
        for j in range(n):
            mag = 0.05 + 1.95*rng.random()
            ang = 2*math.pi*rng.random()
            coeffs.append(mag*cmath.exp(1j*ang))
        got = ratio(coeffs)
        slack = target-got
        worst_slack = min(worst_slack, slack)
        if got > target + TOL:
            raise SystemExit(f'inequality failure n={n}: {got} > {target}')
        random_cases += 1

print(f'VERIFY_OK n=5..12 extremizers={extremizers} random_cases={random_cases} min_slack={worst_slack:.12g}')
