#!/usr/bin/env python3
import math
for b in range(-1,20):
    p=3*b+5
    q=8*b+13
    r=24*b+41
    det=q*r
    assert p>=2 and q>=5 and r>=17
    assert math.gcd(p,3)==1 and math.gcd(q,8)==1
    assert math.gcd(q,r)==1
    assert r%3==2
    assert math.isqrt(det)**2 != det
    if b>-1:
        prev=(8*(b-1)+13)*(24*(b-1)+41)
        assert det>prev
print("VERIFY_OK b=-1..19 determinant_growth_and_nonsquare")
