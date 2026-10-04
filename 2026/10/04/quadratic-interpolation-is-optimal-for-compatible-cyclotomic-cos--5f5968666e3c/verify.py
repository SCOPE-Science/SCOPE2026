from fractions import Fraction as Q

# Affine coefficient vectors in coordinates (c, a1, a2).
b2 = (Q(1), Q(-1), Q(0))
b3 = (Q(1), Q(-1,2), Q(-1,2))
b4 = (Q(1), Q(0), Q(-1))
assert tuple(2*b3[i]-b2[i]-b4[i] for i in range(3)) == (Q(0),Q(0),Q(0))

# Converse reconstruction on an exact finite grid.
converse = 0
for B2 in range(-8,9):
    for B4 in range(-8,9):
        B2, B4 = Q(B2), Q(B4)
        B3 = (B2+B4)/2
        c=Q(0); a1=-B2; a2=-B4
        got2=c-a1
        got3=c-(a1+a2)/2
        got4=c-a2
        assert (got2,got3,got4)==(B2,B3,B4)
        converse += 1

# Explicit obstruction.
assert 2*Q(1) != Q(0)+Q(0)

# Source's degree-two exceptional-level correction, checked exactly.
# F1=b2.  F2=b2+c*x2+d*x2*(x2+1/2), with c=-2(b3-b2).
# At level 3, x2=-1/2, so the quadratic correction vanishes.
# At level 4, x2=-1, so choose d to fit b4.
quad_cases=0
for B2 in range(-4,5):
    for B3 in range(-4,5):
        for B4 in range(-4,5):
            B2,B3,B4=Q(B2),Q(B3),Q(B4)
            c=-2*(B3-B2)
            base4=B2-c
            d=2*(B4-base4)
            val3=B2+c*Q(-1,2)+d*Q(-1,2)*(Q(-1,2)+Q(1,2))
            val4=B2+c*Q(-1)+d*Q(-1)*(Q(-1)+Q(1,2))
            assert val3==B3
            assert val4==B4
            quad_cases += 1

print(f"VERIFY_OK affine_relation=exact converse_cases={converse} quadratic_low_level_cases={quad_cases} obstruction=(0,1,0)")
