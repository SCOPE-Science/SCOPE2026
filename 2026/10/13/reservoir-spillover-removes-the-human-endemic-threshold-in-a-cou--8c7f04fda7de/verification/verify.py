#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 60

def pos_root(beta, mu, R, kappa):
    beta=Decimal(beta); mu=Decimal(mu); R=Decimal(R); kappa=Decimal(kappa)
    B=kappa+mu*(Decimal(1)-R)
    return (-B+(B*B+Decimal(4)*mu*R*kappa).sqrt())/(Decimal(2)*beta)

# Exact coefficient reduction at representative rational parameters.
beta=Fraction(3,2)
mu=Fraction(2,5)
sigma=Fraction(4,3)
gamma=Fraction(1,4)
alpha=Fraction(1,5)
A=(sigma+mu)*(gamma+mu+alpha)
R=Fraction(3,4)
# Choose Pi from the exact R formula.
Pi=R*mu*A/(beta*sigma)
kappa=Fraction(1,7)
a=beta*A
b=(kappa+mu)*A-Pi*sigma*beta
c=-Pi*sigma*kappa
assert b/A == kappa+mu*(1-R)
assert c/A == -mu*R*kappa/beta
assert a > 0 and c < 0

# Positive root and positivity of reconstructed human compartments.
I=pos_root("1.5","0.4","0.75","0.1")
assert I > 0
sigma_d=Decimal("1.333333333333333333333333333333333333")
gamma_d=Decimal("0.25")
alpha_d=Decimal("0.2")
mu_d=Decimal("0.4")
A_d=(sigma_d+mu_d)*(gamma_d+mu_d+alpha_d)
S=A_d*I/(sigma_d*(Decimal("0.1")+Decimal("1.5")*I))
E=(gamma_d+mu_d+alpha_d)*I/sigma_d
Rec=gamma_d*I/mu_d
assert S > 0 and E > 0 and Rec > 0

# Subcritical asymptotic.
beta_d=Decimal("1.7")
mu_d=Decimal("0.6")
R_d=Decimal("0.8")
target=R_d/(beta_d*(Decimal(1)-R_d))
for k in ("1e-8","1e-12","1e-16"):
    val=pos_root(beta_d,mu_d,R_d,k)/Decimal(k)
assert abs(val-target) < Decimal("1e-7")

# Critical square-root asymptotic.
R_d=Decimal(1)
target=mu_d.sqrt()/beta_d
for k in ("1e-8","1e-12","1e-16"):
    val=pos_root(beta_d,mu_d,R_d,k)/Decimal(k).sqrt()
assert abs(val-target) < Decimal("1e-7")

# Supercritical autonomous limit.
R_d=Decimal("1.4")
target=mu_d*(R_d-Decimal(1))/beta_d
val=pos_root(beta_d,mu_d,R_d,"1e-16")
assert abs(val-target) < Decimal("1e-7")

# Negative root check for a subcritical forced case.
beta=Decimal("1.7"); mu=Decimal("0.6"); R=Decimal("0.8"); k=Decimal("0.2")
B=k+mu*(Decimal(1)-R)
disc=(B*B+Decimal(4)*mu*R*k).sqrt()
rplus=(-B+disc)/(Decimal(2)*beta)
rminus=(-B-disc)/(Decimal(2)*beta)
assert rplus > 0 and rminus < 0

print("VERIFY_OK")
