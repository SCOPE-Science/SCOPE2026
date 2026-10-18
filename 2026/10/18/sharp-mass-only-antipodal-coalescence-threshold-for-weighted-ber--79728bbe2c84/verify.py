"""Reproducible checks for weighted Bergman boundary-pole coalescence."""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

x = sp.symbols('x', real=True, positive=True)
# Endpoint derivatives for the power weight with exponent three.
assert sp.simplify(sp.integrate(4*(1-x)**4/(1+x)**3, (x, 0, 1)) - (96*sp.log(2)-66)) == 0
assert sp.integrate(4*(1+x), (x, 0, 1)) == 6

nodes, weights = np.polynomial.legendre.leggauss(240)
t = (nodes+1)/2
wt = weights/2

def H(alpha, u):
    # Angular pair interaction (not the squared norm itself).
    return (alpha+1)*np.sum(wt*(1-t)**alpha*(u-t)/(1-2*t*u+t*t))

def Hpminus(alpha):
    return (alpha+1)*np.sum(wt*(1-t)**(alpha+1)/(1+t)**3)

def Hpplus(alpha):
    return alpha*(alpha+1)/((alpha-2)*(alpha-1))

def pair_energy(alpha, q, a, angles):
    z = np.exp(1j*np.asarray(angles))
    ans = q*sum(v*H(alpha, z_i.real) for v,z_i in zip(a,z))
    ans += sum(a[i]*a[j]*H(alpha,(z[i]*np.conjugate(z[j])).real)
               for i in range(len(a)) for j in range(i+1,len(a)))
    return ans

def delta_and_lower(alpha,q,a,angles):
    aa=np.array(a, dtype=float)
    zz=np.exp(1j*np.asarray(angles))
    w=aa.sum()
    baseline=pair_energy(alpha,q,aa,np.full(len(aa),math.pi))
    delta=pair_energy(alpha,q,aa,angles)-baseline
    s=np.sum(aa*(1+zz.real))
    bound=(q*Hpminus(alpha)-w*Hpplus(alpha))*s+0.5*Hpplus(alpha)*abs(np.sum(aa*(zz+1)))**2
    return delta,bound

rng=np.random.default_rng(20261017)
checks=0
for alpha in [2.5,3,4,7]:
    assert Hpminus(alpha)>0 and Hpplus(alpha)>Hpminus(alpha)
    for a in [[1,1],[0.6,1.25,2],[0.3,0.7,2.9,1.5]]:
        crit=sum(a)*Hpplus(alpha)/Hpminus(alpha)
        q=1.05*crit
        for _ in range(30):
            angles=rng.uniform(-math.pi,math.pi,len(a))
            gap,lo=delta_and_lower(alpha,q,a,angles)
            assert gap > -5e-10, (alpha,a,gap)
            assert gap >= lo-5e-9, (alpha,a,gap,lo)
            checks+=1

# The balanced splitting direction destroys the antipodal cluster below its threshold.
for alpha in [3,4,7]:
    a=[0.7,1.4,2.0]
    W=sum(a)
    crit=W*Hpplus(alpha)/Hpminus(alpha)
    q=0.93*crit
    displacement=np.array([a[1],-a[0],0.0])
    for eps in [0.01,0.003]:
        perturbed=np.pi+eps*displacement
        assert pair_energy(alpha,q,a,perturbed) < pair_energy(alpha,q,a,[np.pi]*len(a))
        checks+=1

# The finite Fourier series for the interaction independently checks the integral formula.
for alpha in [3,4,6]:
    for angle in [0.07,0.45,1.2,2.3,math.pi]:
        coef=1.0
        fourier=0.0
        for k in range(1,1501):
            if k==1: coef=1.0
            else: coef*= (k-1)/(k+alpha)
            fourier += coef*math.cos(k*angle)
        assert abs(fourier-H(alpha,math.cos(angle))) < 4e-8,(alpha,angle,fourier,H(alpha,math.cos(angle)))
        checks+=1

print('VERIFY_OK',checks,'energy and Fourier comparisons; alpha3 critical mass ratio =',6/(96*math.log(2)-66))
