#!/usr/bin/env python3
"""Reproduce finite-residue checks for 2-adic paperfolding triple correlations.
All arrays are exact integers; the unknown zero residue has bounded contribution.
"""
from fractions import Fraction
from itertools import combinations

def v2(z):
    assert z
    z=abs(z)
    return (z & -z).bit_length()-1

def chi4(odd):
    assert odd & 1
    return 1 if odd % 4 == 1 else -1

def paperfolding(n):
    assert n != 0
    return chi4(n >> v2(n))

def pair_prediction(h):
    t=v2(h)
    return Fraction(0) if t==0 else Fraction(1)-Fraction(3,2**t)

def triple_prediction(a,b,c):
    assert len({a,b,c})==3
    times=(a,b,c)
    m=min(v2(x-y) for x,y in combinations(times,2))
    close=[(i,j) for i,j in combinations(range(3),2) if v2(times[i]-times[j])>m]
    assert len(close)==1,(times,close)
    i,j=close[0];k=3-i-j
    delta=(times[j]-times[i])>>m
    odd=(times[k]-times[i])>>m
    assert not (delta&1) and odd&1
    t=v2(delta)
    if t==1: v=Fraction(0)
    elif t==2: v=Fraction(1,4)
    else: v=-Fraction(3,2**t)
    return Fraction(1,2**m)*chi4(odd)*v

def test():
    K=13;M=1<<K
    F=[0]+[paperfolding(n) for n in range(1,M)]
    offsets=list(range(-19,20))
    checks=0
    for a,b in combinations(offsets,2):
        if a==0 or b==0:continue
        predicted=triple_prediction(0,a,b)
        # use exact numerator and avoid float approximation. At most three terms
        # of the uniform 2-adic sample are undefined at this precision.
        tot=sum(F[x]*F[(x+a)%M]*F[(x+b)%M] for x in range(M))
        assert abs(Fraction(tot,M)-predicted)<=Fraction(3,M),(a,b,tot,predicted)
        checks+=1
    for h in range(-32,33):
        if h==0: continue
        tot=sum(F[x]*F[(x+h)%M] for x in range(M))
        assert abs(Fraction(tot,M)-pair_prediction(h))<=Fraction(2,M),h
        checks+=1
    assert triple_prediction(0,1,4)==Fraction(1,4)
    assert triple_prediction(0,3,4)==Fraction(-1,4)
    # The (+++) cylinder (0,1,4) is 3/16, and its reversal is 1/8.
    assert (Fraction(1)+pair_prediction(4)+triple_prediction(0,1,4))/8==Fraction(3,16)
    assert (Fraction(1)+pair_prediction(4)+triple_prediction(0,3,4))/8==Fraction(1,8)
    print(f'VERIFY_OK: {checks} exact residue comparisons with rigorous error, two exact cylinders')

if __name__=='__main__':test()
