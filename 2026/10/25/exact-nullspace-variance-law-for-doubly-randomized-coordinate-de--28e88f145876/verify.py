"""Exact rational finite-stage checks for a rank-one doubly sampled coordinate update.

Execute: python verify.py.  Tests finite identities; the limiting theorem is analytic.
"""
from fractions import Fraction as F
from itertools import product


def predicted(rows, columns, steps):
    lam = [F(c) ** 2 for c in rows]
    mean = sum(lam) / len(lam)
    mean2 = sum(x*x for x in lam) / len(lam)
    product_q = F(1)
    variability = F(0)
    expected_product = F(1)
    for eta in steps:
        eta = F(eta)
        variability += eta * eta * mean2 * product_q
        product_q *= 1 - 2*eta*mean + eta*eta*mean2
        expected_product *= 1-eta*mean
    mse = product_q / columns + (1 - F(1, columns)) * variability
    residual = sum(lam)*product_q
    return mse, residual, expected_product, product_q, variability


def enumeration(rows, columns, steps):
    rows = [F(c) for c in rows]
    outcomes = [(tuple([F(0)]*columns), F(1))]
    for eta in steps:
        expanded = []
        for x, prob in outcomes:
            p = 1 - sum(x)
            for i, j in product(range(len(rows)), range(columns)):
                y = list(x)
                y[j] += F(eta) * rows[i]*rows[i]*p
                expanded.append((tuple(y), prob/F(len(rows)*columns)))
        outcomes = expanded
    uniform = F(1,columns)
    mse = sum(prob*sum((z-uniform)**2 for z in x) for x,prob in outcomes)
    residual = sum(prob*sum((c*(sum(x)-1))**2 for c in rows) for x,prob in outcomes)
    expected_product = sum(prob*(1-sum(x)) for x,prob in outcomes)
    return mse, residual, expected_product


def run():
    count = 0
    for k in range(7):
        steps = [F(1,8)]*k
        predicted_values = predicted([1,2],2,steps)
        actual = enumeration([1,2],2,steps)
        assert actual == predicted_values[:3], (k,actual,predicted_values[:3])
        q = F(65,128)
        assert predicted_values[0] == F(17,126) + F(23,63)*q**k
        assert predicted_values[1] == 5*q**k
        count+=1
    for rows,columns,steps in [([1,2,3],3,[F(1,40),F(1,50),F(1,70)]),
                               ([1,2,3],4,[F(1,40),F(1,60)]),
                               ([1,3],3,[F(1,60),F(1,50),F(1,45)])]:
        assert enumeration(rows,columns,steps)==predicted(rows,columns,steps)[:3]
        count+=1
    for rows,columns,steps in [([1,2],2,[F(1,8)]),([1,2],2,[F(1,8),F(1,16)])]:
        mse,resid,p,q,v = predicted(rows,columns,steps)
        assert mse > F(1,2) * steps[0]**2 * F(17,2)
        count+=1
    print('EXACT_RATIONAL_CHECKS_PASS', count)
    print('TWO_BY_TWO_Q', F(65,128), 'ASYMPTOTIC_MSE_FLOOR', F(17,126))

if __name__ == '__main__':
    run()
