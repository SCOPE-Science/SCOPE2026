"""Deterministic finite checks for a logistic correction-sweep phase diagram."""
import math
import random


def correction_map(a, h, x):
    return a * math.exp(h * (1 - (a + x) / 2))


def c_value(a, h):
    return (h * a / 2) * math.exp(h * (1 - a / 2))


def w0(c):
    lo, hi = 0.0, max(1.0, c)
    for _ in range(110):
        mid = (lo + hi) / 2
        if mid + math.log(mid) < math.log(c):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cycle(c):
    if c <= math.e:
        raise ValueError('no nontrivial cycle')
    lo, hi = 0.0, max(4.0, c * 1.2)
    def log_c_d(d):
        if d < 0.00001:
            return 1 + d*d/24-d**4/960
        if d > 40:
            # u_plus ~ d ; log(u_minus) ~ log(d)-d
            return math.log(d) - d - math.log1p(-math.exp(-d)) + d / (-math.expm1(-d))
        v = d / math.expm1(d)
        u = v + d
        return math.log(v) + u
    for _ in range(100):
        m=(lo+hi)/2
        if log_c_d(m) < math.log(c): lo=m
        else: hi=m
    d = (lo + hi)/2
    bottom = d / math.expm1(d) if d < 40 else d*math.exp(-d)/(1-math.exp(-d))
    return bottom, bottom+d


def test():
    rng = random.Random(20261018)
    assertions = 0
    for _ in range(3000):
        a=rng.uniform(0.03,0.98)
        h=rng.uniform(0.03,7.0)
        c=c_value(a,h)
        w=w0(c)
        xstar=2*w/h
        x0=a*math.exp(h*(1-a))
        assert x0>xstar
        assert abs(correction_map(a,h,xstar)-xstar) < 4e-12*(1+xstar)
        assertions+=2
        if c < math.e * (1-0.02):
            x=x0
            for k in range(1500):
                x=correction_map(a,h,x)
            assert abs(x-xstar)<1e-6*(1+xstar), (a,h,c,x,xstar)
            assertions+=1
        if math.e*1.03<c<50:
            uminus,uplus=cycle(c)
            assert abs(c*math.exp(-uminus)-uplus)<2e-10*(1+uplus)
            assert abs(c*math.exp(-uplus)-uminus)<2e-10*(1+uminus)
            assert 0<uminus<w<uplus
            assert uminus*uplus<1
            assertions+=4
            x=x0
            for k in range(1200):
                x=correction_map(a,h,x)
            assert abs(x - 2*uplus/h)<1e-6*(1+x), (a,h,c,x,uminus,uplus)
            assertions+=1
    for a in [0.06,0.2,0.5,0.8,0.95]:
        lo,hi=0.0,6.0
        for _ in range(70):
            m=(lo+hi)/2
            if c_value(a,m)<math.e:lo=m
            else: hi=m
        hc=(lo+hi)/2
        hr=2*math.log(1/a)/(1-a)
        assert 2<hc<hr
        assert abs(c_value(a,hc)-math.e)<1e-13
        for h in [0.85*hc, 0.5*(hc+hr),1.15*hr]:
            w=w0(c_value(a,h)); xstar=2*w/h
            assert (xstar<1) == (h<hr)
        assertions+=6
    # Critical iteration in the normalized variable, avoiding a search over h.
    u=1.5
    for k in range(1,200001):
        u=math.exp(1-u)
    critical = math.sqrt(200000)*(u-1)
    assert abs(critical-math.sqrt(6))<0.02, critical
    assertions+=1
    # One interior-of-box example: correction iteration cycles despite the target < 1.
    a,h=0.5,2.3
    c=c_value(a,h)
    w=w0(c)
    low,high=cycle(c)
    assert math.e<c and 0<2*w/h<1<2*high/h
    print('Interior example (a,h,c,x*,x-,x+):',a,h,c,2*w/h,2*low/h,2*high/h)
    print('Critical sqrt(k)*(u_k-1):',critical,'target',math.sqrt(6))
    print('Deterministic assertion count:', assertions+1)


if __name__=='__main__':
    test()
