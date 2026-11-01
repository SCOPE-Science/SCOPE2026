"""Reproducible numerical spot checks for convex translation fibers.

All identities/inequalities are proved analytically in RESULT.md;
finite numerical checks here do not constitute proofs.
"""
import math


def log_cosh(x):
    q = abs(x)
    return q + math.log1p(math.exp(-2.0*q)) - math.log(2.0)


def polygon_measure(points):
    facets = []
    for p, q in zip(points, points[1:] + points[:1]):
        dx, dy = q[0]-p[0], q[1]-p[1]
        length = math.hypot(dx,dy)
        normal = (dy/length, -dx/length)
        h = normal[0]*p[0] + normal[1]*p[1]
        facets.append((normal, h, length))
    return facets


def phi(facets, z, y):
    s = 0.0
    for (nx,ny), h, mass in facets:
        a = h - nx*z[0] - ny*z[1]
        assert a>0
        b = (nx*y[0] + ny*y[1])/2.0
        s += mass*a*log_cosh(b/a)
    return s


def radial(facets, z, angle, threshold=1.0):
    unit = (math.cos(angle), math.sin(angle))
    lo,hi=0.0,1.0
    while phi(facets,z,(hi*unit[0],hi*unit[1]))<threshold:
        hi*=2
    for _ in range(44):
        m=(lo+hi)/2
        if phi(facets,z,(m*unit[0],m*unit[1]))<threshold:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def area(facets,z, n=1024,threshold=1.0):
    return math.pi/n * sum(radial(facets,z,2*math.pi*(i+.5)/n,threshold)**2 for i in range(n))


def evaluate():
    square=polygon_measure([(-1,-1),(1,-1),(1,1),(-1,1)])
    triangle=polygon_measure([(0,0),(3,0),(.5,2)])
    max_perspective_error=0.0
    for facets,z0,z1 in [(square,(0,0),(.4,-.25)), (triangle,(1.16666666666667,.6666666666667),(.65,.5))]:
        zm=tuple((a+b)/2 for a,b in zip(z0,z1))
        for angle in [(.1+i*.075) for i in range(80)]:
            y0=(.8*math.cos(angle),.8*math.sin(angle))
            y1=(.9*math.cos(angle+.12),.9*math.sin(angle+.12))
            ym=tuple((a+b)/2 for a,b in zip(y0,y1))
            err=phi(facets,zm,ym)-.5*(phi(facets,z0,y0)+phi(facets,z1,y1))
            max_perspective_error=max(max_perspective_error,err)
            assert err<2e-12,err
        v0,v1,vm=(area(facets,z) for z in (z0,z1,zm))
        margin=math.sqrt(vm)-.5*(math.sqrt(v0)+math.sqrt(v1))
        print('areas:',[round(x,10) for x in (v0,vm,v1)], 'concavity margin',margin)
        assert margin>0.00001
    for v in [(1,0),(.5,.6),(-.3,.8)]:
        for lam in (.2,.7,1.1,2.):
            y=(v[0]*lam,v[1]*lam)
            assert phi(square,(0,0),y)<=phi(square,(.4,-.25),y)+1e-12
    c_area=area(square,(0,0))
    s_area=area(square,(.4,-.25))
    print('square centered vs shifted',c_area,s_area)
    assert c_area>s_area
    print('max Jensen error',max_perspective_error)
    print('PASS: convexity, strict volume-root concavity examples, center inclusion')

if __name__=='__main__':
    evaluate()
