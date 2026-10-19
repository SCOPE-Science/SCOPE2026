"""Standalone exact and high-precision checks of alternating bond dimer deposition."""
from fractions import Fraction
from functools import lru_cache
from math import isclose
import mpmath as mp

def recursive_path(m, alpha):
    beta=1-alpha
    p=[Fraction(1)]
    for k in range(1,m+1):
        p.append(alpha*sum(p[j]*p[k-1-j] for j in range(k))/(k-1+alpha))
    return p

def direct_cycle(n,a,b):
    L=2*n; edge_masks=[(1<<i)|(1<<((i+1)%L)) for i in range(L)]
    edge_rates=[a if i%2==0 else b for i in range(L)]
    full=(1<<L)-1
    @lru_cache(None)
    def rec(mask):
        choices=[i for i,E in enumerate(edge_masks) if not (mask&E)]
        if not choices:return Fraction(int(mask==full))
        total=sum(edge_rates[i] for i in choices)
        return sum((Fraction(edge_rates[i],total)*rec(mask|edge_masks[i]) for i in choices),Fraction(0))
    return rec(0)

def check_exact():
    cases=0
    for a,b in [(1,1),(2,3),(3,1),(1,5),(5,1)]:
        alpha=Fraction(a,a+b)
        for n in range(2,9):
            expected=alpha*recursive_path(n-1,alpha)[n-1]+(1-alpha)*recursive_path(n-1,1-alpha)[n-1]
            actual=direct_cycle(n,a,b)
            assert actual==expected,(n,a,b,actual,expected)
            cases+=1
    return cases

def check_special():
    mp.mp.dps=60
    alpha=mp.mpf('0.5'); beta=1-alpha
    u=lambda z:mp.hyp0f1(alpha-1,alpha*beta*z)
    s=mp.findroot(lambda s:s*mp.tanh(s)-1,(1,1.3)); R=s*s
    assert abs(u(R))<mp.mpf('1e-50')
    assert abs(R-mp.mpf('1.43922883989064515078'))<mp.mpf('1e-18')
    # Independently compare Riccati coefficients with the quotient of two 0F1 series.
    p=recursive_path(20,Fraction(1,2))
    # coefficient coefficients (-B)_m of u
    u_coeff=[mp.mpf(1)]
    for k in range(1,21):u_coeff.append(u_coeff[-1]*alpha*beta/(k*(alpha-2+k)))
    v_coeff=[mp.mpf(1)]
    for k in range(1,21):v_coeff.append(v_coeff[-1]*alpha*beta/(k*(alpha-1+k)))
    q=[mp.mpf(1)]
    for m in range(1,21):q.append(v_coeff[m]-sum(u_coeff[j]*q[m-j] for j in range(1,m+1)))
    assert all(abs(q[m]-mp.mpf(p[m].numerator)/p[m].denominator)<mp.mpf('1e-50') for m in range(21))
    root=lambda a:mp.findroot(lambda z:mp.hyp0f1(a-1,a*(1-a)*z),(mp.mpf('1.05'),mp.mpf('2.2')))
    kappa=-mp.diff(root,alpha)/R
    assert mp.mpf('1.0936') < kappa < mp.mpf('1.0937')
    for aa in [mp.mpf('0.3'),mp.mpf('0.7')]:
        r=root(aa)
        pp=[mp.mpf(1)]
        for m in range(1,71):
            pp.append(aa*sum(pp[j]*pp[m-1-j] for j in range(m))/(m-1+aa))
        assert abs(pp[70]*aa*r**71-1)<mp.mpf('0.00001')
    return float(R), float(1/R),float(kappa)

if __name__=='__main__':
    k=check_exact(); R,rate,kappa=check_special()
    print(f'PASS {k} independent exact finite-cycle cases; 21 hypergeometric coefficients; two pole-asymptotic checks; R={R:.16f}; rate={rate:.16f}; kappa={kappa:.12f}')
