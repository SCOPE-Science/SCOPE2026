"""Reproducibility checks for completed-cell current in an instantaneous-reset ratchet.
Requires NumPy and SciPy. This program uses two independent representations:
Gaussian conditional integrals and an integrated Laplace/geometric formula.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr


def kernel(q, z, r, D, L, a):
    assert 0 < a < L and z > D*(q/L)**2-r
    k = math.sqrt((r+z)/D)
    A,B,R = math.exp(-k*a), math.exp(-k*(L-a)), math.exp(-k*L)
    pos = A*(1-R)*math.exp(q)/(1-R*math.exp(q))
    neg = B*(1-R)*math.exp(-q)/(1-R*math.exp(-q))
    return r/(2*(r+z))*(2-A-B+pos+neg)


def root(q,r,D,L,a):
    lower=D*(q/L)**2-r
    small=1e-9*max(1,abs(lower),r)
    lo=lower+small
    while kernel(q,lo,r,D,L,a)<1:
        small/=10
        lo=lower+small
    hi=max(2*r,D*(abs(q)+10)**2/L**2)
    while kernel(q,hi,r,D,L,a)>1: hi*=2
    return brentq(lambda z:kernel(q,z,r,D,L,a)-1,lo,hi,xtol=2e-12,rtol=2e-12)


def conditional_kernel(q,z,r,D,L,a):
    # Independent Gaussian normal-CDF conditional-time integral.
    n=np.arange(-45,46)
    weight=np.exp(q*n)
    def integrand(t):
        if t<=0: return r
        sigma=math.sqrt(2*D*t)
        prob=ndtr((n*L+a)/sigma)-ndtr((n*L-(L-a))/sigma)
        return r*math.exp(-(r+z)*t)*float(np.dot(weight,prob))
    return quad(integrand,0,np.inf,epsabs=3e-9,epsrel=3e-9,limit=160)[0]


def edge_root(q,u):
    def f(z): return z-0.5*math.exp(-u*math.sqrt(1+z))*math.expm1(q)
    return brentq(f,-.9,max(1,math.exp(q)),xtol=2e-14)


def exact_cumulants(r,D,L,a):
    k=math.sqrt(r/D);A=math.exp(-k*a);B=math.exp(-k*(L-a));R=math.exp(-k*L)
    m=(A-B)/(2*(1-R))
    mk=((-a*A+(L-a)*B)*(1-R)-(A-B)*L*R)/(2*(1-R)**2)
    ek2=(A+B)*(1+R)/(2*(1-R)**2)
    return r*m,r*(ek2+k*m*mk)


def run():
    print('Gaussian-resolvent joint transform:')
    for q,z,r,D,L,a in [(.4,.2,1,1,1,.3),(-.5,.8,2,1,1,.2),(.65,.5,1,1.2,1.5,.4)]:
        exact=kernel(q,z,r,D,L,a)
        independent=conditional_kernel(q,z,r,D,L,a)
        error=abs(exact-independent)
        print(f'q={q} z={z} exact={exact:.11f} conditional={independent:.11f} error={error:.2e}')
        assert error<1e-7
    print('Finite-rate implicit SCGF curvature vs cycle rewards:')
    for r,a in [(1,.3),(4,.1),(25,.1)]:
        mean,var=exact_cumulants(r,1,1,a)
        h=5e-4
        num_mean=(root(h,r,1,1,a)-root(-h,r,1,1,a))/(2*h)
        num_var=(root(h,r,1,1,a)-2*root(0,r,1,1,a)+root(-h,r,1,1,a))/h**2
        print(f'r={r}: rate={mean:.9f} numerical={num_mean:.9f}; variance={var:.9f} numerical={num_var:.9f}')
        assert abs(num_mean-mean)<2e-5 and abs(num_var-var)<3e-4
    print('Fast-reset edge full-counting limit:')
    for u,q in [(0.1,-.5),(.5,.4),(1.,.6),(2.,-.4)]:
        lim=edge_root(q,u)
        for r in [400,10000]:
            a=u/math.sqrt(r)
            curr=root(q,r,1,1,a)/r
            print(f'u={u},q={q},r={r}: scaled_root={curr:.9f}, limit={lim:.9f}, err={abs(curr-lim):.2e}')
            assert abs(curr-lim)<2e-4
    print('Third limiting cumulant:')
    for u in [.2,1.,2.]:
        a=math.exp(-u)/2
        third=a-3*u*a*a+(9*u*u+3*u)*a**3/4
        h=.002
        numerical=(edge_root(2*h,u)-2*edge_root(h,u)+2*edge_root(-h,u)-edge_root(-2*h,u))/(2*h**3)
        print(f'u={u}, analytic={third:.8f}, finite-difference={numerical:.8f}')
        assert abs(third-numerical)<2e-4
    print('All deterministic verification checks passed.')

if __name__=='__main__':run()
