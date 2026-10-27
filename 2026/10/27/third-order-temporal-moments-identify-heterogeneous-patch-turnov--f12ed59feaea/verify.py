"""Exact finite illustrations for aggregate binary occupancy identification.

Run with Python 3.9+ standard library. Independent direct-state computations
check covariance and third cumulant identities, and a rational Prony inverse.
"""
from fractions import Fraction as F
from itertools import product
import json


def solve(matrix, rhs):
    n=len(rhs)
    a=[list(map(F,row))+[F(rhs[i])] for i,row in enumerate(matrix)]
    for col in range(n):
        pivot=next((r for r in range(col,n) if a[r][col]),None)
        assert pivot is not None
        a[col],a[pivot]=a[pivot],a[col]
        v=a[col][col]
        a[col]=[w/v for w in a[col]]
        for r in range(n):
            if r!=col:
                v=a[r][col]
                a[r]=[a[r][i]-v*a[col][i] for i in range(n+1)]
    return [a[i][-1] for i in range(n)]


def model_data(ps,zs):
    assert len(ps)==len(zs)
    assert len(set(zs))==len(zs)
    assert all(0<p<1 for p in ps)
    assert all(0<z<1 for z in zs)
    c=[p*(1-p) for p in ps]
    d=[c[i]*(1-2*ps[i]) for i in range(len(ps))]
    return c,d


def predicted(ps,zs,j):
    c,d=model_data(ps,zs)
    return sum((c[i]*zs[i]**j for i in range(len(c))),F(0)),sum((d[i]*zs[i]**(2*j) for i in range(len(d))),F(0))


def prob_transition(p,z,j,x,y):
    prob1=p+z**j*(x-p)
    return prob1 if y else 1-prob1


def direct_moments(ps,zs,j):
    n=len(ps)
    states=list(product((0,1),repeat=n))
    mu=sum(ps,F(0))
    stationary={x:__import__('math').prod(ps[i] if x[i] else 1-ps[i] for i in range(n)) for x in states}
    def edge(x,y):
        return __import__('math').prod(prob_transition(ps[i],zs[i],j,x[i],y[i]) for i in range(n))
    cov=sum((stationary[x]*edge(x,y)*(sum(x)-mu)*(sum(y)-mu)
             for x in states for y in states),F(0))
    thirds=sum((stationary[x]*edge(x,y)*edge(y,z)
                *(sum(x)-mu)*(sum(y)-mu)*(sum(z)-mu)
                for x in states for y in states for z in states),F(0))
    return cov,thirds


def reconstruct(ps,zs):
    n=len(ps)
    cs=[predicted(ps,zs,j)[0] for j in range(2*n)]
    ks=[predicted(ps,zs,j)[1] for j in range(n)]
    hankel=[[cs[i+j] for j in range(n)] for i in range(n)]
    annihilator=solve(hankel,[-cs[i+n] for i in range(n)])
    assert all(sum(annihilator[k]*z**k for k in range(n))+z**n==0 for z in zs)
    recovered_c=solve([[z**j for z in zs] for j in range(n)],cs[:n])
    recovered_d=solve([[z**(2*j) for z in zs] for j in range(n)],ks)
    recovered_p=[(1-recovered_d[i]/recovered_c[i])/2 for i in range(n)]
    assert recovered_p==ps
    return {'n':n,'covariance_lags':2*n,'third_cumulant_lags':n,
            'annihilator_low_to_high':[str(v) for v in annihilator]+['1'],
            'recovered_z':[str(v) for v in zs],
            'recovered_stationary_occupancies':[str(v) for v in recovered_p]}


def main():
    examples=[([F(1,4),F(3,4)],[F(1,2),F(1,3)]),
              ([F(1,5),F(2,5),F(3,4)],[F(1,2),F(1,3),F(1,4)])]
    checked=0
    for ps,zs in examples:
        for j in range(6):
            assert direct_moments(ps,zs,j)==predicted(ps,zs,j)
            checked+=1
    a=[F(1,4),F(3,4)]
    b=[F(3,4),F(1,4)]
    z=[F(1,2),F(1,3)]
    assert sum(a)==sum(b)
    assert model_data(a,z)[0]==model_data(b,z)[0]
    assert predicted(a,z,1)[1]==F(5,384)
    assert predicted(b,z,1)[1]==-F(5,384)
    assert all(predicted(a,z,j)[0]==predicted(b,z,j)[0] for j in range(8))
    report={'format':'exact_rational_verification_v1',
            'independent_joint_state_checks':checked,
            'two_patch_same_mean':'1',
            'two_patch_same_covariance_coefficients':[str(v) for v in model_data(a,z)[0]],
            'two_patch_distinct_third_cumulant_at_equal_lag_one':[str(predicted(a,z,1)[1]),str(predicted(b,z,1)[1])],
            'illustrative_inversions':[reconstruct(*item) for item in examples]}
    print(json.dumps(report,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
