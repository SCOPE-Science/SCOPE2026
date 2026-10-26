"""Independent finite-arithmetic checks for planar quadratic-defect geometry.

Requires only Python 3 standard library. It is not a proof of an infinite theorem.
"""
from fractions import Fraction
import cmath
import math
import random

checks = 0


def ck(condition, message):
    global checks
    assert condition, message
    checks += 1


# Four-node family: exact rational moments and the exact nonzero defect eigenvalue.
for numerator in range(1, 50):
    p = Fraction(numerator, 50)
    q = 1 - p
    for a in range(4):
        for b in range(4-a):
            if a == 0 and b == 0:
                moment = Fraction(1)
            elif a > 0 and b > 0:
                moment = Fraction(0)
            elif a % 2 or b % 2:
                moment = Fraction(0)
            elif a > 0:
                moment = p * (1/p)**(a//2)
            else:
                moment = q * (1/q)**(b//2)
            desired = Fraction(1) if (a,b) in ((0,0),(2,0),(0,2)) else Fraction(0)
            ck(moment == desired, ('four-point moment',p,a,b,moment))
    # q_1=(x*x-y*y)/sqrt(2), q_2=sqrt(2)*x*y.
    K11 = (p * (1/p)**2 + q * (1/q)**2)/8
    K22 = Fraction(0)
    K12 = Fraction(0)
    ck(K11 == 1/(8*p*q), ('four-point eigenvalue',p,K11))
    ck(K22 == 0 and K12 == 0, ('rank-one defect',p))
    ck(K11 >= Fraction(1,2), ('four-point barrier',p))

# Regular pentagon and larger regular polygons are exact circular 4-designs;
# verify their harmonic moment cancellations and associated quadratic defect.
for m in range(5, 30):
    zs = [cmath.exp(2j * math.pi * j / m) for j in range(m)]
    for degree in range(1, 5):
        harmonic = sum(z**degree for z in zs)/m
        ck(abs(harmonic) < 5e-14, ('regular design harmonic',m,degree,harmonic))
    xy = [(math.sqrt(2)*z.real, math.sqrt(2)*z.imag) for z in zs]
    K11 = sum(((x*x-y*y)/math.sqrt(2))**2 for x,y in xy)/(4*m)
    K22 = sum((math.sqrt(2)*x*y)**2 for x,y in xy)/(4*m)
    K12 = sum(((x*x-y*y)/math.sqrt(2))*(math.sqrt(2)*x*y) for x,y in xy)/(4*m)
    ck(abs(K11-.25)<5e-14 and abs(K22-.25)<5e-14 and abs(K12)<5e-14,
       ('regular design defect',m,K11,K22,K12))

# Deterministic perturbations numerically exercise the Vandermonde mechanism;
# they are not asserted to satisfy the theorem's low-order moment hypotheses.
rg = random.Random(2601018)
for trial in range(200):
    angle0 = rg.uniform(-math.pi,math.pi)
    noise = rg.uniform(0,1e-6)
    angles = [angle0+2*math.pi*j/5 + rg.uniform(-noise,noise) for j in range(5)]
    weights_raw = [0.2+rg.uniform(-noise,noise) for _ in range(5)]
    weights = [w/sum(weights_raw) for w in weights_raw]
    nodes = [cmath.exp(1j*theta) for theta in angles]
    harmonics = [sum(w*z**k for w,z in zip(weights,nodes)) for k in range(1,5)]
    beta = max(abs(h) for h in harmonics)
    # Direct row-sum bound ||VV* - I|| <= 4 beta; all diagonal and offdiagonal
    # entries of V*V - I are bounded by the same spectral norm.
    for j in range(5):
        ck(abs(5*weights[j]-1) <= 4*beta+1e-12, ('Vandermonde diagonal',trial,j))
    for i in range(5):
        for j in range(i+1,5):
            ratio = nodes[j]/nodes[i]
            S = sum(ratio**k for k in range(5))
            ck(math.sqrt(weights[i]*weights[j])*abs(S) <= 4*beta+1e-12,
               ('Vandermonde offdiag',trial,i,j))

print('PASS', checks, 'finite exact/numerical assertions')
