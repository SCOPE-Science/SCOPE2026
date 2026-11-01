#!/usr/bin/env python3
"""Reproducible checks for intact sections of finite convex cylinders."""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi

def F(H, a):
    return H/2 - a*math.atan2(H, 2*a) if a > 0 else H/2

def lower(H, r):
    return (H - 2*r*math.atan(H/(2*r)))/(H+PI*r)

def upper(H, r):
    return (math.hypot(H, PI*r)-PI*r)/(H+PI*r)

def polygon_width(verts, phi):
    c,s = math.cos(phi),math.sin(phi)
    projections = [x*c+y*s for x,y in verts]
    return max(projections)-min(projections)

def polygon_perimeter(verts):
    return sum(math.hypot(verts[(i+1)%len(verts)][0]-x,verts[(i+1)%len(verts)][1]-y)
               for i,(x,y) in enumerate(verts))

def exact_numeric_prob(width_fn, H, r):
    n=4096
    vals=[F(H, width_fn(2*PI*(k+0.5)/n)/2) for k in range(n)]
    return 2*sum(vals)/n/(H+PI*r)

def direct_angular_prob(width_fn,H,r):
    n=2048
    # independent 2D angular integration, including truncation and width calculation
    total=0.0
    for k in range(n):
        phi=(k+0.5)*2*PI/n
        w=width_fn(phi)
        theta_star=math.atan2(H,w)
        val=quad(lambda t: max(0.0,H*math.cos(t)-w*math.sin(t))*math.sin(t),
                 0,theta_star,epsabs=1e-12)[0]
        total+=val/n
    return 2*total/(H+PI*r)

def check_algebra():
    import sympy as S
    x, h = S.symbols('x h', positive=True)
    ff=h/2-x*S.atan(h/(2*x))
    assert S.simplify(S.diff(ff,x,2)-4*h**3/(h*h+4*x*x)**2)==0
    k=S.symbols('k',positive=True)
    low=(2*k-2*S.atan(k))/(2*k+S.pi)
    assert S.limit(low/k**3,k,0,dir='+')==2/(3*S.pi)
    high=(S.sqrt(4*k**2+S.pi**2)-S.pi)/(2*k+S.pi)
    assert S.limit(high/k**2,k,0,dir='+')==2/S.pi**2
    print('SYMBOLIC_CONVEXITY_AND_TWO_THIN_HEIGHT_EXPONENTS_PASSED')

def check_shapes():
    for H in (0.3,1.0,2.0,5.0):
        r=1.0
        shapes=[]
        # Perimeter-normalized rectangle and parallelogram
        for sx,sy in ((PI/2,PI/2),(.95*PI,.05*PI)):
            v=[(-sx/2,-sy/2),(sx/2,-sy/2),(sx/2,sy/2),(-sx/2,sy/2)]
            assert abs(polygon_perimeter(v)-2*PI)<1e-12
            shapes.append(v)
        # perimeter-normalized scalene triangle, illustrating width-only dependence
        v=[(-1.7,-.4),(1.4,-.2),(.1,1.9)]
        perimeter=polygon_perimeter(v)
        v=[(2*PI*x/perimeter,2*PI*y/perimeter) for x,y in v]
        shapes.append(v)
        for shape in shapes:
            width=lambda phi: polygon_width(shape,phi)
            ans=exact_numeric_prob(width,H,r)
            direct=direct_angular_prob(width,H,r)
            assert abs(ans-direct)<2e-6,(H,ans,direct)
            assert lower(H,r)<ans<upper(H,r),(H,ans,lower(H,r),upper(H,r))
        disk=exact_numeric_prob(lambda _:2*r,H,r)
        assert abs(disk-lower(H,r))<1e-11
    print('INDEPENDENT_ANGULAR_AND_WIDTH_POLYGON_CHECKS_PASSED',len(shapes)*4)

