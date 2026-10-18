"""Exact-rational checks for periodic-coset B-spline Gabor frame bounds.

Execute: python checker.py
Requires Python standard library only. Finite checks corroborate but do not replace the proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import cmath

def phi(t):
    t=t % 1
    return t*(1-t)

def potential(jset,m,x):
    return sum((phi(x-Q(j,m)) for j in jset),Q(0))

def exact_max_potential(jset,m):
    """Independent exact piecewise-quadratic maximization on every phase cell."""
    jset=sorted(jset)
    k=len(jset)
    nodes=sorted({Q(0),Q(1)}|{Q(j,m) for j in jset})
    best=Q(-1)
    for lo,hi in zip(nodes[:-1],nodes[1:]):
        middle=(lo+hi)/2
        ages=[(middle-Q(j,m))%1 for j in jset]
        # At interior x, u_j=x-j/m+integer, so sum u_j=k*x+constant.
        age_total=sum(ages,Q(0))
        stationary=middle+(Q(k,2)-age_total)/k
        for x in (lo,hi,min(max(stationary,lo),hi)):
            best=max(best,potential(jset,m,x))
    return best

def is_cyclic_block(jset,m):
    k=len(jset)
    S=set(jset)
    return any(S=={(j+i)%m for i in range(k)} for j in range(m))

def closed_mask_bound(jset,m):
    """Cyclic-cut arithmetic formula, independent of cellwise maximization."""
    js=sorted(jset)
    k=len(js)
    variances=[]
    for r in range(k):
        lifts=[j+m if i<r else j for i,j in enumerate(js)]
        variances.append(sum(Q(z*z) for z in lifts)-Q(sum(lifts)**2,k))
    return Q(4,m*m)*min(variances)

def formula(m,k):
    return Q(k*(k*k-1),3*m*m)

checks=0
for m in range(2,11):
    for k in range(1,m+1):
        worst=None
        equality_sets=[]
        for js in combinations(range(m),k):
            A=Q(k)-4*exact_max_potential(js,m)
            assert A==closed_mask_bound(js,m),(m,k,js,A,closed_mask_bound(js,m))
            assert A>=formula(m,k), (m,k,js,A,formula(m,k))
            checks+=1
            if worst is None or A<worst:
                worst=A; equality_sets=[js]
            elif A==worst:
                equality_sets.append(js)
            if k>=2:
                assert A>0,(m,k,js,A)
        assert worst==formula(m,k),(m,k,worst)
        assert all(is_cyclic_block(js,m) for js in equality_sets)
        assert len(equality_sets)==(1 if k==m else m),(m,k,equality_sets)
        assert len(equality_sets)==sum(is_cyclic_block(js,m) for js in combinations(range(m),k))
print('EXACT_SUBSET_CHECKS',checks)

# Independent grid evaluations compare directly computed Fourier-modulus symbols.
from random import Random
rng=Random(20261015)
numerical_checks=0
for m in range(2,15):
    for _ in range(100):
        k=rng.randrange(1,m+1)
        js=rng.sample(range(m),k)
        x=rng.random()
        omega=rng.random()
        theta=2*cmath.pi*omega
        from_zak=sum(abs((1-u)+u*cmath.exp(1j*theta))**2 for j in js for u in [(x-j/m)%1])
        from_quadratic=k-2*(1-cmath.cos(theta))*sum(((x-j/m)%1)*(1-((x-j/m)%1)) for j in js)
        assert abs(from_zak-from_quadratic)<1e-11
        numerical_checks+=1
print('NUMERICAL_SYMBOL_CHECKS',numerical_checks)
print('VERIFY_OK')
