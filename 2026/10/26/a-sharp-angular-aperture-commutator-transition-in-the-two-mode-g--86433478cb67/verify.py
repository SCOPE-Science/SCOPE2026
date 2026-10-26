#!/usr/bin/env python3
"""Reproducible checks of a sharp angular-aperture concentration theorem.

The symbolic checks are exact.  Finite-dimensional quadratures and sampled
angular masks test normalization but are not substitutes for the continuum proof.
"""
import math
import random
import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammainc, gamma

assertions=0

def ck(cond, what):
    global assertions
    if not cond:
        raise AssertionError(what)
    assertions+=1

# Prove the squared spectral norm of the commutator is four times
# the squared Euclidean cross product of the two traceless Bloch vectors.
x1,y1,z1,x2,y2,z2=sp.symbols('x1 y1 z1 x2 y2 z2',real=True)
I=sp.I
A=sp.Matrix([[z1,x1-I*y1],[x1+I*y1,-z1]])
B=sp.Matrix([[z2,x2-I*y2],[x2+I*y2,-z2]])
C=A*B-B*A
cross=sp.Matrix([y1*z2-z1*y2,z1*x2-x1*z2,x1*y2-y1*x2])
ck(sp.simplify(-sp.trace(C*C)/2-4*cross.dot(cross))==0,'matrix commutator norm')

s1,s2,h1,h2,c=sp.symbols('s1 s2 h1 h2 c',real=True)
H=h1*h1*s2*s2+h2*h2*s1*s1-2*h1*h2*s1*s2*c+s1*s1*s2*s2*(1-c*c)
ck(sp.expand(H.subs(c,-h1*h2/(s1*s2))-(s1*s1+h1*h1)*(s2*s2+h2*h2))==0,'interior branch identity')
ck(sp.expand(H.subs(c,-1)-(h1*s2+h2*s1)**2)==0,'antipodal branch identity')
ck(sp.expand(sp.diff(H,c)+2*h1*h2*s1*s2+2*s1*s1*s2*s2*c)==0,'strict concavity')

# Independent polar integrations for Gaussian Fock's first two monomials.
def lowgam(t):
    return gamma(1.5)*gammainc(1.5,t)
def sfun(p,t):
    return lowgam(t)*math.sin(math.pi*p)/math.pi
def hfun(p,t):
    return p*t*math.exp(-t)/2
def rho(p,t):
    return hfun(p,t)/sfun(p,t)
def sharp(p,q,t):
    s,ss=sfun(p,t),sfun(q,t)
    h,hh=hfun(p,t),hfun(q,t)
    if h*hh<=s*ss:
        return 2*math.sqrt((h*h+s*s)*(hh*hh+ss*ss))
    return 2*(h*ss+hh*s)
def optimal_angle(p,q,t):
    return math.acos(-min(1.0,rho(p,t)*rho(q,t)))
def sector_matrix(p,t,center):
    l=2*math.pi*p
    Z=2*math.sin(l/2)*complex(math.cos(center),math.sin(center))
    d0=p*(1-math.exp(-t))
    d1=p*(1-(1+t)*math.exp(-t))
    b=lowgam(t)*Z/(2*math.pi)
    return np.array([[d0,np.conj(b)],[b,d1]],dtype=np.complex128)
def comm_norm(A,B):
    return float(np.linalg.norm(A@B-B@A,ord=2))

for t in [.025,.2,.8,1.0,2.0,9.0]:
    for p in [.12,.3,.5,.78,.93]:
        d0=quad(lambda r: 2*p*r*math.exp(-r*r),0,math.sqrt(t),epsabs=3e-13)[0]
        d1=quad(lambda r: 2*p*r**3*math.exp(-r*r),0,math.sqrt(t),epsabs=3e-13)[0]
        rad=quad(lambda r: r*r*math.exp(-r*r),0,math.sqrt(t),epsabs=3e-13)[0]
        M=sector_matrix(p,t,0)
        ck(abs(M[0,0]-d0)<3e-13,'constant diagonal quadrature')
        ck(abs(M[1,1]-d1)<3e-13,'linear diagonal quadrature')
        ck(abs(M[1,0]-(2*math.sin(math.pi*p)*rad/math.pi))<3e-13,'offdiagonal quadrature')

for t in [.03,.2,.5,.8,1.0,2.0,10.0]:
    for p in [.15,.5,.9]:
        for q in [.2,.5,.8]:
            delta=optimal_angle(p,q,t)
            obs=comm_norm(sector_matrix(p,t,0),sector_matrix(q,t,delta))
            ck(abs(obs-sharp(p,q,t))<5e-12,'attained sharp bound')
            for other in [0.0,.12,1.2,1.9,2.7,math.pi]:
                ck(comm_norm(sector_matrix(p,t,0),sector_matrix(q,t,other))<=sharp(p,q,t)+2e-14,'all angular separation candidates')

# Fixed-mass measurable masks approximated by cells; their first Fourier
# coefficients are EXACT integrals of exp(i theta) over the cell unions.
rng=random.Random(20261019)
N=80
bin_delta=2*math.pi/N
cell_Z=[(complex(math.cos((j+1)*bin_delta),math.sin((j+1)*bin_delta))-complex(math.cos(j*bin_delta),math.sin(j*bin_delta)))/1j for j in range(N)]
for t in [.1,.8,2.5]:
    for k,l in [(8,25),(22,44),(39,60)]:
        p,q=k/N,l/N
        d0a=p*(1-math.exp(-t));d1a=p*(1-(1+t)*math.exp(-t))
        d0b=q*(1-math.exp(-t));d1b=q*(1-(1+t)*math.exp(-t))
        for _ in range(90):
            EA=rng.sample(range(N),k);FB=rng.sample(range(N),l)
            za=sum(cell_Z[i] for i in EA);zb=sum(cell_Z[i] for i in FB)
            a=lowgam(t)*za/(2*math.pi);b=lowgam(t)*zb/(2*math.pi)
            TA=np.array([[d0a,np.conj(a)],[a,d1a]])
            TB=np.array([[d0b,np.conj(b)],[b,d1b]])
            ck(comm_norm(TA,TB)<=sharp(p,q,t)+1e-12,'measurable mask upper bound')

# Strict transition: product of decreasing ratios passes through unity once.
for p,q in [(.15,.35),(.5,.5),(.75,.9),(.25,.8)]:
    tstar=brentq(lambda t:rho(p,t)*rho(q,t)-1,1e-5,25,xtol=1e-13)
    ck(rho(p,tstar)*rho(q,tstar)>1-1e-11 and rho(p,tstar)*rho(q,tstar)<1+1e-11,'transition root')
    ck(rho(p,tstar/2)*rho(q,tstar/2)>1 and rho(p,2*tstar)*rho(q,2*tstar)<1,'branch orientation')
    print('transition p,q,t,R =',p,q,format(tstar,'.12f'),format(math.sqrt(tstar),'.12f'))

print('PASS',assertions,'checks; exact symbolic identities plus numerical normalization, finite mask and phase tests')
