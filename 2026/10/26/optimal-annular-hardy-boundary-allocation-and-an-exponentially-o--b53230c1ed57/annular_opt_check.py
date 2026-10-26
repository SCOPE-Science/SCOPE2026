"""Numerical checks for two-boundary annular Hardy point-evaluation designs.
Requires Python 3 and scipy; no publication metadata or external services.
"""
import math
from scipy.optimize import brentq

def kernel_and_derivative(h, alpha, t, tol=1e-17):
    assert h > 0 and 0 < alpha < 1 and 0 < t < 1
    a = math.exp(-alpha*h)
    b = math.exp(-(1-alpha)*h)
    qq = math.exp(-2*h)
    N = int(math.ceil(44.0/(2*h*min(alpha,1-alpha)))) + 1
    K=1.0; D=0.0; DD=0.0
    for m in range(1,N+1):
        v=qq**m
        am=a**(2*m); bm=b**(2*m)
        x=t+(1-t)*v; y=1-t+t*v
        K += am/x+bm/y
        D += (1-v)*(bm/(y*y)-am/(x*x))
        DD += 2*(1-v)**2*(am/(x*x*x)+bm/(y*y*y))
    return K,D,DD

def optimum(h,alpha):
    t = brentq(lambda z: kernel_and_derivative(h,alpha,z)[1], 1e-9, 1-1e-9,xtol=1e-14)
    return t,kernel_and_derivative(h,alpha,t)[0]

if __name__ == '__main__':
    count=0
    for h in (0.25,0.5,1,2,4,9):
      for alpha in (0.15,0.25,0.4,0.5,0.6,0.75,0.85):
        t,K=optimum(h,alpha)
        assert abs(kernel_and_derivative(h,alpha,t)[1]) < 5e-8
        assert kernel_and_derivative(h,alpha,t)[2] > 0
        assert abs(t+optimum(h,1-alpha)[0]-1) < 1e-9
        assert (t>0.5) == (alpha<0.5) if alpha != 0.5 else abs(t-0.5)<1e-10
        assert K>1
        count+=5
    for lam in (-2,-1,0,1,2):
      for h in (12,16,20):
        alpha=.5+lam/h
        t,K=optimum(h,alpha)
        t0=1/(1+math.exp(2*lam))
        pred=1+4*math.exp(-h)*math.cosh(lam)**2
        assert abs(t-t0)<200*math.exp(-h)
        assert abs(K-pred)< 5e3*math.exp(-2*h)
        count+=2
    for alpha in (.2,.35,.5,.7,.85):
      for h in (.15,.3,.5):
        t,K=optimum(h,alpha)
        coeff=math.pi/(2*h*math.sin(math.pi*alpha))*((1-alpha)**(alpha-1))*(alpha**(-alpha))
        assert abs(t-(1-alpha)) < 2e-4
        assert abs(K/coeff-1)<2e-4
        count+=2
    print('PASS',count,'numeric checks')
    for alpha in (.2,.35,.5,.7,.85):
      print('thin',alpha,'h=.5',optimum(.5,alpha),'harmonic mass',1-alpha)
    for lam in (-2.,-1.,0.,1.,2.):
      h=12.;alpha=.5+lam/h
      print('thick',lam,'t*,kernel',optimum(h,alpha),'logistic',1/(1+math.exp(2*lam)))
