"""Reproduce the centerline hotspot-switch calculations for a two-height plume.
Python >=3.9; only the standard library is required.
"""
import math
import random

RC = 3.0 + 2.0*math.sqrt(2.0)
TC = 2.0 - math.sqrt(2.0)
QC = math.exp(2.0*math.sqrt(2.0))/RC
CWIDTH = 8.0 * 2.0**0.75 * math.exp(2.0*math.sqrt(2.0)) / (3.0*RC*RC*(1+math.sqrt(2)))
KSEP = 2.0*math.sqrt(3.0*math.sqrt(2.0))/RC

def curve(t,r,q):
    return t*(math.exp(-t)+q*math.exp(-r*t))

def der(t,r,q):
    return math.exp(-t)*(1-t)+q*math.exp(-r*t)*(1-r*t)

def log_h(t,r):
    return (r-1)*t+math.log1p(-t)-math.log(r*t-1)

def bisect(fun,left,right,n=75):
    a=fun(left)
    b=fun(right)
    assert a*b<0,(left,right,a,b)
    for _ in range(n):
        mid=(left+right)/2
        if mid==left or mid==right: break
        val=fun(mid)
        if a*val>0:
            left=mid;a=val
        else:
            right=mid;b=val
    return (left+right)/2

def turning_parameters(r):
    assert r>RC
    z=math.sqrt((r-3)**2-8)
    minus=(r+1-z)/(2*r)
    plus=(r+1+z)/(2*r)
    assert 1/r<minus<plus<1
    lo=math.exp(log_h(minus,r))
    hi=math.exp(log_h(plus,r))
    assert lo<hi
    return minus,plus,lo,hi

def three_modes(r,q):
    a,b,lo,hi=turning_parameters(r)
    assert lo<q<hi
    logq=math.log(q)
    rootf=lambda t:log_h(t,r)-logq
    t0=bisect(rootf,1/r+1e-13,a)
    t1=bisect(rootf,a,b)
    t2=bisect(rootf,b,1-1e-13)
    assert t0<t1<t2
    return t0,t1,t2

def balance(r):
    a,b,lo,hi=turning_parameters(r)
    def score(q):
        t0,_,t2=three_modes(r,q)
        return curve(t0,r,q)-curve(t2,r,q)
    q=bisect(score,lo+(hi-lo)*1e-7,hi-(hi-lo)*1e-7)
    t0,t1,t2=three_modes(r,q)
    assert abs(score(q))<1e-11,(r,score(q))
    return q,(t0,t1,t2),lo,hi

def main():
    rng=random.Random(1729)
    n=0
    for _ in range(450):
        r=rng.uniform(6.05,22)
        q,ts,lo,hi=balance(r)
        t0,t1,t2=ts
        assert 1/r<t0<t1<t2<1
        assert curve(t0,r,q) > curve(t1,r,q)
        assert curve(t2,r,q) > curve(t1,r,q)
        assert abs(curve(t0,r,q)-curve(t2,r,q))<2e-11
        # The larger-emission branch strictly favors the farther-downwind peak.
        qlo=lo+.3*(q-lo)
        qhi=q+.3*(hi-q)
        zlo=three_modes(r,qlo);zhi=three_modes(r,qhi)
        assert curve(zlo[0],r,qlo)<curve(zlo[2],r,qlo)
        assert curve(zhi[0],r,qhi)>curve(zhi[2],r,qhi)
        # All critical points lie between the isolated-stack modal coordinates.
        for ti in ts: assert abs(der(ti,r,q))<2e-10
        n+=1
    r=9.0
    q,ts,lo,hi=balance(r)
    assert abs(q-6.1195712176091375)<1e-11
    assert abs(lo-4.42014210660111)<1e-10
    assert abs(hi-20.252290288603735)<1e-9
    assert abs(ts[0]-0.1697122097982155)<1e-12
    assert abs(ts[2]-0.981332067309472)<1e-12
    for d in (.0001,.001,.01):
        r=RC+d
        q,ts,lo,hi=balance(r)
        assert abs((hi-lo)/(d**1.5)-CWIDTH)<0.02
        assert abs((ts[2]-ts[0])/math.sqrt(d)-KSEP)<0.02
        assert abs((q-QC)/d-QC*(6-4*math.sqrt(2)))<0.02
    for r in (10.0,12.0,20.0,25.0):
        q,ts,lo,hi=balance(r)
        est=r-math.e+math.e*(1-math.e/2)/r
        assert abs(q-est)<1.0/r**1.2
    # Check exact normalization against physical centerline plume.
    for _ in range(120):
        h1=rng.uniform(10,50);r=rng.uniform(1.2,20)
        h2=h1*math.sqrt(r);u=rng.uniform(1,10)
        ky=rng.uniform(.05,.3);kz=rng.uniform(.05,.3)
        Q1=rng.uniform(1,200);q=rng.uniform(.5,20)
        x=rng.uniform(100,1000)
        t=h1*h1/(2*kz*kz*x*x)
        full=(Q1*math.exp(-h1*h1/(2*kz*kz*x*x))+q*Q1*math.exp(-h2*h2/(2*kz*kz*x*x)))/(math.pi*u*ky*kz*x*x)
        norm=(2*Q1*kz/(math.pi*u*ky*h1*h1))*curve(t,r,q)
        assert abs(full-norm)<1e-11*max(1,abs(full))
    print('PASS: 450 random global switches, 3 cusp scalings, 4 large-contrast comparisons, 120 dimensional normalizations')
    q,ts,lo,hi=balance(9.0)
    print('benchmark',{'r':9.0,'q_minus':lo,'q_balance':q,'q_plus':hi,'t_values':ts,
        'peak':curve(ts[0],9,q),'x_over_scale_far':1/math.sqrt(2*ts[0]),
        'x_over_scale_near':1/math.sqrt(2*ts[2])})

if __name__=='__main__': main()
