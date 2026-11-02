#!/usr/bin/env python3
"""Exact rational checks for two-leader coherence on weighted friendship graphs."""
from fractions import Fraction as Q
from itertools import combinations


def graph_laplacian(m, t):
    n = 2*m+1
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(m):
        p, q = 2*i+1, 2*i+2
        for u,v,c in ((0,p,Q(1)), (0,q,Q(1)), (p,q,t)):
            a[u][u] += c
            a[v][v] += c
            a[u][v] -= c
            a[v][u] -= c
    return a


def trace_inverse(a, leaders):
    keep = [i for i in range(len(a)) if i not in leaders]
    n = len(keep)
    z = [[a[keep[i]][keep[j]] for j in range(n)] +
         [Q(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        piv = next(i for i in range(k,n) if z[i][k] != 0)
        if piv != k:
            z[k],z[piv] = z[piv],z[k]
        p = z[k][k]
        for j in range(k,2*n): z[k][j] /= p
        for i in range(n):
            if i == k: continue
            coeff=z[i][k]
            if coeff:
                for j in range(k,2*n):
                    z[i][j] -= coeff*z[k][j]
    return sum((z[i][n+i] for i in range(n)),Q(0))


def predicted(m,t):
    A=1/(1+t)+(m-1)*(1+1/(1+2*t))
    B=A+(2*m*t+2*m-t-3)/(2*(1+t))
    C=A+(2*m*t+2*m-7*t-3)/(2*(1+2*t))
    return A,B,C


def orbit(m, pair):
    u,v=pair
    if 0 in pair: return 0
    if (u-1)//2 == (v-1)//2: return 1
    return 2


def expected_orbits(m,t):
    if m == 2:
        if t<Q(1,3): return {0}
        if t==Q(1,3):return {0,2}
        return {2}
    if m==3:
        if t<3:return {0}
        if t==3:return {0,2}
        return {2}
    return {0}


def main():
    counts={'matrices':0,'complete_classifications':0,'boundary_ties':0,'extra_orbit_checks':0}
    ts=[Q(1,7),Q(1,3),Q(1),Q(3),Q(7)]
    for m in range(2,8):
        for t in ts:
            a=graph_laplacian(m,t)
            formulas=predicted(m,t)
            byorbit=[]
            for leaders in combinations(range(2*m+1),2):
                actual=trace_inverse(a,leaders)
                assert actual==formulas[orbit(m,leaders)],(m,t,leaders,actual)
                byorbit.append((actual,orbit(m,leaders)))
                counts['matrices']+=1
            optimum=min(x for x,_ in byorbit)
            attained={k for x,k in byorbit if x==optimum}
            assert attained==expected_orbits(m,t),(m,t,attained)
            counts['complete_classifications']+=1
            if len(attained)==2:counts['boundary_ties']+=1
    for m in range(2,12):
        for t in (Q(1,13),Q(5,2),Q(37,3)):
            a=graph_laplacian(m,t)
            A,B,C=predicted(m,t)
            for leaders, val in (({0,1},A),({1,2},B),({1,3},C)):
                assert trace_inverse(a,leaders)==val
                counts['extra_orbit_checks']+=1
    print('PASS: exact rational independent grounded matrix inversions')
    for k,v in counts.items():print(f'{k}: {v}')
    print('PASS: sharp m=2 threshold 1/3 and m=3 threshold 3; no m>=4 transition')


if __name__=='__main__': main()
