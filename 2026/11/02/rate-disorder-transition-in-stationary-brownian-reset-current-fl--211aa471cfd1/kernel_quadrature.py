import numpy as np
from scipy.special import roots_laguerre, ndtr, erfc
from scipy.integrate import quad

def form(s,r=1.4,D=.8,rho=2.1):
    kap=(r/D)**.5
    h=(2*r*s)**.5
    ph=np.exp(-h*h/2)/np.sqrt(2*np.pi)
    return rho/(4*kap)*((3-h*h)*ndtr(-h)+h*ph)

def integral(s,r=1.4,D=.8,rho=2.1,n=110):
    kap=(r/D)**.5
    sig=(2*D*s)**.5
    nodes,weights=roots_laguerre(n)
    u=nodes[:,None]/kap; z=nodes[None,:]/kap
    # mcommon = 1/2 ∫exp(-t) (u Phi(u/sig)+ sig phi(u/sig)-sig phi(0)) dt
    t=nodes/(kap*sig)
    phi=np.exp(-t*t/2)/np.sqrt(2*np.pi)
    inner=nodes/kap*ndtr(t)+sig*(phi-1/np.sqrt(2*np.pi))
    mcommon=.5*np.dot(weights,inner)
    # mind = ∫ dz .5 e^-kap z * average_u Laplace P(U+B>z)
    q=.5*np.dot(weights,ndtr((u-z)/sig)+ndtr((-u-z)/sig))
    mind=.5/kap*np.dot(weights,q)
    return rho*np.exp(-r*s)*(mcommon-mind)

for r,D,rho in [(1.4,.8,2.1),(.4,2.3,.77),(3.4,.2,7)]:
 for s in [.025,.15,.7,2.7,8.5]:
  a=form(s,r,D,rho);b=integral(s,r,D,rho,130)
  print(f'r={r} D={D} rho={rho} s={s} formula={a:.12g} independent={b:.12g} err={abs(a-b):.3g}')
  assert abs(a-b)<2e-5*max(1,abs(a))
print('PASS: all independent quadrature comparisons')
