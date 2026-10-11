"""Elementary reproducibility checks for radial weighted-perimeter continuity.

No external modules. Numerical tests are finite illustrations, not proofs of
universal inequalities, for which the accompanying analytic argument is needed.
"""
from math import pi, hypot


def disk_energy(radius, power):
    return 2.0*pi*radius**(power+1)


def needle_energy(radius, power):
    # Twice the line integral on the diameter [-radius,radius].
    return 4.0*radius**(power+1)/(power+1)


def allowed_constant(power):
    assert -1 < power < 0
    return 2*pi*(2-power) + 4*pi*(-power)/(power+1)


def polygon_energy(vertices, power, subintervals=100000):
    # Midpoint quadrature for polygon sides not meeting the singular point.
    # For a needle passing through the origin, use needle_energy instead.
    total=0.0
    for a,b in zip(vertices, vertices[1:]+vertices[:1]):
        length=hypot(b[0]-a[0],b[1]-a[1])
        s=0.0
        for j in range(subintervals):
            t=(j+0.5)/subintervals
            x=(1-t)*a[0]+t*b[0]
            y=(1-t)*a[1]+t*b[1]
            s+=hypot(x,y)**power
        total+=length*s/subintervals
    return total


def main():
    # Exact formulas for disks and zero-dimensional limits.
    for p in (-.9,-.75,-.5,-.1):
        const=allowed_constant(p)
        for a,b in ((0.0,0.001),(.001,.03),(.2,.7),(1.5,2.6)):
            diff=abs(disk_energy(b,p)-(disk_energy(a,p) if a else 0))
            assert diff <= const*(b-a)**(p+1)+1e-12, (p,a,b,diff)
        for r in (.005,.2,2.0):
            assert abs(needle_energy(r,p)-4*r**(p+1)/(p+1))<1e-9
        # The exponent p+1 cannot be raised, already for point vs disk.
        for d in (.1,.01,.001):
            assert abs(disk_energy(d,p)/d**(p+1)-2*pi)<1e-10
    # Regimes p=0 and p>0 with K,L in a fixed centered ball of radius R.
    for p in (0,.25,.5,1,2,4):
        for a,b,R in ((0.0,.03,1.0),(.04,.35,.5),(.5,1.1,2.0),(.99,1.0,1.0)):
            lhs=abs(disk_energy(b,p)-(disk_energy(a,p) if a else 0))
            bound=(2*pi if p==0 else 2*pi*(1+max(1,p))*R**p)*(b-a)
            assert lhs <=bound+1e-10,(p,a,b,R,lhs,bound)
    # Support-function first variation for concentric disks: the exact
    # normal-variation integral equals 2*pi*(p+1)*r**p.
    for p in (-.75,-.5,.25,.5,1,2):
        r=0.9
        rhs=2*pi*(p+1)*r**p
        eps=1e-5
        lhs=(disk_energy(r+eps,p)-disk_energy(r-eps,p))/(2*eps)
        assert abs(lhs-rhs) < 1e-6, (p,lhs,rhs)
    # Polygon-side integrals for a nonregular convex triangle away from origin.
    tri=[(.9,.5), (1.75,.4), (1.2,1.4)]
    for p in (-.5,.5,2):
        v1=polygon_energy(tri,p,10000)
        v2=polygon_energy(tri,p,20000)
        assert abs(v1-v2)<1e-7, (p,v1,v2)
    print('RADIAL_WEIGHTED_PERIMETER_FINITE_CHECKS_OK')


if __name__=='__main__':
    main()
