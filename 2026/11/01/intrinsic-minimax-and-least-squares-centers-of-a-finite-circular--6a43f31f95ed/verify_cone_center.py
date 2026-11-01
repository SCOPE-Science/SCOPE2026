"""Numerical finite checks for the radius/diameter formulas of a finite Euclidean cone.
The continuum theorem is proved in RESULT.md; this checker is diagnostic only.
Run: python3 verify_cone_center.py
"""
from math import pi, cos, sin, sqrt, isclose
from random import Random


def dist(r, s, angle, t, length=1.0):
    # angle is the smaller physical azimuthal separation in [0, pi].
    z = t * angle
    return sqrt(max(0.0, r*r + s*s - 2*r*s*cos(z)))


def eccentricity(r, t, length=1.0):
    c = cos(pi*t)
    return max(r, sqrt(max(0.0, r*r+length*length-2*r*length*c)))


def predicted(t, length=1.0):
    beta = pi*t
    c = cos(beta)
    if t <= .25:
        radial = length/(2*c)
        radius = radial
    elif t < .5:
        radial = length*c
        radius = length*sin(beta)
    else:
        radial = 0.0
        radius = length
    diam = max(length, 2*length*sin(beta/2))
    return radial, radius, diam


def frechet_radius(t, length=1.0):
    beta = pi*t
    return (2*length/3)*sin(beta)/beta


def frechet_energy(r, t, length=1.0):
    m = frechet_radius(t, length)
    return (r-m)**2 + length*length/2 - m*m


def bisect(f, low, high):
    assert f(low)*f(high)<0
    for _ in range(100):
        mid=(low+high)/2
        if f(mid)*f(low)>0: low=mid
        else: high=mid
    return (low+high)/2


def quad_frechet(r,t,length=1.0,nrad=240,nangle=160):
    # Midpoint quadrature evaluates the original source-target geodesic law.
    out=0.0
    for i in range(nrad):
        s=length*(i+.5)/nrad
        for j in range(nangle):
            delta=pi*(j+.5)/nangle
            out += (s/length)*(2/nrad/nangle)*dist(r,s,delta,t,length)**2
    return out


def test():
    rng = Random(1729)
    parameters = [.0001, .01, .1, .2, .25, .25001, .28, 1/3, .4, .49999, .5, .50001, .65, .75, .9, .9999]
    parameters += [rng.uniform(0.001, 0.999) for _ in range(50)]
    checks = 0
    max_center_gap = 0.0
    max_target_gap = 0.0
    for t in parameters:
        L = rng.uniform(.05, 20)
        rstar, rho, diam = predicted(t,L)
        assert 0 <= rstar <= L
        assert isclose(eccentricity(rstar,t,L),rho,rel_tol=2e-13,abs_tol=3e-13)
        checks += 1
        # Coarse unrestricted center search: no candidate beats exact radial center.
        for j in range(301):
            r = L*j/300
            assert eccentricity(r,t,L) >= rho - 1.e-11*L
            checks += 1
        # Separate full target enumeration of the claimed farthest-distance formula.
        for k in range(40):
            r = L*rng.random()
            max_target = 0.0
            for j in range(32):
                s = L*j/31
                for m in range(33):
                    angle = pi*m/32
                    d = dist(r,s,angle,t,L)
                    max_target = max(max_target, d)
                    assert d <= eccentricity(r,t,L) + 1.e-11*L
                    checks += 1
            max_target_gap = max(max_target_gap,abs(max_target-eccentricity(r,t,L))/L)
            assert abs(max_target-eccentricity(r,t,L)) <= 1.e-10*L
        # Strict uniqueness of minimizing radius except floating point near equality.
        for j in range(401):
            r=L*j/400
            if abs(r-rstar) > .01*L:
                assert eccentricity(r,t,L)>rho-1.e-11*L
                checks += 1
        # Sample pairs cannot exceed claimed geodesic diameter.
        for j in range(200):
            r = L*rng.random()
            s = L*rng.random()
            angle = pi*rng.random()
            assert dist(r,s,angle,t,L) <= diam+1.e-11*L
            checks += 1
        assert isclose(diam,max(L,dist(L,L,pi,t,L)),rel_tol=1e-14,abs_tol=1e-12)
        checks += 1
    # Sharp ratio has unique peak at t=1/3; sample the whole nondegenerate interval.
    sharp = sqrt(3)/2
    for j in range(1,10000):
        t=j/10000
        r,rho,diam=predicted(t)
        assert rho/diam <= sharp+1e-13
        if abs(t-1/3)>.002:
            assert rho/diam<sharp-1.e-7
        checks+=1
    r,rad,d=predicted(1/3)
    assert isclose(rad/d,sharp,rel_tol=1e-14)
    assert isclose(predicted(.25)[1],sqrt(.5),rel_tol=1e-14)
    assert isclose(predicted(.5)[1],1,rel_tol=1e-14)
    b1=bisect(lambda b:2*sin(2*b)-3*b,.5,pi/4)
    b2=bisect(lambda b:2*__import__('math').tan(b)-3*b,pi/4,1.2)
    assert abs(b1/pi-0.20303365998505848)<1.e-12
    assert abs(b2/pi-0.3079338236512857)<1.e-12
    for t in [.005, b1/pi, .22, .25, .3, b2/pi, .4, .5, .75, .99]:
        rC, rho, D=predicted(t)
        rF=frechet_radius(t)
        assert abs(frechet_energy(rF,t)-(0.5-rF*rF))<1.e-12
        if abs(t-b1/pi)<1e-9 or abs(t-b2/pi)<1e-9:
            assert abs(rC-rF)<1.e-12
        else:
            assert abs(rC-rF)>1.e-5
        for r in [0.,rC,rF,0.52,1.]:
            approx=quad_frechet(r,t)
            exact=frechet_energy(r,t)
            assert abs(approx-exact)<1.1e-5, (t,r,approx,exact)
            checks+=1
    print('Isolated center-coincidence cone ratios:',b1/pi,b2/pi)
    print(f'PASS: {checks:,} counted finite checks; {len(parameters)} cone ratios; 0 numerical failures')
    print('Maximum target-grid discrepancy:', max_target_gap)
    print('Sharp ratio attained at t=1/3:', sharp)

if __name__ == '__main__':
    test()
