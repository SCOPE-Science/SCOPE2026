"""Independent numerical checks for the perimeter-depth theorem of symmetric trapezoids.

Run with Python 3 standard library: python trapezoid_depth_checker.py
Finite numerical sampling is supplementary to the all-parameter analytic proof.
"""
from math import hypot, sqrt, pi, sin, cos, isfinite, atan2
from random import Random


def formula(B, b, h):
    assert B > 0 and 0 <= b <= B and h > 0
    c = (B + 2*b)/(3*(B + b))
    L = hypot(B-b, h)
    a = B-(B-b)*c
    v = c*L
    lo = a/(1-c)
    hi = 2*B
    z = min(hi, max(lo, a + sqrt(a*v)))
    f = z + v*z/(z-a)
    top = 2*b + 2*(1-c)*L
    return min(f, top)/(2*(B+b+L)), (f, top, z)


def boundary_fraction(B, b, h, theta):
    """Find line-boundary intersections independently from the formula."""
    c = (B + 2*b)/(3*(B + b))
    vertices = [(-B, 0.0), (B, 0.0), (b, h), (-b, h)]
    d = (cos(theta), sin(theta))
    cum = 0.0
    intersects = []
    for i in range(4):
        x,y = vertices[i]
        X,Y = vertices[(i+1)%4]
        ex,ey = X-x,Y-y
        length = hypot(ex,ey)
        den = d[0]*ey - d[1]*ex
        if abs(den)>1e-13:
            s = -((-x)*d[1]-(c*h-y)*d[0])/den
            if -1e-11 <= s <= 1+1e-11:
                ss=max(0,min(1,s))
                intersects.append((cum+ss*length, x+ss*ex, y+ss*ey))
        cum += length
    unique=[]
    for hit in intersects:
        if not any(hypot(hit[1]-old[1],hit[2]-old[2])<1e-8 for old in unique):
            unique.append(hit)
    if len(unique)!=2:
        return None
    arc=abs(unique[0][0]-unique[1][0])
    return min(arc,cum-arc)/cum


def run():
    rng=Random(173291)
    tests=0; rays=0; tolerance=3e-7
    shapes=[(1.0,b,h) for b in (0.0,.01,.1,.3,.5,.9,1.0)
            for h in (.01,.3,1,2,5,20,100)]
    for _ in range(155):
        shapes.append((1.0,rng.random(),10**rng.uniform(-2,2.5)))
    for B,b,h in shapes:
        val,parts=formula(B,b,h)
        assert val > .25 - 3e-13
        samples=[]
        for k in range(1801):
            p=boundary_fraction(B,b,h,pi*k/1801)
            if p is not None and isfinite(p):
                assert p >= val-tolerance,(B,b,h,k,p,val)
                samples.append(p)
                rays+=1
        # Evaluate the optimal finite wedge chord by independent
        # intersections rather than relying on grid resolution.
        f,top,z=parts
        c=(B+2*b)/(3*(B+b))
        L=hypot(B-b,h)
        a=B-(B-b)*c
        beta=c*L*z/(z-a)
        X=(B-z,0)
        Y=(B-(B-b)*beta/L, h*beta/L)
        th=atan2(Y[1]-X[1],Y[0]-X[0])
        observed=boundary_fraction(B,b,h,th)
        if observed is not None:
            assert abs(min(f,2*(B+b+L)-f)/(2*(B+b+L))-observed)<2e-6,(B,b,h,observed,f)
        horiz=boundary_fraction(B,b,h,0.0)
        if horiz is not None:
            assert abs(horiz-min(top,2*(B+b+L)-top)/(2*(B+b+L)))<2e-6
        tests+=1
    # The exact median of an isosceles triangle of sides 15,15,2
    # cuts an arc of length 2+15/2 from a perimeter of 32.
    assert 19*10 < 3*64
    assert (19/64)<(3/10)
    # The open family b=1/k, B=1, h=k approaches depth 1/4.
    for k in (1000,10000,100000):
        val,_=formula(1,1/k,k)
        assert .25 < val < .25+1.0/k
    print('TRAPEZOID_DEPTH_OK shapes=',tests,'direct_rays=',rays,'triangle_fraction=19/64')

if __name__=='__main__': run()
