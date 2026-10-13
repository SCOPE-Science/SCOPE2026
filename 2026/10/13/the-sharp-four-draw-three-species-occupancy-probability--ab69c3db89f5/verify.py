"""Exact checks for four-draw occupancy; no finite test certifies the universal inequality."""
from fractions import Fraction as F
from itertools import product

def formula(p):
    s2=sum((x*x for x in p),F(0))
    s3=sum((x*x*x for x in p),F(0))
    s4=sum((x*x*x*x for x in p),F(0))
    return 6*(s2-2*s3+2*s4-s2*s2)

def enumerate_four(p):
    ans=F(0)
    for labels in product(range(len(p)),repeat=4):
        if len(set(labels))==3:
            z=F(1)
            for i in labels:
                z*=p[i]
            ans+=z
    return ans

assert formula([F(1,5)]*5)==F(72,125)
assert formula([F(1,4)]*4)==F(9,16)
assert formula([F(1,6)]*6)==F(5,9)
for m in range(1,101):
    val=formula([F(1,m)]*m)
    assert val==F(6*(m-1)*(m-2),m**3)
    assert val<=F(72,125)

count=0
for m in range(1,6):
    for nums in product(range(5),repeat=m):
        if sum(nums)!=4:
            continue
        p=[F(k,4) for k in nums]
        q=formula(p)
        assert q==enumerate_four(p)
        assert q<=F(72,125)
        count+=1
# The two-mass-sum direction is rigorously polynomial; numeric rational instances check the algebra.
checks=0
for others in [[F(1,3)],[F(1,9),F(2,9)],[F(1,10),F(1,10),F(1,5)],[]]:
    s=1-sum(others,F(0))
    t2=sum((x*x for x in others),F(0))
    c=-2+6*s-4*s*s+4*t2
    for k in range(1,10):
        a=s*F(k,10)
        b=s-a
        assert formula([a,b]+others)-formula([s,F(0)]+others)==6*c*a*b
        checks+=1
print(f'VERIFY_OK compositions={count} pair_split={checks} m_uniform=100 max={F(72,125)}')
