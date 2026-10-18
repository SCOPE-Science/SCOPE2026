"""Exact finite-size checks for leaf-status / total-depth covariances.

Run: python verify.py
Uses only the Python standard library. Enumeration checks do not replace proof.
"""
from fractions import Fraction
from itertools import product
from math import factorial, log, e

checks=0
for n in range(2,10):
    total=0
    sum_p=0
    sum_l=0
    sum_pl=0
    sum_i=[0]*(n+1)
    sum_pi=[0]*(n+1)
    for parents in product(*(range(t-1) for t in range(2,n+1))):
        depths=[0]*(n+1)
        children=[0]*(n+1)
        for t,par0 in enumerate(parents,2):
            par=par0+1
            depths[t]=depths[par]+1
            children[par]+=1
        path=sum(depths)
        indicators=[0,0]+[int(children[j]==0) for j in range(2,n+1)]
        leaf_count=sum(indicators)
        total+=1
        sum_p+=path
        sum_l+=leaf_count
        sum_pl+=path*leaf_count
        for j in range(2,n+1):
            sum_i[j]+=indicators[j]
            sum_pi[j]+=path*indicators[j]
    assert total==factorial(n-1)
    checks+=1
    harmonic=[Fraction(0)]*(n+1)
    for j in range(1,n+1): harmonic[j]=harmonic[j-1]+Fraction(1,j)
    expected_path=n*(harmonic[n]-1)
    assert Fraction(sum_p,total)==expected_path
    checks+=1
    expected_leaf=Fraction(n,2) if n>=2 else Fraction(1)
    assert Fraction(sum_l,total)==expected_leaf
    checks+=1
    expected_cov=Fraction(-(n-2),4)
    actual_cov=Fraction(sum_pl,total)-Fraction(sum_p,total)*Fraction(sum_l,total)
    assert actual_cov==expected_cov,(n,actual_cov,expected_cov)
    checks+=1
    for j in range(2,n+1):
        p_i=Fraction(sum_i[j],total)
        assert p_i==Fraction(j-1,n-1)
        checks+=1
        delta=Fraction(sum_pi[j],sum_i[j])-expected_path
        exact_delta=harmonic[j-1]-harmonic[n-1]
        assert delta==exact_delta,(n,j,delta,exact_delta)
        checks+=1
        cov=Fraction(sum_pi[j],total)-Fraction(sum_p,total)*p_i
        exact_cov=p_i*exact_delta
        assert cov==exact_cov
        checks+=1

# The exact covariance sequence has strictly increasing adjacent differences.
for n in range(3,500):
    N=n-1
    H_N=sum((Fraction(1,k) for k in range(1,N+1)),Fraction(0))
    H=Fraction(0)
    previous=None
    differences=[]
    for k in range(1,N+1):
        H+=Fraction(1,k)
        val=Fraction(k,N)*(H-H_N)
        if previous is not None: differences.append(val-previous)
        previous=val
    assert all(a<b for a,b in zip(differences,differences[1:]))
    checks+=1
for n in (100,1000,10000):
    H=[0.0]
    for k in range(1,n): H.append(H[-1]+1/k)
    values=[k/(n-1)*(H[k]-H[n-1]) for k in range(1,n)]
    jmin=values.index(min(values))+2
    assert abs(jmin/n-1/e)<.025,(n,jmin)
    checks+=1
print(f"PASS: {checks} exact/structural assertions; exhaustive recursive trees through 9 vertices")
