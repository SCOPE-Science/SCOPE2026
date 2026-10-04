from fractions import Fraction as F


def soft1(y):
    if y > 1:
        return y - 1
    if y < -1:
        return y + 1
    return F(0)


def clip1(y):
    if y > 1:
        return F(1)
    if y < -1:
        return F(-1)
    return y


def hstar(y, lam):
    s = soft1(y)
    return s*s/(2*lam)


def source_printed(y, lam):
    s = soft1(y)
    r = clip1(y)
    return y*y/(2*lam) - abs(s)/lam + r*r/(2*lam)


def primal_objective_at_maximizer(y, lam):
    x = soft1(y)/lam
    return y*x - abs(x) - lam*x*x/2

for lam in [F(1,7), F(1,1), F(5,2), F(9,1)]:
    for y in [F(-4),F(-2),F(-1),F(-1,2),F(0),F(1,2),F(1),F(2),F(4)]:
        # x = soft_1(y)/lam satisfies the scalar optimality condition exactly.
        x = soft1(y)/lam
        if x > 0:
            assert y - 1 - lam*x == 0
        elif x < 0:
            assert y + 1 - lam*x == 0
        else:
            assert -1 <= y <= 1
        assert primal_objective_at_maximizer(y,lam) == hstar(y,lam)
        assert source_printed(y,lam) - hstar(y,lam) == clip1(y)**2/lam

# Exact witness for the printed expression: at lambda=1,y=2 it is 3/2, but the conjugate is 1/2.
assert source_printed(F(2),F(1)) == F(3,2)
assert hstar(F(2),F(1)) == F(1,2)

# One-sided derivative test at y=1 for the printed scalar expression:
# inside (-1,1): g(y)=y^2/lam, so g'_-(1)=2/lam;
# outside (1,infinity): g(y)=(y-1)^2/(2lam)+1/lam, so g'_+(1)=0.
for lam in [F(1,7),F(1),F(5,2),F(9)]:
    left = F(2,1)/lam
    right = F(0)
    assert left > right

print('VERIFY_OK')
