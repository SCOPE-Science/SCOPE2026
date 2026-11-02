"""Reproducibility checks for homogeneous Bregman-gradient stability.

Pure Python 3, no third-party dependencies. All diagnostics are finite tests,
not replacements for the analytic proof of the universal assertions.
"""
from math import sqrt, isfinite
from random import Random

def update(x, a, eta, p):
    r = sqrt(sum(t*t for t in x))
    h = 1+r**(p-2)
    u = [(h-eta*ai*abs(t)**(p-2))*t for ai,t in zip(a,x)]
    z = sqrt(sum(v*v for v in u))
    if z == 0: return tuple(0.0 for _ in x)
    q = z if z<=1 else z**(1/(p-1))
    for _ in range(35):
        q -= (q+q**(p-1)-z)/(1+(p-1)*q**(p-2))
    return tuple(v/(1+q**(p-2)) for v in u)

def norm(x): return sqrt(sum(t*t for t in x))

def main():
    rng=Random(327119)
    tests=0
    for p in (3.,4.,5.,6.):
        for n in (1,2,3,5):
            for _ in range(120):
                a=[10**rng.uniform(-1,1) for _ in range(n)]
                x=[rng.uniform(-1,1)*10**rng.uniform(-2,1) for _ in range(n)]
                if norm(x)<1e-9: continue
                eta=2/max(a)*rng.choice((.11,.7,1.0))
                xn=update(x,a,eta,p)
                assert norm(xn)<norm(x)*(1+1e-12), (p,n,x,a,eta,xn)
                tests+=1
    axis=0
    for p in (3.,4.,5.,6.):
        for a in (.2,1.,3.):
            eta=3/a
            critical=(2/(eta*a-2))**(1/(p-2))
            q=update((critical,),(a,),eta,p)[0]
            assert abs(q+critical)<2e-12*critical
            assert norm(update((.5*critical,),(a,),eta,p))<.5*critical
            assert norm(update((1.5*critical,),(a,),eta,p))>1.5*critical
            extinct=(1/(eta*a-1))**(1/(p-2))
            assert abs(update((extinct,),(a,),eta,p)[0])<1e-12
            axis+=1
    a=[1.,2.,.4]
    eta=.65
    x=[1.25,-.7,.44]
    for _ in range(30000): x=update(x,a,eta,4.)
    for xi,ai in zip(x,a):
        value=30000*xi*xi
        target=1/(2*eta*ai)
        assert abs(value/target-1)<.025,(value,target)
    # Period-two boundary and non-convergence above it are analytical:
    # a fixed finite numeric check also verifies the sharp phase portrait.
    for t in (.5,1.,1.25,2.):
        eta=3.
        v=t*sqrt(2)
        w=v
        for _ in range(60):
            w=update((w,),(1.,),eta,4.)[0]
            if abs(w)>1e12: break
        if t<1: assert abs(w)<abs(v)
        if t==1: assert abs(abs(w)-abs(v))<1e-10
        if t>1: assert abs(w)>abs(v)
    print(f'VERIFY_OK radial_trials={tests} axial_boundary_cases={axis} asymptotic_coordinates=3 phase_portrait=4')

if __name__=='__main__': main()
