#!/usr/bin/env python3
"""Numerical diagnostics for the explicit two-zone crossing-time identities."""
import math


def u(t, tau, D):
    delta2 = tau*tau-4.0*D
    if delta2 < 0:
        w = math.sqrt(-delta2)/2
        return math.exp(tau*t/2)*math.sin(w*t)/w
    if delta2 > 0:
        h = math.sqrt(delta2)/2
        return math.exp(tau*t/2)*math.sinh(h*t)/h
    return t*math.exp(tau*t/2)


def w_int(t, tau, D):
    delta2 = tau*tau-4.0*D
    if delta2 < 0:
        w = math.sqrt(-delta2)/2
        alpha = tau/2
        return (1-math.exp(alpha*t)*(math.cos(w*t)-(alpha/w)*math.sin(w*t)))/D
    if delta2 > 0:
        delta=math.sqrt(delta2)
        lp=(tau+delta)/2
        lm=(tau-delta)/2
        return (math.expm1(lp*t)/lp-math.expm1(lm*t)/lm)/delta
    alpha=tau/2
    return (math.exp(alpha*t)*(alpha*t-1)+1)/(alpha*alpha)


def r_at(t, tau, D, a):
    return a*w_int(t,tau,D)/u(t,tau,D)


def simpson(fn,t,n=2000):
    h=t/n
    return h/3*(fn(0)+fn(t)+sum((4 if k%2 else 2)*fn(k*h) for k in range(1,n)))


def close(a,b,rtol=0.000002,atol=0.000002):
    assert abs(a-b)<=atol+rtol*max(abs(a),abs(b)),(a,b)


for tau in [-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]:
    D=1.0
    for t in [0.2,0.6,1.2]:
        numeric=simpson(lambda s:u(s,tau,D),t)
        close(w_int(t,tau,D),numeric,rtol=1e-6,atol=1e-9)
        r=r_at(t,tau,D,1)
        assert r>0
        # Verify positivity of the left flight at an interior time, and exact closing.
        for s in [t/4,t/2,3*t/4]:
            v=r*u(s,tau,D)-w_int(s,tau,D)
            assert v>0,(tau,t,s,v)
        close(r*u(t,tau,D)-w_int(t,tau,D),0,atol=1e-10)
    # Sample monotonicity, never treated as proof.
    rr=[r_at(t,tau,D,1) for t in (0.2,0.6,1.2)]
    assert rr[0]<rr[1]<rr[2]

# Independently test the reflected right-zone flow at interior points.
def uprime(t, tau, D):
    delta2=tau*tau-4*D
    if delta2<0:
        omega=math.sqrt(-delta2)/2
        alpha=tau/2
        return math.exp(alpha*t)*(math.cos(omega*t)+alpha*math.sin(omega*t)/omega)
    if delta2>0:
        delta=math.sqrt(delta2)
        lp=(tau+delta)/2
        lm=(tau-delta)/2
        return (lp*math.exp(lp*t)-lm*math.exp(lm*t))/delta
    return math.exp(tau*t/2)*(1+tau*t/2)


def right_state(s,t,tau,D,a,k,r):
    z=t-k*s
    v=r*u(z,tau,D)-a*w_int(z,tau,D)
    vp=r*uprime(z,tau,D)-a*u(z,tau,D)
    return v/k, vp-tau*v


for tau in [-3.0,-2.0,-0.5,0.0,1.0,2.0,3.0]:
    t=0.6;D=a=1.0;k=1.7
    r=r_at(t,tau,D,a)
    xend,yend=right_state(t/k,t,tau,D,a,k,r)
    close(xend,0.0,atol=1e-10)
    close(yend,r,atol=1e-10)
    ss=t/(2*k);h=1e-6
    xx,yy=right_state(ss,t,tau,D,a,k,r)
    xp,yp=right_state(ss+h,t,tau,D,a,k,r)
    xm,ym=right_state(ss-h,t,tau,D,a,k,r)
    close((xp-xm)/(2*h),-k*tau*xx-yy,rtol=5e-6,atol=5e-6)
    close((yp-ym)/(2*h),k*k*D*xx+k*a,rtol=5e-6,atol=5e-6)

# Focus endpoint (tau=0, D=a=1): tmax = pi, r~2/(pi-t).
focust=math.pi-1e-3
close((math.pi-focust)*r_at(focust,0.0,1.0,1.0),2.0,rtol=5e-4)
# Stable distinct node (tau=-3): relative log law at long time.
t=15.0; delta=math.sqrt(5.0);lp=(-3+delta)/2
rr=r_at(t,-3.0,1.0,1.0)
close(math.log(rr/delta)/(-lp)/t,1.0,rtol=0.002)
# Stable defective node: log + log log asymptotics (slow convergence).
t=14.0
rr=r_at(t,-2.0,1.0,1.0)
assert abs(math.log(rr)+math.log(math.log(rr))-t)<0.25
# Unstable defective node: reciprocal gap; R=1.
t=12.0
rr=r_at(t,2.0,1.0,1.0)
close(t*(1.0-rr),1.0,rtol=1e-4)
# Unstable distinct node: exponentially small gap, R=1/lp.
t=11.0;delta=math.sqrt(5.0);lp=(3+delta)/2;R=1/lp
rr=r_at(t,3.0,1.0,1.0)
close((R-rr)*math.exp(delta*t)/delta,1.0,rtol=0.02)
print('CHECK_OK')
