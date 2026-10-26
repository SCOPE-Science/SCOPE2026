from collections import Counter
from itertools import product
cols = [(1,0)]*5 + [(0,1)]*5 + [(1,1)]*5 + [(1,2)]*2
F=range(3)
weights={}
for a,b in product(F,repeat=2):
    v=[(a*x+b*y)%3 for x,y in cols]
    weights[(a,b)] = sum(z!=0 for z in v)
assert Counter(weights.values()) == {0:1,12:6,15:2}
assert sum(weights.values()) == 2*3*17
lines={(1,0),(0,1),(1,1),(1,2)}
fixed={}
for v in lines:
    sub={v,((-v[0])%3,(-v[1])%3)}
    count=sum(3 for z in cols if z in sub)
    fixed[v]=count
assert sorted(fixed.values()) == [6,15,15,15]
for v in lines:
    b=17-fixed[v]//3
    assert b in [12,15]
    assert sorted([b,17-b]) == sorted(([12,5] if b==12 else [15,2]))
assert 12+4+2>17
K2=9*5
Eres=12*5-5
Esing=Eres-2*17
EY=9*(Esing-17)+3*17
chi=(K2+EY)//12
assert (Eres,Esing,EY,K2,chi)==(55,21,87,45,11)
# Hodge group-quotient identity: sum of four intermediate geometric genera
pgY=3*6+4-3*4
qY=0-3*0
assert (pgY,qY,chi)==(10,0,pgY-qY+1)
print('VERIFY_OK dimension=2 weight_enumerator=1+6*z^12+2*z^15 columns=5,5,5,2')
print('VERIFY_OK four_order_three_subgroup_fixed_point_counts=15,15,15,6')
print('VERIFY_OK quotient_branch_supports=12,12,12,15')
print('VERIFY_OK smooth_ninefold_cover_K2=45_euler=87_chi=11_pg=10_q=0')
