"""Reproducibility checks for exact finite-lag circulation of the Brownian gyrator.

Run: python brownian_gyrator_optimal_checker.py
These finite checks supplement, and do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import brentq
from numpy.polynomial.hermite_e import hermegauss
from itertools import product

checks = 0

def close(x, y, atol=1e-10, rtol=1e-9):
    global checks
    assert np.allclose(x, y, atol=atol, rtol=rtol), (x, y)
    checks += 1


def truth(p):
    global checks
    assert p
    checks += 1


def stationary(u, tx, ty):
    A=np.array([[-1.,u],[u,-1.]])
    D=np.diag([tx,ty])
    cov=solve_continuous_lyapunov(-A, 2*D)
    return A,cov


def exact(u, tx,ty,t):
    A,S=stationary(u,tx,ty)
    M=expm(A*t)
    C=S@M.T
    mu=C[0,1]-C[1,0]
    # Four-variable Wick pairing, no use of the closed theorem.
    vv=2*S[0,0]*S[1,1]-2*S[0,1]**2 + 2*(C[0,1]**2+C[1,0]**2-C[0,0]*C[1,1]-C[0,1]*C[1,0])-mu**2
    return S, mu,vv,C


def root(u):
    u=abs(u)
    def g(t):
        return u /math.tanh(u*t)*(-math.expm1(-2*t))-1
    return brentq(g, 0.02, 60., xtol=1e-13)

# Independent four-dimensional Gauss-Hermite integration of Gaussian chord moments.
GH_X,GH_W=hermegauss(3)
GH_W=GH_W/math.sqrt(2*math.pi)
for u,tx,ty,t in [(.3,1.7,4.,.3),(-.6,1.,5.,1.1),(.8,2.,.4,2.2),(.15,3.,1.,.8)]:
    S,mu,vv,C=exact(u,tx,ty,t)
    G=np.block([[S,C],[C.T,S]])
    L=np.linalg.cholesky(G)
    first=second=0.0
    for inds in product(range(3),repeat=4):
        y=np.array([GH_X[i] for i in inds]); w=math.prod(GH_W[i] for i in inds)
        z=L@y
        q=z[0]*z[3]-z[1]*z[2]
        first+=w*q
        second+=w*q*q
    close(first,mu,rtol=1e-9)
    close(second-first*first,vv,rtol=1e-9)

for u in [-0.91,-0.7,-0.32,0.08,0.35,0.66,0.89]:
  for tx,ty in [(0.25,1.),(1.2,4.1),(9.,2.)]:
    A,S=stationary(u,tx,ty)
    s12=u*(tx+ty)/(2*(1-u*u))
    S_expected=np.array([[tx+u*s12,s12],[s12,ty+u*s12]])
    close(S,S_expected)
    close(A@S+S@A.T+2*np.diag([tx,ty]), np.zeros((2,2)))
    for t in [0.015,0.1,0.4,0.9,1.3,2.7,4.5]:
      S,mu,vv,C=exact(u,tx,ty,t)
      predicted=(tx-ty)*math.exp(-t)*math.sinh(u*t)
      variance=2*np.linalg.det(S)*(-math.expm1(-2*t))+predicted**2
      close(mu,predicted)
      close(vv,variance,rtol=5e-9)
      truth(vv>0)
      close(np.linalg.det(C),np.linalg.det(S)*math.exp(-2*t))
    opt=root(u)
    f=lambda t:math.sinh(abs(u)*t)**2/math.expm1(2*t)
    truth(f(opt)>f(opt*.9999))
    truth(f(opt)>f(opt*1.0001))

for u in [.01,.05,.3,.5,.7,.85,.95,.99,.999,.9999]:
  t=root(u)
  close(u/math.tanh(u*t),1/(-math.expm1(-2*t)),rtol=1e-10)
  close(root(-u),t)
  truth(t>.796)

# The optimal lag is universal in the temperature pair and strictly increasing in |u|.
roots=[root(u) for u in [.01,.1,.3,.5,.7,.9,.99,.999]]
truth(all(x<y for x,y in zip(roots,roots[1:])))
t0=brentq(lambda t: -math.expm1(-2*t)-t, .1,1.)
close(t0,.79681213002002,rtol=1e-10)
truth(abs(root(.001)-t0)<1e-5)
for u in [.99,.999,.9999]:
  truth(abs(root(u)-0.5*math.log(1/(1-u)))<.045)

print('PASS:',checks,'deterministic checks')
