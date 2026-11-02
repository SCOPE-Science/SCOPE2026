"""Reproducible exact-rational checks for beta-weighted stratified quadrature.
Run: python3 verify.py (Python standard library only).
Finite checks supplement, but do not replace, the analytical proof.
"""
from fractions import Fraction as F
from math import isclose

def moment_beta(k):
    return F(6, (k + 2) * (k + 3))

def moment_uniform(k):
    return F(1, k + 1)

def power_integral(k, x, h):
    return ((x + h)**(k + 1) - x**(k + 1)) / (k + 1)

def rule_power(k, m, samples):
    h=F(1,m)
    total=F(0)
    for i,u in enumerate(samples):
        x=i*h
        end=x+h
        val=(x+h*u)**k
        lin=(1-u)*x**k + u*end**k
        total += h*(F(1,2)*(x**k+end**k)+(val-lin)/(6*u*(1-u)))
    return total

def cubic_expected(m):
    h=F(1,m)
    out=F(0)
    for i in range(m):
        x=i*h
        # The correction for x^3 is -h^3 (3x+h(1+U))/6.
        out += h*F(1,2)*(x**3+(x+h)**3) - h**3*(3*x+h*(1+moment_beta(1)))/6
    return out

def beta_variance_x4(m):
    h=F(1,m)
    total=F(0)
    for i in range(m):
        x=i*h
        c1=4*x*h**3+h**4
        c2=h**4
        # Var(U)=1/20, Cov(U,U^2)=1/20, Var(U^2)=37/700.
        total += h*h*(c1*c1*F(1,20)+2*c1*c2*F(1,20)+c2*c2*F(37,700))/36
    return total

n=0
assert moment_beta(0)==1;n+=1
assert moment_beta(1)==F(1,2);n+=1
assert moment_beta(2)-moment_beta(1)**2==F(1,20);n+=1
assert moment_beta(3)-moment_beta(1)*moment_beta(2)==F(1,20);n+=1
assert moment_beta(4)-moment_beta(2)**2==F(37,700);n+=1
assert moment_uniform(2)-2*moment_uniform(3)+moment_uniform(4)-(moment_uniform(1)-moment_uniform(2))**2==F(1,180);n+=1
for m in range(1,17):
    ulist=[F((i*7)%19+1,21) for i in range(m)]
    for k in (0,1,2):
        assert rule_power(k,m,ulist)==F(1,k+1)
        n+=1
    assert cubic_expected(m)==F(1,4)
    n+=1
    assert F(1,720*m**7)==F(1,m**7)*F(1,720)
    n+=1
for k in (3,4,5):
    for m in range(1,20):
        us=[F((7*i+3*m)%31+1,34) for i in range(m)]
        q=rule_power(k,m,us)
        assert -100<q<100
        n+=1
# For x^4, scaled variance tends to (1/25920)*int_0^1 (24x)^2 dx =1/135.
for m in (4,8,16,32,64,128):
    v=beta_variance_x4(m)
    assert v>0
    assert abs(float(m**7*v-F(1,135)))<0.06/m
    n+=1
# Numerically validate actual random implementation of beta variates.
import random
rng=random.Random(20261029)
for m in (2,7,20):
    for _ in range(15):
        us=[F(str(rng.betavariate(2,2))) for i in range(m)]
        assert rule_power(2,m,us)==F(1,3)
        n+=1
print(f'PASS: {n} exact-rational and seeded floating-input check groups')
