"""Reproducible exact and finite-size checks for capped-debt exchange equilibrium.

Uses only Python standard library. Finite checks corroborate, but do not prove,
the large-population statement established by the combinatorial argument.
"""
from fractions import Fraction
from itertools import product
from math import comb, exp, log, sqrt, isclose


def sector_count(n, total, debt):
    """Number of integer n-vectors with sum=total and negative-part sum=debt."""
    if debt == 0:
        return comb(total + n - 1, n - 1)
    return sum(comb(n, j) * comb(debt - 1, j - 1)
               * comb(total + debt + n - j - 1, n - j - 1)
               for j in range(1, min(n - 1, debt) + 1))


def stationary_weight(state, a, b):
    """Unnormalized product-form weight for positive/nonpositive jump rates a,b."""
    return Fraction(1, 1) * a ** (-sum(max(k, 0) for k in state)) * b ** sum(max(-k, 0) for k in state)


def predicted_debt(kappa, r, tau):
    crit = 1 / (kappa * sqrt(r * (1+r)))
    if tau <= crit:
        return r*kappa
    return 0.5 * (sqrt(kappa*kappa + 4/(tau*tau)) - kappa)


def finite_debt(n, kappa, r, tau):
    total = round(kappa*n*n)
    cap = round(r*total)
    terms = [(d, log(sector_count(n, total, d)) - tau*d/n) for d in range(cap+1)]
    m = max(t for _,t in terms)
    p = [(d, exp(t-m)) for d,t in terms]
    return sum(d*w for d,w in p) / sum(w for _,w in p) / (n*n)


def run():
    tests = 0
    for n in (2, 3):
        for total in range(1, 6):
            for debt in range(0, 5):
                all_states = product(range(-debt, total+debt+1), repeat=n)
                brute = sum(sum(x)==total and sum(max(-y,0) for y in x)==debt for x in all_states)
                assert brute==sector_count(n,total,debt)
                tests+=1
    # Exact detailed balance of the product law on all admissible transitions.
    a=Fraction(2,3);b=Fraction(1,2)
    n=3;total=3;cap=2
    states=[x for x in product(range(-cap,total+cap+1),repeat=n)
            if sum(x)==total and sum(max(-y,0) for y in x)<=cap]
    states=set(states)
    for state in states:
        for i in range(n):
            for j in range(n):
                if i==j:continue
                other=list(state);other[i]-=1;other[j]+=1;other=tuple(other)
                if other not in states:continue
                rate=lambda z: a if z>=1 else b
                assert stationary_weight(state,a,b)*rate(state[i])==stationary_weight(other,a,b)*rate(other[j])
                tests+=1
    # Formula continuity at the threshold and strict unsaturated regime.
    for kap,r in ((1.0,.5),(.5,1.0),(2.0,.2),(3.0,2.0)):
        crit=1/(kap*sqrt(r*(1+r)))
        assert isclose(predicted_debt(kap,r,crit),r*kap,abs_tol=1e-12)
        assert predicted_debt(kap,r,crit+1e-3)<r*kap
        assert predicted_debt(kap,r,crit-1e-3)==r*kap
        tests+=3
    print('Exact count/detailed-balance and critical-curve checks:',tests)
    for tau in (-1,0,1,2,4):
        ds=predicted_debt(1,.5,tau)
        print('tau=%s  limiting debt=%.9f  N=20 %.9f  N=40 %.9f'%(
              tau,ds,finite_debt(20,1,.5,tau),finite_debt(40,1,.5,tau)))
    assert predicted_debt(1,.5,2)>0 and predicted_debt(1,.5,2)<.5
    print('PASS')
if __name__=='__main__':
    run()
