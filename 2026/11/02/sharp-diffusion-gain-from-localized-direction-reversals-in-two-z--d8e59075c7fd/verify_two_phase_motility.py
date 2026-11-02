#!/usr/bin/env python3
"""Independent numerical and symbolic diagnostics for two-zone velocity-jump dispersion."""
import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def analytic(v1, v2, lam1, lam2, f=0.5):
    I=f/v1+(1-f)/v2
    J=f*lam1/v1+(1-f)*lam2/v2
    return 1/(2*I*J)

def finite_state_diffusivity(v1, v2, lam1, lam2, n=200, f=0.5):
    assert abs(n*f-round(n*f))<1e-10
    pos=np.arange(n); v=np.where(pos<int(round(n*f)),v1,v2)
    lam=np.where(pos<int(round(n*f)),lam1,lam2)
    dx=1.0/n
    rows=[]; cols=[]; data=[]; rates=[]; dest=[]; displacement=[]
    for si,sg in enumerate((1,-1)):
        for i in range(n):
            a=si*n+i; b=si*n+(i+sg)%n; c=(1-si)*n+i
            q=v[i]/dx
            rows.extend([a,a,a,a]);cols.extend([b,c,a,a]);data.extend([q,lam[i],-q,-lam[i]])
            rates.append((a,b,q));dest.append(b);displacement.append(sg*dx)
            rates.append((a,c,lam[i]));dest.append(c);displacement.append(0.)
    Q=coo_matrix((data,(rows,cols)),shape=(2*n,2*n)).tocsr()
    stationary=np.tile(1/v,2);stationary/=stationary.sum()
    check=np.max(np.abs(Q.T@stationary))
    g=np.r_[v,-v]; assert abs(stationary@g)<1e-12
    assert check<1e-9,check
    A=Q.tolil();A[0,:]=0;A[0,0]=1
    rhs=-g;rhs[0]=0
    phi=spsolve(A.tocsr(),rhs)
    assert np.max(np.abs((Q@phi+g)[1:]))<1e-8
    mu=sum(stationary[a]*q*(step+phi[b]-phi[a])**2 for (a,b,q),step in zip(rates,displacement))
    return 0.5*mu

def main():
    f,r=sp.symbols('f r',positive=True)
    R=r**2/((f*r+1-f)**2*(f+(1-f)*r))
    critical=f*r**2+(f-1)*r-2*f
    derivative=sp.factor(sp.diff(R,r))
    assert sp.simplify(derivative+r*(1-f)*critical/((f*r+1-f)**3*(f*r-f-r)**2))==0
    rstar=(1-f+sp.sqrt(9*f**2-2*f+1))/(2*f)
    assert sp.simplify(critical.subs(r,rstar))==0
    assert sp.simplify(R.subs({f:sp.Rational(1,2),r:2})-sp.Rational(32,27))==0
    e,z=sp.symbols('e z',real=True)
    D=sp.factor(analytic(1+e,1-e,1+z,1-z))
    assert sp.factor(D/(sp.Rational(1,2))-(1-e*e)**2/(1-e*z))==0
    rng=np.random.default_rng(1947)
    samples=0
    for k in range(240):
        ff=float(rng.uniform(.04,.95)); v1=float(rng.uniform(.2,5));v2=float(rng.uniform(.2,5))
        lam1=float(rng.uniform(.03,4));lam2=float(rng.uniform(.03,4))
        exact=analytic(v1,v2,lam1,lam2,ff)
        I=ff/v1+(1-ff)/v2
        J=ff*lam1/v1+(1-ff)*lam2/v2
        assert abs(exact*2*I*J-1)<1e-12
        rr=float(rstar.subs(f,ff))
        vals=np.array([float(R.subs({f:ff,r:rv})) for rv in rng.uniform(1,20*rr,40)])
        assert np.max(vals)<=float(R.subs({f:ff,r:rr}))+1e-12
        samples+=1
    for v1,v2,l1,l2 in [(4/3,2/3,2,0),(.7,2.6,.4,1.7),(2.,1.,2.3,.2)]:
        exact=analytic(v1,v2,l1,l2)
        for n in (80,160,320):
            approximate=finite_state_diffusivity(v1,v2,l1,l2,n)
            # Upwind scheme adds order(dx) lattice-step noise.
            assert abs(approximate-exact)<0.05, (n,approximate,exact)
            print('CTMC',v1,v2,l1,l2,n,round(approximate,9),'target',round(exact,9))
    print('PASS symbolic identities; %d random envelope checks; 9 independently built CTMC corrector checks' % samples)

if __name__=='__main__':main()
