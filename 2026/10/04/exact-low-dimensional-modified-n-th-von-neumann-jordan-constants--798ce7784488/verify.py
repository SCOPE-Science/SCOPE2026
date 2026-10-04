from fractions import Fraction
from math import comb
from itertools import product

def a(n):
    if n == 0:
        return Fraction(0)
    direct = sum(Fraction(comb(n,j) * abs(n-2*j), 2**n) for j in range(n+1))
    closed = Fraction(n * comb(n-1,(n-1)//2), 2**(n-1))
    assert direct == closed
    return direct

def formula(n):
    vals=[a(k)*a(n-k) for k in range(n+1)]
    return Fraction(1)+Fraction(2,n)*max(vals)

def piecewise(n):
    r=n//2
    if n%2:
        return Fraction(1)+Fraction(2,n)*a(r)*a(r+1)
    if r%2:
        return Fraction(1)+Fraction(1,r)*a(r)*a(r)
    return Fraction(1)+Fraction(1,r)*a(r)*a(r+1)

def vertex_value(sigmas):
    n=len(sigmas)
    total=0
    for signs in product((-1,1), repeat=n):
        s=sum(signs)
        t=sum(si*ri for si,ri in zip(sigmas,signs))
        total += max(s*s,t*t)
    return Fraction(total, n*(2**n))

for n in range(2,13):
    assert formula(n)==piecewise(n)
    if n<=8:
        brute=max(vertex_value(sig) for sig in product((-1,1), repeat=n))
        assert brute==formula(n), (n,brute,formula(n))
expected={2:Fraction(2),3:Fraction(5,3),4:Fraction(7,4),5:Fraction(8,5),6:Fraction(7,4),7:Fraction(23,14),8:Fraction(109,64)}
for n,v in expected.items(): assert formula(n)==v
print('VERIFY_OK')
