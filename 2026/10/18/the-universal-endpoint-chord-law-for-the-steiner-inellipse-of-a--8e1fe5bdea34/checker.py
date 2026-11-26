"""Finite symbolic, quadrature and physical checks of the closed chord law."""
import math

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.stats import qmc


def cuts(s):
    eta = math.sqrt(3)*s/math.sqrt(4-s*s)
    return (1-eta)/2, (1+eta)/2


def closed(s):
    if s == 0:
        return 0.0
    if s == 1:
        return 2/3+2*math.log(2)/9
    a,b = cuts(s)

    def F(t):
        return (1-1/t)*math.sqrt(t*t-t+1)+(
            math.asinh((2*t-1)/math.sqrt(3))-math.asinh((2/t-1)/math.sqrt(3)))/2

    return ((8-s*s)*(b-a)+(s*s-2)*math.log(b/a)+(1+s*s)*(1/b-1/a)-2*s*(F(a)+F(b)))/9


def section(u,s):
    # Directly take the length of the nonpositive region of the polynomial in v.
    k = 3*u-1
    A,B,C = k*k-s*s,u*(s*s-2*k),(1-s*s)*u*u
    bounds = [0.0,1.0]
    if A == 0:
        roots = [-C/B] if B != 0 else []
    else:
        disc = u*u*s*s*(4*(k*k-k+1)-3*s*s)
        root = math.sqrt(disc)
        q = -(B+math.copysign(root,B))/2
        roots = [q/A,C/q] if q else [-B/(2*A)]
    bounds = sorted(bounds + [x for x in roots if 0 < x < 1])
    ans = 0.0
    for lo, hi in zip(bounds,bounds[1:]):
        v = (lo+hi)/2
        if (A*v+B)*v+C <= 0:
            ans += hi-lo
    return ans


def direct_hit(V,X,Y,s):
    affine = np.column_stack((V[1]-V[0],V[2]-V[0]))
    inv = np.linalg.inv(affine)
    x = (X-V.mean(axis=0))@inv.T
    d = (Y-X)@inv.T
    H = np.array([[1,0.5],[0.5,1]])
    term = np.einsum('ni,ij,nj->n',x,H,d)
    diag = np.einsum('ni,ij,nj->n',d,H,d)
    coeff = np.divide(-term,diag,out=np.zeros_like(diag),where=diag>0).clip(0,1)
    r = x+coeff[:,None]*d
    value = np.einsum('ni,ij,nj->n',r,H,r)
    return value <= s*s/12+1e-12


def main():
    t,u,v = sp.symbols('t u v',positive=True)
    D = t*t-t+1
    F = (1-1/t)*sp.sqrt(D)+(sp.asinh((2*t-1)/sp.sqrt(3))-sp.asinh((2/t-1)/sp.sqrt(3)))/2
    assert sp.simplify(sp.diff(F,t)-(1+t)*sp.sqrt(D)/t**2) == 0
    assert sp.factor((3*u*v-u-v)**2-(u*u+v*v-u*v)) == 3*u*v*(3*u*v-2*u-2*v+1)
    assert sp.simplify(1-sp.integrate((1-2*u)/(2-3*u),(u,0,sp.Rational(1,2)))-sp.Rational(2,3)-2*sp.log(2)/9)==0
    for s in (.0001,.01,.1,.3,.5,.75,.9,.99,.999,1.0):
        points = sorted(set(x for x in (*cuts(s),(1+s)/3,(1-s)/3) if 0 < x < 1))
        val = quad(lambda u:section(u,s),0,1,points=points,epsabs=5e-11,epsrel=5e-11)[0]
        assert abs(val-closed(s)) < 8e-10,(s,val,closed(s))
    seq = qmc.Sobol(d=4,scramble=True,seed=13).random_base2(17)
    shapes = [((0,0),(1,0),(0,1)),((0,0),(3,0),(.3,2)),((1,-1),(5,0),(1.1,.1)),((0,0),(1.9,.1),(.1,1))]
    for coords in shapes:
        V = np.array(coords,float)
        U = np.roll(V,-1,axis=0)-V
        weights = np.linalg.norm(U,axis=1)
        p = weights/weights.sum()
        sigma = sum(p*p)
        cum = np.cumsum(p); cum[-1] = 1
        a = np.searchsorted(cum,seq[:,0]); b = np.searchsorted(cum,seq[:,2])
        X = V[a]+seq[:,1,None]*U[a]
        Y = V[b]+seq[:,3,None]*U[b]
        for s in (.1,.5,.8,.999,1.0):
            h = direct_hit(V,X,Y,s)
            target = (1-sigma)*closed(s)+(sigma/2 if s==1 else 0)
            assert abs(h.mean()-target)<.004,(coords,s,h.mean(),target)
            assert abs(np.mean(h & (a==b))-(sigma/2 if s==1 else 0))<.004
        X = np.array([V[0]+.17*U[0], V[0]+.18*U[0]])
        Y = np.array([V[0]+.71*U[0], V[0]+.29*U[0]])
        assert direct_hit(V,X,Y,1).tolist() == [True,False]
        assert direct_hit(V,X,Y,.999).tolist() == [False,False]
    print('PASS: symbolic identities, 10 direct quadratures, 20 physical trials, 4 side-contact tests')


if __name__=='__main__':
    main()
