"""Independent finite checks of a closed-form planar lattice discrepancy theorem.
This script tests instances only; it is not a proof of the all-parameter claim.
"""
from fractions import Fraction

def direct(b, k):
    assert b >= 3 and b % 2 and k > (b + 1)//2
    area = Fraction((k-(b+1)//2)**2, 4*b)
    count = sum((k-b*y)//2 for y in range(1,k//b+1))
    return area-count

def formula(b,k):
    q,r=divmod(k,b)
    t=Fraction((2*r-b-1)**2,16*b)
    if q % 2:
        t += Fraction(1,4) if r%2 else -Fraction(1,4)
    return t

def low(b):
    return -Fraction(1,4) if b%4==3 else -Fraction(b-1,4*b)

def high(b):
    return Fraction((b+1)**2,16*b)

for b in range(3,122,2):
    for k in range((b+1)//2+1, 7*b+1):
        a=direct(b,k)
        assert a==formula(b,k),(b,k,a,formula(b,k))
        assert low(b)<=a<=high(b),(b,k,a)
        q,r=divmod(k,b)
        assert (a<0)==(q%2==1 and r%2==0 and (2*r-b-1)**2<4*b),(b,k,a)
    residues=[formula(b,k) for k in range(2*b,4*b)]
    assert min(residues)==low(b),(b,min(residues),low(b))
    assert max(residues)==high(b),(b,max(residues),high(b))
    qodd_min=[r for r in range(b) if formula(b,b+r)==low(b)]
    c=(b+1)//2
    assert qodd_min==([c] if b%4==3 else [c-1,c+1]),(b,qodd_min)
    assert [r for r in range(b) if formula(b,2*b+r)==high(b)]==[0]
    assert [r for r in range(b) if formula(b,b+r)==high(b)]==[1]
print('PASS: b=3..121 odd; direct count, area, 2b periodic profile, extrema, equality residues, and sign window.')
