#!/usr/bin/env python3
"""Exact finite diagnostic for a periodic three-tap STFT counterexample.

The all-dimension assertion is proved algebraically in RESULT.md;
these integer tests check representative dimensions and indexing conventions.
"""
from fractions import Fraction

def corr(block):
    # A window segment's Fourier intensity is the Laurent polynomial of
    # its exact autocorrelation coefficients (difference in [-2, 2]).
    return {shift: sum(block[j+shift]*block[j] for j in range(3-shift))
            for shift in range(3)}

def graph_connected(sites,d):
    unseen=set(sites)
    queue=[next(iter(unseen))]
    unseen.remove(queue[0])
    while queue:
        a=queue.pop()
        for b in list(unseen):
            dist=min((a-b)%d,(b-a)%d)
            if dist <=2:
                queue.append(b)
                unseen.remove(b)
    return not unseen

count=0
for d in (6,9,12,15,18,21):
    a,b=Fraction(2),Fraction(3)
    f=[(a,b,Fraction(0))[j%3] for j in range(d)]
    h=[(b,a,Fraction(0))[j%3] for j in range(d)]
    assert f != h
    assert any(x==0 for x in f)
    assert graph_connected({j for j,x in enumerate(f) if x},d)
    for t in range(d):
        F=[f[(t+j)%d] for j in range(3)]
        H=[h[(t+j)%d] for j in range(3)]
        # For real inputs negative-lag coefficients are the reflections.
        assert corr(F)==corr(H), (d,t,F,H)
        count+=1
# Roots of x^2-13x+36 are 4 and 9, exhibiting two magnitude orders.
assert Fraction(4)+Fraction(9)==13
assert Fraction(4)*Fraction(9)==36
print(f'THREE_TAP_PERIODIC_FIBER_PASS exact_window_rows={count} dimensions=6')
