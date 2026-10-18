"""Reproduce spectral John-contact identities for odd-cycle matching polytopes.
Standard-library numerical checks supplement, but do not replace, the proof."""
import math


def h_root(n):
    assert n >= 7 and n % 2 == 1
    cs = [math.cos(2 * math.pi * j / n) for j in range(n)]
    def F(h):
        return sum(h * (h + 2) / (2 * (h + 1 + c)) for c in cs) / n
    lo, hi = 0., 4.
    for _ in range(100):
        mid = (lo + hi) / 2
        if F(mid) > 1: hi = mid
        else: lo = mid
    return (lo + hi)/2


def test_large(n):
    h=h_root(n)
    t=1/(h+2)
    ev=[h / (2*(h+2)*(h+1+math.cos(2*math.pi*j/n))) for j in range(n)]
    assert min(ev)>0
    q0=sum(ev)/n
    q1=sum(ev[j]*math.cos(2*math.pi*j/n) for j in range(n))/n
    lam0=ev[0]
    assert abs(q0-t*t)<3e-12
    assert abs(2*(q0+q1)-(1-2*t)**2)<3e-12
    oddslack=(n-1)/2-n*t-math.sqrt(n*lam0)
    assert oddslack>0
    alpha=2*t; beta=1-2*t
    assert alpha>0 and beta>0
    assert abs(alpha/t-2*beta/(1-2*t))<2e-13
    # Verify the inverse Fourier eigenvalues match the John decomposition.
    for j,l in enumerate(ev):
        theta=2*math.pi*j/n
        rho=alpha/t**2+beta/(1-2*t)**2*(2+2*math.cos(theta))
        assert abs(rho*l-1)<2e-12
    return t,oddslack


def test_five():
    r6=math.sqrt(6)
    t=(21-r6)/60
    a=12-2*r6; b=8*r6-18; c=252-102*r6
    assert min(a,b,c)>0
    ev=[1/(a+b*(2+2*math.cos(2*math.pi*j/5))+(5*c if j==0 else 0)) for j in range(5)]
    assert min(ev)>0
    q0=sum(ev)/5
    q1=sum(ev[j]*math.cos(2*math.pi*j/5) for j in range(5))/5
    assert abs(q0-t*t)<1e-12
    assert abs(2*(q0+q1)-(1-2*t)**2)<1e-12
    assert abs(5*ev[0]-(2-5*t)**2)<1e-12
    alpha=a*t*t;beta=b*(1-2*t)**2; gamma=c*(2-5*t)**2
    assert min(alpha,beta,gamma)>0
    assert abs(-alpha/t+2*beta/(1-2*t)+gamma/(2-5*t))<2e-11
    assert abs(5*alpha+5*beta+gamma-5)<2e-11
    return t,alpha,beta,gamma

if __name__=='__main__':
    print('C5',tuple(round(x,12) for x in test_five()))
    tests=0
    for n in range(7,302,2):
        t,slack=test_large(n)
        tests+=1
        if n in (7,9,15,101,301):
            print('n=',n,'center=',round(t,12),'odd-facet-clearance=',round(slack,12))
    print('PASS:',tests,'odd dimensions plus the exact C5 formula numerically checked')
