"""Exact-rational sanity checks for the analytical local-oracle theorem.

These finite checks are not a proof of any universal statement.
Run: python verify.py
"""
from fractions import Fraction as F

count = 0
for eta in [F(1, 1000), F(1, 100), F(1, 10), F(1, 2), F(1, 1)]:
    for n in [2, 3, 4, 10, 100, 1000]:
        a = F(1, n)
        C = max(F(0), (F(2) / eta - (1 + a*a)) / a)
        # X = {z_2 >= 0}; f = ||z||^2/2 + C*z_2.
        # x=(1,a), y=(2,0), x_star=(0,0).
        R2 = 1 + a*a
        distance_xy2 = 1 + a*a
        Delta = 1 + a*a + C*a
        E = F(2)
        y2 = F(4)
        assert distance_xy2 == R2
        assert C >= 0 and E <= eta*Delta
        assert y2 <= F(2)*E
        assert y2 / R2 <= 4
        count += 1

for eta in [F(i, 100) for i in range(101)]:
    # X = R, f(z)=z^2/2, x=1, x_star=0, y=eta.
    x, y, g = F(1), eta, F(1)
    Delta, E = g*x, g*y
    assert E == eta*Delta and abs(y) == eta*abs(x)
    count += 1

# Generic exact-arithmetic geometry for sample feasible points y in a trust ball.
for p in range(-9, 10):
    for q in range(0, 10):
        x = (F(2), F(3))
        y = (F(p, 4), F(q, 4))
        R2 = sum(t*t for t in x)
        if sum((y[i]-x[i])**2 for i in range(2)) <= R2:
            for C in [F(0), F(1, 3), F(17)]:
                E = (x[0]*y[0] + (x[1]+C)*y[1])
                assert E >= sum(t*t for t in y)/2
                count += 1
print(f'VERIFY_OK {count} exact-rational checks')
