"""Independent finite checks of an intrinsic flat-strip distance-law theorem.

Python 3 standard library only. These tests corroborate, but cannot replace,
the unrestricted analytic arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, log, hypot
from random import Random


def shortcut_probability(s, h):
    x = h / s
    if x <= 1:
        return x * x / 8
    return .5 - 3/(8*x*x) - log(x)/(2*x*x)


def simpson(f, a, b, n=2000):
    if b <= a:
        return 0.
    if n % 2: n += 1
    dt = (b-a)/n
    v = f(a) + f(b)
    for i in range(1,n):
        v += (4 if i % 2 else 2)*f(a + i*dt)
    return v*dt/3


def cdf_gap(r, s, h):
    if r <= s or r >= hypot(s,2*h):
        return 0.
    lower = max(0., 2*s-r)
    def f(t):
        c = sqrt(max(0., (r-t)*(r+t)))
        a = max(0., 2*h-c)
        b = sqrt(max(0., (r-(2*s-t))*(r+(2*s-t))))
        z = min(a,b)
        return a*z-z*z/2
    return simpson(f,lower,s,3600)/(2*h*h*s)


def cyl_tail_near_diameter(r,s,h):
    lower = sqrt(max(0.,r*r-4*h*h))
    def f(t):
        c = sqrt(max(0.,(r-t)*(r+t)))
        z = max(0.,2*h-c)
        return z*z/(4*h*h)
    return simpson(f,lower,s,3600)/s


def verify_exact_decks():
    checks=0
    for s,h in ((F(1),F(1)),(F(3,2),F(2,5)),(F(3,4),F(7,3))):
        L=2*s
        for i in range(7):
            x=L*F(i,7)
            for j in range(7):
                xx=L*F(j,7)
                delta=x-xx
                k0=delta//L
                q=delta-k0*L
                for yi in range(-3,4):
                    y=h*F(yi,3)
                    for zi in range(-3,4):
                        yy=h*F(zi,3)
                        signs=(-1 if k0%2 else 1)
                        t=q if q<=s else L-q
                        yp=signs*yy if q<=s else -signs*yy
                        a=t*t+(y-yp)**2
                        b=(L-t)**2+(y+yp)**2
                        v=min(a,b)
                        brute=min((delta-k*L)**2+(y-((-1 if k%2 else 1)*yy))**2 for k in range(-4,5))
                        assert v==brute, (s,h,x,xx,y,yy,v,brute)
                        checks+=1
    return checks


def verify_gap_and_frequency():
    rng=Random(20261029)
    checks=0
    for s,h in ((1.,.35),(1.,1.),(1.,2.4)):
        N=250000
        radii=(s+.09, (s+hypot(s,2*h))/2)
        hits=[0,0]
        short=0
        for _ in range(N):
            t=rng.random()*s
            y=(2*rng.random()-1)*h
            yy=(2*rng.random()-1)*h
            a=t*t+(y-yy)**2
            b=(2*s-t)**2+(y+yy)**2
            short+=int(b<a)
            for k,r in enumerate(radii):
                hits[k]+=int(b<=r*r<a)
            assert (b<a)==(-y*yy>s*(s-t)), (s,h,t,y,yy)
            checks+=1
        predicted=shortcut_probability(s,h)
        assert abs(short/N-predicted)<.004,(s,h,short/N,predicted)
        for j,r in enumerate(radii):
            pred=cdf_gap(r,s,h)
            assert abs(hits[j]/N-pred)<.005,(s,h,r,hits[j]/N,pred)
        checks+=3
    return checks


def verify_endpoints():
    checks=0
    for s,h in ((1.,.7),(1.,1.),(1.,3.)):
        for eps in (1e-5, 5e-6):
            obs=cdf_gap(s+eps,s,h)/eps**1.5
            target=2*sqrt(2)/(3*h*sqrt(s))
            assert abs(obs/target-1)<.025,(s,h,eps,obs,target)
            checks+=1
        R=hypot(s,2*h)
        for eps in (5e-4,2e-4):
            obs=cyl_tail_near_diameter(R-eps,s,h)/eps**3
            target=R**3/(48*h**4*s**2)
            assert abs(obs/target-1)<.018,(s,h,eps,obs,target)
            checks+=1
    return checks


def verify_shortcut_smoothness():
    from math import isclose
    # Exact symbolic derivatives at the transition, computed independently:
    # left derivatives (0..3): (1/8, 1/4, 1/4, 0)
    # right derivatives (0..3): (1/8, 1/4, 1/4, -4).
    x=1.
    right=(.5-3/(8*x*x)-log(x)/(2*x*x),
           (.25+log(x))/x**3,
           (.25-3*log(x))/x**4,
           (12*log(x)-4)/x**5)
    left=(x*x/8,x/4,.25,0)
    assert all(isclose(left[i],right[i],abs_tol=1e-13) for i in range(3))
    assert left[3]!=right[3]
    return 4


if __name__=='__main__':
    a=verify_exact_decks()
    b=verify_gap_and_frequency()
    c=verify_endpoints()
    d=verify_shortcut_smoothness()
    print('PASS: exact lift/deck comparisons:',a)
    print('PASS: deterministic seeded finite gap and shortcut comparisons:',b)
    print('PASS: endpoint scaling comparisons:',c)
    print('PASS: transition derivative comparisons:',d)
    print('TOTAL CHECKS:',a+b+c+d)
