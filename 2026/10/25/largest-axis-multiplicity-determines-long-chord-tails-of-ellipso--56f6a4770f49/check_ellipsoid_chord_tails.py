"""Numerical checks for invariant-line chords of ellipsoids.
Run: python3 ellipsoid_chord_checker.py
Uses numpy and scipy; no external data.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gamma


def sphere_integral_sqrt_q(axes, nodes=130):
    a,b,c=map(float, axes)
    t,w=leggauss(nodes)
    theta=(np.arange(nodes)+0.5)*2*math.pi/nodes
    q=(t[:,None]**2/a**2+(1-t[:,None]**2)*(
        np.cos(theta)[None,:]**2/b**2+np.sin(theta)[None,:]**2/c**2))
    return float(2*math.pi/nodes*np.sum(w[:,None]*np.sqrt(q)))


def p_triaxial_integral(axes, eps, nodes=128):
    a,b,c=map(float,axes)
    assert a>b and b>=c
    x,w=leggauss(nodes)
    th=(x+1)*math.pi
    beta=(a*a/b**2-1)*np.cos(th)**2+(a*a/c**2-1)*np.sin(th)**2
    max_s=((1-eps)**-2-1)/beta
    assert np.max(max_s)<1
    z=(x+1)/2
    wz=w/2
    s=max_s[:,None]*z[None,:]
    Q=1/a**2+(beta[:,None]/a**2)*s
    integrand=np.sqrt(Q)*np.maximum(0,1-(1-eps)**2*a*a*Q)/np.sqrt(1-s)
    return float(math.pi*np.dot(w, np.sum(integrand*wz[None,:]*max_s[:,None], axis=1)))


def p_oblate_integral(axes, eps, nodes=128):
    a,b,c=map(float,axes)
    assert a==b and b>c
    beta=a*a/c**2-1
    zmax=math.sqrt(((1-eps)**-2-1)/beta)
    assert zmax<1
    x,w=leggauss(nodes)
    z=zmax*(x+1)/2
    Q=1/a**2+(1/c**2-1/a**2)*z*z
    return float(4*math.pi*zmax/2*np.dot(w,np.sqrt(Q)*np.maximum(0,1-(1-eps)**2*a*a*Q)))


def predicted_constant(axes,H):
    d=3
    a=axes[0]
    k=sum(abs(z-a)<1e-14 for z in axes)
    p=d-k
    alpha=(2*d-k-1)/2
    # |S^(k-1)| = 2 pi^(k/2)/Gamma(k/2)
    sphere=2*math.pi**(k/2)/gamma(k/2)
    prod=math.prod((a*a/z**2-1)**(-0.5) for z in axes[k:])
    C=sphere*math.pi**(p/2)*gamma((d+1)/2)*2**alpha*prod/(a*H*gamma((2*d-k+1)/2))
    return alpha,C


def main():
    configs=[('triaxial',(2.,1.5,1.)),('prolate',(2.,1.,1.)),('oblate',(2.,2.,1.)),('sphere',(2.,2.,2.))]
    for name,axes in configs:
        H=sphere_integral_sqrt_q(axes)
        alpha,C=predicted_constant(axes,H)
        assert H>0 and C>0
        errors=[]
        for eps in (0.009,0.003,0.001):
            if name in ('triaxial','prolate'):
                exact=p_triaxial_integral(axes,eps)/H
            elif name=='oblate':
                exact=p_oblate_integral(axes,eps)/H
            else:
                exact=2*eps-eps*eps
            ratio=exact/(C*eps**alpha)
            errors.append(abs(ratio-1))
            assert abs(ratio-1)<0.04,(name,eps,ratio)
        assert errors[-1]<errors[0], (name,errors)
        print('SHARP_END_TAIL_OK',name,'exponent=',alpha,'C=',format(C,'.9g'),'ratio_error_at_0.001=',format(errors[-1],'.5g'))
    # Separate direct line-measure sampling at a non-asymptotic threshold.
    a,b,c=2.,1.5,1.
    eps=0.1
    H=sphere_integral_sqrt_q((a,b,c))
    quadrature=p_triaxial_integral((a,b,c),eps)/H
    rng=np.random.default_rng(20261019)
    n=550000
    v=rng.normal(size=(n,3));v/=np.linalg.norm(v,axis=1)[:,None]
    q=(v[:,0]/a)**2+(v[:,1]/b)**2+(v[:,2]/c)**2
    # Conditional random translations uniform on the two-dimensional projected ellipse:
    radial_square=rng.random(n)
    lengths=2*np.sqrt(1-radial_square)/np.sqrt(q)
    weights=np.sqrt(q)
    estimated=float(np.average(lengths>2*a*(1-eps),weights=weights))
    assert abs(estimated-quadrature)<0.005,(estimated,quadrature)
    print('UNBIASED_LINE_MEASURE_VS_DIRECT_QUADRATURE_OK',format(quadrature,'.6g'),format(estimated,'.6g'))

    # Direct geometric line test: Haar direction and translation in a
    # radius-a disk in its perpendicular plane, then intersect the true quadric.
    n2=450000
    u=rng.normal(size=(n2,3))
    u/=np.linalg.norm(u,axis=1)[:,None]
    raw=rng.normal(size=(n2,3))
    v=raw-np.sum(raw*u,axis=1)[:,None]*u
    v/=np.linalg.norm(v,axis=1)[:,None]
    p=2*np.sqrt(rng.random(n2))[:,None]*v
    inv=np.array([1/a**2,1/b**2,1/c**2])
    aa=np.sum(inv*u*u,axis=1)
    bb=np.sum(inv*u*p,axis=1)
    cc=np.sum(inv*p*p,axis=1)-1
    discr=bb*bb-aa*cc
    hit=discr>0
    ll=2*np.sqrt(np.maximum(discr[hit],0))/aa[hit]
    direct=float(np.mean(ll>2*a*(1-eps)))
    assert abs(direct-quadrature)<0.005,(direct,quadrature)
    print('DIRECT_QUADRATIC_LINE_INTERSECTIONS_OK',int(hit.sum()),format(direct,'.6g'))
    print('ALL_ELLIPSOID_MULTIPLICITY_TAIL_CHECKS_OK')

if __name__=='__main__': main()
