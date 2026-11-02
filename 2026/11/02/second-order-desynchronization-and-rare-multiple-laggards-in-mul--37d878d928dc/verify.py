"""Exact finite-stage checks and independent numerical diagnostics for simultaneous coupon collectors."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, gamma, pi, sqrt

checks = 0

def check(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)


def exact_law(d, q):
    """First divergence level and number of collectors lagging, with d as terminal sentinel."""
    survival = Fraction(1)
    mass = {}
    for k in range(1, d):
        u = Fraction(k, d)
        denominator = 1 - u**q
        for j in range(1, q):
            mass[k, j] = survival * comb(q, j) * u**j * (1 - u)**(q-j) / denominator
        survival *= (1 - u)**q / denominator
    return mass, survival


def bridge_max_law(d):
    """All equal-weight simple-walk bridges with 2d-1 steps and endpoint -1."""
    n = 2*d - 1
    counts = Counter()
    for ups in combinations(range(n), d-1):
        ups = set(ups)
        pos = 0
        highest = 0
        for t in range(n):
            pos += 1 if t in ups else -1
            highest = max(highest, pos)
        check(pos == -1, 'bridge endpoint')
        counts[highest+1] += 1
    total = comb(n, d-1)
    return {k: Fraction(v, total) for k, v in counts.items()}

# Exhaustive rational stage model, including conditional all-idle erasure.
for d in range(2, 13):
    for q in range(2, 7):
        law, terminal = exact_law(d, q)
        check(sum(law.values(), Fraction(0)) + terminal == 1, (d, q, 'total probability'))
        check(all(v >= 0 for v in law.values()), (d, q, 'negative mass'))
        for k in range(1, d):
            u = Fraction(k, d)
            stage_total = sum((comb(q,j)*u**j*(1-u)**(q-j) for j in range(1,q)), Fraction(0))
            check(stage_total == 1 - (1-u)**q - u**q, (d,q,k,'mixed patterns'))
            check(sum(law[k,j] for j in range(1,q)) > 0, (d,q,k,'positive hazard'))
        if q == 2:
            p = {k:sum(law[k,j] for j in range(1,q)) for k in range(1,d)}
            p[d]=terminal
            for k in range(1,d+1):
                check(p[k] == Fraction(2*k,d)*Fraction(comb(2*d,d-k),comb(2*d,d)), (d,k,'binomial law'))
            check(sum(k*p[k] for k in p)==Fraction(4**d,2*comb(2*d,d)),(d,'mean'))
            check(sum(k*k*p[k] for k in p)==d,(d,'second moment'))
            check(sum(k**4*p[k] for k in p)==2*d*d-d,(d,'fourth moment'))
            check(sum(k**6*p[k] for k in p)==6*d**3-8*d*d+3*d,(d,'sixth moment'))
            if d <= 7:
                bridge=bridge_max_law(d)
                for k in range(1,d+1):
                    check(bridge.get(k,0)==p[k],(d,k,'bridge law'))

# Diagnostics of asymptotics (not substituted for the analytic proof).
def float_law(d, q):
    s=1.0
    mean=0.0
    j2=0.0
    for k in range(1,d):
        u=k/d
        den=1-u**q
        c=(1-u)**q/den
        mean+=k*s*(1-c)
        if q>=3:
            j2+=s*comb(q,2)*u*u*(1-u)**(q-2)/den
        s*=c
    mean+=d*s
    return mean,j2

for q in (3,4,5,6):
    d=9000
    mean,j2=float_law(d,q)
    limit_mean=-1/(3*q)
    limit_j2=(q-1)/2*sqrt(pi/(2*q))
    check(abs((mean-sqrt(pi*d/(2*q)))-limit_mean)<0.014,(q,'constant mean correction'))
    check(abs(sqrt(d)*j2-limit_j2)<0.03,(q,'double-laggard rate'))

print(f'PASS {checks} exact finite and supplementary numerical checks')
