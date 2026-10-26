"""Checks for fourth-power norms of quadratic polynomials in power-weighted disk Bergman spaces.

Requirements: Python 3.10+, sympy, numpy, scipy. Numerical optimization and
quadrature are diagnostics, not substitutes for the uniform asymptotic proof.
"""
import sympy as s
import numpy as np
from scipy.optimize import minimize

B, x, y, t, q = s.symbols('B x y t q', positive=True, real=True)
U=2*B/(B+1)
V=3*B/(B+2)
W=6*B*(B+1)/((B+2)*(B+3))
assert s.simplify(2*V-W-12*B/((B+2)*(B+3)))==0
assert s.simplify(4*V-2*W-24*B/((B+2)*(B+3)))==0
assert s.simplify(U-4*V+W).subs(B,100).is_real

# The full quartic identity is the Fourier-orthogonal square expansion.
a,b,c,m1,m2,m3,m4=s.symbols('a b c m1 m2 m3 m4', positive=True, real=True)
raw=a**4+4*m1*a*a*b*b+m2*(b*b+2*a*c)**2+4*m3*b*b*c*c+m4*c**4
formal=a**4+4*a*a*b*b*m1+m2*b**4+4*m2*a*b*b*c+4*m2*a*a*c*c+4*m3*b*b*c*c+m4*c**4
assert s.expand(raw-formal)==0
moment=lambda k:s.factor(s.factorial(k)*s.gamma(B)/s.gamma(B+k))
assert s.simplify(moment(1)-1/B)==0
assert s.simplify(moment(2)-2/(B*(B+1)))==0
assert s.simplify(moment(3)-6/(B*(B+1)*(B+2)))==0
assert s.simplify(moment(4)-24/(B*(B+1)*(B+2)*(B+3)))==0
assert s.simplify(moment(2)/moment(1)**2-U)==0
assert s.simplify(moment(3)/(moment(1)*moment(2))-V)==0
assert s.simplify(moment(4)/moment(2)**2-W)==0

# Boundary B=0: the transverse squared-mode derivative is strictly positive.
z=s.symbols('z',real=True)
h=(1-z)**2+2*(V-1)*z*(1-z)+(2*V-W)*z*z
L=4*(1-z)+4*V*z-2*((1-z)**2+4*(1-z)*z+W*z*z)
assert s.factor(L-2*h)==0

# Exact Gaussian-limit deficit and the unique first correction maximum.
A,Y,C=s.symbols('A Y C',nonnegative=True,real=True)
lim_poly=A**4+4*A*A*Y+2*Y**2+4*s.sqrt(2)*A*C*Y+4*A*A*C*C+12*Y*C*C+6*C**4
S=A*A+Y+C*C
certificate=(2*s.sqrt(2)*A*C-Y)**2+3*Y*Y+8*A*A*Y+5*A**4
assert s.simplify(6*S*S-lim_poly-certificate)==0
J=24*q-4*q*q+4*s.sqrt(2)*t*q-8*t*t
assert s.simplify(J-(48-3*(q-4)**2-8*(t-q/(2*s.sqrt(2)))**2))==0

# Exact normalized squared-mass polynomial, before taking the square root C.
poly=(4-2*W)*x*x+(4*V-2*W)*y+(W-3)*x**4+(2*W-4*V)*x*x*y+(W-4*V+U)*y*y
assert s.simplify(s.limit(B*(4*V-2*W),B,s.oo)-24)==0
assert s.simplify(s.limit((4-2*W),B,s.oo)+8)==0
assert s.simplify(s.limit((W-4*V+U),B,s.oo)+4)==0
assert s.simplify(s.limit(4*s.sqrt(U),B,s.oo)-4*s.sqrt(2))==0

def obj(v,beta):
    a,bb,c=np.abs(v)
    u=2*beta/(beta+1); vv=3*beta/(beta+2)
    w=6*beta*(beta+1)/((beta+2)*(beta+3))
    ss=a*a+bb*bb+c*c
    return (a**4+4*a*a*bb*bb+u*bb**4+4*np.sqrt(u)*a*c*bb*bb
            +4*a*a*c*c+4*vv*bb*bb*c*c+w*c**4)/ss**2

# Independent angular/radial Fourier-moment expansion checks at nonzero phases.
for beta in (1.0,2.0,7.0,100.0):
    mu=lambda k: float(s.N(moment(k).subs(B,beta)))
    for aa,bb,cc in ((.4+.2j,.5-.1j,-.3+.7j),(.4+.5j,.1+.8j,.9-.2j)):
        co=[aa*aa,2*aa*bb,bb*bb+2*aa*cc,2*bb*cc,cc*cc]
        independent=sum(mu(k)*abs(co[k])**2 for k in range(5))
        normalized=[aa,bb*np.sqrt(mu(1)),cc*np.sqrt(mu(2))]
        a,b,c=normalized
        u=2*beta/(beta+1); vv=3*beta/(beta+2)
        w=6*beta*(beta+1)/((beta+2)*(beta+3))
        explicit=(abs(a)**4+4*abs(a*b)**2+u*abs(b)**4+4*abs(a*c)**2
                  +4*vv*abs(b*c)**2+w*abs(c)**4
                  +4*np.sqrt(u)*np.real(b*b*np.conj(a*c)))
        assert abs(independent-explicit)<3e-11

for beta in (1.,2.,10.,100.,1000.,10000.):
    starts=((1,1,1),(0.1,0.4,1), (1,0.2,1), (1,1,.1))
    sol=[]
    for v in starts:
        o=minimize(lambda p:-obj(p,beta),np.array(v,float),method='Nelder-Mead',
                   options={'maxiter':25000,'xatol':1e-11,'fatol':1e-11})
        sol.append((-o.fun,np.abs(o.x)/np.linalg.norm(o.x)))
    K,(a,b,c)=max(sol,key=lambda z:z[0]); w=6*beta*(beta+1)/((beta+2)*(beta+3))
    assert K>w+1e-10
    assert min(a,b,c)>1e-6
    print(f'beta={beta:7g}: K={K:.12f}; K-W={K-w:.12g}; '
          f'beta*A={beta*a:.7f}; beta*B2={beta*b*b:.7f}; beta2*(K-W)={beta**2*(K-w):.7f}')
print('All symbolic formulas and independent numerical diagnostics passed.')
