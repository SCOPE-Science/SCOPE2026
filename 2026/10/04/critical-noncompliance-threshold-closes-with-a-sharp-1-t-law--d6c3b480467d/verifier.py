from fractions import Fraction as F

b=F(1); delta=F(1); beta=F(1); gamma=F(1); nu=F(1)
q=F(2); alpha=F(1,2); eta=F(0)
K=b/delta
Rb=K*q/(nu+delta)
Rd=K*beta*(1-alpha)**2/(gamma+eta+delta)
assert Rb == 1
assert Rd == F(1,8)

# Linear eigenvalues at the fully compliant DFE on the critical behavioral surface.
behavior_eig = q*K-(nu+delta)
disease_eig = beta*(1-alpha)**2*K-(gamma+eta+delta)
noncompliant_infection_eig = -(gamma+nu+delta)
assert behavior_eig == 0
assert disease_eig == F(-7,4)
assert noncompliant_infection_eig == -3

# Invariant total-population slice T(0)=K, X(0)=1/4.
X0=F(1,4)
def X(t):
    return X0/(1+q*X0*t)
def Xprime_closed(t):
    return -q*X(t)*X(t)
def Xprime_formula(t):
    return -q*X0*X0/(1+q*X0*t)**2
for t in [F(0),F(1,3),F(2),F(7),F(101,5)]:
    assert Xprime_closed(t) == Xprime_formula(t)
    assert X(t) == 1/(4+2*t)

# Exact asymptotic coefficient follows algebraically: t/(4+2t) -> 1/2 = 1/q.
assert F(1,q) == F(1,2)
print('VERIFY_OK')
