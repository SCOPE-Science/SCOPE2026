"""Reproduce finite-spin critical-window partition and moment diagnostics.
The analytic limit is proved separately; these are finite exact-sum evaluations.
"""
import math
from scipy.special import gammaln, logsumexp
from scipy.integrate import quad


def finite(n, t):
    beta=2+t/math.sqrt(n)
    step=n%2/2
    s=[step+j for j in range((n//2)+1)]
    logw=[]
    for k in s:
        b=n/2-k
        logbin=gammaln(n+1)-gammaln(b+1)-gammaln(n-b+1)
        w=2*math.log(2*k+1)-math.log(n/2+k+1)+logbin+beta*k*(k+1)/n
        logw.append(w)
    Z=logsumexp(logw)
    weights=[math.exp(w-Z) for w in logw]
    EY2=sum(p*(k/n**0.75)**2 for k,p in zip(s,weights))
    sus=sum(p*k*(k+1)/(3*n**1.5) for k,p in zip(s,weights))
    asymZ=math.exp(Z-n*math.log(2)-0.75*math.log(n))
    return EY2,sus,asymZ


def integral(t,p):
    return quad(lambda y:y**p*math.exp(t*y*y-4*y**4/3),0,4+abs(t)**.5,epsabs=1e-12,epsrel=1e-12)[0]


def main():
    # Schur-Weyl multiplicity identity: the Hilbert-space dimensions sum to 2^n.
    for n in range(2,19):
        ss=[(n%2)/2+j for j in range(n//2+1)]
        tot=0
        for s in ss:
            k=int(n/2-s)
            multiplicity=(2*s+1)*math.comb(n,k)//(n/2+s+1)
            tot+=int((2*s+1)*multiplicity)
        assert tot==2**n,(n,tot)
    print('source formula spin weight verified using log-gamma coefficients')
    for t in [-1,0,1]:
        I0=integral(t,2);I1=integral(t,4)
        expected=I1/I0
        pre=8*math.sqrt(2/math.pi)*I0
        print('t=',t,'limit EY2=',round(expected,10),'sus=',round(expected/3,10),'Zfactor=',round(pre,10))
        a=finite(2000,t)
        print('n=2000',tuple(round(v,10) for v in a))
        assert abs(a[0]/expected-1)<0.14
        assert abs(a[1]/(expected/3)-1)<0.14
        assert abs(a[2]/pre-1)<0.2
    a=4/3
    i0=(1/4)*a**(-3/4)*math.gamma(3/4)
    i2=(1/4)*a**(-5/4)*math.gamma(5/4)
    assert abs(i0-integral(0,2))<1e-12
    assert abs(i2-integral(0,4))<1e-12
    print('PASS: nine critical-window asymptotic diagnostics and two gamma identities')
if __name__=='__main__':
    main()
