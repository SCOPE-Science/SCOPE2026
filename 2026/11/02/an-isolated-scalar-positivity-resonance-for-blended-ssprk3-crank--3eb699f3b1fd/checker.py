"""Exact stage-vs-factor tests and decimal root checks for a scalar RK stability law."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from random import Random


def direct(x, t):
    z = -x
    y1 = F(1)
    y2 = 1 + z*t*y1/2
    y3 = 1 + z*(t*y1/2+(1-t)*y2)
    y4 = 1 + z*(t*y1/2+(1-t)*(y2+y3)/4)
    return (1 + z*(t*y1/2+(1-t)*(y2+y3)/6 + 2*(1-t)*y4/3))/(1-z*t/2)


def closed(x,t):
    w=(1-t)*x
    return (2-t*x)/(2+t*x)*(1-w+w*w/2-w*w*w/6)

rng=Random(71136)
count=0
for _ in range(1000):
    t=F(rng.randrange(0,26),25)
    x=F(rng.randrange(0,201),rng.randrange(1,41))
    assert direct(x,t)==closed(x,t), (x,t)
    count+=1

with localcontext() as ctx:
    ctx.prec=75
    D=Decimal
    p=lambda y:D(1)-y+y*y/2-y*y*y/6
    low,high=D(1),D(2)
    for _ in range(280):
        mid=(low+high)/2
        if p(mid)>0:low=mid
        else:high=mid
    a=(low+high)/2
    assert abs(p(a))<D('1e-65')
    tstar=D(2)/(D(2)+a)
    u=D(1)-tstar
    q=lambda x:(D(2)-tstar*x)/(D(2)+tstar*x)*p(u*x)
    xzero=a+D(2)
    assert abs(q(xzero))<D('1e-65')
    low,high=xzero,D(16)
    for _ in range(280):
        mid=(low+high)/2
        if q(mid)<1:low=mid
        else:high=mid
    xstar=(low+high)/2
    assert abs(q(xstar)-1)<D('1e-65')
    assert D('7.45048236637796453') < xstar < D('7.45048236637796454')
    # For nonresonant parameters the interval between positive zeros has negative amplification.
    for val in ['0','0.1','0.4','0.5','0.55','0.56','0.6','0.8','0.99','1']:
        t=D(val)
        root_c=D(2)/t if t>0 else D('Infinity')
        root_e=a/(D(1)-t) if t<1 else D('Infinity')
        x=(root_c+root_e)/2 if root_c.is_finite() and root_e.is_finite() else min(root_c,root_e)+D(1)
        r=(D(2)-t*x)/(D(2)+t*x)*p((D(1)-t)*x)
        assert r<0,(t,x,r)
        count+=1
    assert q(D(1))>0 and q(D(1))<1
    assert q(D(4))>0 and q(D(4))<1
    assert q(D(8))>1
    print('CHECKS_PASS',count,'alpha',a,'theta_star',tstar,'x0',xzero,'x_star',xstar)
