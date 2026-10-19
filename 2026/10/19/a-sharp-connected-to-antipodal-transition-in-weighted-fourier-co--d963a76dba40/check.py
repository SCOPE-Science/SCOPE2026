"""Deterministic checks for the two-mode Fourier spectral-mask theorem.

Analytic proof is in RESULT.md. These computations are finite diagnostics only.
"""
import cmath
import math
import random

random.seed(260912226)
PI = math.pi


def fourier_arcs(arcs, k):
    return sum((cmath.exp(-1j*k*start) - cmath.exp(-1j*k*end))/(2j*PI*k)
               for start, end in arcs)


def energy(arcs, p, q):
    return p*abs(fourier_arcs(arcs,1))**2 + q*abs(fourier_arcs(arcs,2))**2


def cap(alpha,p,q):
    c=math.cos(PI*alpha);s=math.sin(PI*alpha)
    return s*s/PI**2*max(p+q*c*c,q)


checks=0
for _ in range(18000):
    alpha=random.uniform(.0003,.5)
    L=PI*alpha
    a=random.uniform(.000001,L-.000001)
    b=L-a
    d=random.uniform(L,2*PI-L)
    p=10**random.uniform(-3,3)
    q=10**random.uniform(-3,3)
    arcs=[(-a,a),(d-b,d+b)]
    actual=energy(arcs,p,q)
    exact=(p*(math.sin(a)**2+math.sin(b)**2+2*math.sin(a)*math.sin(b)*math.cos(d))+
           q*((math.sin(a)*math.cos(a))**2+(math.sin(b)*math.cos(b))**2+
             2*math.sin(a)*math.sin(b)*math.cos(a)*math.cos(b)*math.cos(2*d)))/PI**2
    assert abs(actual-exact)<1e-10*(1+p+q)
    assert actual <= cap(alpha,p,q)+1e-10*(1+p+q)
    checks+=1

for _ in range(2000):
    alpha=random.uniform(.001,.999)
    p=10**random.uniform(-3,3);q=10**random.uniform(-3,3)
    arc=[(-PI*alpha,PI*alpha)]
    split=[(-PI*alpha/2,PI*alpha/2),(PI-PI*alpha/2,PI+PI*alpha/2)]
    aenergy=energy(arc,p,q);benergy=energy(split,p,q)
    assert abs(max(aenergy,benergy)-cap(alpha,p,q))<1e-10*(1+p+q)
    assert ((aenergy>=benergy-1e-12*(1+p+q)) ==
            (q*math.sin(PI*alpha)**2<=p+1e-12*(1+p+q)))
    checks+=1

for _ in range(1000):
    n=128
    alpha=random.randint(1,n-1)/n
    p=10**random.uniform(-2,2);q=10**random.uniform(-2,2)
    ids=random.sample(range(n),int(n*alpha))
    coeff=lambda k:sum(cmath.exp(-2j*PI*k*j/n) for j in ids)/n
    # exact finite samples can overshoot continuum if regarded as Dirac atoms;
    # compare the corresponding piecewise-constant mask instead.
    factor=lambda k: math.sin(PI*k/n)/(PI*k/n)
    val=p*abs(coeff(1)*factor(1))**2 + q*abs(coeff(2)*factor(2))**2
    assert val<=cap(alpha,p,q)+1e-10*(1+p+q)
    checks+=1

print('PASS',checks,'deterministic checks, all bounds hold')
