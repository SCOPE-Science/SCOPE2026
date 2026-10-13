from fractions import Fraction as F

# Exact witness inside the source's stated parameter domain.
mu = gamma = theta = lam = F(1)
phi = w = p = v = F(0)
beta = F(4)
R0 = beta * theta / (lam * (gamma + mu + phi))
assert R0 == F(2)
S = 1 / R0
A = F(0)
I = mu * (1 - 1 / R0) / (mu + phi)
P = theta * I / lam
assert (S, A, I, P) == (F(1,2), F(0), F(1,2), F(1,2))

# alpha(P) and c(P) disappear at A=0; choose arbitrary admissible values.
alpha = F(1,2)
c = F(3,7)
Sdot = mu - beta*S*P + (1-p)*gamma*I + w*A - v*S - mu*S
Adot = -beta*alpha*A*P + p*gamma*I - w*A + v*S - (mu+c)*A
Idot = beta*S*P + beta*alpha*A*P - (gamma+mu+phi)*I
Pdot = theta*I - lam*P
assert (Sdot, Adot, Idot, Pdot) == (0,0,0,0)

# For p=v=0, A'=-q A and q>=mu.  A positive initial value
# is therefore bounded by A0*exp(-mu*t), so it approaches the boundary.
assert mu > 0 and beta >= 0 and alpha >= 0 and w >= 0 and c >= 0
print('VERIFY_OK')
