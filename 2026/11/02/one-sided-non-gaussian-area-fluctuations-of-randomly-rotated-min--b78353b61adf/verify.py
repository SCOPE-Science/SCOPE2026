"""Reproduce geometry and moments for randomly rotated regular polygons.
Only the Python standard library is required. This program checks finite
geometric identities and numerical moment predictions; the infinite theorem
is proved analytically in RESULT.md.
"""
import itertools
import math
import random


def area_polygon(pts):
    return abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(pts,pts[1:]+pts[:1])))/2


def hull_area(points):
    points=sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in points:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-11: lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(points):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=1e-11: up.pop()
        up.append(p)
    return area_polygon(lo[:-1]+up[:-1])


def geometric_area(m,angles):
    polygons=[[(math.cos(t+2*math.pi*k/m),math.sin(t+2*math.pi*k/m))
               for k in range(m)] for t in angles]
    sums=[(sum(z[0] for z in vertices),sum(z[1] for z in vertices))
          for vertices in itertools.product(*polygons)]
    return hull_area(sums)


def analytic_area(m,angles):
    n=len(angles); a=math.pi/m
    perimeter=2*m*math.sin(a)
    base=m*math.sin(a)*math.cos(a)
    total=n*base
    for i in range(n):
        for j in range(i):
            w=(angles[i]-angles[j]+a)%(2*a)-a
            total+=perimeter*math.cos(a-abs(w))
    return total


def variance_analytic(m,n):
    a=math.pi/m
    p=2*m*math.sin(a)
    return n*(n-1)*p*p/2*(.5+math.sin(2*a)/(4*a)-(math.sin(a)/a)**2)


def dirichlet_spectrum_variance(m,terms=50000):
    a=math.pi/m; p=2*m*math.sin(a); mu=math.sin(a)/a
    return p*p*mu*mu*sum(1/(m*m*k*k-1)**2 for k in range(1,terms+1))


def test():
    rng=random.Random(20460715)
    worst=0
    for m,n,reps in [(3,4,200),(4,3,120),(5,3,60)]:
        for _ in range(reps):
            angles=[rng.uniform(-3,3) for _ in range(n)]
            actual=geometric_area(m,angles)
            expected=analytic_area(m,angles)
            worst=max(worst,abs(actual-expected))
            assert abs(actual-expected)<1e-8,(m,n,actual,expected)
    print('independent convex hull enumerations passed; largest difference',worst)
    for m in (3,4,5,7,12):
        a=math.pi/m;p=2*m*math.sin(a)
        area=m*math.sin(a)*math.cos(a)
        D=p*p/(4*math.pi)-area
        mu=math.sin(a)/a
        spectrum_D=p*mu*(sum(1/(m*m*k*k-1) for k in range(1,70001)) + 1/(m*m*70000.5))
        v_spec=dirichlet_spectrum_variance(m)
        v_direct=variance_analytic(m,2)/2
        assert abs(D-spectrum_D)<3e-9,('isoperimetric spectrum',m,D,spectrum_D)
        assert abs(v_spec-v_direct)<1e-10,('variance spectrum',m,v_spec,v_direct)
        assert D>0
    print('regular polygon Fourier spectral sums and isoperimetric bounds passed')
    m,n=3,9
    values=[analytic_area(m,[rng.random()*2*math.pi for j in range(n)]) for _ in range(16000)]
    mean=sum(values)/len(values)
    empirical_variance=sum((x-mean)**2 for x in values)/len(values)
    p=2*m*math.sin(math.pi/m);base=m*math.sin(math.pi/m)*math.cos(math.pi/m)
    expected_mean=n*n*p*p/(4*math.pi)-n*(p*p/(4*math.pi)-base)
    expected_variance=variance_analytic(m,n)
    assert abs(mean-expected_mean)<.17,(mean,expected_mean)
    assert abs(empirical_variance-expected_variance)/expected_variance<.07,(empirical_variance,expected_variance)
    print('Monte Carlo mean',mean,'theoretical',expected_mean)
    print('Monte Carlo variance',empirical_variance,'theoretical',expected_variance)
    print('ALL_ROTATIONAL_MINKOWSKI_CHECKS_PASSED')

if __name__=='__main__':test()
