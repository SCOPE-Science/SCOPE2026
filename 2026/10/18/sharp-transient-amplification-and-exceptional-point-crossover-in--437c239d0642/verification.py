"""Numerical checks for a two-component damped nonreciprocal linear flow.
Uses only the Python standard library. Numerical tests supplement analytic arguments.
"""
import math


def peak(eta, r):
    h = math.sqrt(2) * abs(eta)
    k = math.sqrt(max(0., 1-h*h))
    if r >= h:
        return 0., 1.
    v = math.sqrt(h*h-r*r)
    tau = math.atan2(k*v, r)/k if k else v/r
    g = (1+v)/math.hypot(k,r)*math.exp(-r*tau)
    return tau, g


def gain(eta, r, tau):
    h = math.sqrt(2)*abs(eta)
    k = math.sqrt(max(0.,1-h*h))
    sin_over_k = math.sin(k*tau)/k if k else tau
    return math.exp(-r*tau+math.asinh(h*abs(sin_over_k)))


def singular_norm_of_real_2_by_2(m):
    a,b,c,d=m
    return (math.hypot(a+d,c-b)+math.hypot(a-d,b+c))/2


def independent_matrix_norm(eta, r, tau):
    k2=1-2*eta*eta
    k=math.sqrt(max(0.,k2))
    x=math.cos(k*tau) if k else 1.
    y=math.sin(k*tau)/k if k else tau
    a=x-eta*y
    b=(1+eta)*y
    c=(eta-1)*y
    d=x+eta*y
    z=math.exp(-r*tau)
    return singular_norm_of_real_2_by_2((z*a,z*b,z*c,z*d))


def check():
    checks=0
    for i in range(-28,29):
        eta=i/40
        h=math.sqrt(2)*abs(eta)
        assert h<1
        for r in (0.01,0.05,0.1,0.2,0.35,0.5,0.8,1.1):
            tau_star, g_star=peak(eta,r)
            assert tau_star>=0 and g_star>=1-2e-13
            for tau in (0.,0.01,0.13,0.42,1.1,2.2,3.9,7.,9.1,19.3):
                lhs=independent_matrix_norm(eta,r,tau)
                rhs=gain(eta,r,tau)
                assert abs(lhs-rhs)<2e-9*max(1.,rhs),(eta,r,tau,lhs,rhs)
                assert rhs<=g_star*(1+1e-12),(eta,r,tau,rhs,g_star)
                checks+=1
            if r<h:
                assert tau_star>0 and gain(eta,r,tau_star)>1
                assert abs(gain(eta,r,tau_star)-g_star)<1e-12*g_star
                for delta in (0.0001,0.003,0.05,0.2):
                    assert gain(eta,r,max(0.,tau_star-delta))<=g_star+1e-12
                    assert gain(eta,r,tau_star+delta)<=g_star+1e-12
                    checks+=2
            else:
                assert tau_star==0 and g_star==1
    for s in (0.1,0.3,0.7,1.,2.,4.,10.):
        psi=2/math.hypot(1,s)*math.exp(-s*math.atan(1/s))
        for k in (0.05,0.023,0.007,0.002):
            eta=math.sqrt(1-k*k)/math.sqrt(2)
            tau,g=peak(eta,s*k)
            assert abs(k*g-psi)<3*k*k,(s,k,k*g,psi)
            assert abs(k*tau-math.atan(1/s))<7*k*k,(s,k,k*tau)
            checks+=2
    for r in (0.05,0.1,0.3,0.7,0.9,1.2):
        # Jordan exceptional point itself is included continuously.
        tau,g=peak(1/math.sqrt(2),r)
        if r<1:
            v=math.sqrt(1-r*r)
            assert abs(tau-v/r)<1e-12
            assert abs(g-(1+v)/r*math.exp(-v))<1e-12
        else:
            assert tau==0 and g==1
        checks+=1
    print('PASS',checks,'analytic-vs-matrix norm, peak, and exceptional-point tests')

if __name__=='__main__':
    check()
