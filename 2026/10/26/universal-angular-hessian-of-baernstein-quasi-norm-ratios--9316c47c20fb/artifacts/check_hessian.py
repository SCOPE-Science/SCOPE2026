"""Independent numerical/exact checks of a local angular-root Hessian."""
import math, cmath
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

def logratio(n,r,eps):
    ang=np.mod((2*np.arange(n)+1)*np.pi/n+eps,2*np.pi)
    p=np.sort(np.r_[0.,ang,2*np.pi])
    def f(t):
        prod=np.prod(2*np.abs(np.sin((t-ang)/2)))
        return prod**r/(2*np.pi)
    moment=sum(quad(f,float(a),float(b),epsabs=2e-13,epsrel=2e-11,limit=150)[0] for a,b in zip(p[:-1],p[1:]))
    baseline=math.exp(r*math.log(2)+math.lgamma((r+1)/2)-.5*math.log(math.pi)-math.lgamma(1+r/2))
    return math.log(moment/baseline)/r

def coefficient_check(n):
    zeta=np.exp(1j*(2*np.arange(n)+1)*np.pi/n)
    eps=np.zeros(n);eps[0]=.3;eps[1]=-.3
    sums=np.array([sum(eps*zeta**(-k)) for k in range(1,n)])
    assert abs(sum(abs(sums)**2)-n*sum(eps**2))<1e-9

for n in [2,3,5]:
    coefficient_check(n)
    for r in [.5,1.,2.,4.]:
        ratios=[]
        for delta in [.04,.02,.01]:
            eps=np.zeros(n);eps[0]=delta;eps[1]=-delta
            actual=logratio(n,r,eps)
            prediction=(n*r/8)*sum(eps**2)
            ratios.append(actual/prediction)
        print('n',n,'r',r,'ratios',*[f'{v:.8f}' for v in ratios])
        assert abs(ratios[-1]-1)<.045, (n,r,ratios)
print('CHECK_OK')
