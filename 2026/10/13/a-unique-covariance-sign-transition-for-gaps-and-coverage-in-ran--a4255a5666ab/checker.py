"""Independent, reproducible numerical and rational checks for a circle-coverage covariance theorem.

Usage: python checker.py
Only the Python 3 standard library is needed.
Finite checks are not substitutes for the analytic theorem.
"""
from __future__ import annotations
import math
import random
from fractions import Fraction


def covariance_formula(n: int, s):
    q = 1 - s
    return n * q ** (2*n-1) - q**n - (n-1) * max(1-2*s, type(s)(0))**n


def covariance_via_pair_moments(n: int, s):
    # Derive from marginal and mixed Dirichlet-spacing moments, not the closed form.
    a = (1-s)**(n-1)                # P(D_i>s)
    b = (1-s)**n / n              # E[(D_i-s)_+]
    cross = max(1-2*s, type(s)(0))**n / n # E[1{D_i>s}(D_j-s)_+], i != j
    mixed = n*a - n*b - n*(n-1)*cross  # E[K*C]
    mean_k = n*a
    mean_c = 1-n*b
    return mixed - mean_k * mean_c


def bisect_root(n: int, steps: int = 90) -> float:
    lo, hi = .2 / n, .5
    assert covariance_formula(n, lo)>0
    assert covariance_formula(n, hi)<0
    for _ in range(steps):
        mid = (lo+hi)/2
        if covariance_formula(n, mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def monte_carlo(n: int, s: float, trials: int = 220000, seed: int = 6):
    rng=random.Random(seed)
    k_total=c_total=kc_total=k2_total=c2_total=0.0
    for _ in range(trials):
        lengths=[rng.expovariate(1.0) for _ in range(n)]
        norm=sum(lengths)
        lengths=[d/norm for d in lengths]
        k=sum(d>s for d in lengths)
        c=1.0-sum(max(d-s,0) for d in lengths)
        k_total+=k; c_total+=c; kc_total+=k*c
        k2_total+=k*k; c2_total+=c*c
    mk=k_total/trials;mc=c_total/trials
    cov=kc_total/trials-mk*mc
    # Conservative plug-in Cauchy upper bound of standard error of sample covariance.
    var_k=k2_total/trials-mk**2
    var_c=c2_total/trials-mc**2
    return cov, math.sqrt(max(var_k*var_c,0)/trials)


def direct_circle_simulation(n: int, s: float, trials: int, seed: int):
    rng = random.Random(seed)
    sum_k=sum_c=sum_kc=0.0
    for _ in range(trials):
        xs=sorted(rng.random() for i in range(n))
        ds=[xs[i+1]-xs[i] for i in range(n-1)]
        ds.append(1.0-xs[-1]+xs[0])
        k=sum(d>s for d in ds)
        c=1-sum(max(d-s,0.0) for d in ds)
        sum_k+=k
        sum_c+=c
        sum_kc+=k*c
    return sum_kc/trials-(sum_k/trials)*(sum_c/trials)


def run():
    checks=0
    for n in range(2,41):
        for den in [5, 7, 11, 13, 17, 23, 31]:
            for p in range(1,den):
                s=Fraction(p,den)
                closed=covariance_formula(n,s)
                mixed=covariance_via_pair_moments(n,s)
                assert closed==mixed, (n,s,closed,mixed)
                checks+=1
    for n in [3,4,5,6,10,20,50,100]:
        root=bisect_root(n)
        assert 0<root<.5
        assert covariance_formula(n,root*.9)>0
        assert covariance_formula(n,min(root*1.1,.99))<0
        checks+=3
    for n in [2,3,4,7,13]:
        for j in range(1,300):
            s=j/300
            sign=covariance_formula(n,s)
            if n==2:
                expected=1 if s<.5 else (-1 if s>.5 else 0)
            else:
                root=bisect_root(n)
                expected=1 if s<root else -1
            assert sign*expected>0 or (expected==0 and abs(sign)<1e-13), (n,s,sign,expected)
            checks+=1
    from math import exp
    def limit(c):return exp(-2*c)*(1+c+c*c-exp(c))
    lo,hi=1.,3.
    for _ in range(90):
        mid=(lo+hi)/2
        if limit(mid)>0:lo=mid
        else:hi=mid
    cstar=(lo+hi)/2
    assert 1.79<cstar<1.80
    for n in [50,100,200,400,800]:
        assert abs(n*bisect_root(n)-cstar) < 17/n
        checks+=1
    empirical=[]
    for idx,(n,s) in enumerate([(2,.25),(3,.18),(4,.32),(6,.09),(6,.4),(12,.13),(18,.055)]):
        sample,se=monte_carlo(n,s,seed=1472+idx)
        truth=covariance_formula(n,s)
        assert abs(sample-truth)<.013+7*se,(n,s,truth,sample,se)
        empirical.append((n,s,round(truth,7),round(sample,7)))
        checks+=1
    for idx,(n,s) in enumerate([(3,.16),(4,.42),(9,.23)]):
        truth=covariance_formula(n,s)
        direct=direct_circle_simulation(n,s,240000,804+idx)
        assert abs(truth-direct)<.014,(n,s,truth,direct)
        checks+=1
    print('PASSED:', checks, 'exact-rational and numerical checks')
    print('sparse critical intensity:', format(cstar,'.14f'))
    print('simulation (n, arc length, theoretical covariance, empirical covariance):')
    for row in empirical:print(row)


if __name__=='__main__':run()
