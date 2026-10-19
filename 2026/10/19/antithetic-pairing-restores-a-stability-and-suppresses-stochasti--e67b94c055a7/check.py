"""Reproduce the exact pair identity, stability checks, and finite-step variance asymptotics."""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
import cmath, math, random
getcontext().prec = 65
for a in range(1,22):
    for b in range(1,22):
        u=F(a,23); z=-F(b,17)
        A=(1+(1-u)*z)/(1-u*z)
        B=(1+u*z)/(1-(1-u)*z)
        c=u*(1-u)
        R=(1+z+c*z*z)/(1-z+c*z*z)
        assert A*B==R
for a in [-.01,-.1,-1,-10,-100,-1000]:
    for b in [0, .1,1,10,100,-10]:
        z=complex(a,b)
        for u in [0,.01,.18,.37,.5,.82,.99,1]:
            c=u*(1-u)
            r=(1+z+c*z*z)/(1-z+c*z*z)
            assert abs(r)<1+1e-12,(z,u,r)
assert F(1,6)==F(1,2)-F(1,3)
assert F(1,180)==(F(1,3)-F(1,2)+F(1,5))-F(1,6)**2

def moments(h, paired=True, nodes=4000):
    h=D(str(h)); lam=D(-1); T=D(2); x0=D(1)
    n=int(T/(2*h)) if paired else int(T/h)
    assert (2*n*h if paired else n*h)==T
    s=D(0); s2=D(0)
    for j in range(nodes):
        u=(D(j)+D('0.5'))/D(nodes); z=lam*h
        if paired:
            c=u*(1-u); r=(1+z+c*z*z)/(1-z+c*z*z)
        else:
            r=1+z/(1-z*u)
        s+=r; s2+=r*r
    mean=s/D(nodes); second=s2/D(nodes)
    variance=x0*x0*(second**n-mean**(2*n))
    exp_target=D(-4).exp()
    pred=(D(2)/D(90))*exp_target if paired else (D(2)/D(12))*exp_target
    return float(variance/h**(5 if paired else 3)),float(pred)
for paired in [True,False]:
    values=[moments(h,paired) for h in ['0.05','0.025','0.0125']]
    assert abs(values[-1][0]/values[-1][1]-1)<.12,(paired,values)
    print('paired' if paired else 'iid',values)
print('Exact rational identities: 441. Complex stability grid: 288. Gaussian variance formula and numerical tests: PASS')
