"""Exact-arithmetic checks for a diagonal rejected-probe Kaczmarz selection theorem.
No numerical Monte Carlo is used and no third-party libraries are required.
Run: python3 checker.py
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

n_checks = 0

def verify(condition, message='failed'):
    global n_checks
    n_checks += 1
    if not condition:
        raise AssertionError(message)

def expected_calls_dp(weights):
    """Solve all proper missing-subset first-step equations exactly."""
    weights = tuple(F(x) for x in weights)
    W = sum(weights)
    @lru_cache(None)
    def E(missing):
        if not missing: return F(0)
        R = sum(weights[i] for i in missing)
        return (W + sum(weights[i]*E(tuple(j for j in missing if j != i)) for i in missing))/R
    return E(tuple(range(len(weights))))

def expected_calls_2(a,b):
    a,b = F(a),F(b)
    return F(1)+a/b+b/a

def first_step_spectral_factor(a,b):
    a,b=F(a),F(b)
    return max(a,b)/(a+b)

def frob_cost(W,removed):
    return W-removed

# For any positive three diagonal singular-value squares, verify all row choices,
# and compare optimal expected raw probes and spectral proxy.
for a in range(3,12):
    for b in range(2,a):
        for c in range(1,b):
            w=tuple(map(F,(a,b,c)))
            W=sum(w)
            T=[]; Q=[]; Frobenius=[]
            for i in range(3):
                residual=[w[j] for j in range(3) if j!=i]
                T.append(expected_calls_dp(residual))
                Q.append(first_step_spectral_factor(*residual))
                Frobenius.append(frob_cost(W,w[i]))
                verify(T[-1]==expected_calls_2(*residual), 'two coupon DP identity')
            verify(Frobenius[0]<Frobenius[1]<Frobenius[2], 'Frobenius row index')
            verify(T[1]>T[0] and T[1]>T[2], 'middle never best')
            verify((T[2]<T[0])==(b*b>a*c), 'geometric threshold')
            verify((T[2]==T[0])==(b*b==a*c), 'transition equality')
            verify((Q[2]<Q[0])==(b*b>a*c), 'rate objective transition')
            verify((Q[2]==Q[0])==(b*b==a*c), 'rate transition equality')
            for i in range(3):
                verify((T[i]>T[(i+1)%3])==(Q[i]>Q[(i+1)%3]), 'cost-rate ordering')

# Direct finite-horizon enumeration of ALL sequences of raw draws for two remaining
# coordinates, independently from the recurrence and exact formula.
for a,b in [(1,1),(1,2),(2,3),(7,2),(13,1)]:
    p=F(a,a+b); q=1-p
    for h in range(1,9):
        surviving=F(0)
        for seq in product((0,1),repeat=h):
            if len(set(seq))==1:
                surviving+=p**sum(t==0 for t in seq)*q**sum(t==1 for t in seq)
        verify(surviving==p**h+q**h,'tail enumeration')

# Source-projected coordinate updates: each accepted row is fixed once and stays fixed;
# raw sampling probabilities do not depend on the surviving set.
for n in range(3,9):
    for selected in range(n):
        singular=[F(2)]+[F(1)]*(n-2)+[F(1,5)]
        x=[F(0)]*n
        x[selected]=F(1)
        for j in range(n):
            if j==selected:continue
            sj=singular[j]
            residual=sj*(x[j]-1)
            x[j]-=residual/sj
            verify(x[j]==1, 'coordinate corrected exactly')
            verify(x[selected]==1, 'constraint still enforced')
        verify(all(t==1 for t in x),'two-step/general complete')

# A rigorous finite-family corroboration of the dimension-uniform bounds.
for n in range(3,9):
    for k in range(2,7):
        eps=F(1,k)
        squared=[F(4)]+[F(1)]*(n-2)+[eps*eps]
        Tbad=expected_calls_dp(squared[1:])
        Tgood=expected_calls_dp(squared[:-1])
        Wbad=sum(squared[1:]);Wgood=sum(squared[:-1])
        verify(Tbad >= Wbad/(eps*eps),'rare row lower bound')
        verify(Tgood <= (n-1)*Wgood,'uniform discovered-row bound')
        verify(Wgood/Wbad <= 1+F(4,n-2),'near optimum Frobenius')

print('PASS: exact-arithmetic checks =',n_checks)
print('Example squared weights (4,1,1/100):')
for i in range(3):
    rem=[F(4),F(1),F(1,100)]
    rem.pop(i)
    print('  pinned row',i+1,'cost',expected_calls_dp(rem),'rate',first_step_spectral_factor(*rem))
