#!/usr/bin/env python3
from fractions import Fraction as F
import mpmath as mp

# 1. Exact pointwise failure of the asserted adult-predator inequality
eta = F(1,2)
b2 = F(3,5)
b1 = F(1,2)
c2 = F(4,5)
d3 = F(1,10)
c3 = F(1,50)
P2delay = F(1)
P3 = F(1)

exact_p3dot = c2*P2delay - d3*P3 - c3*P3*P3
asserted_rhs = (eta*b2/b1 - d3)*P3 - c3*P3*P3
assert exact_p3dot == F(17,25)
assert asserted_rhs == F(12,25)
assert exact_p3dot > asserted_rhs

# 2. Source Figure-3 coexistence equilibrium
mp.mp.dps = 60
r=mp.mpf(3); d1=mp.mpf('0.1'); c1=mp.mpf('0.1')
b1m=mp.mpf('0.5'); b2m=mp.mpf('0.6'); b3=mp.mpf('0.2')
d2=mp.mpf('0.1'); d3m=mp.mpf('0.1'); c3m=mp.mpf('0.02')
f=mp.mpf('0.5'); k=mp.mpf(1); etam=mp.mpf('0.5'); c2m=mp.mpf('0.8')

def eqs(P1,P2,P3):
    g=(1+b1m*P1)*(1+k*b3*P3)
    return (
        r*P1/(1+k*f*P3)-d1*P1-c1*P1**2-b2m*P1*P3/g,
        etam*b2m*P1*P3/g-(d2+c2m)*P2,
        c2m*P2-d3m*P3-c3m*P3**2
    )

root = mp.findroot(eqs, (mp.mpf('3.654'),mp.mpf('0.9939'),mp.mpf('4.2827')))
P1s,P2s,P3s = map(mp.mpf, root)
res = max(abs(v) for v in eqs(P1s,P2s,P3s))
claimed_limit = (etam*b2m/b1m-d3m)/c3m
assert res < mp.mpf('1e-40')
assert abs(P3s-mp.mpf('4.28272994079448191714')) < mp.mpf('1e-18')
assert claimed_limit == 25
assert abs(P3s-claimed_limit) > 20

# 3. Exact witness showing the corrected condition is strictly weaker
r=F(11,10); d1=F(1); c1=F(1)
b1=F(1); b2=F(1,5); eta=F(1)
c2=F(1); d2=F(1); d3=F(1,10)
K=(r-d1)/c1
RP=eta*b2*c2*K/((1+b1*K)*(d2+c2)*d3)
assert K == F(1,10)
assert RP == F(1,11)
assert RP < 1
assert eta*b2/b1 > d3

# Verify an admissible alpha interval exists, e.g. after taking epsilon small.
eps=F(1,100)
Aeps=eta*b2*(K+eps)/(1+b1*(K+eps))
q=d2+c2
assert Aeps*c2 < q*d3
lower=Aeps/d3
upper=q/c2
assert lower < upper

print("VERIFY_OK")
print("pointwise_exact_p3dot", exact_p3dot)
print("pointwise_asserted_rhs", asserted_rhs)
print("figure3_equilibrium", mp.nstr(P1s,22), mp.nstr(P2s,22), mp.nstr(P3s,22))
print("figure3_residual", mp.nstr(res,8))
print("source_limit_expression", mp.nstr(claimed_limit,8))
print("exact_witness_K", K)
print("exact_witness_RP", RP)
print("alpha_interval", lower, upper)
