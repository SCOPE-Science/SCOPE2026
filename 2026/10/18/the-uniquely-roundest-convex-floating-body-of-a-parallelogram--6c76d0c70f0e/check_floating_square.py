"""Reproducibility checks for exact Euclidean radii of square floating bodies.
Run: python check_floating_square.py (standard library only).
"""
import math
import random

SQ2=math.sqrt(2.0)
d0=1.5-SQ2

def h(d, theta):
    a,b=abs(math.cos(theta)),abs(math.sin(theta))
    if a<b:a,b=b,a
    if b<=2*d*a: return (1-2*d)*a
    return a+b-math.sqrt(8*d*a*b)

def rin(d):
    return math.sqrt(1-4*d) if d<=0.125 else SQ2-2*math.sqrt(d)

def rout(d):
    return max(1-2*d,SQ2-2*math.sqrt(d))

def exactcap(d,theta):
    # Signed upper quantile in the first octant; direct uniform-square cap formula.
    a,b=abs(math.cos(theta)),abs(math.sin(theta))
    if a<b:a,b=b,a
    q=h(d,theta)
    if b<1e-14:return (a-q)/(2*a)
    if q>=a-b: return (a+b-q)**2/(8*a*b)
    return (a-q)/(2*a)

def support_curve(d,theta):
    a,b=abs(math.cos(theta)),abs(math.sin(theta))
    if a<b:a,b=b,a
    ratio=b/a
    if ratio<=2*d:return (1-2*d)*a
    x=1-math.sqrt(2*d*ratio)
    y=1-math.sqrt(2*d/ratio)
    return a*x+b*y

def test():
    rng=random.Random(1729)
    max_err=0.
    for d in [0.000001,0.01,d0,0.1,0.125,0.2,1/3,0.49,0.499999]:
        for j in range(5001):
            theta=j*math.pi/4/5000
            max_err=max(max_err,abs(h(d,theta)-support_curve(d,theta)))
            if abs(exactcap(d,theta)-d)>3e-11:
                raise AssertionError(('cap',d,theta,exactcap(d,theta)))
        m=min(h(d,j*math.pi/4/5000) for j in range(5001))
        if abs(m-rin(d))>2e-7:raise AssertionError(('inradius',d,m,rin(d)))
        # Direct parameterization of the hyperbolic arc in the positive quadrant.
        ro=max(math.hypot(1-2*d,0), math.sqrt(2)*(1-math.sqrt(2*d)),
               max(math.hypot(x,1-2*d/(1-x)) for x in [(1-2*d)*j/10000 for j in range(10001)]))
        if abs(ro-rout(d))>3e-12:raise AssertionError(('outradius',d,ro,rout(d)))
    # Interior direction where support reaches the minimum.
    for d in [0.001,.03,.08,.1]:
        crit=4*d/(1-4*d)
        theta=math.asin(crit)/2
        assert theta>math.atan(2*d)
        assert abs(h(d,theta)-rin(d))<2e-14
    # Globally optimal parameter and strict monotonicity of the BM distortion.
    def bm(d):return rout(d)/rin(d)
    assert abs(bm(d0)-2*(SQ2-1)/math.sqrt(4*SQ2-5))<1e-13
    grid=[1e-8+(d0-2e-8)*j/1000 for j in range(1001)]
    assert all(bm(grid[i])>bm(grid[i+1]) for i in range(1000))
    grid=[d0+(0.49999-d0)*j/1000 for j in range(1001)]
    assert all(bm(grid[i])<bm(grid[i+1]) for i in range(1000))
    print('VERIFY_OK', 'normalization_samples=45009',
          'support_samples=45009', 'boundary_samples=90009',
          'min_parameter=%.15f'%d0,'min_BM=%.15f'%bm(d0),
          'max_support_discrepancy=%.3g'%max_err)
if __name__=='__main__':test()
