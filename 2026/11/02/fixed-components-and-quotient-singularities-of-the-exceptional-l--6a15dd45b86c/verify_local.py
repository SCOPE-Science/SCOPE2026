"""Finite exact sanity checks for two affine normal forms.
The general geometric theorem requires the proof in RESULT.md; these tests are not
an exhaustive mathematical proof in unbounded rank or genus.
"""
from itertools import product
from math import comb

# A local matrix T=[[a,b],[c,d]] is sent to tr(T)I-T.
# This check deliberately uses independent adjugate and trace definitions.
count=0
for a,b,c,d in product(range(-2,3), repeat=4):
    S=(d,-b,-c,a)
    aa,bb,cc,dd=S
    SS=(dd,-bb,-cc,aa)
    assert SS==(a,b,c,d)
    assert aa+dd==a+d
    assert aa*dd-bb*cc==a*d-b*c
    assert (S==(a,b,c,d)) == (a==d and b==0 and c==0)
    count += 1
assert count==625

# In centered basis h(t)=A+B*(t-s/2), swapping t -> s-t
# negates the odd coefficient, and its fixed solutions have B=0.
for A,B,s,t in product(range(-3,4),repeat=4):
    lhs=2*A+B*(2*(s-t)-s)
    rhs=2*A-B*(2*t-s)
    assert lhs==rhs
    assert (B==-B)==(B==0)

# For the involution's fixed locus the two components have Euler
# characteristics r*chi(Sym^2 C) and binom(r,2)*chi(C).
for r in range(2,19):
    for g in range(0,12):
        chi=2-2*g
        chi_sym2=chi*(chi+1)//2
        by_strata=r*chi_sym2+comb(r,2)*chi
        compact=r*chi*(chi+r)//2
        assert by_strata==compact
        assert (2*r)-(r+1)==r-1
        assert (2*r)-(1+2*(r-2))==3
print('VERIFY_OK: 625 exact matrix examples; 2401 centered exchanges; Euler and codimension identities')
