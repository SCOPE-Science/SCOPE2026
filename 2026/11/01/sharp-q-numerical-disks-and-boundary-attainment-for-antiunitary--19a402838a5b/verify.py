"""Finite supplementary checks for a scalar antiunitary q-range envelope.

All assertions are finite sanity checks, not proofs of an infinite-dimensional claim.
"""
from math import sqrt, pi, cos, sin
from random import Random

R = Random(20261028)
checks = 0
for _ in range(220):
    s, r = R.random(), R.random()
    t, a = sqrt(1-r*r), sqrt(1-s*s)
    target = 1.0 if r <= s else r*s+t*a
    sampled = max(r*(s*k/5000)+t*sqrt(max(0, 1-(s*k/5000)**2)) for k in range(5001))
    assert abs(sampled-target) < 0.00005
    lower = max(0, t*a-r*s)
    vals = [abs(r*(s*k/5000)-t*sqrt(max(0,1-(s*k/5000)**2))) for k in range(5001)]
    assert abs(min(vals)-lower) < 0.00012
    checks += 2
for s in (0.,.2,.5,.8,1.):
    a = sqrt(1-s*s)
    # Real-rotation times conjugation: [[s,-a],[a,s]] conjugates z.
    assert abs(s*s+a*a-1) < 1e-12
    best = 0.0
    for k in range(71):
        theta=k*pi/(2*70)
        for j in range(101):
            phase=2*pi*j/100
            x=complex(cos(theta),0)
            y=sin(theta)*complex(cos(phase),sin(phase))
            ax=s*x.conjugate()-a*y.conjugate()
            ay=a*x.conjugate()+s*y.conjugate()
            scalar=ax*x.conjugate()+ay*y.conjugate()
            best=max(best,abs(scalar))
    assert abs(best-s)<0.0008
    checks+=2
print(f'{checks} supplementary finite assertions passed')
