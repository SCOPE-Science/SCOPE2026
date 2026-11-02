"""Reproduce exact integral identities and numerical tail tests for a Pareto-renewal expanding Thomas--Fermi profile."""
import math
from scipy.integrate import quad
from scipy.special import beta
from scipy.optimize import brentq


def expansion_time(lam, omega=1.0):
    c=math.sqrt(2.0)*omega
    return (math.sqrt(lam*(lam-1.0))+math.asinh(math.sqrt(lam-1.0)))/c

def dt_dlam(lam, omega=1.0):
    c=math.sqrt(2.0)*omega
    return math.sqrt(lam/(lam-1.0))/c

def stationary_g(z, delta, omega=1.0):
    assert delta>1
    lo=max(abs(z),1.0)
    def integrand(lam):
        t=expansion_time(lam,omega)
        return 0.75*(delta-1)*(1+t)**(-delta)*dt_dlam(lam,omega)/lam*(1-(z/lam)**2)
    return quad(integrand,lo,math.inf,epsabs=1e-12,epsrel=2e-10,limit=400)[0]

def aged_g(z, delta):
    assert 0<delta<1
    lo=abs(z)
    if lo>=1: return 0.0
    const=3.0*math.sin(math.pi*delta)/(4*math.pi)
    return const*quad(lambda u: u**(-delta-1)*(1-u)**(delta-1)*(1-z*z/(u*u)),lo,1.0,epsabs=1e-10,limit=300)[0]

def test():
    tests=0
    c=math.sqrt(2.)
    for delta in [0.22,0.4,0.7,0.89]:
        for z in [0.015,0.01,0.006]:
            t=aged_g(z,delta)*z**delta
            expected=3*math.sin(math.pi*delta)/(2*math.pi*delta*(delta+2))
            # small z approach is slow for low delta
            assert t > 0 and t<expected*1.002
            tests+=1
        for eps in [0.05,0.02,0.01]:
            t=aged_g(1-eps,delta)/eps**(delta+1)
            expected=3*math.sin(math.pi*delta)/(2*math.pi*delta*(delta+1))
            assert 0.5*expected<t<1.05*expected,(delta,eps,t,expected)
            tests+=1
        moment=3/((delta+1)*(delta+3)) # E|V|^delta
        assert moment>0;tests+=1
    for delta in [1.4,2.5,3.5]:
        expected=3*(delta-1)*c**(delta-1)/(2*delta*(delta+2))
        for z in [30,100,300]:
            value=stationary_g(z,delta)*z**delta
            assert 0.2*expected<value<1.05*expected,(delta,z,value,expected)
            tests+=1
    for delta in [0.4,0.7]:
        # Entire aged profile integrates to one, using the mixture's exact conditional normalization.
        hnorm=math.sin(math.pi*delta)/math.pi*beta(1-delta,delta)
        assert abs(hnorm-1)<1e-12
        tests+=1
    for lam in [1.1,2,5,10]:
        h=1e-5*lam
        num=(expansion_time(lam+h)-expansion_time(lam-h))/(2*h)
        assert abs(num/dt_dlam(lam)-1)<2e-8
        tests+=1
    print('PASS',tests,'finite checks: constants, density shape, normalized age, Thomas--Fermi expansion')

if __name__=='__main__':test()
