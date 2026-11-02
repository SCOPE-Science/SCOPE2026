"""Standalone analytical/numerical checks for a reversible-diffusion reset identity.
Run: python CHECK.py. Tests are diagnostics, not a substitute for proof.
"""
import math
from fractions import Fraction
import sympy as s
import numpy as np
from scipy.integrate import simpson

ncheck=0

def check(ok, msg):
    global ncheck
    if not ok:
        raise AssertionError(msg)
    ncheck+=1

# For a birth-death chain absorbed at zero, the conductance Green
# kernel is G_ij = sum_{k=0}^{min(i,j)-1} (1/c_k). These exact-rational
# identities test all factors, orientations and weight conventions.
for n in range(2,8):
    for case in range(1,12):
        masses=[s.Integer(1)+s.Rational((i+1)*case % 7,3) for i in range(n)]
        conduct=[s.Integer(1)+s.Rational((i*case+2)%11,4) for i in range(n)]
        Q=s.zeros(n)
        for i in range(n):
            if i>0:
                Q[i,i-1]=conduct[i]/masses[i]
                Q[i,i]-=conduct[i]/masses[i]
            else:
                Q[i,i]-=conduct[0]/masses[0]
            if i<n-1:
                Q[i,i+1]=conduct[i+1]/masses[i]
                Q[i,i]-=conduct[i+1]/masses[i]
        M=s.diag(*masses)
        G=(-Q).inv()
        K=s.Matrix(n,n,lambda i,j:sum(1/conduct[k] for k in range(min(i,j)+1)))
        check(G==K*M, 'discrete Green identity')
        rates=[s.Rational(1+case%5,5),s.Rational(2+case%7,6)]
        values=[]
        for rate in rates:
            k=s.Matrix([conduct[0]/masses[0]]+[0]*(n-1))
            f=(rate*s.eye(n)-Q).inv()*k
            check(all(x>0 for x in f), 'positive hit probability')
            a=(s.ones(n,1)-f)/rate
            check(a==G*f, 'expected stopped time equals Green transform')
            values.append((f,a))
        f0,a0=values[0];fq,aq=values[1]
        Z=sum(masses[i]*f0[i]**2 for i in range(n))
        R0=sum(masses[i]*f0[i]**2*a0[i]/f0[i] for i in range(n))/Z
        Rq=sum(masses[i]*f0[i]**2*aq[i]/fq[i] for i in range(n))/Z
        h=[fq[i]/f0[i] for i in range(n)]
        gap=sum(masses[i]*masses[j]*K[i,j]*f0[i]*f0[j]*(h[i]-h[j])**2/(h[i]*h[j]) for i in range(n) for j in range(n))/(2*Z)
        check(s.factor(Rq-R0-gap)==0,'exact pairwise risk gap')
        check(gap>=0,'nonnegative risk gap')

# Continuum constant-force reflecting interval. Compare the reset MFPT
# independently computed from Poisson first-hit Laplace transforms with
# the proposed symmetric Green double integral.
for D,v,L,r0,r1 in [(1.,0.,3.,.7,2.3),(.8,.5,2.,1.3,.6),(1.2,1.4,4.,.4,1.6),(.7,2.,1.,1.5,.3)]:
    x=np.linspace(0,L,801)
    delta=v/(2*D)
    def f_r(r):
        gamma=math.sqrt(delta**2+r/D)
        return np.exp(delta*x)*(np.cosh(gamma*(L-x))+(delta/gamma)*np.sinh(gamma*(L-x)))/(math.cosh(gamma*L)+(delta/gamma)*math.sinh(gamma*L))
    fp=f_r(r0);fq=f_r(r1)
    m=np.exp(-v*x/D)
    Z=simpson(m*fp**2,x=x)
    R0=simpson(m*fp**2*((1-fp)/r0)/fp,x=x)/Z
    Rq=simpson(m*fp**2*((1-fq)/r1)/fq,x=x)/Z
    h=fq/fp
    K=(np.expm1(v*np.minimum.outer(x,x)/D)/v if v else np.minimum.outer(x,x)/D)
    integrand=(K*(fp*m)[:,None]*(fp*m)[None,:])*((h[:,None]-h[None,:])**2/(h[:,None]*h[None,:]))
    gap=simpson(simpson(integrand,x=x,axis=1),x=x)/(2*Z)
    check(abs(Rq-R0-gap)<4e-7,f'continuum gap error {Rq-R0-gap}')
    check(Rq+1e-10>=R0,'continuum inequality')
    check(abs(fp[0]-1)<1e-12,'unit hitting boundary')
    check(abs(np.gradient(fp,x)[-1])<.008,'reflecting boundary finite-difference')

# Inward drift half-line: exact algebra for the claimed Poisson optimum.
D,v,l,a=s.symbols('D v l a', positive=True)
a0=(D*l-v)/(2*D)
F=1/((D*a+v)*(l-a))
Fstar=4*D/(D*l+v)**2
GAP=4*D**2*(a-a0)**2/((D*l+v)**2*(D*a+v)*(l-a))
check(s.factor(F-Fstar-GAP)==0,'Poisson quadratic gap factorization')
print(f'PASS {ncheck} deterministic assertions, including exact rational discrete Green kernel and Poisson comparisons and continuum quadrature.')
