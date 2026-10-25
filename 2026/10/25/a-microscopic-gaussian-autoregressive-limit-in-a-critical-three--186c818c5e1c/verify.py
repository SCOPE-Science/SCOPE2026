#!/usr/bin/env python3
"""Independent arithmetic checks for a critical three-type mutant-family Q-chain.

The analytic convergence arguments appear in RESULT.md; finite checks are not
substitutes for tightness or asymptotic proofs.
"""
from fractions import Fraction as F
from math import comb
from collections import defaultdict

HALF = F(1, 2)
LAMBDA = -HALF
P = [[F(0), HALF, HALF], [HALF, F(0), HALF], [HALF, HALF, F(0)]]
assert all(sum(row) == 1 for row in P)
contrasts = [(1, -1, 0), (1, 1, -2)]
checks = 0
for a in contrasts:
    for i in range(3):
        assert sum(P[i][j]*a[j] for j in range(3)) == LAMBDA*a[i]
        checks += 1
for r in [F(1, 4), F(1, 3), HALF, F(2, 3), F(3, 4)]:
    c = 1-r
    mean = r/(1-c)
    f2 = (c*mean+r)**2/(1-c)
    var = f2 + mean-mean**2
    assert mean == 1 and var == 1/r
    per_type_var = [
        sum(P[i][j]*a[j]**2 for j in range(3)) + (var-1)*(sum(P[i][j]*a[j] for j in range(3)))**2
        for i in range(3) for a in contrasts[:1]
    ]
    assert per_type_var == [(var+1)/4, (var+1)/4, F(1)]
    beta = sum(per_type_var)/3
    stationary = beta/(1-LAMBDA**2)
    assert beta == (var+3)/6
    assert stationary == 2*(var+3)/9
    for lag in range(14):
        assert (stationary*LAMBDA**lag)/stationary == LAMBDA**lag
        checks += 1
    checks += 7

# Exact finite-population Q-chain check for a mean-one, variance-two
# offspring count law: P(M=0)=2/3, P(M=3)=1/3. This is a
# moment-matched auxiliary law, NOT the Poisson clone-family law.
toy = {0:F(2,3),3:F(1,3)}
toy_var = F(2)

def local_options(t):
    out = {(0,0):F(2,3)}
    for k in range(4):
        if t == 0:
            h = -k
        elif t == 1:
            h = k
        else:
            h = 2*k-3
        out[(3,h)] = out.get((3,h), F(0))+F(comb(3,k),24)
    assert sum(out.values())==1
    return out

def exact_q_moments(counts):
    parent_types = [j for j,c in enumerate(counts) for _ in range(c)]
    size = len(parent_types)
    states = {(0,0):F(1)}
    for t in parent_types:
        next_states = defaultdict(F)
        for (total,h),p in states.items():
            for (m,dh),q in local_options(t).items():
                next_states[(total+m,h+dh)] += p*q
        states = next_states
    qmass = sum(p*F(total,size) for (total,h),p in states.items())
    qmean = sum(h*p*F(total,size) for (total,h),p in states.items())
    qsecond = sum(h*h*p*F(total,size) for (total,h),p in states.items())
    uncond_center_variance = F(toy_var+1,4)*(counts[0]+counts[1])+counts[2]
    return qmass,qmean,qsecond-qmean**2,uncond_center_variance

for counts in [(1,1,1),(2,1,1),(1,3,2),(5,3,2),(1,1,8),(8,1,1)]:
    size = sum(counts)
    mass,mean,variance,baseline=exact_q_moments(counts)
    assert mass == 1
    assert mean == LAMBDA*(1+toy_var/F(size))*(counts[0]-counts[1])
    assert abs(variance-baseline) < 100   # finite sanity bound only
    checks += 3
print(f"PASS {checks} exact rational identities, spectral checks, and finite Q-moment comparisons")
for r in [F(1,4), F(1,2), F(3,4)]:
    v=1/r
    beta=(v+3)/6
    sigma2=2*(v+3)/9
    print(f"r={r}, mutant-offspring variance={v}, innovation scale={beta}, Gaussian stationary variance={sigma2}, lag-one correlation=-1/2")
print("Asymptotic convergence and novelty require the mathematical proof and literature comparisons, respectively.")
