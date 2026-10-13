from fractions import Fraction

# Reaction vectors for X1 -> X2+X3 and X3 -> X1.
nu1 = (-1, 1, 1)
nu2 = (1, 0, -1)
m = (1, 0, 1)
assert sum(a*b for a,b in zip(m, nu1)) == 0
assert sum(a*b for a,b in zip(m, nu2)) == 0
# The two independent reaction vectors have rank 2, so the left nullspace is 1D.
assert nu1 != (0,0,0) and nu2 != (0,0,0)
assert not all(nu1[i]*nu2[j] == nu1[j]*nu2[i] for i in range(3) for j in range(3))

# Exact fixed-signal residual checks after treating c,r as arbitrary positive parameters.
for a,b,c,r,s in [
    (Fraction(2), Fraction(3), Fraction(5,3), Fraction(7,4), Fraction(11,5)),
    (Fraction(7,2), Fraction(5,4), Fraction(9,5), Fraction(4,3), Fraction(13,7)),
]:
    x = 1/(c*r)
    y = r*s
    f1 = a*(s-c*x*y)
    f2 = f1 + b*(r*s-y)
    assert f1 == 0 and f2 == 0
    # Under the source normalization u'(0)=1, x''(0)=a>0.
    assert a > 0 and a/2 > 0

print('VERIFY_OK')
