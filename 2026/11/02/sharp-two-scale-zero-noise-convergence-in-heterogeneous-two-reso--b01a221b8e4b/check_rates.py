"""Numerical checks of two-resource heterogeneous congestion asymptotics.
Requires scipy; analytic argument and formulas are documented separately.
"""
from math import exp, log, pi, sqrt
from scipy.integrate import quad
from scipy.optimize import brentq

G = lambda x: 2.0+x
T0 = sqrt(11)-3.0
SHIFT = -pi*pi/(6*sqrt(11))
L1_COEFF = 2*log(2)
L2_SQUARED_COEFF = 2*log(2)-1

def logistic(v):
    if v>=0: return 1/(1+exp(-v))
    e=exp(v)
    return e/(1+e)

def q(s,x,t):
    return logistic((t-x)/s)

def integrate_piecewise(f, t):
    cuts=sorted(set([0.,1.] + [z for z in (t,T0) if 0<z<1]))
    return sum(quad(f,cuts[i],cuts[i+1],epsabs=1e-12,epsrel=1e-12,limit=200)[0] for i in range(len(cuts)-1))

def compute(s):
    def equation(t):
        return t + integrate_piecewise(lambda x: G(x)*q(s,x,t),t)-1
    t = brentq(equation,-2,2,xtol=1e-14)
    L1=integrate_piecewise(lambda x: abs(q(s,x,t)-(1 if x<T0 else 0)),t)
    L2sq=integrate_piecewise(lambda x: (q(s,x,t)-(1 if x<T0 else 0))**2,t)
    A=integrate_piecewise(lambda x: (1+x)*q(s,x,t),t)
    B=integrate_piecewise(lambda x: 1-q(s,x,t),t)
    assert abs(t-(B-A))<2e-12
    return t,L1,L2sq,A,B

if __name__=='__main__':
    assert abs(T0+.0-0.3166247903553998)<1e-13
    prev_t = T0
    print('constant cutoff',format(T0,'.16f'))
    print('shift coefficient',format(SHIFT,'.12f'))
    print('L1 coefficient',format(L1_COEFF,'.12f'))
    print('L2 squared coefficient',format(L2_SQUARED_COEFF,'.12f'))
    for s in [0.005,0.01,0.02,0.04,0.08,0.2,1.0,10.0,100.0]:
        t,L1,L2sq,A,B=compute(s)
        assert -.25<t<T0
        assert t<prev_t
        prev_t=t
        print(f'sigma={s:g} t={t:.12f} (t-t0)/s2={(t-T0)/s**2:.9f} L1/s={L1/s:.9f} L2sq/s={L2sq/s:.9f} A={A:.9f} B={B:.9f}')
    s=.005
    t,L1,L2sq,_,_=compute(s)
    assert abs((t-T0)/s**2-SHIFT)<0.00005
    assert abs(L1/s-L1_COEFF)<0.0005
    assert abs(L2sq/s-L2_SQUARED_COEFF)<0.0005
    assert abs(compute(100.)[0]+.25)<0.01
    # Strict non-potential directional-cross-derivative witness: u=1_[0,1/4], v=1_[3/4,1].
    u = .25
    v = .25
    gu=.5+.25**2/2
    gv=.5+(1-.75**2)/2
    gap = u*gv-v*gu
    assert abs(gap-3/64)<1e-14
    print('nonpotential_cross_derivative_gap',gap)
    print('VERIFY_OK sigma_cases=9 asymptotic_orders=3 nonpotential_gap=3/64')

# Nonuniform density and nonconstant weights: verifies the same general coefficient.
if __name__=='__main__':
    rho=lambda x:.5+x
    w1=lambda x:1+x*x
    w2=lambda x:1+x
    f=lambda x:(w1(x)+w2(x))*rho(x)
    W2=quad(lambda x:w2(x)*rho(x),0,1)[0]
    t0g=brentq(lambda t:t+quad(f,0,t)[0]-W2,0,1)
    fp=lambda t:(1+2*t)*rho(t)+(w1(t)+w2(t))
    k=-(pi*pi/6)*fp(t0g)/(1+f(t0g))
    for s in [.02,.01,.005]:
        def eq(t):
            cuts=sorted([0,t,1]) if 0<t<1 else [0,1]
            val=sum(quad(lambda x:f(x)*q(s,x,t),cuts[i],cuts[i+1],epsabs=1e-12)[0] for i in range(len(cuts)-1))
            return t+val-W2
        t=brentq(eq,0,1,xtol=1e-14)
        ratio=(t-t0g)/s**2
        print(f'general_case_sigma={s:g} t={t:.12f} shift_over_s2={ratio:.8f} expected={k:.8f}')
        assert abs(ratio-k)<.1
    print('VERIFY_GENERAL_OK density_and_heterogeneous_weights')
