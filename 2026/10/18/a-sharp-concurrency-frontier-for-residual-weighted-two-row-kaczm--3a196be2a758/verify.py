"""Exact reproducibility checks for synchronous residual-weighted Kaczmarz batches.

Uses only the Python standard library. The theorem for all T and parameters
is proved analytically; this program tests finite cases and key identities.
"""
from fractions import Fraction as F
from math import comb

checks = 0


def expected_binomial(T, beta, z):
    total = F(0)
    for j in range(T + 1):
        prob = F(comb(T, j)) * z**j * (1-z)**(T-j)
        loss = z*(1-beta*j)**2+(1-z)*(1-beta*(T-j))**2
        total += prob*loss
    return total


def formula(T, beta, z):
    return (1-beta*T)**2 + z*(1-z)*(4*beta*T-beta*beta*T*(3*T-1))


def rate(T, beta):
    a = (1-beta*T)**2
    b = 1-beta*T+beta*beta*T*(T+1)/4
    return max(a, b)


for T in range(1, 12):
    for b in [F(1,7), F(2,3), F(1,1), F(4,3*T-1), F(2,T+1)]:
        for z in [F(0),F(1,13),F(1,4),F(1,2),F(4,5),F(1)]:
            assert expected_binomial(T,b,z) == formula(T,b,z), (T,b,z)
            checks+=1
        assert max(formula(T,b,F(0)),formula(T,b,F(1,2))) == rate(T,b)
        checks += 1

for T in range(1, 101):
    opt = F(2,T+1) if T<=3 else F(4,3*T-1)
    target = F(1,T+1) if T<=3 else F((T+1)**2,(3*T-1)**2)
    assert rate(T,opt) == target
    checks += 1
    for num in range(1, 600):
        b=F(num,200*T)
        assert rate(T,b) >= target, (T,b)
        if b!=opt:
            assert rate(T,b)>target, (T,b)
        checks+=2

# The uniform-sampling benchmark (both row probabilities 1/2) is isotropic.
for T in range(1, 101):
    opt=F(2,T+1)
    benchmark=1-opt*T+opt**2*T*(T+1)/4
    assert benchmark==F(1,T+1)
    checks+=1

# Strict discrepancy from uniform sampling at T>=4.
for T in range(4,101):
    assert F((T+1)**2,(3*T-1)**2)>F(1,T+1)
    checks+=1

print(f"PASS: {checks} exact-arithmetic checks")
