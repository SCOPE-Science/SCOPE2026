#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import ceil

def comps_pos(total,k,prefix=()):
    if k==1:
        if total>=1: yield prefix+(total,)
        return
    for x in range(1,total-k+2):
        yield from comps_pos(total-x,k-1,prefix+(x,))

def jefferson(weights,h):
    qs=[]
    for i,w in enumerate(weights):
        for d in range(1,h+2):
            qs.append((Fraction(w,d),i,d))
    qs.sort(key=lambda z:z[0], reverse=True)
    if qs[h-1][0] == qs[h][0]:
        return None
    a=[0]*len(weights)
    for _,i,_ in qs[:h]: a[i]+=1
    return tuple(a)

def divisor_check(weights,a):
    lows=[Fraction(w, ai+1) for w,ai in zip(weights,a)]
    highs=[Fraction(w, ai) for w,ai in zip(weights,a) if ai>0]
    lo=max(lows); hi=min(highs)
    if not lo < hi: return False
    d=(lo+hi)/2
    return tuple(w*d.denominator//d.numerator for w in weights)==a

def uq(weights,h,i):
    P=sum(weights)
    q=Fraction(h*weights[i],P)
    return (q.numerator + q.denominator-1)//q.denominator

def violation(weights,h):
    a=jefferson(weights,h)
    if a is None: return None
    assert divisor_check(weights,a)
    return tuple(i for i,x in enumerate(a) if x>uq(weights,h,i))

# Safe boundary finite consistency sweeps.
for P in range(2,31):
    for w in comps_pos(P,2):
        for h in range(1,11):
            v=violation(w,h)
            assert v in (None,()), (w,h,v,jefferson(w,h))

for P in range(3,31):
    for w in comps_pos(P,3):
        v=violation(w,2)
        assert v in (None,()), (w,v,jefferson(w,2))

# Exact chamber checks on all integer profiles in wide windows.
bad33=[]
for P in range(3,31):
    for w in comps_pos(P,3):
        a=jefferson(w,3)
        if a is None: continue
        v=violation(w,3)
        pred=[]
        for i,A in enumerate(w):
            others=[w[j] for j in range(3) if j!=i]
            if 5*A>3*P and 3*A<=2*P and all(3*b<A for b in others):
                pred.append(i)
        assert tuple(pred)==v, (w,a,v,pred)
        if v: bad33.append((w,a,v))

bad42=[]
for P in range(4,31):
    for w in comps_pos(P,4):
        a=jefferson(w,2)
        if a is None: continue
        v=violation(w,2)
        pred=[]
        for i,A in enumerate(w):
            others=[w[j] for j in range(4) if j!=i]
            if 5*A>2*P and 2*A<=P and all(2*b<A for b in others):
                pred.append(i)
        assert tuple(pred)==v, (w,a,v,pred)
        if v: bad42.append((w,a,v))

# Minimal integer witnesses.
minP33=min(sum(w) for w,_,_ in bad33)
min33=sorted({tuple(sorted(w,reverse=True)) for w,_,_ in bad33 if sum(w)==minP33})
assert minP33==6 and min33==[(4,1,1)]
minP42=min(sum(w) for w,_,_ in bad42)
min42=sorted({tuple(sorted(w,reverse=True)) for w,_,_ in bad42 if sum(w)==minP42})
assert minP42==6 and min42==[(3,1,1,1)]

# Exact simplex probabilities, derived analytically.
# 3 states, fixed dominant state: density 2, width 5x/3-1, x in [3/5,2/3].
def F3(x): return Fraction(5,6)*x*x-x
fixed3 = 2*(F3(Fraction(2,3))-F3(Fraction(3,5)))
assert fixed3==Fraction(1,135)
prob3=3*fixed3
assert prob3==Fraction(1,45)

# 4 states, fixed dominant state: integrand (3/4)(5x-2)^2, x in [2/5,1/2].
def F4(x):
    return Fraction(25,4)*x**3 - Fraction(15,2)*x**2 + 3*x
fixed4=F4(Fraction(1,2))-F4(Fraction(2,5))
assert fixed4==Fraction(1,160)
prob4=4*fixed4
assert prob4==Fraction(1,40)

# Direct witnesses and quotas.
assert jefferson((4,1,1),3)==(3,0,0)
assert uq((4,1,1),3,0)==2
assert jefferson((3,1,1,1),2)==(2,0,0,0)
assert uq((3,1,1,1),2,0)==1

print("VERIFY_OK")
print("safe_two_entities_P_le_30_h_le_10", True)
print("safe_three_entities_two_seats_P_le_30", True)
print("three_by_three_chamber_grid_P_le_30", True)
print("four_by_two_chamber_grid_P_le_30", True)
print("minimal_integer_witness_3_entities_3_seats", (4,1,1))
print("minimal_integer_witness_4_entities_2_seats", (3,1,1,1))
print("uniform_simplex_probability_3_entities_3_seats", "1/45")
print("uniform_simplex_probability_4_entities_2_seats", "1/40")
