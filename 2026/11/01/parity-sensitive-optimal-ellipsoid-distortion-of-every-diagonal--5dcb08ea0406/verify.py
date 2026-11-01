"""Reproducible finite tests of the exact diagonal-cube-section ellipsoid theorem.

Requires Python 3, NumPy and SciPy. Exact rational calculations check
vertices, contact radii and covariance; linear programming independently
checks the complete vertex list. Numerical samples are not infinite proofs.
"""
from fractions import Fraction as Q
from itertools import combinations
import random
import numpy as np
from scipy.optimize import linprog

checks = 0

def require(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def all_vertices(n, s):
    """Enumerate active intersections of n-1 coordinate hyperplanes."""
    found = set()
    for free in range(n):
        other = [i for i in range(n) if i != free]
        for k in range(n):
            for ones in combinations(other, k):
                rem = s - k
                if Q(0) <= rem <= Q(1):
                    v = [Q(0)] * n
                    for j in ones:
                        v[j] = Q(1)
                    v[free] = rem
                    found.add(tuple(v))
    return sorted(found)

def analytic_r2(n,s):
    return min(s,n-s)**2/Q(n*(n-1))

def analytic_R2(n,s):
    k = int(s)
    return Q(k)+(s-k)**2-s*s/Q(n)

def verify():
    rng = random.Random(720231)
    for n in range(3, 11):
        ss={Q(j, 5) for j in range(1,5*n)}
        ss.update({Q(k) for k in range(1,n)})
        ss.update({Q(2*k+1,2) for k in range(n) if Q(2*k+1,2)<n})
        ss.update({Q(n,2),Q(1,17),Q(n)-Q(1,17)})
        ss.update({Q(n*j, 31) for j in range(1,31)})
        for s in sorted(x for x in ss if 0<x<n):
            vlist=all_vertices(n,s)
            require(bool(vlist),'nonempty sections have vertices')
            c=s/Q(n)
            require(all(sum(v)==s and all(0<=a<=1 for a in v) for v in vlist),'feasible vertices')
            require(all(sum((v[i]-c)**2 for i in range(n))==analytic_R2(n,s) for v in vlist),'circumradius')
            require(all(sum(v[i] for v in vlist)/len(vlist)==c for i in range(n)),'centroid')
            for i,j in [(0,0),(0,1),(n-1,n-1)]:
                covariance=sum((v[i]-c)*(v[j]-c) for v in vlist)/len(vlist)
                target=analytic_R2(n,s)*(Q(int(i==j))-Q(1,n))/Q(n-1)
                require(covariance==target,'Loewner isotropic contact covariance')
            if s<=Q(n,2):
                touch=[Q(0)]+[s/Q(n-1)]*(n-1)
            else:
                touch=[Q(1)]+[(s-Q(1))/Q(n-1)]*(n-1)
            require(0<=min(touch) and max(touch)<=1,'John contact feasibility')
            require(sum((x-c)**2 for x in touch)==analytic_r2(n,s),'John contact radius')
            obj=np.array([rng.uniform(-3,3) for _ in range(n)])
            lp=linprog(-obj, A_eq=np.ones((1,n)),b_eq=np.array([float(s)]), bounds=[(0,1)]*n, method='highs')
            require(lp.success,'independent linear program succeeded')
            support=max(np.dot(obj,[float(x) for x in v]) for v in vlist)
            require(abs(support+lp.fun)<2e-8,'LP support agrees with vertex enumeration')
            require(analytic_R2(n,s)==analytic_R2(n,n-s),'reflection symmetry of R')
        center=Q(n,2)
        minimum=analytic_R2(n,center)/analytic_r2(n,center)
        parity=Q(n-1) if n%2==0 else Q((n-1)**2,n)
        require(minimum==parity,'sharp parity law')
        for j in range(1,400):
            s=Q(n*j,400)
            require(analytic_R2(n,s)/analytic_r2(n,s)>=minimum,'global sharp bound')
        for s in [Q(1,10),Q(1,2),Q(3,4)]:
            require(analytic_R2(n,s)/analytic_r2(n,s)==Q((n-1)**2),'simplex plateau')
        # Exact derivative test: for k<s<k+1, the sign of
        # d[(R^2)/(s^2)]/ds is the sign of k*(s-k-1).
        for k in range(1,n):
            s=Q(2*k+1,2)
            if s<Q(n,2):
                require(Q(k)*(s-k-1)<0,'strict derivative for left half')
    print('VERIFY_OK',checks,'exact and independent numerical checks')

if __name__=='__main__':
    verify()
