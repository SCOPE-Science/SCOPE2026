"""Standalone checks for fixed-label partial-permutohedron volume asymptotics.

All measurements use ordinary coordinate Euclidean volume; normalized volume
is m! times coordinate volume. Finite checks do not prove the asymptotic claim.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad


def volume_pair_cap_formula(m, n):
    S = n*(n+1)//2
    B = S-(2*n-1)
    return (m-B)*B**(m-1)+(B-1)**m


def volume_pair_cap_integral(m, n):
    S = n*(n+1)//2
    B = S-(2*n-1)
    fun = lambda t: (1-t)*(B-t)**(m-2)
    return m*(m-1)*quad(fun, 0, 1, epsabs=1e-12)[0]


def partial_permutohedron_vertices(m, n):
    pts = [tuple(0 for _ in range(m))]
    for k in range(1, min(m,n)+1):
        for coords in itertools.combinations(range(m), k):
            for labels in itertools.permutations(range(n-k+1,n+1),k):
                x=[0]*m
                for i,a in zip(coords,labels): x[i]=a
                pts.append(tuple(x))
    return np.array(pts, dtype=float)


def contains_facets(x, n):
    m=len(x); S=n*(n+1)//2
    if min(x)<-1e-9 or sum(x)>S+1e-9: return False
    for k in range(1,min(m,n-1)+1):
        threshold=k*(2*n-k+1)/2
        if sum(sorted(x,reverse=True)[:k])>threshold+1e-9:return False
    return True


def tests():
    passed=0
    for n in range(3,9):
        for m in range(2,13):
            exact=volume_pair_cap_formula(m,n)
            numeric=volume_pair_cap_integral(m,n)
            assert abs(exact-numeric)<1e-8*max(1,abs(exact)),(n,m,exact,numeric)
            assert exact>0
            passed+=1
    print('pair-defect analytic-vs-quadrature checks:',passed)
    passed=0
    for m in (2,3,4):
        for n in (2,3,4,5):
            pts=partial_permutohedron_vertices(m,n)
            assert all(contains_facets(v,n) for v in pts)
            v=ConvexHull(pts).volume*math.factorial(m)
            if n==2: expected=3**m-m
            elif n==3: expected=6**m-m*3**m-(m-1)*math.comb(m,2)
            elif n==4: expected=10**m-m*6**m-m*(m-1)*(m-3)*3**m/6-(3*m*m-6*m+1)*math.comb(m,3)
            else: expected=None
            if expected is not None:
                assert abs(v-expected)<1e-6*max(1,expected),(m,n,v,expected)
            print('hull',m,n,'vertices',len(pts),'normal_vol',round(v,6), 'published',expected)
            passed+=1
    print('convex-hull + facet tests:',passed)
    for n in (5,6,7):
        S=n*(n+1)//2; A=S-n; B=S-(2*n-1)
        print('n,S,A,B:',n,S,A,B)
        for m in (20,40,100):
            cap=m*(A/S)**m
            pair=math.comb(m,2)*((m-B)*B**(m-1)+(B-1)**m)/S**m
            print('m,leading loss,second scale:',m,cap,pair)
    print('CHECKER PASS')

if __name__=='__main__': tests()
