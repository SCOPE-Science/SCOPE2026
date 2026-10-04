from fractions import Fraction
from decimal import Decimal, getcontext

def det(K, q):
    q = Fraction(q)
    return Fraction(1) - q * (q - 1) / Fraction(K - 1)

for K in range(2, 25):
    for q in range(0, 10):
        assert (det(K, q) > 0) == (q * (q - 1) < K - 1)

for p in range(2, 12):
    first = p * (p - 1) + 2
    assert det(first, p) > 0
    assert det(first - 1, p) == 0

assert det(2, 2) < 0
assert det(3, 2) == 0
assert det(4, 2) > 0

getcontext().prec = 60
phi = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)
assert abs(phi * (phi - 1) - Decimal(1)) < Decimal('1e-55')

for total in range(2, 80):
    vals=[]
    for n0 in range(1,total):
        n1=total-n0
        m=min(Fraction(n0,n1),Fraction(n1,n0))
        vals.append((m,n0,n1))
    best=max(v[0] for v in vals)
    assert best <= 1
    if total % 2 == 0:
        maximizers=[(a,b) for m,a,b in vals if m==best]
        assert maximizers == [(total//2,total//2)]
        assert best == 1

print('VERIFY_OK')
