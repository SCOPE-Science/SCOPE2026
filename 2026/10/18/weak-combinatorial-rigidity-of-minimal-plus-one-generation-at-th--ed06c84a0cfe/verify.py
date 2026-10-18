#!/usr/bin/env python3
"""Exact integer consistency checks of sharp conic-arrangement syzygy bounds.

The quoted inequalities and minimal-plus-one characterization are mathematical
theorems; this program verifies their finite applications, not those theorems.
"""
from fractions import Fraction
from math import ceil


def bounds(d, r):
    lower = (d - 1) * (d - r - 1)
    upper = lower + r*r
    if 2*r + 1 > d:
        upper -= (2*r + 1 - d)*(2*r + 2 - d)//2
    return lower, upper


for k in (2, 3, 4):
    d = 2*k
    nodes, tacnodes = 2, k*(k-1)-1
    tau = nodes + 3*tacnodes
    assert nodes + 2*tacnodes == 4*(k*(k-1)//2)
    ds_lower = ceil(Fraction(3*d, 4)-2)
    candidates = [r for r in range(1, d)
                  if r >= ds_lower and bounds(d,r)[0] <= tau <= bounds(d,r)[1]]
    assert candidates == [k], (k, candidates)
    assert k*k-k*(d-1)+(d-1)**2 == tau+2
    print(f'k={k}; nodes={nodes}; tacnodes={tacnodes}; tau={tau}; '
          f'Dimca-Sernesi_min_r={ds_lower}; admissible_mdr={candidates}; '
          f'du_Plessis_Wall_r=k+1_upper={bounds(d,k+1)[1]}; '
          f'exponents=({k},{k},{k+1})')
print('VERIFY_OK')
