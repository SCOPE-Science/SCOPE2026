"""Standalone reproducible tests for finite-mass complete-graph maximal norms.
Uses Python standard library only; checks do not replace the analytic proof.
"""
from itertools import combinations,product
from fractions import Fraction
from math import sqrt,isclose
from random import Random


def phi(t):
    return (2-t+sqrt(t*(4-3*t)))/2


def subset_formula(weights):
    total=sum(weights)
    values=[]
    n=len(weights)
    for mask in range(1,(1<<n)-1):
        s=sum(w for i,w in enumerate(weights) if mask & (1<<i))
        values.append((phi(s/total),mask,s/total))
    return max(values)


def maximal_ratio_sq(weights, values):
    f=[abs(x) for x in values]
    a=sum(w*x for w,x in zip(weights,f))/sum(weights)
    return sum(w*max(x,a)**2 for w,x in zip(weights,f))/sum(w*x*x for w,x in zip(weights,f))


def top_eigen_ratio(t):
    z=phi(t)
    return (z-(1-t)**2)/(t*(1-t))


def check_exact_special():
    for n in range(2,9):
        weights=[1]*n
        got,mask,t=subset_formula(weights)
        if n%3==0:
            assert isclose(got,4/3,abs_tol=1.e-12)
        if n==2:
            assert isclose(sqrt(got),sqrt(3+sqrt(5))/2,abs_tol=1.e-12)
        for m in range(1,n):
            val=phi(m/n)
            assert val <= got+1e-12
    print('KNOWN_COUNTING_MEASURE_FORMULA_OK')


def check_exact_rational_matrix():
    trials=0
    for denom in range(2,19):
        for numerator in range(1,denom):
            t=Fraction(numerator,denom)
            a=Fraction(1,1)+t*(1-t)
            d=(1-t)**2
            b2=(1-t)**2*t*(1-t)
            tr=a+d
            det=a*d-b2
            assert det==(1-t)**2
            assert tr==2-t
            assert tr*tr-4*det==t*(4-3*t)
            trials+=1
    print('EXACT_RATIONAL_2_BY_2_SPECTRAL_IDENTITY_OK',trials)


def check_numerical_bounds():
    rng=Random(20261031)
    configurations=0
    tests=0
    for n in range(2,8):
        for _ in range(35):
            w=[rng.randint(1,25) for __ in range(n)]
            optimum, mask, t = subset_formula(w)
            ratio=top_eigen_ratio(t)
            y=[ratio if (mask>>j)&1 else 1 for j in range(n)]
            assert ratio>1
            assert isclose(maximal_ratio_sq(w,y), optimum,rel_tol=1e-12,abs_tol=1e-12)
            configurations+=1
            for __ in range(60):
                f=[rng.uniform(-2,5) for j in range(n)]
                assert maximal_ratio_sq(w,f)<=optimum+1e-11
                tests+=1
    print('EQUALITY_EXTREMIZERS_OK',configurations)
    print('RANDOM_INPUT_SHARP_UPPER_ENVELOPES_OK',tests)


def check_subset_sum_reduction():
    rng=Random(24)
    count=0
    for n in range(1,9):
        for _ in range(40):
            A=[rng.randint(1,21) for i in range(n)]
            target=rng.randint(1,sum(A))
            L=2*sum(A)+1
            weights=A+[L-target,2*L-sum(A)+target]
            assert all(x>0 for x in weights)
            assert sum(weights)==3*L
            subset_original=any(sum(A[i] for i in range(n) if mask & (1<<i))==target for mask in range(1<<n))
            subset_new=any(sum(weights[i] for i in range(len(weights)) if mask & (1<<i))==L for mask in range(1<<len(weights)))
            assert subset_original==subset_new
            count+=1
    print('EXACT_INTEGER_SUBSET_SUM_REDUCTION_OK',count)


def check_universal_one_third():
    import math
    for w in [[1,1,1],[1,2,3],[1,3,8],[2,5],[2,3,4],[4,8,12]]:
        z,mask,t=subset_formula(w)
        total=sum(w)
        exists=any(sum(w[i] for i in range(len(w)) if mask>>i&1)*3==total for mask in range(1,(1<<len(w))-1))
        assert (abs(z-4/3)<1e-12)==exists
    print('ONE_THIRD_MASS_RIGIDITY_OK')

if __name__=='__main__':
    check_exact_rational_matrix()
    check_exact_special()
    check_numerical_bounds()
    check_subset_sum_reduction()
    check_universal_one_third()
    print('ALL_WEIGHTED_CLIQUE_MAXIMAL_CHECKS_OK')
