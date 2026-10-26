"""Exact-rational independent column and metric checks for cyclic equilateral extension.
All data are synthetic 3+3 rational metrics. No third-party services required.
"""
from fractions import Fraction as F
from itertools import combinations, product

EXTREMES = [(F(0), F(1), F(1)), (F(0), F(1), F(0)),
            (F(0), F(0), F(-1)), (F(0), F(-1), F(-1)),
            (F(0), F(-1), F(0)), (F(0), F(0), F(1))]

def metric_ok(d, s, L=F(1)):
    if min(d) <= 0 or min(s,L) <= 0: return False
    for i,j in combinations(range(3),2):
        if abs(d[i]-d[j]) > min(L,s) or d[i]+d[j] < max(L,s):
            return False
    return True

def matrix_dist(i,j,d,s,L=F(1)):
    if i == j: return F(0)
    if i < 3 and j < 3: return L
    if i >=3 and j >=3: return s
    if i < 3: i,j=j,i
    return d[(j-(i-3))%3]

def kernel(d,L=F(1)):
    S=sum(d)
    dd=sorted(enumerate(d),key=lambda p:p[1]); indices=[p[0] for p in dd]
    if dd[2][1]<=dd[0][1]+dd[1][1]:
        w=[1-2*r/S for r in d]
        phase='three'
    else:
        w=[F(0)]*3
        i,j=indices[:2]
        w[i]=d[j]/(d[i]+d[j]);w[j]=d[i]/(d[i]+d[j])
        phase='two'
    return w,phase

def check(d,s):
    assert metric_ok(d,s)
    L=F(1)
    w,phase=kernel(d,L)
    assert sum(w)==1 and all(0<=v<=1 for v in w)
    S=sum(d)
    asserted=max(F(1), 2*L/S)
    # Matrix check of all 15 pairs on all six extreme source functions.
    amp=F(0)
    for f in EXTREMES:
        vals=list(f)
        for k in range(3):
            vals.append(sum(w[j]*f[(k+j)%3] for j in range(3)))
        for i,j in combinations(range(6),2):
            value=abs(vals[i]-vals[j])/matrix_dist(i,j,d,s)
            amp=max(amp,value)
            assert value<=asserted,(d,s,phase,w, i,j,value,asserted)
    assert amp==asserted, (d,s,phase,w,amp,asserted)
    # Exact lower-bound certificate via cyclic averaging and the equilateral dual.
    assert sum(F(1)-w[i] for i in range(3))==2
    if asserted>1:
        assert phase=='three' and sum(d[i]*(F(1)-w[i])/d[i] for i in range(3))==2
    return phase

def main():
    cases=set(); phases={'three':0,'two':0}
    for n in range(4,35):
        # select all distinct distance profiles, including asymmetric cyclic data
        v=[F(n,20),F(n+2,20),F(n+5,20)]
        for shift in range(3):
            d=tuple(v[shift:]+v[:shift])
            for q in [F(2,5), F(3,5), F(4,5), F(1),F(7,5)]:
                if metric_ok(d,q): cases.add((d,q))
    for d,s in [((F(1,2),F(1,2),F(1,2)),F(1,2)),
                ((F(1,2),F(3,5),F(13,20)),F(3,5)),
                ((F(51,100),F(51,100),F(11,10)),F(4,5)),
                ((F(1,2),F(1,2),F(1)),F(1)),
                ((F(1,2),F(3,5),F(9,10)),F(1,2)),
                ((F(3,5),F(3,5),F(13,10)),F(4,5))]:
        assert metric_ok(d,s),(d,s)
        cases.add((d,s))
    for d,s in sorted(cases):
        phases[check(d,s)]+=1
    assert phases['three']>0 and phases['two']>0
    print(f'CYCLIC_TRIANGLE_EXACT_OK metrics={len(cases)} full_pairs={len(cases)*15} extreme_pair_checks={len(cases)*90} phases={phases}')

if __name__=='__main__':main()
