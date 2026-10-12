from fractions import Fraction as F

def proj_interval(x):
    return min(F(1), max(F(-1), x))

def Q(x):
    return x

def bias(x):
    return -2*x

# Printed alignment condition with eta = 0.
for j in range(-20, 21):
    x = F(j, 20)
    assert bias(x) * x <= 0 * (Q(x) * x)

# Quasi-gradient normalization for f(x)=x^2/2:
# <Q(x),x> = x^2 = 2(f(x)-f(0)).
for j in range(-20, 21):
    x = F(j, 20)
    assert Q(x) * x == 2 * (x*x/F(2))

# Replay the source Theorem-1 steps alpha_k = 1/(k+1).
x = F(1, 2)
trajectory = [x]
for k in range(20):
    alpha = F(1, k+1)
    x = proj_interval(x - alpha*(Q(x) + bias(x)))
    trajectory.append(x)

assert trajectory[1] == F(1)
assert all(v == F(1) for v in trajectory[1:])

# Source Lemma-1 recursion eventually fails even with the sharp Q bound G=1.
# At k=5, alpha=1/6, x_k=1, b=-2, sigma=0.
alpha = F(1, 6)
G = F(1)
lhs = F(1)
rhs = (1 - 2*alpha)*F(1) + alpha*alpha*(2*G*G + 2*F(4))
assert rhs == F(17, 18)
assert lhs > rhs

# Corrected directional condition gives the intended algebra.
# If <b,d> >= -eta<Q,d>, then <Q+b,d> >= (1-eta)<Q,d>.
qdot = F(7, 5)
eta = F(2, 5)
bdot = -eta*qdot
assert qdot + bdot == (1-eta)*qdot

print("VERIFY_OK")
