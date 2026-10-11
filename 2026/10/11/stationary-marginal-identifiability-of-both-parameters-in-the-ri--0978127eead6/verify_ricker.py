from fractions import Fraction

# Exact rational checks of the algebra used in the proof.
for Y in [Fraction(-3,2), Fraction(2,5), Fraction(7,3)]:
    for U in [Fraction(1,4), Fraction(3,2), Fraction(9,5)]:
        for r in [Fraction(1,3), Fraction(7,4), Fraction(5,2)]:
            d = r * (1 - U)
            lhs = (Y + d)**2 - Y**2
            rhs = 2*r*Y*(1-U) + r*r*(1-U)**2
            assert lhs == rhs

# If E[U]=1 and 2 E[Y(U-1)] = r Var(U), then
# C = Cov(log X, X) = K E[Y(U-1)] and V = Var(X) = K^2 Var(U),
# hence 2 K C = r V.
for K in [Fraction(2,3), Fraction(5,2), Fraction(11,4)]:
    for r in [Fraction(1,2), Fraction(3,1), Fraction(7,5)]:
        var_u = Fraction(4,9)
        ey = r * var_u / 2
        C = K * ey
        V = K*K * var_u
        assert 2*K*C == r*V
        assert r == 2*K*C/V

print('ALGEBRA_OK')
