from fractions import Fraction as F

N = 11
c = N // 2
# Five grids, using exact rational arithmetic.
def grid(v=F(0)):
    return [[v for _ in range(N)] for __ in range(N)]

S0 = grid(F(1))
E0 = grid(F(0))
I0 = grid(F(0))
Q0 = grid(F(0))
R0 = grid(F(0))
# Localized central source.
E0[c][c] = F(1, 5)
I0[c][c] = F(1, 10)
S0[c][c] = F(7, 10)

# Positive illustrative parameters. Only locality and zero structure matter.
k = F(1, 100)
h = F(1, 10)
r = k / (h*h)
phi = k
lamS = lamE = lamI = lamQ = lamR = F(1, 100)
Lam = F(1, 10)
rho = F(1, 20)
b1 = F(1, 100)
b2 = F(1, 50)
mu = F(1, 100)
delta = F(1, 20)
gamma = F(1, 20)
alpha = F(1, 20)

def nbr(A,j,l):
    # Interior verification only; corners chosen below are remote and boundary
    # values are not needed for the support argument. Use reflected values to
    # mimic a no-flux treatment at the edge.
    jm=max(j-1,0); jp=min(j+1,N-1); lm=max(l-1,0); lp=min(l+1,N-1)
    return A[jm][l]+A[jp][l]+A[j][lm]+A[j][lp]

def first_step():
    S1,E1,I1,Q1,R1=grid(),grid(),grid(),grid(),grid()
    for j in range(N):
      for l in range(N):
        S1[j][l]=(S0[j][l]+lamS*r*nbr(S0,j,l)+phi*(Lam+rho*Q0[j][l]))/(1+4*lamS*r+phi*(b1*E0[j][l]+b2*I0[j][l]+mu))
    for j in range(N):
      for l in range(N):
        E1[j][l]=(E0[j][l]+lamE*r*nbr(E0,j,l)+phi*b1*E0[j][l]*S1[j][l])/(1+4*lamE*r+phi*(delta+mu))
    for j in range(N):
      for l in range(N):
        I1[j][l]=(I0[j][l]+lamI*r*nbr(I0,j,l)+phi*(b2*I0[j][l]*S1[j][l]+delta*E1[j][l]))/(1+4*lamI*r+phi*(gamma+mu))
    for j in range(N):
      for l in range(N):
        Q1[j][l]=(Q0[j][l]+lamQ*r*nbr(Q0,j,l)+phi*gamma*I1[j][l])/(1+4*lamQ*r+phi*(alpha+rho+mu))
    for j in range(N):
      for l in range(N):
        R1[j][l]=(R0[j][l]+lamR*r*nbr(R0,j,l)+phi*alpha*Q1[j][l])/(1+4*lamR*r+phi*mu)
    return S1,E1,I1,Q1,R1

S1,E1,I1,Q1,R1=first_step()
# A corner is many lattice edges from the central source.
z=(0,0)
for A0,A1 in [(E0,E1),(I0,I1),(Q0,Q1),(R0,R1)]:
    assert A0[z[0]][z[1]] == 0
    assert A1[z[0]][z[1]] == 0

def nu(prev,curr):
    if curr == 0:
        raise ZeroDivisionError("Eq. (25) is undefined at current state zero")
    return -(curr-prev)/(k*curr)

for A0,A1 in [(E0,E1),(I0,I1),(Q0,Q1),(R0,R1)]:
    try:
        nu(A0[z[0]][z[1]], A1[z[0]][z[1]])
        raise AssertionError("expected zero denominator")
    except ZeroDivisionError:
        pass

# No unique continuous extension of 1+k*nu = prev/curr at (0,0).
for eps in [F(1,10),F(1,100),F(1,1000)]:
    assert eps/eps == 1
    assert (2*eps)/eps == 2

print("VERIFY_OK")
