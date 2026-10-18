#!/usr/bin/env python3
"""Independent arithmetic and Monte Carlo tests of the stated cylinder cap-contact law.
Requires numpy. Run: python verify.py .
The theorem itself is proved analytically; these finite checks are corroborative only.
"""
import math
import numpy as np

rng=np.random.default_rng(674901)
P=math.pi

def w(phi,shape):
    if shape=='disk':return np.full_like(phi,2.0)
    if shape=='rectangle':return 2.0*(np.abs(np.cos(phi))+0.6*np.abs(np.sin(phi)))
    if shape=='ellipse':return 2.0*np.sqrt((1.4*np.cos(phi))**2+(0.7*np.sin(phi))**2)
    if shape=='harmonic2':return 2.0+np.cos(2*phi)/15.0
    if shape=='harmonic4':return 2.0+np.cos(4*phi)/15.0
    raise ValueError(shape)

def prediction(shape,h,nphi=65536):
    phi=2*P*(np.arange(nphi)+0.5)/nphi
    ww=w(phi,shape)
    mu=float(np.mean(ww))
    G=float(np.mean(0.5*ww*np.arctan(ww/(2*h))))
    denom=h+P*mu/4
    both=G/denom
    neither=(h-P*mu/4+G)/denom
    return np.array([both,neither,1-both-neither]),mu,G

def direct_quadrature(shape,h,nphi=400,nc=3000):
    phi=2*P*(np.arange(nphi)+.5)/nphi
    ww=w(phi,shape)[:,None]
    c=((np.arange(nc)+.5)/nc)[None,:]
    s=np.sqrt(1-c*c)
    ell=ww*s
    delta=2*h*c
    B=np.maximum(ell-delta,0)
    E=np.maximum(delta-ell,0)
    O=ell+delta-B-E
    nums=np.array([B.mean(),E.mean(),O.mean()])
    return nums/nums.sum()

def weighted_mc(shape,h,n=420000):
    phi=2*P*rng.random(n)
    z=2*rng.random(n)-1
    ww=w(phi,shape)
    s=np.sqrt(1-z*z)
    a=.5*ww*s
    b=h*np.abs(z)
    x=(2*rng.random(n)-1)*(a+b)
    # A cap at z=+h gives an interval centered +h|normal-z|, other at minus.
    # Since bases are centered at the origin, the cap intervals have radius a.
    top=np.abs(x-b)<a
    bottom=np.abs(x+b)<a
    weights=2*(a+b)
    vals=np.array([np.dot(weights,top&bottom),np.dot(weights,~top&~bottom),np.dot(weights,top^bottom)])
    return vals/weights.sum()

for shape in ['disk','rectangle','ellipse','harmonic2','harmonic4']:
    for h in [0.25,0.8,2.25]:
        exact,mu,G=prediction(shape,h)
        quad=direct_quadrature(shape,h)
        err=float(np.max(abs(exact-quad)))
        assert err<0.00035,(shape,h,'quadrature',exact,quad,err)
        assert abs(sum(exact)-1)<3e-14
        assert min(exact)>0
        assert abs(exact[1]-exact[0]-(h-P*mu/4)/(h+P*mu/4))<3e-14
    exact,_,_=prediction(shape,0.8)
    mc=weighted_mc(shape,0.8)
    assert max(abs(exact-mc))<.006,(shape,exact,mc)
    print('CASE',shape,'probabilities h=0.8',*(f'{v:.9f}' for v in exact),'max_MC_error',f'{max(abs(exact-mc)):.6f}')
for h in [.25,.8,2.25]:
    a=prediction('harmonic2',h)[0];b=prediction('harmonic4',h)[0]
    assert max(abs(a-b))<3e-15, (a,b)
    assert prediction('harmonic2',h)[0][0]>prediction('disk',h)[0][0]
    assert prediction('harmonic2',h)[0][1]>prediction('disk',h)[0][1]
    assert prediction('harmonic2',h)[0][2]<prediction('disk',h)[0][2]
print('EQUIMEASURABLE_NONCONGRUENT_AND_STRICT_JENSEN_OK')
# Infer the first two even moments by the h->infty expansion of G.
for shape in ['disk','rectangle','ellipse','harmonic2']:
    phi=2*P*(np.arange(131072)+.5)/131072
    ww=w(phi,shape)
    mu2=np.mean(ww*ww);mu4=np.mean(ww**4)
    G=prediction(shape,100.)[2]
    mu2est=4*100*G
    mu4est=48*100**3*(mu2/(4*100)-G)
    assert abs(mu2est-mu2)<.001
    assert abs(mu4est-mu4)<.01
    print('RECOVERY',shape,'m2',f'{mu2:.8f}','m4',f'{mu4:.8f}','m4_from_profile',f'{mu4est:.8f}')
print('CAP_CONTACT_VERIFICATION_OK')
