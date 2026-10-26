"""Reproducible rational checks of a two-agent fuzzy-influence dyadic stopping law."""
from fractions import Fraction as F
from collections import defaultdict
from math import exp, log, ceil, isclose


def rational_test(seq):
    """At each distance level use q from seq, with q=1 forcing terminal equality."""
    states = {(F(0), F(1)): F(1)}
    atoms = defaultdict(F)
    expected_time = F(0)
    survived = F(1)
    for k, q in enumerate(seq):
        h = 2*q-q*q
        s = q/(2-q)
        expected_time += survived / h
        next_states = defaultdict(F)
        for (a,b), mass in states.items():
            middle = (a+b)/2
            atoms[middle] += mass*s
            next_states[(a,middle)] += mass*(1-s)/2
            next_states[(middle,b)] += mass*(1-s)/2
        for j in range(2**k):
            key = F(2*j+1,2**(k+1))
            assert atoms[key] == survived*s/F(2**k), (seq,k,j,atoms[key])
        survived *= (1-s)
        states = dict(next_states)
    assert survived == 0
    assert sum(atoms.values(), F(0)) == 1
    mean = sum((x*p for x,p in atoms.items()),F(0))
    variance = sum(((x-mean)**2*p for x,p in atoms.items()),F(0))
    surv = F(1)
    predicted_variance_adjust = F(0)
    predicted_time = F(0)
    for k,q in enumerate(seq):
        s=q/(2-q)
        predicted_variance_adjust += surv*s / F(4**k)
        predicted_time += surv/(2*q-q*q)
        surv *= 1-s
    assert mean == F(1,2)
    assert variance == (1-predicted_variance_adjust)/12
    assert expected_time == predicted_time
    return len(atoms)

cases = 0
atoms_total = 0
for qs in [
    [F(1)],
    [F(1,4), F(1)],
    [F(1,8), F(1,4), F(3,4), F(1)],
    [F(1,10), F(1,5), F(1,2), F(4,5), F(1)],
    [F(1,100), F(1,20), F(1,5), F(1,2), F(9,10), F(1)],
]:
    atoms_total += rational_test(qs)
    cases += 1

beta, d = 3.0, 0.6
for epsilon in (0.2,0.1,0.06):
    survival = 1.0
    mean_time = 0.0
    second_variance_term = 0.0
    for k in range(120):
        z = beta*(d/(2.0**k)/epsilon-1)
        q = (1+exp(-beta))/(1+exp(z)) if z<700 else (1+exp(-beta))*exp(-z)
        h = 2*q-q*q
        s = q/(2-q)
        mean_time += survival/h
        second_variance_term += survival*s*(4.0**(-k))
        survival *= 1-s
        if survival<1.e-15:
            break
    assert survival<1.e-15
    assert mean_time>0
    assert 0.0 < d*d/12*(1-second_variance_term)<d*d/12
    leading = exp(beta*d/epsilon)/(2*(1+exp(beta)))
    assert abs(mean_time/leading-1) < (0.03 if epsilon ==0.2 else 0.001)

print('PASS: exact rational transition-tree and stagewise waiting-time checks:',cases)
print('PASS: exact terminal atomic probabilities:',atoms_total)
print('PASS: logistic positive-parameter asymptotic checks: 3')
