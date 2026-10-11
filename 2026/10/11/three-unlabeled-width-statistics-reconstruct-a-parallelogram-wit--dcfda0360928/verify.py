"""Deterministic checks of exact width moments and inverse formulas."""
import math
import random

PI = math.pi


def width(t, a, b, angle):
    return a * abs(math.cos(t)) + b * abs(math.cos(t-angle))


def invariants(a, b, angle):
    mean = 2*(a+b)/PI
    second = 0.5*(a*a+b*b) + (2*a*b/PI)*(math.sin(angle)+(PI/2-angle)*math.cos(angle))
    maximum = math.sqrt(a*a+b*b+2*a*b*math.cos(angle))
    return mean, second, maximum


def recover(mean, second, maximum):
    s = PI*mean/2
    x = s*s-maximum*maximum
    t = (s*s/2-second)/x
    def T(angle):
        return 0.5-(math.sin(angle)-angle*math.cos(angle))/(PI*(1-math.cos(angle)))
    lo, hi = 1e-10, PI/2
    for _ in range(90):
        mid = (lo+hi)/2
        if T(mid) > t:
            lo = mid
        else:
            hi = mid
    angle = (lo+hi)/2
    p=x/(2*(1-math.cos(angle)))
    discr=max(0., s*s-4*p)
    return (s+math.sqrt(discr))/2, (s-math.sqrt(discr))/2, angle


def test():
    rng = random.Random(731015)
    count=0
    for a,b,angle in [
        (2.0,1.0,PI/3), (3.0,1.0,PI/2), (1.0,1.0,PI/3),
        (0.5,2.5,0.8), (7.0,4.0,PI/2)]:
        mean, second, maximum=invariants(a,b,angle)
        n=200000
        step=2*PI/n
        w=[width(step*j,a,b,angle) for j in range(n)]
        assert abs(sum(w)/n-mean) < 5e-9
        assert abs(sum(x*x for x in w)/n-second) < 1e-8
        assert abs(max(w)-maximum) < 1e-8
        count+=3
    for j in range(2000):
        a=0.5+5*rng.random()
        b=0.5+5*rng.random()
        angle=0.1+(PI/2-0.1)*rng.random()
        obs=invariants(a,b,angle)
        ar,br,pr=recover(*obs)
        assert abs(ar-max(a,b)) < 2e-5, (a,b,angle,ar,br,pr)
        assert abs(br-min(a,b)) < 2e-5
        assert abs(pr-angle)<1e-8
        count+=3
    # The angle-independent conditional expression is strictly decreasing.
    angles=[0.01+j*(PI/2-0.02)/1000 for j in range(1001)]
    T=lambda u:0.5-(math.sin(u)-u*math.cos(u))/(PI*(1-math.cos(u)))
    assert all(T(angles[j])>T(angles[j+1]) for j in range(1000))
    count+=1000
    # Near an equal-sided parallelogram the observables vary quadratically.
    base=invariants(1.,1.,0.7)
    for t in [0.1,0.02,0.005,0.001]:
        alt=invariants(1.+t,1.-t,0.7)
        assert max(abs(x-y) for x,y in zip(base,alt))<3*t*t
        count+=1
    print('VERIFY_OK', count)

if __name__=='__main__':
    test()
