#!/usr/bin/env python3
"""Scientific reproducibility checks for the local sine-map period-four theorem."""
import math

P = math.pi
A0 = math.sqrt(P * P + 2.0)

def f(x, a):
    return x + a * math.sin(x)

def f_deriv(x, a):
    return 1 + a * math.cos(x)

def f2(x, a):
    return f(f(x, a), a)

def f4(x, a):
    return f2(f2(x, a), a)

def B(sign):
    return 0.5 * (2 + sign * math.sqrt(2)) * (5 * P * P + 2)

def bisect(fun, lo, hi):
    vlo = fun(lo); vhi = fun(hi)
    assert vlo * vhi < 0, (lo, hi, vlo, vhi)
    for _ in range(75):
        mid = 0.5 * (lo + hi)
        vmid = fun(mid)
        if vmid == 0:
            return mid
        if vlo * vmid < 0:
            hi, vhi = mid, vmid
        else:
            lo, vlo = mid, vmid
    return 0.5 * (lo + hi)

def bisect_near_branch(fun, center, halfwidth, n=120):
    xx=[center-halfwidth + 2*halfwidth*i/n for i in range(n+1)]
    roots=[]
    for l,r in zip(xx[:-1],xx[1:]):
        v1=fun(l);v2=fun(r)
        if v1*v2<0:
            z=bisect(fun,l,r)
            if all(abs(z-w)>1e-7 for w in roots): roots.append(z)
    return roots

def local_parent(a, sign):
    u=math.asin(P/a)
    return u if sign>0 else P-u

def multiplier4(x, a):
    mult=1.0
    for j in range(4):
        mult *= f_deriv(x,a)
        x=f(x,a)
    return mult

assert all(B(s)>0 for s in (-1,1))
assert abs(math.sqrt(B(-1)/B(1))-(math.sqrt(2)-1))<1e-12
checks=2
for sign in (+1,-1):
    t=sign*math.sqrt(2)
    # Independent chain-rule assembly, evaluated exactly at the flip threshold.
    q2=P*((1+t)**2-(1-t))
    q3=t*(1+t)**3-3*P**2*(1+t)-(1-t)*t
    assert abs(q2-P*(3*t+t*t))<1e-12
    assert abs(q3-(4*t*t+3*t**3+t**4-3*P**2*(1+t)))<1e-12
    assert abs(q2*q2/4+q3/6-B(sign))<5e-12
    checks+=3
    for d in (2,3,5,9):
        h=A0/(d+1)
        center=math.asin(P/A0) if sign>0 else P-math.asin(P/A0)
        transverse=(1+h*math.cos(center))*(1+h*math.cos(center+P))
        assert abs(transverse**2-(1-2/(d+1)**2)**2)<1e-12
        assert 0 < transverse**2 < 1
        checks+=2

for eps in (1e-4, 4e-4, 1e-3):
    a=math.sqrt(A0*A0+eps)
    for sign in (+1,-1):
        c=local_parent(a, sign)
        assert abs(f2(c,a)-c)<3e-14
        assert abs(f_deriv(c,a)*f_deriv(c+P,a)-(-1-eps))<2e-13
        amp=math.sqrt(eps/B(sign))
        # Parent and two daughter roots of the fourth iterate in a local window.
        sampled=bisect_near_branch(lambda x:f4(x,a)-x,c,3.5*amp)
        candidates=[c]+[z for z in sampled if abs(z-c)>1e-7]
        assert len(candidates)==3,(eps,sign,candidates,amp)
        newborn=[r for r in candidates if abs(r-c)>1e-7]
        assert len(newborn)==2
        assert newborn[0]<c<newborn[1]
        for z in newborn:
            assert abs(f4(z,a)-z)<1e-10
            assert abs(f2(z,a)-z)>0.001*amp
            assert abs(multiplier4(z,a))<1
        # Leading amplitude convergence, allowing finite-offset correction.
        if eps<=4e-4:
            assert abs((newborn[1]-newborn[0])/(2*amp)-1)<0.15
        checks+=7
print('PASS:',checks,'analytic-identity and finite-root assertions; no infinite proof is inferred from sampling')
