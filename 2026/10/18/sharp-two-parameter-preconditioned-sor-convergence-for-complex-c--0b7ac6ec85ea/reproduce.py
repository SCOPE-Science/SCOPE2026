"""Numerical cross-checks for exact BPSOR two-parameter spectral optimization.

Requires Python 3 with numpy. Each assert checks a finite-dimensional instance;
the universal lower bound is established in the accompanying proof.
"""
import cmath
import math
import random
import numpy as np


def optimal_parameters(u, v):
    assert v > 0 and u != 0
    h = u*u + v*v - 1.0
    delta = math.hypot(h, 2*u)
    theta = 2*u / (h + delta)
    D = u*u + v*v + 1.0
    q = 2*v / (D + math.hypot(h, 2*u))
    r = (q/(1.0 + math.sqrt(1.0-q*q)))**2
    omega = 1.0 + r
    return theta, q, omega, r


def matrix_BPSOR(S, theta, omega):
    n = S.shape[0]
    I = np.eye(n)
    Z = np.linalg.solve(theta*I+S, theta*S-I)
    a = 1-omega
    return np.block([[a*I, omega*Z],[-omega*a*Z, a*I-omega**2*(Z@Z)]])


def eigmode_radius(mu, theta, omega):
    tau = (theta*mu-1)/(theta+mu)
    a = 1-omega
    # Characteristic polynomial z^2 - (2a-omega^2*tau^2)z + a^2.
    roots = np.roots([1, -(2*a-omega*omega*tau*tau), a*a])
    return max(abs(z) for z in roots)


def run():
    rg = random.Random(47035)
    checks = 0
    for i in range(200):
        u = (rg.random()-.5)*16
        if abs(u)<.08:
            u=.08 if u>=0 else -.08
        v = .04+6*rg.random()
        theta,q,omega,r=optimal_parameters(u,v)
        mu=complex(u,v)
        tau=(theta*mu-1)/(theta+mu)
        assert abs(tau.real)<3e-12*(1+abs(tau))
        assert abs(tau.imag-q)<3e-12*(1+q)
        assert 0<q<1 and 1<omega<2
        checks+=3
        J=np.array([[0.0,-1.0],[1.0,0.0]])
        S=u*np.eye(2)+v*J
        L=matrix_BPSOR(S,theta,omega)
        radius=max(abs(z) for z in np.linalg.eigvals(L))
        assert abs(radius-r)<3e-7
        checks+=1
        # Nonorthogonal similarities preserve eigenvalues, not one-step norms.
        X=np.array([[1.0,.33],[-.5,1.0]])
        B=X@S@np.linalg.inv(X)
        radius2=max(abs(z) for z in np.linalg.eigvals(matrix_BPSOR(B,theta,omega)))
        assert abs(radius2-r)<3e-7
        checks+=1
        # Search many nontuned parameters, including near the predicted optimum.
        for j in range(40):
            t=theta + (rg.random()-.5)*(2+abs(theta))*4
            w=.01+1.98*rg.random()
            rad=eigmode_radius(mu,t,w)
            assert rad+5e-10>=r,(u,v,t,w,rad,r)
            checks+=1
        assert abs(abs((mu-1j)/(mu+1j))-(1-q)/(1+q))<2e-12
        checks+=1
    u,v=1.0,2.0
    theta,q,omega,r=optimal_parameters(u,v)
    assert abs(theta-(math.sqrt(5)-2))<1e-12
    assert abs(q-(3-math.sqrt(5))/2)<1e-12
    assert abs(r-.0394057578502667)<1e-11
    example_q = q
    assert abs(eigmode_radius(complex(1,2),theta,omega)-r)<1e-7
    checks+=4
    # Exact upper-half-plane invariance and boundary cases.
    for v in (.05,.5,.999,1.01,3.5):
        if v==1:continue
        c=abs((1j*v-1j)/(1j*v+1j))
        q=(1-c)/(1+c)
        assert abs(q-min(v,1/v))<5e-13
        checks+=1
    print('PASS:', checks, 'analytic-identity and finite-matrix checks')
    print('Example u=1,v=2:', 'theta=',theta,'q=',example_q,'omega=',omega,'rho=',r)


if __name__=='__main__':
    run()
