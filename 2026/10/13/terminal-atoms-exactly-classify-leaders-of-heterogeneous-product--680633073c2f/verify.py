#!/usr/bin/env python3
"""Exact finite-law replay for sample-leader inequalities; no infinite certification."""
from fractions import Fraction
from itertools import product
from math import comb

X = [(0, Fraction(1,2)), (1, Fraction(1,3)), (2, Fraction(1,6))]
Y = [(0, Fraction(2,3)), (2, Fraction(1,3))]
rows = [((x,y),px*py) for (x,px),(y,py) in product(X,Y)]
p_top = Fraction(1,6)*Fraction(1,3)
q = Fraction(1,6)  # X > 1
checked=0
for n in range(1,5):
    a=Fraction(0)
    for sample in product(rows,repeat=n):
        values = [r[0] for r in sample]
        w=Fraction(1)
        for _,pr in sample: w*=pr
        leaders = any(all(u[0]<=v[0] and u[1]<=v[1] for u in values) for v in values)
        if leaders:a+=w
    # By a top-vector occurrence and by a selected X-maximum with top Y,
    # both valid but structurally distinct lower bounds.
    assert a >= 1-(1-p_top)**n
    assert a >= Fraction(1,3)
    gy = (Fraction(2,3)**n)+Fraction(1,3)
    upper=(1-q)**n+n*q*gy
    assert a<=upper
    checked+=1

# Exact identity for an atomless first coordinate and Bernoulli(p) second:
# argmax of the first coordinate is uniform and independent of Bernoulli labels.
p=Fraction(2,7)
for n in range(1,20):
    # The probability that the selected max-X label is a global Y-max:
    # either its label is one (p), or all n labels are zero ((1-p)^n).
    sharp=p+(1-p)**n
    # Independent binomial expansion of the all-zero event.
    by_counts=sum(Fraction(comb(n,k))*p**k*(1-p)**(n-k)*(
        Fraction(1) if k==0 else Fraction(k,n)) for k in range(n+1))
    assert sharp==by_counts
    assert p <= sharp <=p+(1-p)**n

# Higher-dimensional top-vector witness.
pa,pb,pc=Fraction(1,2),Fraction(1,4),Fraction(3,5)
prod=pa*pb*pc
for n in range(1,12):
    assert 1-(1-prod)**n>=prod

print(f"VERIFY_OK exact_finite_rows={checked} sharp_bernoulli_limit={p} all_top_product={prod}")
