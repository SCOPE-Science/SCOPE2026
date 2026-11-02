"""Numerical and finite-algebra consistency checks for reset-clock arrival inversion.

The asymptotic theorem is proved analytically in RESULT.md; these finite checks
only test formulas and representative parameters.
"""
from math import erf, erfc, exp, sqrt, isclose, comb, pi
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import erf as erf_vec

checks = 0

def check(condition, label):
    global checks
    if not bool(condition):
        raise AssertionError(label)
    checks += 1

def q0(t, d=1.0, D=1.0):
    return 1.0 if t == 0 else erf(d / sqrt(4 * D * t))

def h2(p):
    return 3 * p * p - 2 * p**3

def L(j, z, d=1.0, D=1.0):
    return quad(lambda t: exp(-z*t)*q0(t,d,D)**j,
                0.0, np.inf, epsabs=2e-11, limit=300)[0]

def pole(j, r=1.0, d=1.0, D=1.0):
    return brentq(lambda theta: r*L(j,r-theta,d,D)-1,
                  0.0, 0.999*r, xtol=1e-12)

# Laplace identity for the one-body first-passage survival.
for d in (0.6,1.0,1.4):
    for z in (0.4, 0.8, 1.4, 2.0):
        lhs=L(1,z,d,1.)
        rhs=(1-exp(-d*sqrt(z)))/z
        check(isclose(lhs,rhs,rel_tol=1e-9,abs_tol=1e-11), "one-body Laplace transform")

# Binomial-mixture rank formulas for three searchers and Jensen comparisons.
for m in (0.04, 0.15, 0.30, 0.45):
    for delta in (0.001, 0.005, 0.01):
        p_low,p_high=m-delta,m+delta
        check(0<p_low<p_high<0.5, "convex interval")
        check((h2(p_low)+h2(p_high))/2>h2(m), "strict early-time convexity")
        check((p_low**3+p_high**3)/2>m**3, "last rank Jensen")
        check(((1-p_low)**3+(1-p_high)**3)/2>(1-m)**3,
              "first rank Jensen")

# Exhaustive counting identity for N=3, K<=1 and K>=2.
for p in np.linspace(0.,1.,21):
    probs=[comb(3,k)*p**k*(1-p)**(3-k) for k in range(4)]
    check(isclose(sum(probs),1.,abs_tol=1e-12), "binomial partition")
    check(isclose(probs[2]+probs[3],h2(p),abs_tol=1e-12), "median CDF")
    check(isclose(probs[0]+probs[1],1-h2(p),abs_tol=1e-12), "median survival")

# Two positive renewal poles and strictly subadditive joint-survival exponent.
for d in (0.7,1.0,1.3):
    theta1=pole(1,d=d)
    theta2=pole(2,d=d)
    check(0<theta1<theta2<1., "pole locations")
    check(theta2<2*theta1, "strict theta2 < 2 theta1")
    check(isclose(L(1,1-theta1,d),1.,rel_tol=1e-9), "first pole equation")
    check(isclose(L(2,1-theta2,d),1.,rel_tol=1e-9), "second pole equation")
    check(L(3,1-theta2,d)<1., "third joint survival faster than second")

# Small-time convexity cutoff, with a strict gap even for a single reset.
for t in (0.02,0.04,0.08,0.12,0.16):
    f=erfc(1/sqrt(4*t))
    if t<1/6:
        check(f<0.5, "small-time hit bound")
        check(1-q0(t/2)**2<f, "strict one-reset hit deficit")

# Independent renewal Volterra check at finite times; this is a discretization.
step=0.02
points=1001
xs=np.arange(points)*step
q=np.ones(points)
q[1:]=erf_vec(1/np.sqrt(4*xs[1:]))
sol={}
for j in (1,2,3):
    ker=np.exp(-xs)*q**j
    s=np.zeros(points);s[0]=1.
    for n in range(1,points):
        s[n]=(ker[n]+step*(0.5*ker[n]*s[0]
              +np.dot(ker[1:n],s[n-1:0:-1])))/(1-step/2)
    sol[j]=s
for t, expected_sign in ((0.1,-1),(0.5,-1),(3.,1),(5.,1),(10.,1),(20.,1)):
    k=round(t/step)
    a,b,c=(sol[j][k] for j in (1,2,3))
    global_median=3*b-2*c
    independent_median=3*a*a-2*a**3
    check(expected_sign*(global_median-independent_median)>1e-9,
          "Volterra early/late sign")

print(f"PASS: {checks} numerical and finite-algebra checks")
print("Reference parameters: D=d=r=1")
theta1=pole(1); theta2=pole(2)
print(f"theta_1={theta1:.12f}, theta_2={theta2:.12f}, "
      f"2theta_1-theta_2={2*theta1-theta2:.12f}")
