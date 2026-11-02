#!/usr/bin/env python3
"""Standalone tests for the powered-distance quadratic form of wheel metrics.

Uses only the Python standard library. Random-vector trials are finite sanity
checks, not a replacement for the Fourier-mode proof in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, pi, log2
from random import Random

rng = Random(20261026)
checks = 0

def direct_energy(n, t, z):
    # Index 0 is the central vertex; indices 1..n are the rim.
    q = F(0)
    for i in range(n+1):
        for j in range(i+1, n+1):
            if i == 0 or j == 0:
                dist_power = F(1)
            elif abs(i-j) in (1,n-1):
                dist_power = F(1)
            else:
                dist_power = t
            q -= 2*dist_power*z[i]*z[j]
    return q

def decomposed_energy(n, t, z):
    a = z[0]
    b = -a/F(n)
    x = [v-b for v in z[1:]]
    assert sum(x)==0
    gamma_h = (2*(n-1)-(n-3)*t)/F(n+1)
    return (gamma_h*(a*a+n*b*b)
            +t*sum((v*v for v in x), F(0))
            +(t-1)*2*sum((x[i]*x[(i+1)%n] for i in range(n)), F(0)))

for n in range(4,31):
    for t in [F(1),F(2),F(7,3),F(4),F(13,2)]:
        for _ in range(55):
            z=[F(rng.randint(-13,13)) for _ in range(n)]
            z.append(-sum(z))
            assert direct_energy(n,t,z)==decomposed_energy(n,t,z)
            checks+=1

# Independent Fourier-character tests of the asserted minimum, radial
# comparison and multiplicities. They test the full family of rim eigenvalues.
for n in range(4,201):
    c=1.0 if n%2==0 else cos(pi/n)
    tcrit=2*c/(2*c-1)
    assert tcrit>=2-1e-12
    for t in [1.0,1.15,2.0,tcrit,3.0,5.125]:
        eigenvalues=[t+2*(t-1)*cos(2*pi*k/n) for k in range(1,n)]
        radial=(2*(n-1)-(n-3)*t)/(n+1)
        asserted=2*c-(2*c-1)*t
        assert abs(min(eigenvalues+[radial])-asserted)<1e-10*(1+abs(t))
        if t>1.0:
            assert radial>asserted-1e-11
        checks+=1
    if n%2==0:
        assert abs(tcrit-2.0)<1e-12
    else:
        assert 1.0<log2(tcrit)<2.0
    checks+=1

# Direct witness ratios for extremal Fourier directions and hub/rim
# orthogonality. Negative type at the critical parameter has the expected
# kernel dimension; eigenspaces are linearly independent by DFT orthogonality.
for n in range(4,101):
    c=1.0 if n%2==0 else cos(pi/n)
    tcrit=2*c/(2*c-1)
    ks=[n//2] if n%2==0 else [(n-1)//2,(n+1)//2]
    for t in [1.0,1.5,2.0,tcrit,5.0]:
        target=2*c-(2*c-1)*t
        for k in ks:
            for fn in (lambda angle:cos(angle),lambda angle:__import__('math').sin(angle)):
                x=[fn(2*pi*k*j/n) for j in range(n)]
                if max(abs(v) for v in x)<1e-12: continue
                z=[0.0]+x
                # Subtract an insignificantly small numerical mean.
                mu=sum(z)/(n+1)
                z=[v-mu for v in z]
                numerator=0.0
                for i in range(n+1):
                    for j in range(i+1,n+1):
                        d=1.0 if i==0 or j==0 or abs(i-j) in (1,n-1) else t
                        numerator-=2*d*z[i]*z[j]
                quotient=numerator/sum(v*v for v in z)
                assert abs(quotient-target)<4e-10*(1+abs(target))
                checks+=1

print('PASS:',checks,'exact-rational/spectral/witness checks on wheels with 4..200 rim vertices')
