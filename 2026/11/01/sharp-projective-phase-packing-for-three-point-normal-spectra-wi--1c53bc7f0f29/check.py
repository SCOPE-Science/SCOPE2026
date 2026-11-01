"""Reproducible finite checks for the three-modulus Cartesian-radius theorem.
The infinite-dimensional and all-parameter theorem is proved analytically in RESULT.md;
these samples are only independent numerical sanity checks.
"""
import math
import random

PI = math.pi

def top(r):
    a=math.asin(r/2)
    return (PI-4*a+math.sin(4*a)+r*r*(4*a+2*math.sin(2*a)))/(2*PI)

def scalar_upper(r,L):
    return (L+math.sin(L)+r*r*(PI-L+2*math.sin((PI-L)/2)))/(2*PI)

def direct(r,p,q,n=20000):
    dt=PI/n
    total=0.0
    for j in range(n):
        t=(j+0.5)*dt
        total+=max(math.cos(t)**2, r*r*math.cos(t-p)**2, r*r*math.cos(t-q)**2)
    return total/n

checks=0
rng=random.Random(261004844)
for r in (0.02,0.07,0.2,0.35,0.5,0.8,0.95,1.0):
    a=math.asin(r/2)
    th=PI/2-a
    L=PI-4*a
    m=top(r)
    assert 0<L<PI and 0<a<=PI/6+1e-15
    checks+=1
    assert abs(m-scalar_upper(r,L))<3e-15
    checks+=1
    assert abs(direct(r,th,-th)-m)<2e-8
    checks+=1
    assert math.isclose(math.sin(L/2),1-r*r/2,rel_tol=2e-14,abs_tol=2e-14)
    checks+=1
    for j in range(100):
        x=rng.random()*PI
        assert scalar_upper(r,x)<=m+5e-15
        checks+=1
    for j in range(40):
        p=rng.random()*PI
        q=rng.random()*PI
        val=direct(r,p,q,n=1200)
        # Midpoint quadrature error is O(1/n) from bounded Lipschitz integrand.
        # Each square cosine has derivative <=1; maximum derivative <=1;
        # the integral-average midpoint error is <= pi/(4*n) (conservative).
        assert val <= m+PI/(4*1200)+1e-12
        checks+=1
for r in (0.0005,0.001,0.002,0.004):
    val=top(r)-0.5
    ratio=val/r**3
    assert abs(ratio-4/(3*PI))<0.000001
    checks+=1
print(f'PASS: {checks} deterministic numerical checks; analytical proof is separate.')
