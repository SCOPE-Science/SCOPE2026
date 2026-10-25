"""Exact-arithmetic checks for a balanced two-patch Allee migration theorem.
Uses Python 3 standard library only; it corroborates, not substitutes for, the proof.
"""
from fractions import Fraction as Q
from itertools import product


def poly_value(coefficients, v):
    return sum(a * v**j for j, a in enumerate(coefficients))


def base_P(m, e, h, s):
    # ascending coefficient order, derived independently from the ODE
    return [s*m, -m*(e+s), s, 1-e-s-h*m, Q(0), -h]


def p_prime(p):
    return [j*p[j] for j in range(1,len(p))]


assert base_P(Q(1),Q(2,5),Q(1,10),Q(1,5)) == [Q(1,5),-Q(3,5),Q(1,5),Q(3,10),Q(0),-Q(1,10)]
p=base_P(Q(1),Q(2,5),Q(1,10),Q(1,5)); coeffs=[10*x for x in p]
assert coeffs == [2,-6,2,3,0,-1]
assert [ (v,poly_value(coeffs,v)) for v in [Q(1,3),Q(1,2),Q(1),Q(3,2),Q(8,5)]] == [(Q(1,3),Q(80,243)),(Q(1,2),-Q(5,32)),(Q(1),Q(0)),(Q(3,2),Q(1,32)),(Q(8,5),-Q(2118,3125))]
assert poly_value(p_prime(coeffs),Q(1))==2
assert len(coeffs)==6

# The identity F(v)=f(v^2,v)=vP(v)/(m+v^2), independently evaluating both sides.
# The Jacobian satisfies det J=-s F'(v) at arbitrary v on the nullcline u=v^2.
checks=0
for m,e,h,s,v in product([Q(1,2),Q(1),Q(3)], [Q(1,7),Q(2,5),Q(4,5)], [Q(1,10),Q(2,3)], [Q(1,5),Q(3,4)], [Q(1,4),Q(1,2),Q(1),Q(3,2),Q(5)]):
    u=v*v
    f=u*(u/(m+u)-e-h*u)+s*(v-u)
    P=base_P(m,e,h,s)
    assert f==v*poly_value(P,v)/(m+v*v)
    fu=u*(2*m+u)/(m+u)**2-e-2*h*u-s
    fv=s
    gu=s
    gv=-2*s*v
    det=fu*gv-fv*gu
    # chain rule F'=2v f_u + f_v
    assert det==-s*(2*v*fu+s)
    pvalue=poly_value(P,v); dp=poly_value(p_prime(P),v)
    dF=(pvalue+v*dp)/(m+v*v)-(2*v*v*pvalue)/(m+v*v)**2
    assert 2*v*fu+s==dF
    checks+=3

# Exact saddle at v=1 in the witness.
m,e,h,s=Q(1),Q(2,5),Q(1,10),Q(1,5)
u=v=Q(1)
fu=u*(2*m+u)/(m+u)**2-e-2*h*u-s
assert fu==-Q(1,20)
det=fu*(-2*s*v)-s*s
assert det==-Q(1,50)
assert fu-2*s*v==-Q(9,20)
checks+=3
print(f'PASS: {checks} exact rational checks; Q signs and exact saddle verified')
