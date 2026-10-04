from fractions import Fraction as F

# Exact witness at the critical threshold.
a1=a2=a3=F(2)
gE=gL=gN=F(1)
muA=F(1)
K=F(10)
beta=F(8)

# R0 = 1.
assert beta*gE*gL*gN == a1*a2*a3*muA

# Critical Jacobian.
J=[[-a1,F(0),F(0),beta],
   [gE,-a2,F(0),F(0)],
   [F(0),gL,-a3,F(0)],
   [F(0),F(0),gN,-muA]]

r=[beta/a1, beta*gE/(a1*a2), beta*gE*gL/(a1*a2*a3), F(1)]
ell=[F(1), a1/gE, a1*a2/(gE*gL), beta/muA]

def matvec(M,v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]

def leftvec(v,M):
    return [sum(v[i]*M[i][j] for i in range(len(v))) for j in range(len(M[0]))]

assert matvec(J,r) == [F(0)]*4
assert leftvec(ell,J) == [F(0)]*4

H=F(1,a1)+F(1,a2)+F(1,a3)+F(1,muA)
dot=sum(ell[i]*r[i] for i in range(4))
assert dot == beta*H

C=F(1)+r[1]+r[2]
kappa=C/(K*H)
Q=K*H/C
assert r == [F(4),F(2),F(1),F(1)]
assert H == F(5,2)
assert C == F(4)
assert kappa == F(4,25)
assert Q == F(25,4)
assert [Q*v for v in r] == [F(25),F(25,2),F(25,4),F(25,4)]

# At threshold the Lyapunov coefficient c1*beta equals mu_A.
c1=gE*gL*gN/(a1*a2*a3)
assert c1*beta == muA

print("VERIFY_OK")
