"""Supplementary numerical checks of the stated Hardy-space Berezin strip formulas.
The analytic argument, not this finite testing, establishes the theorem.
Run: python3 verify.py
Dependencies: Python standard library and scipy.
"""
from math import cos, sin, pi, sqrt, exp, log, sinh, tanh, atan2
from scipy.optimize import brentq, minimize_scalar

def berezin(w,m,q):
    return (1-abs(w)**2)/(1-q*w**m*w.conjugate())

def width_at_u(u,alpha,eta):
    return (1-exp(-u))/(2*sinh(eta+alpha*u))

def critical(m,q):
    a=(m+1)/2
    eta=-log(q)
    upper=log1p(1/a)
    def equation(u):
        return tanh(eta+a*u)-a*(exp(u)-1)
    u=brentq(equation,1e-12,upper,xtol=1e-14)
    return u,width_at_u(u,a,eta)
from math import log1p

def test():
    checks=0
    for m in (2,3,4,6):
        a=(m+1)/2
        for q in (.1,.5,.9,.99,.999):
            eta=-log(q)
            u,h=critical(m,q)
            assert u>0 and 0<h<1/(2*a)
            checks+=2
            def minus(u_): return -width_at_u(u_,a,eta)
            opt=minimize_scalar(minus,bounds=(.0000001,7),method='bounded',options={'xatol':1e-12})
            assert abs(opt.fun+h)<2e-9,(m,q,opt.fun,h)
            checks+=1
            t=exp(-u); d=q*t**a
            phase_complex=complex(2*d,1-d*d)/(1+d*d)
            for s in (1,-1):
                phase=atan2(s*phase_complex.imag,phase_complex.real)
                for j in range(m-1):
                    theta=(phase+2*pi*j)/(m-1)
                    w=sqrt(t)*complex(cos(theta),sin(theta))
                    # q chosen real; phase correction already signed
                    z=berezin(w,m,q)
                    assert abs(z.imag-s*h)<1e-9,(m,q,s,z,h)
                    checks+=1
            # Nonreal symbol phases must rotate the angular maximizers.
            for gamma in (.2,.8,1.7):
                lam=q*complex(cos(gamma),sin(gamma))
                top_phase=atan2(phase_complex.imag,phase_complex.real)
                for j in range(m-1):
                    theta=(top_phase-gamma+2*pi*j)/(m-1)
                    w=sqrt(t)*complex(cos(theta),sin(theta))
                    assert abs(berezin(w,m,lam).imag-h)<1e-9
                    checks+=1
            # sampled real/imag points never exceed the formula
            for k in range(37):
                u2=.003+(k+.13)*.2
                for j in range(61):
                    phase=2*pi*(j+.31)/61
                    w=exp(-u2/2)*complex(cos(phase),sin(phase))
                    assert abs(berezin(w,m,q).imag)<=h+1e-11
                    checks+=1
        for q in (1e-4,1e-5,1e-6):
            u,h=critical(m,q)
            c=a**a/(a+1)**(a+1)
            assert abs(h/q/c-1)<1e-5
            checks+=1
        for q in (.999999,.99999999):
            eta=-log(q)
            u,h=critical(m,q)
            c=1/(sqrt(2)*a**1.5)
            assert abs((1/(2*a)-h)/sqrt(eta)/c-1)<.005,(m,q)
            assert abs(u/sqrt(2*eta/a)-1)<.005
            checks+=2
        for u in (.0001,.003,.02,.2,1,3):
            h=width_at_u(u,a,0)
            assert h < 1/(2*a)
            checks+=1
    print('PASS',checks,'supplementary assertions')

if __name__=='__main__':test()
