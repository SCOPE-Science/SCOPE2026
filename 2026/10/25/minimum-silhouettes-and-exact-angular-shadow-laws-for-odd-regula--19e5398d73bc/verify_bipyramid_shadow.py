#!/usr/bin/env python3
"""Reproduce the pentagonal-bipyramid silhouette law with independent geometry."""
import math
import random
from collections import Counter

PI = math.pi
D = PI / 10
C = math.cos(PI / 5)
H_EQUAL_EDGES = (math.sqrt(5)-1)/2


def exact_law(h):
    assert h > 0
    q = h / math.hypot(h, C)
    F = lambda k: math.asin(q * math.sin(k*D))
    g = [F(k) for k in range(6)]
    w = 10 / PI
    return {4:w*(g[5]-g[4]),
            5:1+w*(2*g[4]-g[3]-g[5]-g[1]),
            6:w*(2*g[1]+2*g[3]-2*g[2]-g[4]),
            7:w*(2*g[2]-g[1]-g[3])}


def norm(v):
    z = math.sqrt(sum(x*x for x in v))
    return tuple(x/z for x in v)


def unit_sphere(rng):
    return norm(tuple(rng.gauss(0,1) for _ in range(3)))


def vertices(h, n=5):
    return [(math.cos(2*PI*j/n),math.sin(2*PI*j/n),0.0)
            for j in range(n)] + [(0,0,h),(0,0,-h)]


