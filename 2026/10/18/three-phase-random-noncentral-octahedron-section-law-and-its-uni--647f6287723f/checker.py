"""Reproducible numerical checks for an exact octahedron slicing law.

The symbolic proof is given in RESULT.md. Simulations here test the event
classification directly against the formula; they do not certify it.
"""
import math
import random

PI = math.pi
B0 = 1/math.sqrt(3)
B1 = 1/math.sqrt(2)
TSTAR = math.sqrt((5 + 2*math.sqrt(2))/17)


def J(t):
    assert 0 <= t <= B1 + 1e-14
    s = min(t, B1)
    theta = math.asin(min(1.,s/math.sqrt(1-s*s)))
    return s*theta + math.atan(math.sqrt(max(0.,1-2*s*s))) - PI/4


def law(t):
    assert 0 <= t <= 1
    a1 = 1-t
    a2 = 1-2*t+4*J(t)/PI if t < B1 else 0.
    a3 = 1-3*t+12*J(t)/PI if t < B0 else 0.
    return (1-3*a1+3*a2-a3,3*a1-6*a2+3*a3,3*a2-2*a3)


def section_vertex_count_from_edges(u,t):
    # Exact graph incidence: the regular octahedron has one vertex for
    # each signed standard basis vector, with edges between distinct axes.
    endpoints=[(k,sgn,sgn*u[k]) for k in range(3) for sgn in (-1,1)]
    return sum((p[2]-t)*(q[2]-t)<0 for i,p in enumerate(endpoints)
               for q in endpoints[i+1:] if p[0] != q[0])


def test():
    assert abs(TSTAR**2-(5+2*math.sqrt(2))/17)<1e-14
    assert B0 < TSTAR < B1
    samples=250_000
    rng=random.Random(710247)
    orientations=[]
    for _ in range(samples):
        xyz=[rng.gauss(0,1) for _ in range(3)]
        m=math.sqrt(sum(x*x for x in xyz))
        orientations.append(tuple(x/m for x in xyz))
    for t in (0.05,0.30,B0,0.62,TSTAR,0.69,B1,0.85):
        p=law(t)
        assert abs(sum(p)-1)<2e-12
        assert min(p)>-2e-12
        counts={0:0,4:0,6:0}
        for u in orientations:
            n=section_vertex_count_from_edges(u,t)
            assert n in counts, (t,n,u)
            counts[n]+=1
        measured=tuple(counts[n]/samples for n in (0,4,6))
        err=max(abs(a-b) for a,b in zip(p,measured))
        print('offset=',round(t,9),'theory=',tuple(round(x,8) for x in p),
              'empirical=',tuple(round(x,8) for x in measured),'maxerr=',round(err,7))
        assert err<0.008
    theta=3*PI/8
    assert abs(math.asin(TSTAR/math.sqrt(1-TSTAR*TSTAR))-theta)<1e-13
    pm=law(TSTAR)[1]
    closed=3-(24/PI)*math.atan(math.sqrt((7-4*math.sqrt(2))/17))
    assert abs(pm-closed)<1e-13
    for t in (0.2,0.5,0.6,B0,0.65,0.67,0.69,B1,0.8,0.9):
        if abs(t-TSTAR)>1e-12: assert law(t)[1]<pm
    print('unique analytical maximum at',TSTAR,'probability',pm)
    print('all checks passed')


if __name__=='__main__': test()
