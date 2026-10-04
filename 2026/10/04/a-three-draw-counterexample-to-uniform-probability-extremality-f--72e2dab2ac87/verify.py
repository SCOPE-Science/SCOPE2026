from fractions import Fraction
from itertools import product

def corr_for_s(s):
    values = (Fraction(-1), Fraction(0), Fraction(1))
    probs = (s, 1-2*s, s)
    EL=EU=EL2=EU2=ELU=Fraction(0)
    for idx in product(range(3), repeat=3):
        pr = probs[idx[0]]*probs[idx[1]]*probs[idx[2]]
        vals = [values[i] for i in idx]
        L=min(vals); U=max(vals)
        EL += pr*L; EU += pr*U
        EL2 += pr*L*L; EU2 += pr*U*U; ELU += pr*L*U
    vL=EL2-EL*EL; vU=EU2-EU*EU; cov=ELU-EL*EU
    assert vL == vU and vL > 0
    return cov/vL, (EL,EU,EL2,EU2,ELU,vL,cov)

def formula(s):
    return s*(9*s*s-10*s+3)/(3-12*s+20*s*s-9*s*s*s)

for s in (Fraction(3,10), Fraction(1,3), Fraction(1,4), Fraction(2,5)):
    rho, moments = corr_for_s(s)
    assert rho == formula(s)

rho_counter,_=corr_for_s(Fraction(3,10))
rho_uniform,_=corr_for_s(Fraction(1,3))
assert rho_counter == Fraction(81,319)
assert rho_uniform == Fraction(1,4)
assert rho_counter-rho_uniform == Fraction(5,1276)

# Exact derivative at the uniform point for the displayed rational formula.
s=Fraction(1,3)
N=lambda x: x*(9*x*x-10*x+3)
D=lambda x: 3-12*x+20*x*x-9*x*x*x
Np=lambda x: 27*x*x-20*x+3
Dp=lambda x: -12+40*x-27*x*x
deriv=(Np(s)*D(s)-N(s)*Dp(s))/(D(s)*D(s))
assert deriv == Fraction(-9,32)
print('VERIFY_OK')
