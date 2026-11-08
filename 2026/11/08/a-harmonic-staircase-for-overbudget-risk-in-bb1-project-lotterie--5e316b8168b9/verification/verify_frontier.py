"""Exact construction and independent finite LP tests for a budget-overrun risk frontier.

Usage: python verify_frontier.py
Requires Python 3 standard library; optional SciPy adds independent LP checks.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil


def ceil_frac(x):
    return -((-x.numerator)//x.denominator)


def model(k, c, q, delta):
    assert k >= 2 and F(1) < c < k and F(0) <= q <= 1 and delta >= 0
    if q == 0:
        return F(0), {(False, tuple(range(k))): F(1)}
    t = ceil_frac(c)
    if c.denominator == 1:
        omitted = t
        return F(0), cyclic_lottery(k, q, {t: q})
    f = c - (t-1)
    if delta < f:
        return None, None
    ell = max(0, ceil_frac(c-delta))
    assert 0 <= ell < t <= k
    risk = q * (t-c) / (t-ell)
    return risk, cyclic_lottery(k, q, {ell: risk, t: q-risk})


def cyclic_lottery(k, q, masses):
    result = {(False, tuple(range(k))): F(1)-q}
    for z, mass in masses.items():
        for shift in range(k):
            omitted = {(shift + j) % k for j in range(z)}
            included = tuple(i for i in range(k) if i not in omitted)
            key = (True, included)
            result[key] = result.get(key, F(0)) + mass / k
    return {a:p for a,p in result.items() if p}


def bb1(k, c, contains_special, selected):
    cost = F(len(selected)) + (c if contains_special else 0)
    if cost <= k:
        if (contains_special and len(selected) < k and cost+1 >= k):
            return True
        if (not contains_special and cost+c >= k):
            return True
        if len(selected) < k and cost+1 >= k:
            return True
        return cost == k and (contains_special or len(selected)>0)
    return (contains_special and len(selected)<=k) or (len(selected)>0 and cost-1<=k)


def check_case(k, c, q, delta):
    predicted, lottery = model(k,c,q,delta)
    if lottery is None:
        return
    assert sum(lottery.values(),F(0)) == 1
    assert sum(p for (s,_),p in lottery.items() if s) == q
    for i in range(k):
        assert sum(p for (_,a),p in lottery.items() if i in a) == 1-c*q/k
    assert sum(p*(len(a)+(c if s else 0)) for (s,a),p in lottery.items()) == k
    objective = F(0)
    for (s,a),p in lottery.items():
        cost = F(len(a))+(c if s else 0)
        assert cost <= k+delta
        assert bb1(k,c,s,a)
        if cost>k:
            objective+=p
    assert objective==predicted


def lp_case(k,c,q,delta):
    import numpy as np
    from scipy.optimize import linprog
    states=[]; costs=[]
    for bits in product((0,1),repeat=k+1):
        s=bool(bits[k]); a=tuple(i for i in range(k) if bits[i]); cost=F(len(a))+(c if s else 0)
        if cost <= k+delta and bb1(k,c,s,a):
            states.append(bits)
            costs.append(1 if cost>k else 0)
    A=[[1]*len(states)] + [[x[j] for x in states] for j in range(k+1)]
    b=[1] + [float(1-c*q/k)]*k + [float(q)]
    opt=linprog(costs,A_eq=np.array(A),b_eq=np.array(b),bounds=(0,None),method='highs')
    expected,_=model(k,c,q,delta)
    if expected is None:
        assert not opt.success, (k,c,q,delta,opt)
    else:
        assert opt.success and abs(opt.fun-float(expected))<1e-7, (k,c,q,delta,opt.fun,expected,opt.message)


def main():
    tested=0;lp_tested=0
    try:
        import scipy
        lp_available=True
    except ImportError:
        lp_available=False
    for k in range(2,7):
        vals = {F(j)+f for j in range(1,k) for f in (F(0),F(1,4),F(1,2),F(3,4)) if F(1)<F(j)+f<k}
        for c in sorted(vals):
            for q in (F(0),F(1,4),F(3,5),F(1)):
                thresholds = {F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(2),F(3),F(4),F(5),c}
                thresholds |= {max(F(0),c-j) for j in range(k+1)}
                for delta in sorted(thresholds):
                    check_case(k,c,q,delta)
                    tested +=1
                    if lp_available and q !=0 and lp_tested < 420 and k<=5:
                        lp_case(k,c,q,delta)
                        lp_tested+=1
    print(f'PASS: {tested} exact-fraction construction checks and {lp_tested} independent full-distribution LP comparisons.')


if __name__=='__main__':
    main()
