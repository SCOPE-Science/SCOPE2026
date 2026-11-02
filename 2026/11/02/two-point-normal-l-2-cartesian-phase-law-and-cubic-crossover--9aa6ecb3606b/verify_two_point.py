"""Numerical consistency checks for the two-point normal spectral formula.

This program tests formulas on finitely many samples. It is not an
independent proof of the analytic statements.
"""
import math


def closed_square(r, beta):
    assert 0 < r < 1 and 0 <= beta <= math.pi/2
    a = (1-r*r)/2
    s = r*math.sin(beta)
    return 0.5 + (s - a*math.atan(s/a))/math.pi


def quadrature_square(r,beta,m=50000):
    return sum(max(math.cos(2*math.pi*(k+0.5)/m)**2,
                   r*r*math.cos(2*math.pi*(k+0.5)/m-beta)**2)
               for k in range(m))/m


def sharp_max(r):
    return 0.5+(r-(1-r*r)*math.atan(r))/math.pi

checks=0
for r in (0.03,0.13,0.37,0.74,0.92,0.99):
    last = -1
    for j in range(13):
        beta=math.pi*j/24
        v=closed_square(r,beta)
        measured=quadrature_square(r,beta,12000)
        assert abs(v-measured)<3e-8,(r,beta,v,measured)
        checks+=1
        assert v>=last-1e-14
        last=v
        checks+=1
    assert abs(closed_square(r,math.pi/2)-sharp_max(r))<2e-15
    checks+=1
for r in (0.2,0.5,0.85):
    A=(1-r*r)/2
    pred=r**3/(3*math.pi*A*A)
    for beta in (1e-2,5e-3,2e-3):
        err=(closed_square(r,beta)-.5)/beta**3
        assert abs(err/pred-1)<0.04,(r,beta,err,pred)
        checks+=1
for t in (.25,.75,1.5,3):
    for eps in (1e-3,1e-4):
        v=(closed_square(1-eps,t*eps)-.5)/eps
        target=(t-math.atan(t))/math.pi
        assert abs(v-target)<0.002,(t,eps,v,target)
        checks+=1
# Both global cubic coefficients are sharp on the phase interval.
for r in (0.08, 0.25, 0.5, 0.75, 0.95):
    a=(1-r*r)/2
    cminus=(r-(1-r*r)*math.atan(r))/math.pi
    cplus=r**3/(3*math.pi*a*a)
    for j in range(1, 49):
        beta=(math.pi/2)*j/49
        s=math.sin(beta)
        deficit=closed_square(r,beta)-.5
        assert cminus*s**3 <= deficit+4e-15, (r,beta,'lower')
        checks += 1
        assert deficit <= cplus*s**3+4e-15, (r,beta,'upper')
        checks += 1
        assert deficit>0
        checks += 1
    # The lower coefficient is realized at projective right angles.
    assert abs((closed_square(r,math.pi/2)-.5)-cminus)<2e-15
    checks+=1
    # The upper coefficient is the small-angle ratio limit.
    beta=0.001
    ratio=(closed_square(r,beta)-.5)/math.sin(beta)**3
    assert abs(ratio/cplus-1)<0.002
    checks+=1
print(f'{checks} consistency assertions passed')
