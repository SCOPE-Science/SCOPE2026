"""Reproducible symbolic and numerical checks for Kottler circular-frequency inversion.

Only the metric conventions and exact formulas stated in RESULT.md are used.
Run: python verify_kottler.py (requires sympy).
"""
import math
import random
import sympy as sp

r, M, Lam, ell = sp.symbols('r M Lambda ell', positive=True)
f = 1-2*M/r-Lam*r**2/3
omega_sq = sp.simplify(sp.diff(f,r)/(2*r))
kappa_sq = sp.factor((f*sp.diff(f,r,2)-2*sp.diff(f,r)**2+3*f*sp.diff(f,r)/r)/2)
assert sp.simplify(omega_sq-(M/r**3-Lam/3)) == 0
assert sp.simplify(kappa_sq-(M/r**3*(1-6*M/r)-Lam/3*(4-15*M/r))) == 0
L2 = sp.factor(r**3*sp.diff(f,r)/(2*f-r*sp.diff(f,r)))
E2 = sp.factor(2*f**2/(2*f-r*sp.diff(f,r)))
V = f*(1+ell**2/r**2)
# Independent effective-potential second-variation identity for coordinate time.
epi_from_potential = sp.factor((f**2/E2) * (sp.diff(V,r,2)/2).subs(ell**2,L2))
assert sp.simplify(epi_from_potential-kappa_sq) == 0
assert sp.simplify(L2-(r**2*(M/r-Lam*r**2/3)/(1-3*M/r))) == 0

rng=random.Random(810452)
checks=0
for j in range(1500):
    a = rng.uniform(1e-5, 1/6-1e-5)
    factor = rng.uniform(1e-7,1-1e-7)
    b = a*(1-6*a)*factor
    r0 = math.exp(rng.uniform(-4,4))
    x=(1+5*a-math.sqrt(1-6*a+25*a*a+4*b))/6
    mass=x*r0; lam=3*(x-a)/(r0*r0)
    assert mass>0 and lam>0 and x<1/6 and x>a
    assert 1-2*x-lam*r0*r0/3>0
    Om2=mass/r0**3-lam/3
    Kap2=mass/r0**3*(1-6*mass/r0)-lam/3*(4-15*mass/r0)
    assert math.isclose(Om2*r0*r0,a,rel_tol=1e-9,abs_tol=1e-12)
    assert math.isclose(Kap2*r0*r0,b,rel_tol=1e-8,abs_tol=1e-12)
    checks+=1

# Known-mass inverse: bracketed bisection with exact derivative monotonicity.
for j in range(1000):
    mass=math.exp(rng.uniform(-4,4))
    u=rng.uniform(1e-3,0.165)
    om2=u**3/mass**2
    kap2=om2*(1-6*u)*rng.uniform(1e-7,1-1e-7)
    lo=6*mass; hi=mass/u
    def kval(R):
        return 9*mass**2/R**4 - 3*mass/R**3 + om2*(4-15*mass/R)
    assert kval(lo)<kap2<kval(hi)
    for t in range(75):
        md=(lo+hi)/2
        if kval(md)>kap2: hi=md
        else: lo=md
    R=(lo+hi)/2
    lam=3*(mass/R**3-om2)
    assert lam>0 and R>6*mass
    assert math.isclose(kval(R),kap2,rel_tol=5e-12,abs_tol=1e-13)
    checks+=1

# Observations alone: all radii in the open feasible interval generate the same pair.
for j in range(1000):
    om=math.exp(rng.uniform(-4,4))
    rho=rng.uniform(1e-5,1-1e-5)
    amax=(1-rho)/6
    a=amax*rng.uniform(1e-5,1-1e-5)
    R=math.sqrt(a)/om
    b=rho*a
    x=(1+5*a-math.sqrt(1-6*a+25*a*a+4*b))/6
    mass=x*R; lam=3*(x-a)/R**2
    assert mass>0 and lam>0 and 0<R<math.sqrt(amax)/om
    assert math.isclose(mass/R**3-lam/3,om**2,rel_tol=1e-10)
    assert math.isclose(mass/R**3*(1-6*mass/R)-lam/3*(4-15*mass/R),rho*om**2,rel_tol=1e-9)
    checks+=1

# Frequency-only fiber parameterized by x=M/r: exact range, all coordinates monotone.
for j in range(1200):
    om=math.exp(rng.uniform(-4,4))
    rho=rng.uniform(1e-5,1-1e-5)
    xmax=(1-rho)/6
    x=xmax*rng.uniform(1e-5,1-1e-5)
    def trip(t):
        a=3*t*(1-3*t)/(4-rho-15*t)
        R=math.sqrt(a)/om
        return R,t*R,om*om*(1-rho-6*t)/(1-3*t)
    R,mm,ll=trip(x)
    assert R>0 and mm>0 and ll>0
    assert math.isclose(mm/R**3-ll/3,om**2,rel_tol=1e-9)
    assert math.isclose(mm/R**3*(1-6*mm/R)-ll/3*(4-15*mm/R),rho*om**2,rel_tol=1e-9)
    xa=x*0.97
    xb=x+0.03*(xmax-x)
    Ra,Ma,La=trip(xa)
    Rb,Mb,Lb=trip(xb)
    assert Ra<R<Rb and Ma<mm<Mb and La>ll>Lb
    assert R<math.sqrt((1-rho)/6)/om
    assert mm<((1-rho)/6)**1.5/om
    assert ll<(1-rho)*om*om
    checks+=1

# Strict feasibility inequalities exclude their own boundaries by definition.
for aa in [0,1/6,0.19]:
    assert not (0<aa<1/6)
print('PASS: symbolic identities (forward, effective potential, orbit constants),')
print(checks,'random inversion and feasibility comparisons')
