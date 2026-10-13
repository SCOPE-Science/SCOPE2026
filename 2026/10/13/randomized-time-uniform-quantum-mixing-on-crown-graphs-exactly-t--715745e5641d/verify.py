#!/usr/bin/env python3
"""Exact orbit-table verification for random-time mixing on crown graphs.

This script does not replace the general pointwise inequality in the proof.
"""
from fractions import Fraction as F
from math import pi,cos,sin

def probs(n,c,d,s,e):
    return (((n-1)*c+d)**2/n**2, (d-c)**2/n**2,
            (e-(n-1)*s)**2/n**2, (e+s)**2/n**2)

# Exact values at 0, pi/3, 2pi/3, pi when n=3.
# The sine inputs are rational coefficients of h=sqrt(3)/2;
# the final squared probabilities are rational since h*h=3/4.
trig_values = [
 (F(1),F(1),F(0),F(0)),
 (F(1,2),F(-1,2),F(1),F(1)),
 (F(-1,2),F(-1,2),F(1),F(-1)),
 (F(-1),F(1),F(0),F(0)),
]
def exact_n3_orbits(c,d,s_coeff,e_coeff):
    return (((2*c+d)**2)/9,((d-c)**2)/9,
            ((e_coeff-2*s_coeff)**2)*F(3,4)/9,
            ((e_coeff+s_coeff)**2)*F(3,4)/9)
time_orbits=[exact_n3_orbits(*values) for values in trig_values]
expected_orbits = [
 (F(1),F(0),F(0),F(0)),
 (F(1,36),F(1,9),F(1,12),F(1,3)),
 (F(1,4),F(0),F(3,4),F(0)),
 (F(1,9),F(4,9),F(0),F(0)),
]
assert time_orbits==expected_orbits
weights=(F(1,12),F(1,2),F(1,6),F(1,4))
assert sum(weights)==1
assert all(sum(w*row[j] for w,row in zip(weights,time_orbits))==F(1,6) for j in range(4))
assert all(row[0]+2*row[1]+row[2]+2*row[3]==1 for row in time_orbits)
# n=4, t=pi/4: all of c,s,e are 1/sqrt(2), and d=-1/sqrt(2).
# Their squares therefore produce exact 1/8 probabilities.
for coef in ((3-1),(-1-1),(1-3),(1+1)):
    assert F(coef*coef,2*4*4)==F(1,8)
# The pointwise obstruction: 1/n > 4/n^2 at all n >= 5.
assert all(F(1,n)>F(4,n*n) for n in range(5,200))
# Optional independent numerical matrix exponential evaluation.
tested=0
try:
    import numpy as np
    from scipy.linalg import expm
    for n in (3,4,5,9):
        B=np.ones((n,n))-np.eye(n)
        A=np.block([[np.zeros_like(B),B],[B,np.zeros_like(B)]])
        for t in [0,pi/3,2*pi/3,pi,pi/4,0.7231,1.375]:
            observed=np.abs(expm(1j*t*A))**2
            c,d,s,e=cos(t),cos((n-1)*t),sin(t),sin((n-1)*t)
            p0,p1,p2,p3=probs(n,c,d,s,e)
            expected=np.block([[p1*np.ones_like(B)+(p0-p1)*np.eye(n),
                                p3*np.ones_like(B)+(p2-p3)*np.eye(n)],
                               [p3*np.ones_like(B)+(p2-p3)*np.eye(n),
                                p1*np.ones_like(B)+(p0-p1)*np.eye(n)]])
            assert np.max(np.abs(observed-expected))<1e-12
            assert p1+p3<=4/(n*n)+1e-13
            tested+=1
except ImportError:
    pass
print(f'VERIFY_OK exact_four_time_rows=4 exact_weighted_orbits=4 '+
      f'exact_n4_orbits=4 optional_full_matrix_trials={tested}')
