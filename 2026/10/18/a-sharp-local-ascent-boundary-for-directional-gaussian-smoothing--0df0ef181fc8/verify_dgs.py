#!/usr/bin/env python3
"""Reproduce checks for the DGS ridge-direction ascent theorem (standard library only)."""
import math

ROOT2 = math.sqrt(2.0)
K = math.sqrt(math.pi / 2.0)
DELTA = 1.0 / 1000.0
U = (1.0, 10.0)
V = (-9.9, 1.0)


def g(s):
    return K * s * math.erf(s / ROOT2) + 2.0 * math.expm1(-s * s / 2)


def gp(s):
    return K * math.erf(s / ROOT2) - s * math.exp(-s * s / 2)


def gpp(s):
    return s * s * math.exp(-s * s / 2)


def smooth_gp(s, tau):
    a = 1.0 + tau * tau
    return K * math.erf(s / math.sqrt(2.0 * a)) - s * a**(-1.5) * math.exp(-s * s / (2.0 * a))


def smooth_gpp_at_zero(tau):
    return tau * tau / (1.0 + tau * tau)**1.5


def simpson(f, lo, hi, n=24000):
    assert n % 2 == 0
    step = (hi - lo) / n
    val = f(lo) + f(hi)
    for i in range(1, n):
        val += (4 if i % 2 else 2) * f(lo + step * i)
    return val * step / 3


def normal_mean(fn):
    return simpson(lambda z: fn(z) * math.exp(-z*z/2) / math.sqrt(2*math.pi), -9.0, 9.0)


def objective(z):
    x, y = z
    return DELTA * (x*x + y*y) / 2.0 + g(x + 10*y)


def gradient(z):
    x, y = z
    q = gp(x + 10*y)
    return (DELTA*x + q, DELTA*y + 10*q)


def dgs(z):
    x, y = z
    s = x + 10*y
    return (DELTA*x + smooth_gp(s, 1.0), DELTA*y + 10*smooth_gp(s, 10.0))


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def vector_scale(a, t):
    return tuple(t*x for x in a)


def jacobian_at_zero():
    c = (smooth_gpp_at_zero(1.0), smooth_gpp_at_zero(10.0))
    a = (c[0], 10*c[1])
    return ((DELTA+a[0]*U[0], a[0]*U[1]),
            (a[1]*U[0], DELTA+a[1]*U[1])), a


def check():
    count=0
    for tau in (0.25, 1.0, 2.5, 10.0):
        actual = normal_mean(lambda zz: gpp(tau*zz))
        predicted = smooth_gpp_at_zero(tau)
        assert abs(actual-predicted)<2e-9, (actual,predicted)
        count += 1
    for tau in (1.0, 3.0, 10.0):
        for s in (-1.7, -0.3, 0., 0.06, 0.9):
            actual = normal_mean(lambda zz: gp(s+tau*zz))
            predicted = smooth_gp(s,tau)
            assert abs(actual-predicted)<2e-9, (tau,s,actual,predicted)
            count += 1
    for s in (-1.5,-0.7,-.15,.1,.8,1.7):
        h=1e-5
        assert abs((gp(s+h)-gp(s-h))/(2*h)-gpp(s))<1e-8
        assert abs((g(s+h)-g(s-h))/(2*h)-gp(s))<1e-8
        count += 2
    J,a=jacobian_at_zero()
    crit=(math.hypot(*U)*math.hypot(*a)-dot(U,a))/2
    assert abs(crit-0.15692124922833184)<1e-12
    jv=(J[0][0]*V[0]+J[0][1]*V[1],J[1][0]*V[0]+J[1][1]*V[1])
    q=dot(V,jv)
    assert q < -0.13, q
    assert (1.0/(2*ROOT2) > 1.0/3.0 and 100.0/101**1.5 < .1)
    count+=3
    # Characteristic roots of symmetric rank-two sym(a u^T) in two dimensions.
    S00=a[0]*U[0]
    S01=(a[0]*U[1]+a[1]*U[0])/2
    S11=a[1]*U[1]
    mineig=(S00+S11-math.hypot(S00-S11,2*S01))/2
    assert abs(mineig+crit)<1e-12
    count+=1
    for i in (0,1):
        for j in (0,1):
            h=1e-5
            zp=[0.0,0.0];zm=[0.0,0.0]
            zp[j]=h;zm[j]=-h
            numerical=(dgs(zp)[i]-dgs(zm)[i])/(2*h)
            assert abs(numerical-J[i][j])<1e-7, (i,j,numerical,J[i][j])
            count+=1
    for t in (.1,.01,.001,.0001):
        z=vector_scale(V,t)
        lhs=dot(gradient(z),dgs(z))
        assert lhs<0, (t,lhs)
        assert abs(lhs/t**2-DELTA*q)<4e-6
        count+=2
        for h in (.001,.01,.1,1.0):
            F=dgs(z)
            advanced=(z[0]-h*F[0],z[1]-h*F[1])
            gain=objective(advanced)-objective(z)
            assert gain>0, (t,h,gain)
            leading=DELTA*t*t*(-h*q+(h*h/2)*dot(jv,jv))
            if t <= .001:
                assert abs(gain-leading)<.001*leading, (t,h,gain,leading)
            count+=1
    print('PASS',count,'analytic and numerical checks')
    print('c1 =',format(a[0],'.16g'),'c2 =',format(a[1]/10,'.16g'))
    print('sharp delta_crit =',format(crit,'.16g'))
    print('witness v^T J v =',format(q,'.16g'))
    print('example strong convexity =',DELTA,'global Lipschitz bound =',DELTA+202/math.e)
    for h in (.01,.1,1.):
        t=.001;z=vector_scale(V,t);F=dgs(z)
        gain=objective((z[0]-h*F[0],z[1]-h*F[1]))-objective(z)
        print('objective increase: t=0.001, h=',h,' delta=',format(gain,'.12g'))


if __name__=='__main__':
    check()
