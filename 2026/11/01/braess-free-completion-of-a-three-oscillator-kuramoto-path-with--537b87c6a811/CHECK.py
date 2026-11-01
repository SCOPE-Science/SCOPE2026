"""Reproducible numerical stress tests for a three-site sine-coupled Kuramoto theorem.
The analytical proof, not these finite tests, establishes universal claims.
Python 3, numpy, scipy.
"""
import math
import numpy as np
from scipy.optimize import minimize

RNG=np.random.default_rng(20261028)


def test_case(w1,w2,omega1,omega3,a,k):
    def energy(z):
        alpha,beta=z
        return k*(w1*(1-math.cos(alpha))+w2*(1-math.cos(beta))
                  +a*(1-math.cos(alpha-beta)))-omega1*alpha-omega3*beta
    def grad(z):
        alpha,beta=z
        s=math.sin(alpha-beta)
        return np.array([k*(w1*math.sin(alpha)+a*s)-omega1,
                         k*(w2*math.sin(beta)-a*s)-omega3])
    out=minimize(energy, [0.0,0.0], jac=grad,
            method='L-BFGS-B',bounds=[(-math.pi/2,math.pi/2)]*2,
            options={'gtol':1.e-11,'ftol':1.e-14,'maxiter':3000})
    alpha,beta=out.x
    c1,c2,c3=math.cos(alpha),math.cos(beta),math.cos(alpha-beta)
    h11=k*(w1*c1+a*c3);h22=k*(w2*c2+a*c3);h12=-k*a*c3
    eig=np.linalg.eigvalsh([[h11,h12],[h12,h22]])
    return out.x,max(abs(grad(out.x))),eig.min()


def main():
    assert abs((2-math.sqrt(2))*(1+1/math.sqrt(2))-1)<1.e-14
    # The exact strict-improvement witness has an interior stationary point.
    z,e,l=test_case(1.,1.,-1.,1.,1.,2-math.sqrt(2))
    assert np.linalg.norm(z-np.array([-math.pi/4,math.pi/4]))<1.e-6
    assert e<1.e-6 and l>0
    # Equal normalized leaf loads cannot be served below the original tree threshold.
    for a in [0.01,.3,1.,20.]:
        z,e,l=test_case(1.,1.,1.,1.,a,1.2)
        assert e<1.e-7 and l>0
        assert np.linalg.norm(z-np.array([math.asin(1/1.2)]*2))<1.e-6
    # A broad finite numerical stress check, including strong added links and
    # unequal positive path weights. This is NOT a proof of the general theorem.
    passed=0
    for _ in range(450):
        w1,w2=np.exp(RNG.uniform(-1.3,1.3,2))
        omega1,omega3=RNG.uniform(-2.5,2.5,2)
        a=math.exp(RNG.uniform(-2.0,2.0))
        k0=max(abs(omega1)/w1,abs(omega3)/w2)
        k=1.05*k0
        z,e,l=test_case(w1,w2,omega1,omega3,a,k)
        assert e<2.e-6,(w1,w2,omega1,omega3,a,k,e)
        assert l>1.e-8,(w1,w2,omega1,omega3,a,k,l)
        assert max(abs(z[0]),abs(z[1]))<math.pi/2-1.e-5
        passed+=1
    print('PASS: exact improvement/equality examples and',passed,
          'positive-Hessian principal-square cases')

if __name__=='__main__':main()
