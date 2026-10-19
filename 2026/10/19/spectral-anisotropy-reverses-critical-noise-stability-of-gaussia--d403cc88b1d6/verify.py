"""Deterministic reproducer for Gaussian state-dependent noisy Newton on quadratics.

The recurrence identities are exact analytical claims. Finite checks here are only
cross-checks, not a proof of the infinite-time limit theorems.
"""
import math
import numpy as np
from scipy.special import digamma, gammaln

checks = 0

def check(statement, label):
    global checks
    if not statement:
        raise AssertionError(label)
    checks += 1


def mu_dim2_exact(l1, l2):
    return -float(np.euler_gamma) + 2.0*math.log((math.sqrt(l1)+math.sqrt(l2))/2)


def mu_dim2_midpoint(l1, l2, n=4000):
    theta = (np.arange(n)+0.5)*2*math.pi/n
    return -float(np.euler_gamma) + float(np.mean(np.log(l1*np.cos(theta)**2+l2*np.sin(theta)**2)))

# The radial Gaussian term has mean log(chi2_2/2)=-EulerGamma.
for l1 in [0.1, 0.4, 1., 2., 8.]:
    for l2 in [0.15, 0.5, 1., 3., 6.]:
        check(abs(mu_dim2_exact(l1, l2)-mu_dim2_midpoint(l1, l2)) < 2e-12,
              'two-dimensional spectral log integral')

# Exact state-to-log-energy recurrence and orthogonal invariance.
rng = np.random.default_rng(240602)
for d in [1, 2, 3, 5, 9]:
    for alpha in [0., .2, .5, .75, 1., 1.3]:
        Avals=np.linspace(0.4,2.2,d)
        x=rng.normal(size=d)
        for _ in range(18):
            z=rng.normal(size=d)
            F=.5*float(np.dot(Avals*x,x))
            xnew=(F**alpha)*z
            Fnew=.5*float(np.dot(Avals*xnew,xnew))
            W=.5*float(np.dot(Avals*z,z))
            check(math.isclose(math.log(Fnew), 2*alpha*math.log(F)+math.log(W),abs_tol=4e-12),
                  'energy log recursion')
            x=xnew
            # Avoid dynamic overflow or underflow in the full-coordinate route.
            if Fnew < 1e-60 or Fnew > 1e60:
                break

# Exact zero-drift boundary in two dimensions and anisotropy reversal.
gamma=float(np.euler_gamma)
trace=4.0
iso=(trace/2,trace/2)
aniso=(3.9,0.1)
check(mu_dim2_exact(*iso)>0 and mu_dim2_exact(*aniso)<0,
      'anisotropy reversal at equal trace')
check(abs(mu_dim2_exact(math.exp(gamma),math.exp(gamma))) < 2e-14,
      'isotropic critical curvature')
for r in [.001,.02,.1,.3,.6,.9]:
    l1=trace-r
    l2=r
    check(mu_dim2_exact(l1,l2)<mu_dim2_exact(*iso),'strict two-dimensional Schur-concavity')

# At alpha=1/2 the expected energy ratio is trace(A)/2,
# even though the pathwise Lyapunov exponent depends on the eigenvalues.
for vals in [(2.,2.),(3.9,.1),(.3,1.4),(1.0,1.0)]:
    samples=rng.normal(size=(150000,2))
    q=.5*(vals[0]*samples[:,0]**2 + vals[1]*samples[:,1]**2)
    check(abs(float(np.mean(q))-sum(vals)/2) < .024,
          'first energy-moment trace identity')

# For fixed trace, the quenched log growth decreases under a majorizing
# eigenvalue redistribution in dimensions larger than two as well.
for eig1,eig2 in [((1.,1.,1.),(2.8,.1,.1)),
                  ((1.,1.,1.,1.),(3.7,.1,.1,.1))]:
    sim=rng.normal(size=(180000,len(eig1)))
    m1=float(np.mean(np.log(.5*np.sum((sim**2)*eig1,axis=1))))
    m2=float(np.mean(np.log(.5*np.sum((sim**2)*eig2,axis=1))))
    check(m2<m1-.1,'spectral majorization log-energy comparison')

# The stationary Mellin transform is a convergent product for 0 <= p < 1.
# For A=a I_d, E[(Z^T A Z/2)^t] = a^t Gamma(d/2+t)/Gamma(d/2).
for d in [1,2,3,8]:
    for p in [0.,.2,.5,.8]:
        for q in [.2, 1., 2., -min(.2,d/4)]:
            a=.7
            log_moment=sum((q*p**j)*math.log(a) +
                           float(gammaln(d/2+q*p**j)-gammaln(d/2))
                           for j in range(2000) if j==0 or p>0)
            # Cumulant identity: E log F = E log W/(1-p).
            h=1e-5
            def lnM(x):
                return sum((x*p**j)*math.log(a)+
                           float(gammaln(d/2+x*p**j)-gammaln(d/2))
                           for j in range(100) if j==0 or p>0)
            numder=(lnM(h)-lnM(-h))/(2*h)
            theory=(math.log(a)+float(digamma(d/2)))/(1-p)
            check(abs(numder-theory)<3e-8 and math.isfinite(log_moment),
                  'stationary product cumulant')

# Direct sample log moments of Q/2, deliberately not a proof of SLLN.
for eigs in [(1.,1.),(2.,2.),(3.9,.1),(.1,5.),(2.,.7)]:
    zs=rng.normal(size=(240000,2))
    Q=.5*((zs[:,0]**2)*eigs[0]+(zs[:,1]**2)*eigs[1])
    estimate=float(np.mean(np.log(Q)))
    check(abs(estimate-mu_dim2_exact(*eigs)) < .017,
          'Monte Carlo of critical log drift')

# Exact finite-product law for p > 1 in log energy, evaluated without
# overflowing the original nonlinear recurrence.
for p in [1.1, 1.5, 2., 3.]:
    for _ in range(40):
        increments=rng.normal(size=60)
        u=float(rng.normal())
        u0=u
        for n in range(1,10):
            un=p*u+increments[n-1]
            exact=p**n*(u0 + sum(p**(-j-1)*increments[j] for j in range(n)))
            check(abs(un-exact)<1e-10,'expanding log recursion')
            u=un

print(f'PASS: {checks} finite exact-identity and numerical checks')
print('critical examples (mu):',mu_dim2_exact(*iso),mu_dim2_exact(*aniso))
