"""Supplementary finite checks for a colored-noise switching-response theorem.
These numerical tests support, but do not replace, the analytic proof.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def corr(t, D, tau):
    # expm1 maintains accuracy as t/tau tends to zero.
    x = t / tau
    return math.exp(-D * tau * (x + math.expm1(-x)))


def moment(k, gamma, D, tau):
    f = lambda t: t**k * math.exp(-gamma*t)*corr(t,D,tau)
    val,err=quad(f,0,math.inf,epsabs=2e-11,epsrel=2e-11,limit=250)
    return val


def ccritical(D,tau):
    return moment(0,0,D,tau)/moment(1,0,D,tau)


def derivative(gamma,c,D,tau):
    M0=moment(0,gamma,D,tau)
    M1=moment(1,gamma,D,tau)
    return M0-(gamma+c)*M1


def gamma_star(c,D,tau):
    if c>=ccritical(D,tau):return 0.0
    top=1.0
    while derivative(top,c,D,tau)>0:
        top*=2
        if top>1e10:raise ArithmeticError('unable to bracket root')
    return brentq(lambda g:derivative(g,c,D,tau),0,top,xtol=1e-11)


def test():
    checks=0
    for D in (0.7,1.0,1.8):
        taus=(0.05,0.25,0.75,1.0,2.0,5.0,10.0)
        cs=[ccritical(D,t) for t in taus]
        for left,right in zip(cs,cs[1:]):
            assert left>right>0
            checks+=1
        for tau in taus:
            cc=ccritical(D,tau)
            for c in (.25*cc,.55*cc,.85*cc,1.05*cc,1.7*cc):
                gopt=gamma_star(c,D,tau)
                if c<cc:
                    assert gopt>0
                    assert abs(derivative(gopt,c,D,tau))<2e-9
                    checks+=2
                    for gg in (0,0.3*gopt,0.8*gopt):
                        assert derivative(gg,c,D,tau)>0
                        checks+=1
                    for gg in (1.15*gopt,2*gopt,8*gopt):
                        assert derivative(gg,c,D,tau)<0
                        checks+=1
                else:
                    assert gopt==0
                    checks+=1
                    for gg in (0,1,10):
                        assert derivative(gg,c,D,tau)<0
                        checks+=1
                for gamma in (.3,2.0):
                    direct=quad(lambda t:t*(D*(-math.expm1(-t/tau))-c)*math.exp(-gamma*t)*corr(t,D,tau),0,math.inf,epsabs=2e-11,epsrel=2e-11)[0]
                    assert abs(direct-derivative(gamma,c,D,tau))<2e-9
                    checks+=1
    taucrit=brentq(lambda t:ccritical(1,t)-.5,3,6)
    assert abs(taucrit-4.221462440171415)<1e-8
    checks+=1
    for tau in (.001,.003,.01,.03):
        b=tau*gamma_star(.5,1,tau)
        b0=math.sqrt(.5)/(1-math.sqrt(.5))
        assert abs(b-b0)<tau
        checks+=1
    for tau in (200,500,1000):
        ratio=ccritical(1,tau)/math.sqrt(math.pi/(2*tau))
        assert abs(ratio-1)<.055
        checks+=1
    print('PASS:',checks,'finite assertions; taucritical=',taucrit)

if __name__=='__main__':test()
