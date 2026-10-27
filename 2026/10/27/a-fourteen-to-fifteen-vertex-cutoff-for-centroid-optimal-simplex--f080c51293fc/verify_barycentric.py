#!/usr/bin/env python3
"""Exact rational proof certificate: barycentric subdivision Lipschitz cutoff.

No dependencies beyond the Python standard library. This program exhausts
all symmetric pairs of nonempty faces of regular (n-1)-simplices, 3<=n<=14.
The comparisons use exact fractions and squared Euclidean distances.
"""
from fractions import Fraction as Q

D = 10000000
A_NUMERATORS = {3: [4742166], 4: [4179577, 3232233], 5: [3872218, 2893806, 2450807], 6: [3682499, 2683912, 2231777, 1972506], 7: [3554785, 2542033, 2083485, 1820535, 1649780], 8: [3463344, 2440096, 1976796, 1711122, 1538597, 1417468], 9: [3394819, 2363482, 1896520, 1628745, 1454856, 1332770, 1242314], 10: [3341641, 2303878, 1834006, 1564563, 1389591, 1266744, 1175725, 1105573], 11: [3296761, 2253770, 1781531, 1510731, 1334877, 1211411, 1119933, 1049428, 993419], 12: [3255410, 2208082, 1733880, 1461954, 1285368, 1161389, 1069531, 998733, 942491, 896733], 13: [3220911, 2169928, 1694070, 1421195, 1243993, 1119581, 1027403, 956357, 899919, 854001, 815911], 14: [3189320, 2135214, 1657942, 1384256, 1206527, 1081746, 989294, 918036, 861431, 815376, 777173, 744971]}


def coefficient(n, k, in_face):
    if k == 1:
        return Q(int(in_face))
    if k == n:
        return Q(1, n)
    a = Q(A_NUMERATORS[n][k-2], D)
    return a if in_face else (1-k*a)/(n-k)


def verify():
    total = 0
    tight = 0
    min_positive = None
    for n in range(3,15):
        unit_sq = Q(2*(n-1),n)
        for k in range(2,n):
            a=coefficient(n,k,True)
            b=coefficient(n,k,False)
            assert Q(0) <= a <= 1 and Q(0) <= b <= 1
            assert k*a+(n-k)*b==1
        cnt=0
        for k in range(1,n+1):
            for l in range(k,n+1):
                for t in range(max(0,k+l-n),min(k,l)+1):
                    if k==l==t:continue
                    # Number of indices in the four intersections of the two subsets
                    blocks = ((t,True,True),(k-t,True,False),
                              (l-t,False,True),(n-k-l+t,False,False))
                    l1 = sum(m*abs(coefficient(n,k,i)-coefficient(n,l,j))
                             for m,i,j in blocks)
                    kr = l1/2
                    dist_sq = Q(k+l-2*t,2*k*l)
                    slack = unit_sq*dist_sq-kr*kr
                    assert slack >= 0, (n,k,l,t,slack)
                    if slack == 0:
                        tight+=1
                    elif min_positive is None or slack<min_positive:
                        min_positive=slack
                    cnt+=1
        total+=cnt
        print('n=%d nonidentical pair orbits=%d exact PASS' % (n,cnt))
    assert Q(1,1)-Q(7,14) < Q(49,96)
    assert Q(1,1)-Q(7,15) > Q(49,96)
    print('exact PASS: %d orbit inequalities, %d tight, n=14/15 rational threshold'% (total,tight))
    print('smallest strictly positive squared slack:',float(min_positive))

if __name__=='__main__':
    verify()
