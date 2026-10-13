#!/usr/bin/env python3
"""Exact finite sanity checks for weighted-star observability identities.
The accompanying proof, not this finite program, establishes the all-order statement.
"""
from fractions import Fraction
from itertools import combinations


def matmul(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def det(matrix):
    a = [[Fraction(z) for z in row] for row in matrix]
    n = len(a)
    sign = 1
    output = Fraction(1)
    for i in range(n):
        j = next((j for j in range(i,n) if a[j][i]), None)
        if j is None:
            return Fraction(0)
        if j != i:
            a[i],a[j] = a[j],a[i]
            sign *= -1
        pivot = a[i][i]
        output *= pivot
        for j in range(i+1,n):
            if a[j][i]:
                t = a[j][i]/pivot
                for k in range(i+1,n):
                    a[j][k] -= t*a[i][k]
                a[j][i] = 0
    return sign*output


def determinants(ws):
    n=len(ws)+1
    lap = [[Fraction(0) for j in range(n)] for i in range(n)]
    for i,w in enumerate(ws,1):
        w=Fraction(w)
        lap[0][0]+=w
        lap[0][i]=-w
        lap[i][0]=-w
        lap[i][i]=w
    cur = [[int(i==j) for j in range(n)] for i in range(n)]
    pows = []
    for k in range(n):
        pows.append(cur)
        cur=matmul(cur,lap)
    return [det([pows[k][j] for k in range(n)]) for j in range(n)]


def scores(ws):
    ws=list(map(Fraction,ws))
    return [ws[j]**(len(ws)-1)/abs(__import__('math').prod(ws[j]-ws[k] for k in range(len(ws)) if k!=j)) for j in range(len(ws))]


def check(ws):
    ds=determinants(ws)
    ws=list(map(Fraction,ws))
    base=__import__('math').prod(ws)
    vander=__import__('math').prod(ws[i]-ws[j] for i in range(len(ws)) for j in range(i+1,len(ws)))
    assert abs(ds[0])==abs(base*vander), (ws,ds[0])
    for j in range(len(ws)):
        z=base*ws[j]**(len(ws)-1)
        z*=__import__('math').prod(ws[a]-ws[b] for a in range(len(ws)) for b in range(a+1,len(ws)) if a!=j and b!=j)
        assert abs(ds[j+1])==abs(z), (ws,j,ds)
    if len(set(ws))==len(ws):
        scr=scores(ws)
        for j in range(len(ws)):
            assert ds[j+1]**2*scr[0]**2==ds[1]**2*scr[j]**2,ws
        assert scr[1]>scr[0] if len(ws)>=2 else True
        assert max(scr)>1


def main():
    count=0
    cases=[]
    for m in range(2,7):
        cases += list(combinations(range(1,9),m))
    cases += [(1,1),(1,1,2),(1,2,2),(1,1,2,3),(1,1,2,2),(1,1,1),(2,2,2,2),(1,2,2,3,4),(1,2,3,3,4)]
    for ws in cases:
        check(ws)
        count+=1
    # Every nonminimum rank is attainable as the unique best sensor.
    for m in range(2,10):
        for rank in range(2,m+1):
            ws=[Fraction(k,100*m) for k in range(1,rank-1)]
            ws += [Fraction(1), Fraction(10**30+1,10**30)]
            ws += [Fraction(10+3*k) for k in range(1,m-rank+1)]
            assert len(ws)==m
            scr=scores(ws)
            assert scr.index(max(scr))==rank-1,(m,rank,ws,scr)
    print('VERIFY_OK',count,'exact star Krylov identities, including repeated weights; 36 rank-realisability constructions')

if __name__ == '__main__': main()