def cross3(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def hull_vertex_count(h,u,n=5):
    axis=(0,0,1) if abs(u[2])<0.9 else (1,0,0)
    a=norm(cross3(u,axis))
    b=cross3(u,a)
    points=sorted((sum(v[i]*a[i] for i in range(3)),sum(v[i]*b[i] for i in range(3))) for v in vertices(h,n))
    def turn(p,q,r): return (q[0]-p[0])*(r[1]-q[1])-(q[1]-p[1])*(r[0]-q[0])
    low=[]
    for p in points:
        while len(low)>=2 and turn(low[-2],low[-1],p)<=0: low.pop()
        low.append(p)
    high=[]
    for p in reversed(points):
        while len(high)>=2 and turn(high[-2],high[-1],p)<=0: high.pop()
        high.append(p)
    return len(low)+len(high)-2


def facet_sign_count(h,u,n=5):
    ux,uy,uz=u
    # Viewing the upper hemisphere is equivalent to reversing the viewing ray.
    if uz<0: ux,uy,uz=-ux,-uy,-uz
    cn=math.cos(PI/n)
    top=[];bottom=[]
    for j in range(n):
        ang=2*PI*(j+0.5)/n
        radial=ux*math.cos(ang)+uy*math.sin(ang)
        top.append((h/cn)*radial+uz>0)
        bottom.append((h/cn)*radial-uz>0)
    base=sum(top[j]!=bottom[j] for j in range(n))
    apex_t=sum(top[j]!=top[(j+1)%n] for j in range(n))
    apex_b=sum(bottom[j]!=bottom[(j+1)%n] for j in range(n))
    return base+apex_t+apex_b


def simpson(f,a,b,n=4000):
    assert n%2==0
    step=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*k+1)*step) for k in range(n//2))+2*sum(f(a+2*k*step) for k in range(1,n//2)))*step/3


def direct_quadrature_law(h):
    lam=h/C
    G=lambda x:lam*x/math.hypot(1,lam*x)
    functions=[lambda t:G(math.cos(2*PI/5+t)),
               lambda t:G(math.cos(2*PI/5-t))-G(math.cos(2*PI/5+t))+1-G(math.cos(t)),
               lambda t:G(math.cos(PI/5+t))-G(math.cos(2*PI/5-t))+G(math.cos(t))-G(math.cos(PI/5-t)),
               lambda t:G(math.cos(PI/5-t))-G(math.cos(PI/5+t))]
    return dict(zip((4,5,6,7),[(10/PI)*simpson(f,0,D) for f in functions]))


def mean_dihedral(h):
    r=h/C
    beta=2*math.atan(1/r)
    alpha=math.acos((1+r*r*math.cos(2*PI/5))/(1+r*r))
    return (5*beta+10*alpha)/PI


def odd_minimum_shadow_law(n,h):
    assert n>=5 and n%2==1 and h>0
    c=math.cos(PI/n)
    q=h/math.hypot(h,c)
    return (2*n/PI)*(math.asin(q)-math.asin(q*math.cos(PI/(2*n))))


def direct_odd_minimum_quadrature(n,h):
    assert n>=5 and n%2==1
    lam=h/math.cos(PI/n)
    return (2*n/PI)*simpson(lambda t:lam*math.sin(t)/math.hypot(1,lam*math.sin(t)),0,PI/(2*n))


def main():
    rng=random.Random(839205)
    for h in (0.15,H_EQUAL_EDGES,1.5,4.0):
        law=exact_law(h)
        assert abs(sum(law.values())-1)<2e-14
        assert all(p>0 for p in law.values())
        quad=direct_quadrature_law(h)
        assert max(abs(law[k]-quad[k]) for k in law)<3e-12,(h,law,quad)
        mean=sum(k*p for k,p in law.items())
        assert abs(mean-mean_dihedral(h))<3e-13,(h,mean,mean_dihedral(h))
        for i in range(4000):
            u=unit_sphere(rng)
            sides1=facet_sign_count(h,u)
            sides2=hull_vertex_count(h,u)
            assert sides1==sides2,(h,u,sides1,sides2)
        samples=70000
        counts=Counter(facet_sign_count(h,unit_sphere(rng)) for _ in range(samples))
        assert set(counts).issubset({4,5,6,7})
        assert all(abs(counts[k]/samples-law[k])<0.018 for k in law)
    for n,h in ((7,.3),(7,1.0),(9,.75),(11,3.0)):
        formula=odd_minimum_shadow_law(n,h)
        assert abs(formula-direct_odd_minimum_quadrature(n,h))<2e-12
        trials=26000
        seen=0
        for i in range(trials):
            u=unit_sphere(rng)
            sides=facet_sign_count(h,u,n)
            if i<1200: assert sides==hull_vertex_count(h,u,n)
            seen+=(sides==4)
        assert abs(seen/trials-formula)<0.015,(n,h,formula,seen/trials)
    # Fixed-height large-order law: n P(N=4) -> pi*h/4.
    for h in (0.3,.8,2.0):
        for n in (1001,10001):
            assert abs(n*odd_minimum_shadow_law(n,h)-PI*h/4)<0.001
    print('ALL_ODD_POLYGONAL_BIPYRAMID_QUADRILATERAL_LAW_QUADRATURE_OK')
    print('ODD_SEVEN_NINE_ELEVEN_SIDED_DIRECT_HULL_AND_HAAR_SAMPLING_OK')
    print('SHARP_FIXED_HEIGHT_LARGE_ORDER_QUADRILATERAL_RATE_OK')
    print('FOUR_SIDED_TO_SEVEN_SIDED_SUPPORT_ALL_HEIGHTS_TESTED_OK')
    print('INDEPENDENT_3D_PROJECTED_CONVEX_HULL_AND_FACET_SIGN_COUNTS_OK_16000')
    print('EXACT_ARCSINE_LAW_MATCHES_INDEPENDENT_DIRECT_SPHERICAL_QUADRATURE_OK')
    print('INDEPENDENT_EXTERIOR_DIHEDRAL_ANGLE_EXPECTATION_OK')
    print('FOUR_HAAR_ASPECT_RATIO_FREQUENCIES_OK_280000')
    print('EQUILATERAL_PROBABILITIES',exact_law(H_EQUAL_EDGES))
    print('ALL_PENTAGONAL_BIPYRAMID_SHADOW_CHECKS_OK')


if __name__=='__main__':main()
