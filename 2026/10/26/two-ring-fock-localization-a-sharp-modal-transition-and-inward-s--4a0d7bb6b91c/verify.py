"""Numerical consistency checks for a radial Gaussian concentration theorem.

Requires Python 3.10+, scipy 1.8+. These finite checks are not a proof of
an asymptotic statement. All numbers and tests are deterministic.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammaln


def gaussian_sum(s, delta):
    return math.exp(-(s-delta)**2/2)+math.exp(-(s+delta)**2/2)


def edgeworth(s, delta):
    result = 0.0
    for v in (-delta, delta):
        poly = v**3/3-s*v*v/2+s**3/6-s/2
        result += math.exp(-(s-v)**2/2)*poly
    return result


def mode_shift(delta):
    assert delta > 1
    return brentq(lambda r: delta*math.tanh(delta*r)-r, 1e-9, delta)


def eigenvalue(n, T, delta):
    assert n>=0
    def density(t):
        return math.exp(-t+n*math.log(t)-gammaln(n+1))
    ans=0.0
    for sign in (-1, 1):
        mid=T+sign*delta*math.sqrt(T)
        ans+=quad(density, mid-.5, mid+.5, epsabs=2e-13, epsrel=2e-13)[0]
    return ans


def verify():
    passed=0
    def check(test, label):
        nonlocal passed
        if not test:
            raise AssertionError(label)
        passed+=1

    for d in (1.02, 1.1, 1.3, 1.6, 2.0, 2.5):
        r=mode_shift(d)
        check(0<r<d,'positive mode')
        check(abs(r-d*math.tanh(d*r))<1e-12,'stationary eq')
        peak=gaussian_sum(r,d)
        predicted_negative=peak*r*(r*r-d*d-3)/6
        check(abs(edgeworth(r,d)-predicted_negative)<2e-12,'cubic correction')
        check(abs(edgeworth(-r,d)+edgeworth(r,d))<2e-12,'parity')

    for d in (.4,.7,.85,1.1,1.3,1.6,2.0):
        for T in (800,3000,15000):
            lo=math.floor(T-d*math.sqrt(T)-.5)-2
            hi=math.ceil(T+d*math.sqrt(T)+.5)+2
            ns=list(range(max(lo,0),hi+1))
            lam=[eigenvalue(n,T,d) for n in ns]
            diff=[lam[j+1]-lam[j] for j in range(len(lam)-1)]
            # Count strict sign changes; two adjacent almost ties do not occur
            signs=[1 if x>0 else (-1 if x<0 else 0) for x in diff]
            nonzero=[x for x in signs if x]
            flips=sum(a!=b for a,b in zip(nonzero,nonzero[1:]))
            if d < 1:
                check(flips==1,f'unimodal {T} {d}: {flips}')
                check(nonzero[0]==1 and nonzero[-1]==-1,'ends')
                maxj=max(range(len(lam)),key=lam.__getitem__)
                check(abs(ns[maxj]-T)<12+d*d*3,'central peak')
                ratio=lam[maxj]*math.sqrt(2*math.pi*T)
                check(abs(ratio-gaussian_sum(0,d))<0.1,'leading central')
            else:
                check(flips==3,f'bimodal {T} {d}: {flips}')
                check(nonzero[0]==1 and nonzero[-1]==-1,'ends')
                maxima=[j for j in range(1,len(lam)-1) if lam[j]>=lam[j-1] and lam[j]>lam[j+1]]
                check(len(maxima)==2,f'two peaks {T} {d}')
                left,right=maxima
                check(lam[left]>lam[right],f'inner dominant {T} {d}')
                r=mode_shift(d)
                predicted=gaussian_sum(r,d)*r*(d*d+3-r*r)/(3*math.sqrt(2*math.pi))
                empirical=T*(lam[left]-lam[right])
                check(abs(empirical-predicted)<.018, f'peak gap {T} {d}: {empirical} vs {predicted}')
                check(abs((ns[left]-T)/math.sqrt(T)+r)<.1,'inner location')
                check(abs((ns[right]-T)/math.sqrt(T)-r)<.1,'outer location')
    print('PASS deterministic checks:',passed)
    print('Asymptotic claims require the separate analytical proof; finite tests do not certify all T.')
    for d in (1.1,1.3,1.6,2.0):
        r=mode_shift(d)
        constant=gaussian_sum(r,d)*r*(d*d+3-r*r)/(3*math.sqrt(2*math.pi))
        print('delta=%.1f, r=%.10f, predicted T-scaled peak gap=%.10f'%(d,r,constant))

if __name__=='__main__':
    verify()
