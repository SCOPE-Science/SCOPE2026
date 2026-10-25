"""Independent finite spot checks for an exact isosceles-triangle inequality.

The general claim is proved analytically in RESULT.md; finite tests here are not a proof.
"""
from math import sqrt, hypot
from random import Random

def defect(h, x, y):
    """Returns the three pairwise vertex-versus-side deficits, apex first."""
    L = hypot(1.0, h)
    A, B, C = (0.0,h), (1.0,0.0), (-1.0,0.0)
    P=(x,y)
    verts=(A,B,C)
    R=[hypot(P[0]-v[0],P[1]-v[1]) for v in verts]
    r=[y,(h+h*x-y)/L,(h-h*x-y)/L]
    S=sum(r)
    return [sum(R)-R[i]-S-r[i] for i in range(3)]

rng=Random(2023)
for h in (0.025,0.1,0.3,1/sqrt(3),sqrt(3)):
    for _ in range(10000):
        a,b,c=[-__import__('math').log(rng.random()) for i in range(3)]
        x=(-b+c)/(a+b+c)
        y=h*a/(a+b+c)
        assert min(defect(h,x,y))>-5e-12, (h,x,y,defect(h,x,y))

for h in (0.65,0.8,1.0):
    L=hypot(1,h);t=h/L
    x=-sqrt(t*(1-t)/((1+t)*(2-t)))
    assert min(defect(h,x,0))<-1e-4
for h in (1.05,1.4,1.7):
    assert min(defect(h,0,h/3))<-1e-4
for h in (1.8,2.5,4.0):
    L=hypot(1,h)
    y=(L-1)/sqrt(2*L-1)
    assert 0<y<h and defect(h,0,y)[0]<-1e-4

# Exact algebraic identities used in the proof, sampled at rational points.
from fractions import Fraction as F
for t in [F(k,50) for k in range(1,36)]:
    left=(1-t*t)*(3*t-1)**2-t**3*(2-t)
    assert left==-(2*t-1)*(4*t**3-4*t+1)
print('Finite samples and exact polynomial identity: PASS; universal proof is analytic.')
