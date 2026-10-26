#!/usr/bin/env python3
"""Exact polynomial verification of [2/2] Pade endpoint map on an eight-state directed cycle.
Run: python3 verify_cycle.py . No third-party packages needed.
"""
from fractions import Fraction

DEN = [2239488,
 8957952,
 17169408,
 20901888,
 18071424,
 11757312,
 5951232,
 2389824,
 769392,
 199584,
 41832,
 7056,
 924,
 84,
 4]
NUMS = [[2239488, 6718464, 9331200, 7838208, 4354560, 1632960, 399168, 58320, 7344, 4536, 3276, 1512, 420, 63, 4],
 [0, 2239488, 6718464, 9331200, 7838208, 4339008, 1586304, 333072, 0, -27864, -11016, -2376, -288, -15],
 [0, 0, 1119744, 3359232, 4665600, 3950208, 2255040, 903312, 254016, 47520, 4644, -180, -108, -9],
 [0, 0, 0, 373248, 1119744, 1524096, 1244160, 675216, 254016, 66528, 11664, 1188, 36, -3],
 [0, 0, 0, 0, 93312, 295488, 404352, 320112, 163296, 55944, 12852, 1872, 144, 3],
 [0, 0, 0, 0, 0, 15552, 62208, 92016, 72576, 34776, 10584, 2016, 216, 9],
 [0, 0, 0, 0, 0, 0, 0, 9072, 18144, 15120, 6804, 1764, 252, 15],
 [0, 0, 0, 0, 0, 0, 0, -1296, 0, 3024, 3024, 1260, 252, 21]]
P1 = [-746496, -2239488, -3110400, -2612736, -1446336, -528768, -111024, 0, 9288, 3672, 792, 96, 5]
P2 = [-62208, -155520, -181440, -128736, -60912, -19728, -4248, -516, 0, 10, 1]
P3 = [-124416, -373248, -508032, -414720, -225072, -84672, -22176, -3888, -396, -12, 1]
P7 = [-432, 0, 1008, 1008, 420, 84, 7]

def trim(a):
    while len(a)>1 and a[-1] == 0: a.pop()
    return a

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return trim(c)

def mul_cyc(m,terms):
    out=[[0] for _ in range(8)]
    for i,a in enumerate(m):
        for j,b in enumerate(terms):
            out[(i+j)%8]=add(out[(i+j)%8],mul(a,b))
    return out

def val(p,t):
    return sum((c*t**i for i,c in enumerate(p)),0)

def transitions(p):
    nonzero=[1 if c>0 else -1 for c in reversed(p) if c]
    return sum(a!=b for a,b in zip(nonzero,nonzero[1:]))

def bisect_root(p,lo,hi,steps=120):
    lo=Fraction(lo);hi=Fraction(hi)
    assert val(p,lo)<0 and val(p,hi)>0
    for _ in range(steps):
        m=(lo+hi)/2
        if val(p,m)>0: hi=m
        else:lo=m
    return float((lo+hi)/2)

# Matrix identity: (12-6h(P-I)+h²(P-I)²)*R = 12+6h(P-I)+h²(P-I)².
# x denotes P (cyclic forward shift) with x^8=1.
M=[[12,6,1],[0,-6,-2],[0,0,1]]
# Expand: 12-6h(x-1)+h²(x-1)²:
# coefficient x^0: 12+6h+h²; x^1:-6h-2h²; x²:h².
N=[[12,-6,1],[0,6,-2],[0,0,1]]
left=mul_cyc(M,NUMS)
right=[mul(DEN,n) if j<3 else [0] for j,n in enumerate(N)]
assert all(trim(a)==trim(b) for a,b in zip(left,right)),"matrix identity failed"
assert add(mul([-3],mul([0,1],P1)),[0])==NUMS[1]
assert mul([-9],mul([0,0,1],mul([2,1],P2)))==NUMS[2]
assert mul([-3],mul([0,0,0,1],P3))==NUMS[3]
assert mul([3],mul([0]*7+[1],P7))==NUMS[7]
for j in (0,4,5,6):assert all(v>=0 for v in NUMS[j]) and any(v>0 for v in NUMS[j])
assert transitions(P1)==transitions(P2)==transitions(P3)==transitions(P7)==1
assert P1[0]<0 and P2[0]<0 and P3[0]<0 and P7[0]<0
assert P1[-1]>0 and P2[-1]>0 and P3[-1]>0 and P7[-1]>0
assert val(P7,0)<0<val(P7,1)
assert val(P1,3)<0<val(P1,4)
assert val(P2,4)<0 and val(P3,4)<0
assert all(c>0 for c in DEN)
print("EXACT_POLYNOMIAL_IDENTITY_OK")
print("DESCARTES_ONE_POSITIVE_ROOT_EACH_OK")
print("EXACT_WINDOW_SIGN_CERTIFICATE_OK")
print("LOWER",format(bisect_root(P7,0,1),'.14f'))
print("UPPER",format(bisect_root(P1,3,4),'.14f'))
