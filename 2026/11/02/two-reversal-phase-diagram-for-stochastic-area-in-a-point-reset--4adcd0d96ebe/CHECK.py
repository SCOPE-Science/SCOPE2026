"""Independent analytic and numerical checks of the claimed mean signed area rate.
Run: python CHECK.py (sympy, mpmath, numpy)."""
import sympy as s
import mpmath as mp
import numpy as np
r,u,Tx,Ty,a,b=s.symbols('r u Tx Ty a b',real=True)
Delta=Tx-Ty
z=a*a-b*b
Den=(r+1)**2-u*u
# Generator moment equations: solve for the stationary first and signed-square moments.
mx,my,Q=s.symbols('mx my Q')
sol=s.solve([-(r+1)*mx+u*my+r*a, u*mx-(r+1)*my+r*b, -(r+2)*Q+2*Delta+r*z],[mx,my,Q],dict=True)[0]
cont=u*sol[Q]
jump=r*(b*sol[mx]-a*sol[my])
full=s.factor(cont+jump)
expected=u/(r+2)*(2*Delta + r*(1-u*u)*z/Den)
assert s.factor(full-expected)==0
assert s.simplify(jump + r*r*u*z/Den)==0
assert s.simplify(s.limit(full,r,0,dir='+')-u*Delta)==0
# Exact critical example: u=3/5, Tx=2, Ty=1, a=0, b=5/sqrt(2).
ex={u:s.Rational(3,5),Tx:2,Ty:1,a:0,b:5/s.sqrt(2)}
num=s.factor(full.subs(ex)); print('EXAMPLE',num)
assert s.simplify(num.subs(r,s.Rational(2,5)))==0
assert s.simplify(num.subs(r,s.Rational(8,5)))==0
assert num.subs(r,s.Rational(1,10))>0
assert num.subs(r,s.Integer(1))<0
assert num.subs(r,s.Integer(3))>0
sval=s.sqrt(1-u*u)
q=-z*(1-u*u)/(2*Delta)
shape=r/Den
assert s.simplify(s.diff(shape,r)-(1-u*u-r*r)/Den**2)==0
assert s.simplify(shape.subs(r,sval)-1/(2*(1+sval)))==0
# Product of distinct sign-flip roots is 1-u^2.
R=s.symbols('R',real=True)
poly=R**2+(2-q)*R+(1-u*u)
assert s.simplify(s.Poly(poly,R).all_coeffs()[-1]-(1-u*u))==0
# Independent renewal-reward integral, using expected OU evolution within a complete cycle.
mp.mp.dps=45
cases=[(0.6,2.,1.,0.,5/mp.sqrt(2), rr) for rr in (.1,.7,1.,2.5,5.)]
cases +=[(.25,3.2,.7,1.3,-2.1,.37),(.8,1.1,3.,2.5,0.4,1.7),(.45,2.2,2.2,4,1,0.9)]
for uu,tx,ty,aa,bb,rr in cases:
    dd=tx-ty; zz=aa*aa-bb*bb
    # OU propagator from a deterministic reset point.
    mean_x=lambda t: mp.exp(-t)*(aa*mp.cosh(uu*t)+bb*mp.sinh(uu*t))
    mean_y=lambda t: mp.exp(-t)*(bb*mp.cosh(uu*t)+aa*mp.sinh(uu*t))
    moment_diff=lambda t: dd+(zz-dd)*mp.exp(-2*t)
    # Reward for one reset cycle, divided by its mean cycle length 1/r.
    area_cont=rr*mp.quad(lambda t: mp.exp(-rr*t)*uu*moment_diff(t),[0,mp.inf])
    area_jump=rr*mp.quad(lambda t: rr*mp.exp(-rr*t)*(bb*mean_x(t)-aa*mean_y(t)),[0,mp.inf])
    direct=area_cont+area_jump
    closed=uu/(rr+2)*(2*dd+rr*(1-uu**2)*zz/((rr+1)**2-uu**2))
    assert abs(direct-closed)<mp.mpf('1e-12'), (direct,closed)
    print('CHECK',round(float(rr),3),float(direct),float(area_cont),float(area_jump))
# Independent random-time sample of stationary mean and signed moment (finite numerical experiment).
rng=np.random.default_rng(4177)
N=120000
for rr in (0.1,1.0,3.0):
    uu=.6;aa=0.;bb=5/np.sqrt(2);tx=2.;ty=1.
    ages=rng.exponential(scale=1/rr,size=N)
    # Conditional exact covariance from two OU eigenmodes, via analytic matrix integral.
    # Sample a Gaussian using quadrature discretization of positive definite OU covariance.
    normals=rng.normal(size=(2,N));xx=np.empty(N); yy=np.empty(N)
    for i,t in enumerate(ages):
        ev=np.array([[1.,1.],[1.,-1.]])/np.sqrt(2)
        lam=np.array([1-uu,1+uu]);DD=np.array([[tx,0.],[0.,ty]])
        d0=ev.T @ DD @ ev
        cov_e=np.array([[2*d0[j,k]*(1-np.exp(-(lam[j]+lam[k])*t))/(lam[j]+lam[k]) for k in range(2)] for j in range(2)])
        cov=ev@cov_e@ev.T
        mu=np.exp(-t)*np.array([aa*np.cosh(uu*t)+bb*np.sinh(uu*t),bb*np.cosh(uu*t)+aa*np.sinh(uu*t)])
        sample=mu+np.linalg.cholesky(cov)@normals[:,i]
        xx[i],yy[i]=sample
    emp=uu*np.mean(xx**2-yy**2)+rr*np.mean(xx*bb-yy*aa)
    exact=float(expected.subs({u:s.Rational(3,5),Tx:2,Ty:1,a:0,b:5/s.sqrt(2),r:rr}))
    stderr=np.std(uu*(xx*xx-yy*yy)+rr*(xx*bb-yy*aa))/np.sqrt(N)
    assert abs(emp-exact)<6*stderr,(rr,emp,exact,stderr)
    print('STATIONARY',rr,emp,exact,stderr)
print('PASS all symbolic identities, exact boundary examples, eight high-precision renewal quadratures, three independent stationary-law sampling tests')
