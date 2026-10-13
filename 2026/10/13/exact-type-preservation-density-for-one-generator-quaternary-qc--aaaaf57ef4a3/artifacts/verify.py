#!/usr/bin/env python3
import itertools, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# Low-degree-first Z4 polynomials.
def z4_mod(a,b):
    a=[x%4 for x in a]
    b=[x%4 for x in b]
    while len(a)>1 and a[-1]==0:
        a.pop()
    while len(a)>=len(b):
        z=a[-1]
        d=len(a)-len(b)
        for j,c in enumerate(b):
            a[d+j]=(a[d+j]-z*c)%4
        while len(a)>1 and a[-1]==0:
            a.pop()
    return a

p1_z4=[3,1]       # x-1
p2_z4=[1,1,1]     # x^2+x+1
g=[3,1,1]         # x^2+x+3
gp=[0,2,2]        # 2x^2+2x

assert z4_mod(g,p1_z4)==[1]
assert z4_mod(g,p2_z4)==[2]
assert z4_mod(gp,p1_z4)==[0]
assert z4_mod(gp,p2_z4)==[2]

# GF(2) polynomial represented as a bit integer.
p1=0b11
p2=0b111
factors=(p1,p2)
degrees=(1,2)

def gf2_mod(a,b):
    while a and a.bit_length()>=b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

elements=list(itertools.product(range(4),repeat=3))
assert len(elements)==64

def mod2_bits(e):
    return sum((c&1)<<i for i,c in enumerate(e))

def unit_at(e, factor):
    return gf2_mod(mod2_bits(e),factor)!=0

def exact_good(tup,active):
    return all(any(unit_at(e,factors[i]) for e in tup) for i in active)

def joint_good(tup):
    return all(any(unit_at(e,f) for e in tup) for f in factors)

def formula(ell,active):
    x=Fraction(4**(3*ell),1)
    for i in active:
        x *= 1-Fraction(1,2**(ell*degrees[i]))
    assert x.denominator==1
    return x.numerator

expected={
    (0,1):{1:24,2:2880,3:225792},
    (1,):{1:48,2:3840,3:258048},
    (0,):{1:32,2:3072,3:229376},
}

for active,table in expected.items():
    for ell in (1,2,3):
        brute=0
        joint=0
        for tup in itertools.product(elements,repeat=ell):
            brute += exact_good(tup,active)
            joint += joint_good(tup)
        assert brute==formula(ell,active)==table[ell]
        assert joint==formula(ell,(0,1))==expected[(0,1)][ell]

for active,key in [((0,1),"both_active"),((1,),"degree2_active"),((0,),"degree1_active")]:
    for ell in (1,2,3):
        assert expected[active][ell]==CERT["m3_checks"][key][str(ell)]

for ell in (1,2,3):
    assert expected[(0,1)][ell]==CERT["m3_checks"]["joint"][str(ell)]

# Source g' has only degree-two active. Check the advertised probabilities.
assert Fraction(expected[(1,)][1],64)==Fraction(3,4)
assert Fraction(expected[(1,)][2],64**2)==Fraction(15,16)
assert Fraction(expected[(1,)][3],64**3)==Fraction(63,64)
assert Fraction(expected[(0,1)][1],64)==Fraction(3,8)
assert Fraction(expected[(0,1)][2],64**2)==Fraction(45,64)
assert Fraction(expected[(0,1)][3],64**3)==Fraction(441,512)

print("VERIFY_OK")
