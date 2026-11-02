#!/usr/bin/env python3
"""Fully rational proof certificate for qubit information backflow.
Requires Python 3 stdlib and the adjacent backflow_cover.csv.
The CSV is finite proof data, not simulation input.
"""
import csv
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from sys import argv

DEN = 1000000
N = 130
REM = F(5 * 131 * 26**130, 4 * factorial(130))
assert REM < F(1, 10**30)
assert F(26 * 132, 131**2) < F(1,5)

def mul(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]

def sqabs(x): return x[0]**2+x[1]**2

def truncation(r,t):
    # f(r,t) = 1F1(a;1;z), a=i/(r+i), z=-(r+i)t.
    a=(1/(1+r*r),r/(1+r*r)); z=(-r*t,-F(t))
    term=(F(1),F(0)); s=term
    for k in range(1,N):
        fac=(a[0]+k-1,a[1]); term=mul(mul(term,fac),z)
        term=(term[0]/(k*k),term[1]/(k*k))
        s=(s[0]+term[0],s[1]+term[1])
    return s

def certify(rows):
    covered=F(1,5)
    min_half_gap=None
    for i,row in enumerate(rows,1):
        n,t1,t2,u,l=map(int,row)
        q=F(n,DEN); U=F(u,DEN); L=F(l,DEN)
        assert F(1,5)<=q<=F(1,2)
        assert 1<=t1<t2<=23 and L>U>0
        p1=truncation(q,t1);p2=truncation(q,t2)
        assert sqabs(p1)<(U-REM)**2, (i,'early certificate')
        assert sqabs(p2)>(L+REM)**2, (i,'late certificate')
        # Superposition of two Poisson processes couples their trajectories:
        # |f_r(t)-f_q(t)| <= 2*t*|r-q|.
        half_gap=(L-U)/2
        if min_half_gap is None or half_gap<min_half_gap:min_half_gap=half_gap
        radius=(L-U)/(4*(t1+t2))
        lo=q-radius;hi=q+radius
        assert lo<=covered,(i,'gap',float(lo-covered))
        if hi>covered:covered=hi
    assert covered>=F(1,2),('incomplete interval',float(covered))
    assert min_half_gap>F(1,400),('insufficient uniform backflow',min_half_gap)
    return covered,min_half_gap

if __name__=='__main__':
    path=Path(__file__).with_name('backflow_cover.csv')
    with path.open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    expected=['rate_numerator_over_1000000','t_early','t_late','early_upper_over_1000000','late_lower_over_1000000']
    assert list(rows[0])==expected
    data=[[r[k] for k in expected] for r in rows]
    if len(argv)>1 and argv[1]=='--test':data=data[:20]
    result=certify(data) if len(argv)==1 else None
    if len(argv)>1:
        for row in data:
            n,t1,t2,u,l=map(int,row)
            p1=truncation(F(n,DEN),t1);p2=truncation(F(n,DEN),t2)
            assert sqabs(p1)<(F(u,DEN)-REM)**2
            assert sqabs(p2)>(F(l,DEN)+REM)**2
        print(f'PASS: first {len(data)} exact rational local certificates')
    else:
        print(f'PASS: {len(data)} exact rational local certificates cover 0.2 <= r/omega <= 0.5')
        print(f'Final covered endpoint: {float(result[0]):.12f}')
        print(f'Uniform trace-distance increase: > 1/400 = {float(F(1,400))}')
        print('Global Kummer truncation remainder < 1e-30')
