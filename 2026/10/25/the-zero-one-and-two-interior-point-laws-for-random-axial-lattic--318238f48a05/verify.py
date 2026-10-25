#!/usr/bin/env python3
"""Self-contained finite cross-check for small-interior axial triangles."""
from fractions import Fraction as F
from math import gcd


def direct_count(a, b, c):
    # Solve bc*x + ac*y + ab*z = abc with x,y,z strictly positive.
    count = 0
    total = a * b * c
    step_x = b * c
    step_y = a * c
    step_z = a * b
    for x in range(1, a):
        for y in range(1, b):
            rem = total - step_x * x - step_y * y
            if rem > 0 and rem % step_z == 0 and rem // step_z < c:
                count += 1
    return count


def classified(g, u, v, w):
    if g == 1 and u == v == 1:
        return 0
    if (g,u,v,w) == (2,1,1,1): return 0
    if (g,u,v,w) in ((3,1,1,1), (2,1,1,2), (1,1,2,3)):
        return 1
    if (g,u,v,w) in ((2,1,1,3), (1,1,2,5)):
        return 2
    return None


def run():
    observed = set()
    for a in range(1, 26):
        for b in range(1, 26):
            for c in range(1, 26):
                g = gcd(a, gcd(b, c))
                A, B, C = gcd(a,b), gcd(b,c), gcd(c,a)
                u, v, w = sorted((A//g,B//g,C//g))
                D = gcd(a*b, gcd(a*c,b*c))
                I2 = D - A - B - C + 2
                assert I2 % 2 == 0
                I = I2 // 2
                assert D == g*g*u*v*w
                assert gcd(u,v) == gcd(v,w) == gcd(w,u) == 1
                assert I == direct_count(a,b,c), (a,b,c,I)
                expected = classified(g,u,v,w)
                assert (I if I <= 2 else None) == expected, (a,b,c,I,expected)
                if I <= 2: observed.add((I,g,u,v,w))
    assert {(0,1,1,1,1),(0,2,1,1,1),
            (1,3,1,1,1),(1,2,1,1,2),(1,1,1,2,3),
            (2,2,1,1,3),(2,1,1,2,5)} <= observed
    def e(p):return 1-F(3,p*p)+F(2,p**3)
    def r(p):return (1-F(1,p))*(F(1,p*p)-F(1,p**4))/e(p)
    for p in (2,3,5):assert r(p) == F(p+1,p*p*(p+2))
    assert r(2)==F(3,16) and r(3)==F(4,45) and r(5)==F(6,175)
    strong = (F(1,2)-F(1,4))*(F(1,16)-F(1,64))/e(2)
    assert strong == F(3,128)
    assert F(1,27)+3*strong+6*r(2)*r(3) == F(3583,17280)
    assert 3*F(1,8)*r(3)+6*r(2)*r(5)==F(151,2100)
    print('checked ordered triple box [1,25]^3:',25**3)
    print('checked exact local ratios and rational density coefficients')
    print('VERIFY_OK')

if __name__ == '__main__': run()
