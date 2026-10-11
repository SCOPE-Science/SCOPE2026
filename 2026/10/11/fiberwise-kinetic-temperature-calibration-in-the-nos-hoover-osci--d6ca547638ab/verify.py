from fractions import Fraction as F

x = F(7, 5)
alpha = F(9, 4)
zdot = alpha * (x*x - 1)
assert x*x - 1 == zdot / alpha

# Exact variance algebra under E[X^2]=1.
EX2 = F(1)
EX4 = F(17, 10)
var_X2 = EX4 - EX2*EX2
residual = EX4 - 2*EX2 + 1
assert var_X2 == residual

# Thermostat speed scaling.
Ezdot2 = alpha*alpha*residual
assert var_X2 == Ezdot2/(alpha*alpha)

# A nonconstant nonnegative variable with mean one cannot lie strictly on one side.
vals = [F(1, 2), F(3, 2)]
weights = [F(1, 2), F(1, 2)]
mean = sum(w*v for w, v in zip(weights, vals))
assert mean == 1
assert any(v < 1 for v in vals) and any(v > 1 for v in vals)

print("VERIFY_OK")
