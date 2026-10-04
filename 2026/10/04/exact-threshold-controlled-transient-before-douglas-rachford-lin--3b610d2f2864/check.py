#!/usr/bin/env python3
import math

def step(y,a,b,gamma):
    d=1.0+a*a
    residual=b-y[0]-a*y[1]
    p=(y[0]+residual/d, y[1]+a*residual/d)
    r=(2.0*p[0]-y[0], 2.0*p[1]-y[1])
    s=(math.copysign(max(abs(r[0])-gamma,0.0),r[0]) if r[0] else 0.0,
       math.copysign(max(abs(r[1])-gamma,0.0),r[1]) if r[1] else 0.0)
    yn=(s[0]+y[0]-p[0], s[1]+y[1]-p[1])
    return yn,p,r

def norm(v):
    return math.hypot(v[0],v[1])

cases=[
    (0.1,1.7,1.7/(1.0-0.1)*1.2),
    (0.3,2.0,2.0/(1.0-0.3)*1.4),
    (0.5,1.0,2.0),
    (0.8,1.3,1.3/(1.0-0.8)*1.1),
    (0.9,0.7,0.7/(1.0-0.9)*1.05),
]
for a,b,gamma in cases:
    assert 0.0<a<1.0 and b>0.0 and gamma>=b/(1.0-a)
    d=1.0+a*a
    t=gamma*d/b
    kstar=max(0,math.floor(t)-1)
    y=(0.0,0.0)
    ys=[y]
    refl=[]
    for k in range(kstar+12):
        yn,p,r=step(y,a,b,gamma)
        refl.append(r)
        y=yn
        ys.append(y)
    inq=[(r[0]>gamma and abs(r[1])<=gamma+1e-12) for r in refl]
    first=next(k for k,q in enumerate(inq) if q)
    assert first==kstar, (a,b,gamma,kstar,first)
    assert all(inq[kstar:])
    ystar=(b-gamma,-a*gamma)
    # fixed point check using original nonlinear map
    yn,p,r=step(ystar,a,b,gamma)
    assert norm((yn[0]-ystar[0],yn[1]-ystar[1]))<1e-12
    assert norm((p[0]-b,p[1]))<1e-12
    factor=a/math.sqrt(d)
    errs=[norm((ys[kstar+n][0]-ystar[0],ys[kstar+n][1]-ystar[1])) for n in range(8)]
    for n in range(7):
        assert abs(errs[n+1]-factor*errs[n]) <= 2e-11*max(1.0,errs[n])
    # verify exact zero-shrinkage formulas before entry
    for k in range(kstar):
        expected=(-k*b/d,-k*a*b/d)
        assert norm((ys[k][0]-expected[0],ys[k][1]-expected[1]))<2e-12
        rr=refl[k]
        er=((k+2)*b/d,(k+2)*a*b/d)
        assert norm((rr[0]-er[0],rr[1]-er[1]))<2e-12
print('VERIFY_OK')
