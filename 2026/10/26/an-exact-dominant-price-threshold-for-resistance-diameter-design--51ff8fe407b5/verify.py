"""Reproducibility checks for the explicitly priced star resistance-diameter optimum.

Run with Python 3.9+; SymPy and SciPy are optional but used for the independent
matrix-inverse and numerical-convex-optimization checks.
"""
import json
import itertools
import math
import random
from fractions import Fraction


def analytical(prices, budget):
    total = sum(prices)
    j = max(range(len(prices)), key=lambda k: prices[k])
    peak = prices[j]
    rest = total-peak
    if peak <= rest:
        weights = [budget/total] * len(prices)
        return 2*total/budget, weights
    sp, sr = math.sqrt(peak), math.sqrt(rest)
    weights = [budget/(sr*(sp+sr))]*len(prices)
    weights[j] = budget/(sp*(sp+sr))
    return (sp+sr)**2/budget, weights


def diameter(weights):
    reciprocals=[1/w for w in weights]
    return max(reciprocals[i]+reciprocals[j]
               for i in range(len(weights)) for j in range(i+1,len(weights)))


def check():
    rng=random.Random(20261024)
    checked=0
    max_identity_error=0.0
    max_slsqp_gap=0.0
    cases=[]
    for m in range(2,8):
        for trial in range(9):
            prices=[0.1+10**rng.uniform(-1.0,2.0) for _ in range(m)]
            if trial==0:
                prices=[1.0]*m
            if trial==1:
                prices=[m*20.0]+[1.0]*(m-1)
            B=0.4+20*rng.random()
            value, weights=analytical(prices,B)
            assert abs(sum(c*w for c,w in zip(prices,weights))-B)<1e-9*B
            identity=abs(diameter(weights)-value)
            max_identity_error=max(max_identity_error,identity)
            assert identity<=1e-9*(1+value)
            for z in range(150):
                raw=[10**rng.uniform(-2,2) for _ in range(m)]
                scale=B/sum(c*w for c,w in zip(prices,raw))
                competitor=diameter([scale*w for w in raw])
                assert competitor+1e-9*(1+value)>=value
            cases.append((prices,B,value))
            checked+=1
    from scipy.optimize import minimize
    for prices,B,value in cases:
        m=len(prices)
        constraints=[]
        for i in range(m):
            for j in range(i+1,m):
                row=[0.0]*m
                row[i]=-1.0;row[j]=-1.0
                constraints.append((row,-1.0))
        from scipy.optimize import LinearConstraint
        import numpy as np
        A=np.array([row for row,_ in constraints])
        lb=np.full(len(A),-np.inf)
        ub=np.ones(len(A))
        def obj(r):return sum(c/r[i] for i,c in enumerate(prices))
        def jac(r):return np.array([-c/r[i]**2 for i,c in enumerate(prices)])
        result=minimize(obj,[0.5]*m,jac=jac,method='SLSQP',
            constraints=[LinearConstraint(-A,lb,ub)],bounds=[(1e-8,None)]*m,
            options={'maxiter':250,'ftol':1e-10})
        # This objective is the cost at normalized resistance diameter one.
        if result.success:
            rel=abs(result.fun-B*value)/(1+B*value)
            max_slsqp_gap=max(max_slsqp_gap,rel)
            assert rel < 5e-6, (prices,rel,result.message)
    # Independent reduced-Laplacian checks use rational matrices.
    import sympy as S
    rational_tests=[([1,1,1],3),([9,4,4,1],18),([25,4,4,1],34),([49,4,4,1],58)]
    rational_matrix_pairs=0
    for costs,B in rational_tests:
        m=len(costs)
        C=sum(costs)
        if max(costs)<=C-max(costs):
            w=[S.Rational(B,C)]*m
        else:
            k=max(range(m),key=lambda z:costs[z]); a=costs[k];R=C-a
            ss=S.sqrt(a);sr=S.sqrt(R)
            w=[S.Rational(B)/(sr*(ss+sr))]*m
            w[k]=S.Rational(B)/(ss*(ss+sr))
        K=S.diag(*w)
        inverse=K.inv()
        for i in range(m):
            for j in range(i+1,m):
                b=S.zeros(m,1);b[i]=1;b[j]=-1
                e=(b.T*inverse*b)[0]
                assert S.simplify(e-(1/w[i]+1/w[j]))==0
                rational_matrix_pairs+=1
    # Uniform allocation can be arbitrarily close to twice worse.
    big=10**12
    val,ws=analytical([big,1,1,1],big+3)
    ratio=(2*(big+3)/(big+3))/val
    assert 1.99 < ratio < 2.0
    return {'status':'passed','random_allocations_checked':checked*150,
            'independent_normalized_convex_optimizations':checked,
            'exact_reduced_laplacian_resistance_pairs':rational_matrix_pairs,
            'analytical_identity_cases':checked,
            'max_analytical_identity_error':max_identity_error,
            'max_successful_slsqp_relative_gap':max_slsqp_gap,
            'near_two_ratio':ratio,'random_seed':20261024}

if __name__=='__main__':
    print(json.dumps(check(),sort_keys=True,indent=2))
