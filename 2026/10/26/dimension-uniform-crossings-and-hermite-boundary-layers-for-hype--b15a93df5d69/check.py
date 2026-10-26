"""Exact polynomial and independent quadrature checks for ultraspherical cap spectra."""
import math
import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_gegenbauer, roots_gegenbauer, roots_hermite, gammaln

x = sp.symbols('x')
checks = 0
for lam in (sp.Rational(1,2), sp.Rational(1), sp.Rational(3,2), sp.Rational(2), sp.Rational(3)):
    for ell in range(1,10):
        p = sp.gegenbauer(ell,lam,x)
        for m in range(ell):
            dm=sp.diff(p,x,m)
            d1=sp.diff(p,x,m+1)
            d2=sp.diff(p,x,m+2)
            D=(ell-m)*(ell+m+2*lam)
            residual=sp.expand((1-x*x)*d2 - (2*lam+2*m+1)*x*d1+D*dm)
            assert residual==0, (lam,ell,m,'ode')
            checks+=1
            # The complete boundary antiderivative identity after removing the weight.
            # Derivative of (1-x^2)^(lambda+m+1/2) dm*d1 equals
            # (1-x^2)^(lambda+m-1/2) [(1-x^2)*d1^2-D*dm^2].
            resid=sp.expand((1-x*x)*(d1*d1+dm*d2)
                -(2*lam+2*m+1)*x*dm*d1 -((1-x*x)*d1*d1-D*dm*dm))
            assert resid==0, (lam,ell,m,'boundary')
            checks+=1
            # Derivative-zero root count for even dimensional spheres (symbolic).
            r1=sp.polys.polytools.intervals(dm,eps=sp.Rational(1,1000000))
            r2=sp.polys.polytools.intervals(d1,eps=sp.Rational(1,1000000))
            npos=sum((1 if a>0 else 0) for (a,b),mult in r1)+sum((1 if a>0 else 0) for (a,b),mult in r2)
            assert npos==ell-m-1,(lam,ell,m,npos)
            checks+=1

for dim in range(2,8):
    lam=(dim-1)/2
    for ell in range(1,6):
        pnorm=lambda m: math.exp(math.log(math.pi)+(1-2*lam)*math.log(2)
                 +gammaln(ell+2*lam+m)-gammaln(ell-m+1)-math.log(ell+lam)-2*gammaln(lam))
        for m in range(ell):
            N=pnorm(m+1)
            if not N>0: raise AssertionError('norm')
            p0=lambda t: (2.0**m)*math.exp(gammaln(lam+m)-gammaln(lam))*eval_gegenbauer(ell-m,lam+m,t)
            p1=lambda t: (2.0**(m+1))*math.exp(gammaln(lam+m+1)-gammaln(lam))*eval_gegenbauer(ell-m-1,lam+m+1,t)
            for c in (0.2,0.4,0.6,0.8):
                v0=quad(lambda t:(1-t*t)**(lam+m-0.5)*p0(t)**2,c,1,epsabs=2e-10)[0]/pnorm(m)
                v1=quad(lambda t:(1-t*t)**(lam+m+0.5)*p1(t)**2,c,1,epsabs=2e-10)[0]/pnorm(m+1)
                rhs=(1-c*c)**(lam+m+0.5)*p0(c)*p1(c)/N
                assert abs(v0-v1-rhs)<2e-8,(dim,ell,m,c,v0-v1,rhs)
                checks+=1

# Fixed-degree high-dimension crossing radii tend to positive Hermite zeros
# under c -> sqrt(lambda)*c, with no fitted parameters.
for ell in range(2,9):
    for m in range(ell):
        herm=np.r_[roots_hermite(ell-m)[0],(roots_hermite(ell-m-1)[0] if ell-m-1>0 else np.array([]))]
        herm=np.sort(herm[herm>1e-8]); n=len(herm)
        assert n==ell-m-1
        lam=2000.5
        z=np.r_[roots_gegenbauer(ell-m,lam+m)[0],(roots_gegenbauer(ell-m-1,lam+m+1)[0] if ell-m-1>0 else np.array([]))]
        z=np.sort(z[z>1e-8])*np.sqrt(lam)
        assert len(z)==n
        assert n==0 or np.max(np.abs(z-herm))<0.025,(ell,m,z,herm)
        checks+=1
print(f'PASS {checks} exact-polynomial, quadrature and Hermite-root assertion groups')
