#!/usr/bin/env python3
"""Finite consistency checks for asymmetric-exponential Zak formulas.

All estimates are finite diagnostics; the associated analytic statements require proof.
"""
import cmath
import math


def g(x, a, b):
    return math.exp(a*x) if x < 0.0 else math.exp(-b*x)


def zak_sum(x, w, a, b, K=300):
    return sum(g(x-k, a, b)*cmath.exp(2j*math.pi*k*w)
               for k in range(-K, K+1))


def zak_formula(x, w, a, b):
    u, v = math.exp(-a), math.exp(-b)
    z = cmath.exp(2j*math.pi*w)
    return math.exp(-b*x)/(1-v/z) + math.exp(a*x)*u*z/(1-u*z)


def data(a,b):
    s=a+b
    u,v=math.exp(-a),math.exp(-b)
    x0=(math.log1p(math.exp(a))-math.log1p(v))/s
    A=math.exp(-b*x0)/(1+v)
    beta=(1-u*v)/((1+u)*(1+v))
    J=4*math.pi*a*b*beta*A*A
    C=math.pi/J
    H=2*math.cosh(a/2)
    K=2*math.cosh(b/2)
    C2=math.exp((1+2*b/s)*math.log(H)+(1+2*a/s)*math.log(K)-math.log(8*a*b*math.sinh(s/2)))
    return x0,A,beta,J,C,C2


def zn(x,w,a,b):
    return zak_formula(x,w,a,b)*math.sqrt(2*a*b/(a+b))


def sublevel_polar_area(a,b,eps,N=240):
    x0,_,_,_,C,_=data(a,b)
    total=0
    for k in range(N):
        phi=2*math.pi*(k+0.5)/N
        cs,sn=math.cos(phi),math.sin(phi)
        def zabs(r):
            return abs(zn(x0+r*cs,0.5+r*sn,a,b))
        hi=max(eps,1e-6)
        while zabs(hi)<eps and hi<0.16:
            hi*=1.5
        assert hi<0.16, (a,b,eps,hi)
        lo=0
        for _ in range(45):
            mid=(lo+hi)/2
            if zabs(mid)<eps:
                lo=mid
            else:
                hi=mid
        total+=0.5*((lo+hi)/2)**2
    area=total*2*math.pi/N
    return area,C*eps*eps


def Hfun(q):
    t=math.tanh(q)
    return 2*q*t-2*q*q*(1-t*t)-1


def bisect(f,lo,hi):
    assert f(lo)<0<f(hi)
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def F(a):
    ea=math.exp(a)
    return (1+ea)**3/(4*a*ea)


def main():
    pairs=[(0.32,0.94),(1.,1.),(1.2,3.8),(.9,19.1),(3.2,.7),(9.,9.)]
    worst_closed, worst_sum, worst_jac, worst_asym=0.,0.,0.,0.
    for a,b in pairs:
        x0,A,beta,J,C,C2=data(a,b)
        assert 0<x0<1 and J>0
        worst_closed=max(worst_closed,abs(C/C2-1))
        worst_sum=max(worst_sum,abs(zak_sum(.37,.28,a,b)-zak_formula(.37,.28,a,b)))
        assert abs(zn(x0,.5,a,b))<1e-12
        h=1e-5
        dx=(zn(x0+h,.5,a,b)-zn(x0-h,.5,a,b))/(2*h)
        dw=(zn(x0,.5+h,a,b)-zn(x0,.5-h,a,b))/(2*h)
        jac=abs(dx.real*dw.imag-dx.imag*dw.real)
        worst_jac=max(worst_jac,abs(jac/J-1))
        if a+b<=6:
            numeric,predicted=sublevel_polar_area(a,b,1e-4)
            worst_asym=max(worst_asym,abs(numeric/predicted-1))
    print("debug errors",worst_closed,worst_sum,worst_jac,worst_asym)
    assert worst_closed<1e-12 and worst_sum<3e-13 and worst_jac<2e-8
    assert worst_asym<0.007, worst_asym
    qc=bisect(Hfun,0.1,5.)
    sc=4*qc
    assert 4.59<sc<4.60
    for s in (2.,4.,5.,6.,8.,12.):
        dd=5e-3
        _,_,_,_,cb,_=data(s/2,s/2)
        _,_,_,_,cd,_=data(s/2+dd,s/2-dd)
        predicted_sign=1 if s<sc else -1
        assert (cd-cb)*predicted_sign>0, (s,cb,cd)
    alpha=bisect(lambda a:a*(2*math.exp(a)-1)-(math.exp(a)+1),.01,3.)
    assert .888<alpha<.889
    for s in (40.,100.,200.):
        _,_,_,_,c,_=data(alpha,s-alpha)
        assert abs(s*c/F(alpha)-1)<.09, (s,s*c,F(alpha))
    print('tests_passed=True')
    print('direct_Zak_max_abs_error=',format(worst_sum,'.5g'))
    print('Jacobian_max_relative_error=',format(worst_jac,'.5g'))
    print('closed_mass_coefficient_max_relative_error=',format(worst_closed,'.5g'))
    print('small_level_area_max_relative_error=',format(worst_asym,'.5g'))
    print('critical_total_rate=',format(sc,'.15f'))
    print('asymptotically_optimal_small_rate=',format(alpha,'.15f'))
    print('asymptotically_optimal_mass_numerator=',format(F(alpha),'.15f'))

if __name__=='__main__':
    main()
