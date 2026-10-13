#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

K = 300
r = F(1,10)
delta = F(1,100)
m = F(1111,1000)
beta = F(3,5)
k = F(1000)
a = F(1,200)
b = F(1,500)
c = F(1,50000)
alpha = F(1)
h = F(10000)
mu = F(2)

def rates(x,y,z):
    x=F(x); y=F(y); z=F(z)
    r1 = r*x*(1-x/F(K))
    r2 = delta*x*y/(m+x)
    r3 = beta*x*y/(k+x) + b*y*z
    r4 = a*y + c*y*y
    r5 = alpha*x*y/(h+x)
    r6 = mu*z
    return (r1,r2,r3,r4,r5,r6)

x,y,z = 3,10,10
selected_product = F(1)
for j in range(y,0,-1):
    rr = rates(x,j,z)
    total = sum(rr)
    assert rr[3] > 0 and total > 0
    q = rr[3]/total
    assert 0 < q <= 1
    selected_product *= q
assert selected_product > 0

for xx in range(x,K):
    rr = rates(xx,0,z)
    assert rr[0] > 0
    assert rr[1] == rr[2] == rr[3] == rr[4] == 0
    total = sum(rr)
    q = rr[0]/total
    assert 0 < q <= 1

getcontext().prec = 60
upper = Decimal(1) - Decimal("0.05") ** (Decimal(1)/Decimal(10000))
target = Decimal("0.00029952835977661200928347133894762364718314969727")
assert abs(upper-target) < Decimal("1e-50")

print("VERIFY_OK")
