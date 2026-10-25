"""Standalone scientific checks for rank-two clipped hypersimplex widths.
Python 3 + numpy; scipy is not required.  Seeded tests are diagnostics,
not a substitute for the analytic extreme-value argument.
"""
from itertools import combinations, permutations
from math import comb, factorial, log, sqrt, pi, e
import numpy as np

RNG=np.random.default_rng(513927)
checked=0
for p in range(1,6):
    for q in range(2,8):
        n=p+q
        vertices=np.asarray([tuple(int(i in ij) for i in range(n))
                             for ij in combinations(range(n),2)
                             if not (ij[0]<p and ij[1]<p)],dtype=float)
        for _ in range(28):
            g=RNG.normal(size=n)
            a=g[:p]; b=g[p:]
            bsorted=np.sort(b)
            hfast=max(bsorted[-1]+bsorted[-2],bsorted[-1]+max(a))
            lfast=min(bsorted[0]+bsorted[1],bsorted[0]+min(a))
            values=vertices @ g
            assert np.isclose(hfast,max(values),rtol=0,atol=1e-11)
            assert np.isclose(lfast,min(values),rtol=0,atol=1e-11)
            proj=g-g.mean()
            u=proj/np.linalg.norm(proj)
            direct_width=np.ptp(vertices @ u)
            assert np.isclose(direct_width,(hfast-lfast)/np.linalg.norm(proj),atol=1e-11)
            checked+=1

# Distribution-free angular contact count: enumerate all ranks.
rank_checks=0
for p in range(1,5):
    for q in range(2,6):
        n=p+q
        if n>8: continue
        use_A=0
        total=0
        for perm in permutations(range(n)):
            # The maximizing admissible pair uses A iff top two
            # globally ranked entries are not both from B.
            use_A+=not(perm[0]>=p and perm[1]>=p)
            total+=1
        assert use_A* n*(n-1)==total*(n*(n-1)-q*(q-1))
        rank_checks+=1

# Two unit exponential arrivals give the top two PPP points;
# a third exponential arrival gives the competing A maximum.
from math import e as EULERS_NUMBER
EULER_GAMMA=0.577215664901532860606512090082402431
N=500000
E1=RNG.exponential(size=N)
E2=RNG.exponential(size=N)
E3=RNG.exponential(size=N)
ppp_checks=0
for c in (0,0.2,0.6,1.0,3.0):
    x1=-np.log(E1)
    x2=-np.log(E1+E2)
    y1=np.full(N,-np.inf) if c==0 else log(c)-np.log(E3)
    z=np.maximum(x2,y1)
    h=x1+z
    mean_theory=2*EULER_GAMMA+log(1+c)-1/(1+c)
    assert abs(h.mean()-mean_theory)<0.025,(c,h.mean(),mean_theory)
    for x in (-1.0,0.0,1.0):
        # Direct Riemann quadrature of the *H* CDF, not the CDF of
        # the second competing extreme alone. Tail beyond t=45 is < e^-45.
        v=np.exp(-x)
        tt=np.linspace(1e-8,45,45001)
        integrand=np.where(tt<=sqrt(v),
                  np.exp(-(1+c)*v/tt),
                  np.exp(-tt-c*v/tt))
        theory=float(np.trapezoid(integrand,tt))
        empirical=float(np.mean(h<=x))
        assert abs(empirical-theory)<0.008,(c,x,empirical,theory)
        ppp_checks+=1
    print('c=',c,' PPP H mean=',round(float(h.mean()),5),
          ' formula=',round(mean_theory,5),
          ' A contact limit=',round(1-(1+c)**-2,5))

print('CHECK_OK',checked,'direct support/width identities;',
      rank_checks,'exhaustive rank-probability identities;',
      ppp_checks,'Poisson-process CDF diagnostics')
