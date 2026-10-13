from fractions import Fraction as F
from math import sqrt

l1, l2, l3, l4 = F(63,100), F(1,5), F(3,20), F(1,50)
assert l1 >= l2 >= l3 >= l4 > 0
assert l1 + l2 + l3 + l4 == 1
assert 2*l2 + l3 < l1

region_A = (2*l3 + l4 - l2 < 0)
region_B = (2*l3 + l4 - l2 >= 0 and l3 <= 2*l4 and l2 > l3 + l4)
region_C = (2*l3 + l4 - l2 >= 0 and l3 > 2*l4 and l2 > F(3,2)*l3)
assert not region_A and not region_B and not region_C

disc = l3*l3 - 4*l2*l4
assert disc > 0
envelope = (1-l1)/2 + F(1,2)*(l3*l3/(4*l2)-l4)
assert envelope == F(121,640)
assert l2 - envelope == F(7,640)
assert l2 > envelope
assert F(25,9) > 2

analytic = 0.5 * float(l3*l3/(4*l2)-l4)
best = -1e100
N = 800
lim = 1/sqrt(2)
for i in range(N+1):
    r = lim*i/N
    for j in range(N+1):
        s = lim*j/N
        h = -float(l2)*r*r - float(l4)*s*s + float(l3)*r*s
        best = max(best, h)
assert abs(best-analytic) < 3e-4, (best, analytic)
print("VERIFY_OK")
