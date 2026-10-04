from fractions import Fraction

# Published baseline decimals represented exactly.
Lambda = Fraction(89, 100)
eta = Fraction(9, 10)
mu = Fraction(17, 400000)
lambda_k = Fraction(117, 50000)
beta_c = Fraction(2081, 5000)
zeta_k = Fraction(7, 200)

assert Lambda > 0
assert beta_c > 0
assert lambda_k > 0
assert zeta_k > 0

S0 = Lambda / (eta + mu)
residual_Ik = lambda_k * S0

assert S0 == Fraction(356000, 360017)
assert residual_Ik == Fraction(20826, 9000425)
assert residual_Ik > 0

# Logical backbone of the symbolic contradiction under strict positive factors:
# S cannot vanish at equilibrium because Sdot = Lambda + pi*R > 0 there.
# Then Ic'=0 with Ic=Ick=0 forces H=0; H'=0 forces Ik=0;
# finally Ik'=0 would require lambda_k*S=0, impossible.
print('VERIFY_OK')
