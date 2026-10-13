from fractions import Fraction as F

# Each pair (r,s) has r^2+s^2=1, so Schur radii are exact rationals.
vals = [
    (F(0), F(1)),
    (F(3,5), F(4,5)), (F(-3,5), F(4,5)),
    (F(4,5), F(3,5)), (F(-4,5), F(3,5)),
    (F(5,13), F(12,13)), (F(-5,13), F(12,13)),
    (F(12,13), F(5,13)), (F(-12,13), F(5,13)),
]
alphas = [F(1,5), F(1,2), F(4,5)]
checked = interior = boundary = 0

for a, sa in vals:
    assert a*a + sa*sa == 1
    for b, sb in vals:
        assert b*b + sb*sb == 1
        s = sa*sb
        for alpha in alphas:
            ab = a*b
            r = (1-alpha)*abs(ab)
            B = 1-alpha*(a*a+b*b)+(alpha*alpha-2*alpha+2)*a*a*b*b
            L = B-2*(1-alpha)*(1-alpha)*a*a*b*b + 2*max(F(0), r-s)**2
            sign = F(0) if ab == 0 else (F(1) if ab > 0 else F(-1))
            d = -sign*min(r,s)
            direct = B + 4*ab*(1-alpha)*d + 2*d*d
            assert direct == L
            assert L <= B + 4*ab*(1-alpha)*s + 2*s*s
            assert L <= B - 4*ab*(1-alpha)*s + 2*s*s
            if r <= s:
                interior += 1
                assert d == -ab*(1-alpha)
                exact_inside = 1-alpha*(a*a+b*b)+alpha*(2-alpha)*a*a*b*b
                assert L == exact_inside
            else:
                boundary += 1
                assert abs(d) == s
            old = (1-a*a)*(1-b*b)
            if a == 0 and b == 0:
                assert L == old
            else:
                assert L > old
            checked += 1

print('VERIFY_OK', checked, interior, boundary)
