#!/usr/bin/env python3
from fractions import Fraction

def mean(xs):
    return Fraction(sum(xs), len(xs))

def variance(xs):
    m=mean(xs)
    return sum((Fraction(x)-m)**2 for x in xs)/len(xs)

def downside_variance_all(xs, target=0):
    return sum(min(Fraction(x)-target, Fraction(0))**2 for x in xs)/len(xs)

def downside_variance_negative_only(xs, target=0):
    neg=[Fraction(x)-target for x in xs if Fraction(x)<target]
    assert neg
    return sum(x*x for x in neg)/len(neg)

def sharpe_sq(xs):
    m=mean(xs)
    assert m>0
    v=variance(xs)
    assert v>0
    return m*m/v

def sortino_sq_all(xs):
    m=mean(xs)
    assert m>0
    d=downside_variance_all(xs)
    assert d>0
    return m*m/d

def sortino_sq_negative_only(xs):
    m=mean(xs)
    assert m>0
    d=downside_variance_negative_only(xs)
    assert d>0
    return m*m/d

# Two equally likely outcomes: finite positive-mean downside risk forces (-a,b)
# with a>0 and b>a. Both ratios are strictly increasing in r=b/a.
for a in range(1,101):
    for b in range(a+1,201):
        xs=(-a,b)
        r=Fraction(b,a)
        assert sharpe_sq(xs) == ((r-1)/(r+1))**2
        assert sortino_sq_all(xs) == (r-1)**2/Fraction(2)
        assert sortino_sq_negative_only(xs) == (r-1)**2/Fraction(4)

# Strict monotonicity on a dense finite rational test set is only a replay of
# the algebraic formulas above, not the proof.
pairs=[]
for a in range(1,31):
    for b in range(a+1,61):
        r=Fraction(b,a)
        pairs.append((r, sharpe_sq((-a,b)), sortino_sq_all((-a,b))))
pairs=sorted(set(pairs))
for i in range(len(pairs)-1):
    if pairs[i][0] < pairs[i+1][0]:
        assert pairs[i][1] < pairs[i+1][1]
        assert pairs[i][2] < pairs[i+1][2]

A=(-1,1,9)
B=(-2,5,6)
assert mean(A)==mean(B)==3
assert variance(A)==Fraction(56,3)
assert variance(B)==Fraction(38,3)
assert sharpe_sq(A)==Fraction(27,56)
assert sharpe_sq(B)==Fraction(27,38)
assert sharpe_sq(A)<sharpe_sq(B)
assert downside_variance_all(A)==Fraction(1,3)
assert downside_variance_all(B)==Fraction(4,3)
assert sortino_sq_all(A)==27
assert sortino_sq_all(B)==Fraction(27,4)
assert sortino_sq_all(A)>sortino_sq_all(B)
assert sortino_sq_negative_only(A)==9
assert sortino_sq_negative_only(B)==Fraction(9,4)
assert sortino_sq_negative_only(A)>sortino_sq_negative_only(B)

# Persistent equal-mean family obtained by padding both samples with their
# common mean 3. This proves a reversal for every sample length n>=3.
for n in range(3,501):
    An=A+(3,)*(n-3)
    Bn=B+(3,)*(n-3)
    assert mean(An)==mean(Bn)==3
    assert variance(An)==Fraction(56,n)
    assert variance(Bn)==Fraction(38,n)
    assert downside_variance_all(An)==Fraction(1,n)
    assert downside_variance_all(Bn)==Fraction(4,n)
    assert sharpe_sq(An)==Fraction(9*n,56)
    assert sharpe_sq(Bn)==Fraction(9*n,38)
    assert sortino_sq_all(An)==9*n
    assert sortino_sq_all(Bn)==Fraction(9*n,4)
    assert sharpe_sq(An)<sharpe_sq(Bn)
    assert sortino_sq_all(An)>sortino_sq_all(Bn)
    # Negative-only downside convention has the same ordering for the family.
    assert sortino_sq_negative_only(An)==9
    assert sortino_sq_negative_only(Bn)==Fraction(9,4)

print("VERIFY_OK")
print("two_outcome_monotone_formula_checked")
print("A_mean_variance_sharpe2_sortino2", mean(A), variance(A), sharpe_sq(A), sortino_sq_all(A))
print("B_mean_variance_sharpe2_sortino2", mean(B), variance(B), sharpe_sq(B), sortino_sq_all(B))
print("negative_only_sortino2", sortino_sq_negative_only(A), sortino_sq_negative_only(B))
print("persistent_family_checked_n_3_to_500")
