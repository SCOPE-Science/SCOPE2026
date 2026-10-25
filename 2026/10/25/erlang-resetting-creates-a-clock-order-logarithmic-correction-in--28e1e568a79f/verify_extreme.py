"""Numerical cross-checks of Gamma-renewal Brownian first-passage extremes.
Requires numpy, scipy, mpmath. Run: python verify_extreme.py
"""
import math
import numpy as np
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 70

def coefficients(v,D,r,x,m):
    root=mp.sqrt(v*v+4*D*r)
    alpha=(root-v)/(2*D); beta=(root+v)/(2*D)
    kap=alpha+beta
    phi=mp.exp(-beta*x)
    p0=(phi-mp.exp(-kap*m)*mp.exp(alpha*x))/(1-mp.exp(-kap*m))
    pm=(mp.exp(alpha*x)-phi)/(mp.exp(alpha*m)-mp.exp(-beta*m))
    return alpha,beta,phi,p0,pm

def T_ell(func,r,ell):
    return sum((-r)**j/mp.factorial(j)*mp.diff(func,r,j) for j in range(ell))

def probability(v,D,r,x,m,ell):
    phi=lambda R:coefficients(v,D,R,x,m)[2]
    low=lambda R:coefficients(v,D,R,x,m)[3]
    high=lambda R:coefficients(v,D,R,x,m)[4]
    p=T_ell(phi,r,ell); pm=T_ell(low,r,ell)
    qm=1-T_ell(lambda R:low(R)+high(R),r,ell)
    return p,pm,1-p,qm

def spectral_exit(v,D,r,x,m,ell,N=80000):
    n=np.arange(1,N+1,dtype=np.float64)
    decay=D*(np.pi*n/m)**2+v*v/(4*D)+r
    weight=sum((r**j)/decay**(j+1) for j in range(ell))
    sin=np.sin(np.pi*n*x/m)
    factor=2*D*np.pi/(m*m)
    p0=factor*math.exp(-v*x/(2*D))*np.sum(n*sin*weight)
    pm=factor*math.exp(v*(m-x)/(2*D))*np.sum(n*sin*((-1)**(n.astype(np.int64)+1))*weight)
    return p0,pm

for v in (-0.7,0.0,0.6):
  for ell in (1,2,3):
    D=1.0;r=0.8;x=1.1;m=3.7
    p,p0,q,q0=probability(mp.mpf(v),mp.mpf(D),mp.mpf(r),mp.mpf(x),mp.mpf(m),ell)
    p_spec,pup_spec=spectral_exit(v,D,r,x,m,ell)
    upper=lambda R:coefficients(mp.mpf(v),mp.mpf(D),R,mp.mpf(x),mp.mpf(m))[4]
    pup=T_ell(upper,mp.mpf(r),ell)
    assert 0<p0<p<1 and 0<q0<q<1
    assert abs(p_spec-float(p0)) < 2e-5,(v,ell,p0,p_spec)
    assert abs(pup_spec-float(pup)) < 2e-5,(v,ell,pup,pup_spec)
    print('spectral-check',v,ell,'lower',round(float(p0),9),'upper',round(float(pup),9),'errors',round(abs(p_spec-float(p0)),9),round(abs(pup_spec-float(pup)),9))

# Verify tail-rate constants, including the one-reset change in decay exponent.
for ell in (1,2,3):
  v=mp.mpf('0.35');D=mp.mpf(1);r=mp.mpf('0.8');x=mp.mpf('1.1');m=mp.mpf(48)
  al,be,ph,_,_=coefficients(v,D,r,x,m)
  kap=al+be;g=mp.sqrt(v*v+4*D*r);C=mp.exp(al*x)-ph
  K=C*(r/g)**(ell-1)/mp.factorial(ell-1)
  K0=C*(2*r/g)**(ell-1)/mp.factorial(ell-1)
  p,p0,q,q0=probability(v,D,r,x,m,ell)
  zero_ratio=(p-p0)/(K0*m**(ell-1)*mp.exp(-kap*m))
  one_ratio=(q-q0)/(K*m**(ell-1)*mp.exp(-al*m))
  assert abs(zero_ratio-1)<mp.mpf('.08') and abs(one_ratio-1)<mp.mpf('.08'),(ell,zero_ratio,one_ratio)
  print('tail-asymptotics',ell,'zero-reset',mp.nstr(zero_ratio,9),'one-or-more',mp.nstr(one_ratio,9))

# Stable differences avoid subtracting 1 from CDFs exponentially close to one.
def stable_gaps(v,D,r,x,m,ell):
    def pair(R):
        al,be,phi,_,_=coefficients(v,D,R,x,m)
        kap=al+be
        C=mp.exp(al*x)-phi
        E=mp.exp(-kap*m)
        return C*E/(1-E),C*(mp.exp(-al*m)-E)/(1-E)
    return (T_ell(lambda R:pair(R)[0],r,ell),
            T_ell(lambda R:pair(R)[1],r,ell))

# Conditional large-reset maxima converge to a Gumbel profile with a clock-order-dependent loglog shift.
for ell in (1,2,3):
  v=mp.mpf('.35');D=mp.mpf(1);r=mp.mpf('.8');x=mp.mpf('1.1');m0=mp.mpf(5)
  al,be,ph,_,_=coefficients(v,D,r,x,m0);root=mp.sqrt(v*v+4*D*r);C=mp.exp(al*x)-ph
  K=C*(r/root)**(ell-1)/mp.factorial(ell-1)
  p=probability(v,D,r,x,m0,ell)[0];q=1-p
  k=mp.power(10,500)
  center=mp.log(k)+(ell-1)*mp.log(mp.log(k))+mp.log(K/(al**(ell-1)*q))
  for s in (-1,0,1):
    m=(center+s)/al
    dp,dq=stable_gaps(v,D,r,x,m,ell)
    F=(1-dp/p)*mp.exp(k*mp.log1p(-dq/q))
    expected=mp.exp(-mp.exp(-s))
    assert abs(F-expected)<mp.mpf('.035'),(ell,s,F,expected)
    print('gumbel-check',ell,s,mp.nstr(F,9),'target',mp.nstr(expected,9))
print('all independent spectral and asymptotic checks passed')
