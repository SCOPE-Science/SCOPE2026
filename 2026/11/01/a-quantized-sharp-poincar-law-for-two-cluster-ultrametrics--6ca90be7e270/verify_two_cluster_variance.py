"""Exact and finite independent checks of the two-cluster Lipschitz variance law.

Run: python3 verify_two_cluster_variance.py
Requires Python 3 and SciPy for optional vertex enumeration.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose


def variance(values):
    n = len(values)
    return sum(x*x for x in values) - sum(values)**2 / n


def formula(m, n, t):
    n_total = m+n
    large, small = max(m, n), min(m, n)
    return max(small + k*t*t - (small+k*t)**2/F(n_total)
               for k in range(large+1))


def candidate_forms(m, n, t):
    for a in range(m+1):
        for b in range(n+1):
            yield [F(0)]*(m-a) + [t]*a + [F(1)-t]*b + [F(1)]*(n-b)
            yield [F(1)]*(m-a) + [F(1)-t]*a + [t]*b + [F(0)]*(n-b)


def main():
    exact = 0
    phase = 0
    for m, n in product(range(1, 11), repeat=2):
        for t in [F(1,7),F(1,3),F(1,2),F(2,3),F(4,5),F(1)]:
            pred = formula(m,n,t)
            direct = max(map(variance,candidate_forms(m,n,t)))
            assert direct == pred, (m,n,t,pred,direct)
            large, small = max(m,n), min(m,n)
            N=m+n
            theta = F(N,2) - small/t
            # Exact completed-square identity with integer rounding.
            ks=range(large+1)
            square = F(N)*t*t/F(4)+small*(1-t)-t*t/F(N)*min((F(k)-theta)**2 for k in ks)
            assert square == pred
            exact += 1
            if large>=small+2:
                threshold=F(2*small, N-1)
                if t<=threshold: assert pred == F(large*small,N)
                else: assert pred>F(large*small,N)
            else: assert pred == F(large*small,N)
            phase += 1
    # Equality of adjacent branches, sharp crossing, and derivative jump.
    kinks=0
    for large, small in product(range(2,13),range(1,9)):
        if large<small: continue
        N=large+small
        for k in range(large):
            if 2*k+1 >= large-small: continue
            t=F(2*small,N-2*k-1)
            f=lambda kk, ss: small+kk*ss*ss-(small+kk*ss)**2/F(N)
            assert f(k,t)==f(k+1,t)
            assert f(k,t-F(1,100000))>f(k+1,t-F(1,100000))
            assert f(k,t+F(1,100000))<f(k+1,t+F(1,100000))
            deriv=lambda kk: 2*kk*t-2*(small+kk*t)*kk/F(N)
            assert deriv(k+1)-deriv(k)==F(2*small,N)
            kinks+=1
    print('EXACT_FOUR_LEVEL_VARIANCE_AND_ROUNDING_OK', exact)
    print('EXACT_KINK_AND_DERIVATIVE_JUMP_OK', kinks)
    print('SHARP_IMBALANCE_TRANSITION_OK', phase)

    try:
        import numpy as np
        from scipy.spatial import HalfspaceIntersection
    except ImportError:
        print('SCIPY_OPTIONAL_VERTEX_TEST_SKIPPED')
        return
    checked=0
    for m, n in [(1,2),(1,3),(2,2),(2,3),(2,4),(3,3),(3,4),(2,5),(3,5)]:
        N=m+n
        for t in (F(1,4),F(1,2),F(3,4)):
            d=[]
            for i in range(N):
                row=[]
                for j in range(N):
                    row.append(0 if i==j else (float(t) if (i<m)==(j<m) else 1))
                d.append(row)
            halfspaces=[]
            for i in range(N):
                for j in range(i+1,N):
                    x=np.zeros(N-1)
                    if i: x[i-1]+=1
                    if j: x[j-1]-=1
                    halfspaces.append(np.r_[x, -d[i][j]])
                    halfspaces.append(np.r_[-x,-d[i][j]])
            vert=HalfspaceIntersection(np.asarray(halfspaces),np.zeros(N-1)).intersections
            vals=[]
            for v in vert:
                z=np.r_[0,v]
                vals.append(np.dot(z,z)-z.sum()**2/N)
            true=float(formula(m,n,t))
            assert abs(max(vals)-true)<2e-8,(m,n,t,len(vert),max(vals),true)
            checked += 1
    print('INDEPENDENT_ALL_LIPSCHITZ_POLYTOPE_VERTICES_OK', checked)
    print('ALL_TWO_CLUSTER_LIPSCHITZ_VARIANCE_TESTS_OK')


if __name__=='__main__': main()
