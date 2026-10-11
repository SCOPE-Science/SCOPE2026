#!/usr/bin/env python3
"""Exact finite enumeration certificate for a binary 4x4 square aperture.
Checks all 8192 sign-normalized configurations by two different moment identities.
No third-party dependencies. Use `python3 checker.py`.
"""
from collections import Counter

SHIFTS=[]
for dx in range(4):
    for dy in range(-3,4):
        if dx == 0 and dy <= 0: continue
        mask=sum(1 << (4*i+j) for i in range(4) for j in range(4)
                 if i+dx<4 and 0<=j+dy<4)
        delta=4*dx+dy
        assert delta>0 and mask.bit_count()==(4-dx)*(4-abs(dy))
        SHIFTS.append((delta,mask))
assert len(SHIFTS)==24

def moment_by_correlations(bits):
    val=256
    for shift,src in SHIFTS:
        disagreements=(((bits>>shift)^bits)&src).bit_count()
        c=src.bit_count()-2*disagreements
        val+=2*c*c
    return val

def moment_by_convolution(bits):
    # Parseval: integral |P|^4 = sum of squares of coefficients of P*P.
    coeffs=[1-2*((bits>>(4*i+j))&1) for i in range(4) for j in range(4)]
    square=[0]*49
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    square[7*(i+k)+j+l]+=coeffs[4*i+j]*coeffs[4*k+l]
    return sum(a*a for a in square)

def transform(bits,turns,transpose,sign_x,sign_y,negate):
    new=0
    for i in range(4):
        for j in range(4):
            x,y=i,j
            for _ in range(turns):x,y=y,3-x
            if transpose:x,y=y,x
            s=((bits>>(4*i+j))&1)^((sign_x*x+sign_y*y)&1)^negate
            new |= s<<(4*x+y)
    return new

def orbit(bits):
    return {transform(bits,t,tr,sx,sy,s0)
            for t in range(4) for tr in range(2)
            for sx in range(2) for sy in range(2) for s0 in range(2)}

# Multiplication by global sign and by (-1)^i, (-1)^j is an order-eight
# free symmetry. Each orbit has one representative a00=a01=a10=+1.
fixed=1|2|(1<<4)
hist=Counter();winners=set()
for bits in range(1<<16):
    if bits&fixed:continue
    a=moment_by_correlations(bits)
    b=moment_by_convolution(bits)
    assert a==b,(bits,a,b)
    hist[a]+=1
    if a<=304:
        assert a==304
        winners.add(bits)
assert sum(hist.values())==8192
assert min(hist)==304 and hist[304]==4
assert sorted(winners)==[19336,22976,27148,30788]
assert sorted(hist)[1]==336
assert len(hist)==79
r1,r2=19336,22976
O1,O2=orbit(r1),orbit(r2)
assert len(O1)==len(O2)==16
assert not O1&O2
assert (O1|O2)&{bits for bits in range(1<<16) if bits&fixed==0}==winners
# All 8 sign modulations of each normalized mask are distinct, so these
# two square symmetry orbits account for 8*(4) =32 unrestricted minima.
for m in winners:
    assert len({transform(m,0,0,p,q,s) for p in range(2)
                for q in range(2) for s in range(2)})==8
assert sum(hist.values())*8==65536
print('CHECK_PASS normalized=8192 allstates=65536 min=304 known_merit=16/3')
print('CHECK_PASS normalized_winners=4 total_winners=32 phase_dihedral_orbits=2 orbit_sizes=16,16')
print('CHECK_PASS second=336 moment_levels=79 independent_identities=8192')
