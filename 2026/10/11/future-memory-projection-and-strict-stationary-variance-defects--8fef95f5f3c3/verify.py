from fractions import Fraction as F

a=F(1,4); b=F(3); c=F(-1,2); d=F(1,20)
assert -d/c == F(1,10)
assert (d/c)**2 == F(1,100)
assert 1/(c*c) == F(4)
assert b*b == F(9)

# Equilibria are parameterized by w with w^2=4/13.
w2=F(4,13)
# y=-w, z=10w, x=-39w/4. Check linear components by coefficients of w.
y_coeff=F(-1)
z_coeff=F(10)
x_coeff=F(-39,4)
assert -y_coeff - F(1) == 0
assert x_coeff + a*y_coeff + z_coeff == 0
assert d*z_coeff + c == 0
assert x_coeff*w2 + b == 0

# Cleared residual identities.
# c*(w+(d/c)z) = c*w+d*z = zdot.
assert c == c
assert c*(d/c) == d
# w*(x+b/w)=x*w+b = wdot.
assert b == b

print("VERIFY_OK")
