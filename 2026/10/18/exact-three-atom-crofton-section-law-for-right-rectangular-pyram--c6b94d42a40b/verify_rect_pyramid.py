"""Numerical checks for exact Crofton section probabilities of right rectangular pyramids.
Uses only the Python standard library. The analytic proof is in RESULT.md.
"""
import math
import random

PI=math.pi

def law(a,b,h):
    assert a>0 and b>0 and h>0
    S=math.hypot(a,b)
    D=math.hypot(S,h)
    J=.5*(D*(math.atan(h*a/(b*D))+math.atan(h*b/(a*D)))
          -a*math.atan(h/b)-b*math.atan(h/a))
    Z=PI*(a+b)+2*J
    return ((PI*(2*(a+b)-D-S)+4*J)/Z,
            (PI*(2*S-a-b)+2*J)/Z,
            (PI*(D-S)-4*J)/Z),J

def midpoint(f,n=10000):
    return (PI/2/n)*sum(f((i+.5)*PI/2/n) for i in range(n))

def verify_integrals(a,b,h):
    p,J=law(a,b,h)
    jp=midpoint(lambda t: .5*(h-(a*math.cos(t)+b*math.sin(t))*math.atan(h/(a*math.cos(t)+b*math.sin(t)))))
    jm=midpoint(lambda t: .5*(h-abs(a*math.cos(t)-b*math.sin(t))*math.atan2(h,abs(a*math.cos(t)-b*math.sin(t)))))
    assert abs(jp-J)<2e-8,(a,b,h,jp,J)
    assert abs(jm-(PI/2*(math.hypot(math.hypot(a,b),h)-math.hypot(a,b))-J))<2e-8,(a,b,h,jm,J)
    den=4*PI*(a+b)+8*J
    assert abs(p[2]-8*(jm-jp)/den)<2e-8

def simulate(a,b,h,seed=0,trials=75000):
    rng=random.Random(seed)
    vertices=((-a,-b,0.),(a,-b,0.),(a,b,0.),(-a,b,0.),(0.,0.,h))
    edges=((0,1),(1,2),(2,3),(3,0),(4,0),(4,1),(4,2),(4,3))
    weighted=[0.,0.,0.]
    total_weight=0.
    for _ in range(trials):
        uz=2*rng.random()-1
        theta=2*PI*rng.random()
        ur=math.sqrt(1-uz*uz)
        x,y,z=ur*math.cos(theta),ur*math.sin(theta),uz
        proj=tuple(x*vx+y*vy+z*vz for vx,vy,vz in vertices)
        low=min(proj); high=max(proj); w=high-low
        t=low+rng.random()*w
        number=sum((proj[i]-t)*(proj[j]-t)<0 for i,j in edges)
        assert number in (3,4,5)
        weighted[number-3]+=w
        total_weight+=w
    estimate=tuple(x/total_weight for x in weighted)
    predicted,_=law(a,b,h)
    err=max(abs(q-p) for p,q in zip(predicted,estimate))
    assert err<.013,(a,b,h,predicted,estimate,err)
    return predicted,estimate,err

if __name__=='__main__':
    shapes=((1.,1.,.1),(1.,1.,1.),(1.,1.,math.sqrt(2)),(1.,1.,3.),
            (1.,1.,10.),(.75,2.,.2),(.75,2.,1.6),(.75,2.,4.),(.25,3.,.9),
            (2.,4.,8.),(3.,.5,2.))
    max_err=0.
    for k,(a,b,h) in enumerate(shapes):
        verify_integrals(a,b,h)
        exact,observed,err=simulate(a,b,h,seed=1311+73*k,trials=75000)
        max_err=max(max_err,err)
        print('case',k,'half-base-height',a,b,h,'exact',tuple(round(q,8) for q in exact),'estimated',tuple(round(q,8) for q in observed),'error',round(err,8))
    print('CROFTON_RECTANGULAR_PYRAMID_OK',len(shapes),'cases',len(shapes)*75000,'orientation-offset samples','maximum_discrepancy',round(max_err,8))