def check_zonoid_envelope():
    for H in (.3,1.,3.,10.):
        r=1.
        for eps in (.5,.1,.01,.0005):
            # thin rectangle with side lengths summing pi, with the long side pi*(1-eps)
            v=[(-PI*(1-eps)/2,-PI*eps/2),(PI*(1-eps)/2,-PI*eps/2),
               (PI*(1-eps)/2,PI*eps/2),(-PI*(1-eps)/2,PI*eps/2)]
            p=exact_numeric_prob(lambda phi: polygon_width(v,phi),H,r)
            assert lower(H,r)<p<upper(H,r)
            if eps==.0005:
                assert abs(p-upper(H,r))<5e-4,(H,p,upper(H,r))
        # strict stability estimate using square support function of symmetral
        v=[(-PI/4,-PI/4),(PI/4,-PI/4),(PI/4,PI/4),(-PI/4,PI/4)]
        n=4096
        avg_variance=sum((polygon_width(v,(j+.5)*2*PI/n)/2-r)**2 for j in range(n))/n
        p=exact_numeric_prob(lambda phi:polygon_width(v,phi),H,r)
        c=4*H**3/((H+PI*r)*(H*H+PI*PI*r*r)**2)
        assert p-lower(H,r)>=c*avg_variance-1e-12
    print('SEGMENT_SUPREMUM_AND_WIDTH_VARIANCE_RIGIDITY_PASSED')

def check_disk_eccentricity():
    for k in (.1,.7,2.,10.):
        end=k/math.sqrt(1+k*k)
        def cdf(x):
            return (k*x*x-math.asin(x)+x*math.sqrt(1-x*x))/(k-math.atan(k))
        assert abs(cdf(end)-1)<1e-10
        assert abs(cdf(0))<1e-12
        for j in range(1,10):
            x=end*j/10
            check=quad(lambda z:2*z*(k-z/math.sqrt(1-z*z))/(k-math.atan(k)),0,x)[0]
            assert abs(cdf(x)-check)<2e-10
    k=1e-3
    for y in (.1,.3,.6,.9):
        x=k*y
        cdf=(k*x*x-math.asin(x)+x*math.sqrt(1-x*x))/(k-math.atan(k))
        assert abs(cdf-(3*y*y-2*y**3))<5e-5
    print('COMPLETE_DISK_ELLIPTICITY_DISTRIBUTION_AND_LIMIT_PASSED')



def check_invariant_plane_sampling():
    """Direct offset/normal rejection, independent of the integrated F formula."""
    rng = np.random.default_rng(77119)
    n = 350000
    H = 2.0
    for base in ('disk','square','asymmetric_triangle'):
        if base == 'disk':
            verts = None
            R = math.sqrt(1 + H*H/4)
            circumference = 2*PI
        elif base == 'square':
            a = PI/4
            verts = np.array([(-a,-a),(a,-a),(a,a),(-a,a)])
            circumference = 2*PI
            R = math.sqrt(max(x*x+y*y for x,y in verts)+H*H/4)
        else:
            raw = [(-1.7,-.4),(1.4,-.2),(.1,1.9)]
            perimeter = polygon_perimeter(raw)
            verts = np.array([(x*2*PI/perimeter,y*2*PI/perimeter) for x,y in raw])
            circumference = 2*PI
            R = math.sqrt(max(x*x+y*y for x,y in verts)+H*H/4)
        u = rng.uniform(size=n)
        phi = rng.uniform(0,2*PI,size=n)
        sin_theta = np.sqrt(1-u*u)
        t = rng.uniform(-R,R,size=n)
        if verts is None:
            v_min = -sin_theta
            v_max = sin_theta
            widthfn = lambda ph: 2.0
        else:
            projections = (verts[:,0,None]*np.cos(phi)[None,:]+verts[:,1,None]*np.sin(phi)[None,:])*sin_theta[None,:]
            v_min=projections.min(axis=0)
            v_max=projections.max(axis=0)
            widthfn = lambda ph:polygon_width(verts,ph)
        hit = (t >= v_min-H*u/2) & (t<=v_max+H*u/2)
        intact = hit & (t>=v_max-H*u/2) & (t<=v_min+H*u/2)
        measured = intact.sum()/hit.sum()
        expected = exact_numeric_prob(widthfn,H,1.)
        assert hit.sum()>35000,hit.sum()
        assert abs(measured-expected)<.006,(base,measured,expected,hit.sum())
    print('INVARIANT_RANDOM_PLANE_REJECTION_SAMPLING_PASSED',n*3)

if __name__=='__main__':
    check_algebra()
    check_shapes()
    check_zonoid_envelope()
    check_disk_eccentricity()
    check_invariant_plane_sampling()
    print('ALL_CHECKS_PASSED')
