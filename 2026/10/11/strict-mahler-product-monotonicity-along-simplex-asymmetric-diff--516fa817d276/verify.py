"""Independent finite diagnostics for simplex unbalanced-difference Mahler profile.
All-dimensional conclusion follows from the accompanying analytic proof, not these checks.
"""
from fractions import Fraction
from math import comb, factorial, cos, pi
import sympy as sp
import numpy as np
from scipy.special import roots_legendre
from scipy.spatial import ConvexHull, HalfspaceIntersection

u = sp.symbols('u')
checks=0
for d in range(2,13):
    n=d+1
    S=sum(comb(d,k)**2*u**k for k in range(d+1))
    P=sp.prod(j+(n-j)*u for j in range(1,n))
    W=sp.cancel((sp.diff(S,u)*P-S*sp.diff(P,u))/(1-u*u))
    assert sp.denom(W)==1
    c=sp.Poly(W,u).all_coeffs()
    assert c and all(k>0 for k in c)
    checks+=len(c)
    assert sp.simplify(u**d*S.subs(u,1/u)-S)==0
    assert sp.simplify(u**d*P.subs(u,1/u)-P)==0
    h=sp.symbols('h')
    # Ratio curvature with t=e^h: (t*d/dt)^2 log S/P at t=1.
    def curvature(F):
        D=lambda Z: u*sp.diff(Z,u)
        return sp.cancel((D(D(F))*F-D(F)**2)/F**2).subs(u,1)
    exact=sp.factor(curvature(S)-curvature(P))
    expected=-sp.Rational(d*(d-1)*(d+4),12*(2*d-1)*(d+1))
    assert exact==expected,(d,exact,expected)
    checks+=3
    for t in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)]:
        ratio=sp.factor((S/P).subs(u,t))
        symmetry=sp.factor((S/P).subs(u,1/t))
        assert ratio==symmetry
        assert ratio<(S/P).subs(u,1)
        checks+=2
for d in range(2,65):
    xs=sorted((float(x) for x in roots_legendre(d)[0] if x>1e-12),reverse=True)
    n=d+1
    assert len(xs)==d//2
    for j,x in enumerate(xs,1):
        cheb=cos(j*pi/n)
        grid=(n-2*j)/n
        assert x>cheb>grid-1e-13,(d,j,x,cheb,grid)
        checks+=2
for d in range(2,5):
    n=d+1
    vertices=np.vstack([np.zeros(d),np.eye(d)])-np.ones((n,d))/n
    for t in [0.,.3,1.,2.]:
        # Exact defining inequalities a_i-t*a_j<=1 for all (i,j).
        H=np.array([np.append(vertices[i]-t*vertices[j],-1.) for i in range(n) for j in range(n)])
        pv=HalfspaceIntersection(H,np.zeros(d)).intersections
        polar_volume=ConvexHull(pv).volume
        predicted=n**n/np.prod([j+(n-j)*t for j in range(1,n)])
        assert abs(polar_volume/predicted-1)<2e-9,(d,t,polar_volume,predicted)
        pointset=np.array([vertices[i]-t*vertices[j] for i in range(n) for j in range(n)])
        primal=ConvexHull(pointset).volume
        expected=sum(comb(d,k)**2*t**k for k in range(n))/factorial(d)
        assert abs(primal/expected-1)<2e-9,(d,t,primal,expected)
        checks+=2
print('VERIFY_OK',checks)
