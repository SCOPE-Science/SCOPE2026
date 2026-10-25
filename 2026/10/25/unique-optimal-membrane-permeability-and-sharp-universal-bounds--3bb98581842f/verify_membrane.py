"""Direct boundary-value and optimization checks for a resetting membrane circle.

Requirements: Python 3, numpy, scipy. Run: python verify_membrane.py
"""
import math
import numpy as np
from scipy.optimize import minimize_scalar, brentq


def data(D, L, rate, ys, weights):
    a = math.sqrt(rate / D)
    U = sum(w * a * math.cosh(a * (L - y)) / math.sinh(a * L)
            for y, w in zip(ys, weights))
    V = sum(w * a * math.cosh(a * y) / math.sinh(a * L)
            for y, w in zip(ys, weights))
    b = 2 * math.tanh(a * L / 2) / (D * a)
    return U, V, b


def direct_point(D, L, rate, kappa, y):
    a = math.sqrt(rate/D)
    sy, cy = math.sinh(a*y), math.cosh(a*y)
    sL, cL = math.sinh(a*(L-y)), math.cosh(a*(L-y))
    # p_left=A1 cosh(ax)+B1 sinh(ax)
    # p_right=A2 cosh(a(L-x))+B2 sinh(a(L-x))
    mat=np.array([[cy,sy,-cL,-sL],
                  [-a*sy,-a*cy,-a*sL,-a*cL],
                  [0,1,0,1],
                  [kappa,-D*a,-kappa,0]],float)
    rhs=np.array([0,-a*a,0,0],float)
    sol=np.linalg.solve(mat,rhs)
    return sol[0],sol[2], -D*a*sol[1]


def entropy(U,V,b,kappa):
    z=1/(1+b*kappa)
    delta=U-V
    return kappa*z*delta*math.log((U+V+z*delta)/(U+V-z*delta))


def zstar(t):
    return brentq(lambda z: math.atanh(t*z)-t*(1-z)/(1-t*t*z*z),
                  0.5, 0.99, xtol=1e-14)


def run():
    rng=np.random.default_rng(20261023)
    for i in range(110):
        D=float(rng.uniform(0.8,2.0))
        L=float(rng.uniform(.6,1.7))
        rate=float(rng.uniform(.3,5))
        kappa=float(rng.uniform(.1,4))
        y=float(rng.uniform(.05,.95))*L
        U,V,b=data(D,L,rate,[y],[1.0])
        p0,pL,J=direct_point(D,L,rate,kappa,y)
        z=1/(1+b*kappa)
        S=U+V
        de=U-V
        assert np.allclose([p0,pL,J],[(S+z*de)/2,(S-z*de)/2,-kappa*z*de],rtol=3e-12,atol=3e-12), (i,p0,pL,J,U,V,b)
        assert math.isclose(J*math.log(pL/p0),entropy(U,V,b,kappa),rel_tol=2e-9,abs_tol=1e-11)
    for i in range(70):
        D=float(rng.uniform(.5,2.5));L=float(rng.uniform(.7,1.8))
        rate=float(rng.uniform(.4,4.0));kappa=float(rng.uniform(.2,3.0))
        ys=list(rng.uniform(.05,.95,3)*L)
        weights=np.array(rng.random(3));weights=weights/sum(weights)
        U,V,b=data(D,L,rate,ys,weights)
        direct=np.sum([w*np.array(direct_point(D,L,rate,kappa,y)) for y,w in zip(ys,weights)],axis=0)
        delta=U-V; z=1/(1+b*kappa); S=U+V
        np.testing.assert_allclose(direct,[(S+z*delta)/2,(S-z*delta)/2,-kappa*z*delta],rtol=3e-12,atol=3e-12)
    for t in [0.001,.01,.03,.1,.2,.4,.6,.8,.99,.99999]:
        z=zstar(t)
        assert .5<z<.565
        # Direct numerical optimization of the universal shape, unrelated to the critical equation.
        sol=minimize_scalar(lambda w: -(1-w)*math.atanh(t*w),bounds=(0,1),method='bounded', options={'xatol':1e-13})
        assert abs(z-sol.x)<2e-7,(z,sol.x,t)
    s=brentq(lambda z:math.atanh(z)-1/(1+z),.5,.9)
    assert .56437<s<.56439
    zvals=[zstar(t) for t in np.linspace(.02,.999,80)]
    assert all(v<w for v,w in zip(zvals,zvals[1:]))
    D,L,y=1.3,1.1,.23
    for rate in [1e-5,1e-4,1e-3,1e-2]:
        U,V,b=data(D,L,rate,[y],[1])
        z=zstar(abs(U-V)/(U+V))
        kap=(1-z)/(b*z)
        assert abs(kap/(D/L)-1)<0.02
    # Sharp weak-reset slope, not merely the leading endpoint value.
    for rate in [2e-4,5e-4,1e-3]:
        U,V,b=data(D,L,rate,[y],[1])
        z=zstar(abs(U-V)/(U+V))
        kap=(1-z)/(b*z)
        assert abs((kap-D/L)/rate-L/12)<2e-4
    # Any reset source has no larger interface dissipation than an endpoint source.
    for i in range(60):
        D=1.2; L=1.1; rate=1.3; kap=0.7
        yy=list(rng.uniform(.001,.999,4)*L)
        ww=rng.random(4); ww=ww/sum(ww)
        U,V,b=data(D,L,rate,yy,ww)
        U0,V0,_=data(D,L,rate,[0.],[1.])
        assert entropy(U,V,b,kap)<=entropy(U0,V0,b,kap)+1e-12
    for rate in [800,1200,1800,2500]:
        U,V,b=data(D,L,rate,[y],[1])
        z=zstar(abs(U-V)/(U+V))
        kap=(1-z)/(b*z)
        assert abs(kap/math.sqrt(D*rate)-(1-s)/(2*s))<.003
    print('PASS: 110 independent point-source BVPs, 70 independent mixed-source BVPs, 10 direct optimizer comparisons, monotonicity grid and both rate limits, weak-rate slope and endpoint-source bound')
    print('universal z1:',format(s,'.15f'))
    print('universal kappa*b lower:',format((1-s)/s,'.15f'))
    print('strong-rate kappa/sqrt(D*r):',format((1-s)/(2*s),'.15f'))


if __name__=='__main__':run()
