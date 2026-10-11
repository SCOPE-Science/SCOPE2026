#!/usr/bin/env python3
import math
from fractions import Fraction

# Printed Section 4.3 parameters (Liu--Zhang, AIMS Mathematics 9(2), 2024).
r=0.721; K=90.0; sigma=0.601; alpha=37.8537234
beta=0.318; omega=0.055; mu=0.02; d=0.12

# Exact cubic obtained from I=(beta/mu)S-alpha and the printed first equilibrium equation.
a=Fraction(-7931,18000000)
b=Fraction(25477,1800000)
c=Fraction(-7818045213,50000000000)
e=Fraction(189268617,250000000)
# Exact cubic discriminant: negative => exactly one real root.
disc=(18*a*b*c*e - 4*b**3*e + b*b*c*c - 4*a*c**3 - 27*a*a*e*e)
assert disc < 0

def P(S):
    return float(a)*S**3 + float(b)*S**2 + float(c)*S + float(e)
assert P(17.0)*P(18.0) < 0

# Bisection is sufficient and deterministic.
lo,hi=17.0,18.0
for _ in range(100):
    mid=(lo+hi)/2
    if P(lo)*P(mid) <= 0: hi=mid
    else: lo=mid
S=(lo+hi)/2
I=beta*S/mu-alpha

def fS(S,I):
    return r*S*(1-S/K)-beta*S*I/(I+alpha)-sigma*S/(omega*S+1)
def fI(S,I):
    return beta*S*I/(I+alpha)-mu*I
assert abs(fS(S,I)) < 2e-13 and abs(fI(S,I)) < 2e-13
assert abs(S-17.407432945150158) < 2e-13
assert abs(I-238.9244604278875) < 3e-12

# The point printed in Section 4.3 is not an equilibrium of the printed equations.
Sr,Ir=17.252,236.374
res=(fS(Sr,Ir),fI(Sr,Ir))
assert abs(res[0]) > 5e-3 and abs(res[1]) > 1e-3

p1=r*(1-2*S/K)-sigma/(1+omega*S)**2-beta*I/(I+alpha)
q1=-S*alpha*beta/(I+alpha)**2
p2=beta*I/(I+alpha)
q2=S*alpha*beta/(I+alpha)**2-mu
Delta=p1*q2-p2*q1
assert p1 > 0 and q1 < 0 and q2 < 0 and p1+q2 < 0 and Delta > 0

# For x=d*k^2*pi^2, DET_k=eps*x*(x-q2)-p1*x+Delta.
def eps_k(k):
    x=d*k*k*math.pi**2
    return (p1*x-Delta)/(x*(x-q2))
x1=d*math.pi**2
eps_c=eps_k(1)
assert abs(eps_c-0.008528798852725174) < 2e-16

# The derivative of phi(x)=(p1*x-Delta)/(x*(x-q2)) has numerator
# -p1*x^2 + 2*Delta*x - Delta*q2.  Its positive zero lies below x1,
# hence phi is strictly decreasing for every spatial mode k>=1.
D=(2*Delta)**2-4*p1*Delta*q2
xcrit=(2*Delta+math.sqrt(D))/(2*p1)
assert xcrit < x1
for k in range(1,20):
    assert eps_k(k) <= eps_c + 1e-15
for k in range(1,19):
    assert eps_k(k+1) < eps_k(k)

# At the corrected crossing mode 1 has a zero eigenvalue and negative companion eigenvalue.
def tr_det(eps):
    tr=-(eps+1)*x1+p1+q2
    det=eps*x1*x1-(p1+q2*eps)*x1+Delta
    return tr,det
tr,det=tr_det(eps_c)
assert abs(det) < 2e-17 and tr < -1.2

# At the paper's quoted value the corrected mode 1 is already unstable.
eps_paper=0.0011360854
trp,detp=tr_det(eps_paper)
lambda_plus=(trp+math.sqrt(trp*trp-4*detp))/2
assert detp < 0 and lambda_plus > 0
assert abs(lambda_plus-0.008760101432708765) < 5e-16

# Even without recomputing the equilibrium, the source's own rounded formula
# p1=0.0120, q2=-0.0172, Delta=0.0005608 gives a different threshold.
eps_rounded=(0.0120*x1-0.0005608)/(x1*(x1+0.0172))
assert abs(eps_rounded-0.009592999111777033) < 2e-16

print('VERIFY_OK')
print(f'S*={S:.15f}')
print(f'I*={I:.15f}')
print(f'p1={p1:.15f}, q1={q1:.15f}, p2={p2:.15f}, q2={q2:.15f}')
print(f'epsilon_c={eps_c:.15f}')
print(f'paper_rounded_formula={eps_rounded:.15f}')
print(f'lambda_plus_at_paper_epsilon={lambda_plus:.15f}')
print(f'reported_point_residuals=({res[0]:.15g},{res[1]:.15g})')
