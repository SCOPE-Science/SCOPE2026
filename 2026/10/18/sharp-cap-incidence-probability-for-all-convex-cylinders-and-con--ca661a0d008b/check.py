"""Reproducible numerical and algebraic checks for cap incidence in generalized cylinders."""
import math
import numpy as np
from scipy.integrate import quad


def probability_from_width(H, width, phi_nodes=720):
    phis = 2*math.pi*(np.arange(phi_nodes)+.5)/phi_nodes
    w = np.asarray(width(phis), dtype=float)
    # Deterministic midpoint integration, independent formula for original normal/offset geometry.
    c, weight = np.polynomial.legendre.leggauss(240)
    c, weight = (c+1)/2, weight/2
    sv = np.sqrt(1-c*c)
    z = H*c[None,:]
    y = w[:,None]*sv[None,:]
    integrals = np.array([
        np.mean(np.sum(weight[None,:]*np.maximum(z-y,0),axis=1)),
        np.mean(np.sum(weight[None,:]*2*np.minimum(z,y),axis=1)),
        np.mean(np.sum(weight[None,:]*np.maximum(y-z,0),axis=1))
    ])
    return integrals/integrals.sum(), w


def polygon_width(vertices):
    vertices=np.asarray(vertices,dtype=float)
    def fw(phi):
        dirs=np.stack([np.cos(phi),np.sin(phi)],axis=1)
        dots=dirs@vertices.T
        return np.max(dots,axis=1)-np.min(dots,axis=1)
    return fw


def expected_from_width(H, w):
    avg_w = w.mean()
    D=H/2+math.pi*avg_w/4
    F=np.mean(w*np.arctan(H/w))
    return np.array([(H/2-F/2)/D,F/D,(math.pi*avg_w/4-F/2)/D])


def test():
    # Independent angle-offset integration vs closed conditional law.
    triangle=polygon_width([[1,0],[-.5,math.sqrt(3)/2],[-.5,-math.sqrt(3)/2]])
    rectangle=polygon_width([[-1,-.5],[-1,.5],[1,-.5],[1,.5]])
    ellipse=lambda phi:2*np.sqrt(1.8**2*np.cos(phi)**2+.75**2*np.sin(phi)**2)
    disk=lambda phi:2*np.ones_like(phi)
    for label,fun in [('disk',disk),('ellipse',ellipse),('rectangle',rectangle),('triangle',triangle)]:
        for H in [0.6,2.0,5.0]:
            measured,w=probability_from_width(H,fun)
            predicted=expected_from_width(H,w)
            err=np.max(np.abs(predicted-measured))
            assert err<1.2e-5,(label,H,err,predicted,measured)
            assert abs(sum(predicted)-1)<2e-14
            print(f'{label:10s} H={H:.1f} P0,P1,P2={predicted.round(8)} independent_error={err:.2g}')
    # Cauchy's perimeter relation for rectangle/triangle: discrete midpoint quadrature convergence.
    for name,fun,P in [('rectangle',rectangle,6.),('triangle',triangle,3*math.sqrt(3))]:
        phis=2*math.pi*(np.arange(50000)+.5)/50000
        w=fun(phis)
        assert abs(math.pi*w.mean()-P)<1e-8, (name,math.pi*w.mean(),P)
    # Strong-concavity rigidity bounds for nonconstant width profiles.
    H=2.3
    for fun in [triangle,rectangle,ellipse]:
        phis=2*math.pi*(np.arange(40000)+.5)/40000
        w=fun(phis)
        avg=w.mean()
        f=lambda v: v*np.arctan(H/v)
        gap=f(avg)-f(w).mean()
        var=np.var(w)
        low=H**3*var/(H**2+w.max()**2)**2
        high=H**3*var/(H**2+w.min()**2)**2
        assert low-1e-12<=gap<=high+1e-12,(low,gap,high)
        assert gap>0
        print(f'rigidity gap={gap:.12f}, bounds=[{low:.12f},{high:.12f}]')
    # Exact second derivative direct finite differences away from zero.
    for H,w in [(.2,2.),(1.,1.4),(3.7,2.3)]:
        f=lambda x:x*math.atan(H/x)
        h=1.e-3
        second=(f(w+h)-2*f(w)+f(w-h))/h**2
        exact=-2*H**3/(H*H+w*w)**2
        assert abs((second-exact)/exact)<1e-5,(H,w,second,exact)
    # Equality for all constant-width shapes is structural: probabilities use only w(phi).
    print('PASS: direct orientation/offset integration, Cauchy widths, strict Jensen bounds and curvature')

if __name__=='__main__':
    test()


def optimal_aspect():
    from scipy.optimize import brentq
    f=lambda x:(x+math.pi/2)/(1+x*x)-math.atan(x)
    root=brentq(f,1,2,xtol=1e-14)
    exact=2/(1+root*root)
    envelope=4*math.atan(root)/(2*root+math.pi)
    assert abs(root-1.45729440014087)<1e-12
    assert abs(exact-0.6402649224309067)<1e-12
    assert abs(exact-envelope)<1e-14
    # Deterministic derivative sign samples: rigorous uniqueness is proved in prose.
    assert all(f(x)>0 for x in [0.1,0.9,1.2])
    assert all(f(x)<0 for x in [1.7,3,100])
    print(f'PASS: unique-ratio numerical check x*={root:.14f}, p*={exact:.14f}')

if __name__=='__main__':
    optimal_aspect()
