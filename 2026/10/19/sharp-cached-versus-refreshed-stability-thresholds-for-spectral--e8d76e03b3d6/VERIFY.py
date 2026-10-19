#!/usr/bin/env python3
"""Exact-rational reproduction for the ideal two-coordinate curvature sampling theorem."""
from fractions import Fraction as F
from itertools import product


def q(g):
    return (F(1) + (F(1) - g)**2)/2


def data(rho, alpha):
    # Oracle-specific curvature, preconditioner, and step scaling; no formulas hard-coded.
    ds = {}
    for j in (0, 1):
        vals = []
        for s,t in product((0,1),repeat=2):
            p = [rho+int(s==i) for i in range(2)]
            l = F(1)/p[t]
            eta = alpha/l
            g = eta/p[j]
            one_step = sum(((F(1)-g)**2 if b==j else F(1)) for b in (0,1))/2
            vals.append((s,t,g,one_step))
        ds[j] = vals
    return ds

n_checks = 0
for rho in (F(1,10),F(1,4),F(1,3),F(1,2),F(1),F(3),F(9,2)):
    for alpha in (F(1,5), F(1,2), F(7,10),F(1), F(3,2)):
        t = rho/(F(1)+rho)
        d = data(rho,alpha)
        for j in (0,1):
            qvalues = sorted([z[3] for z in d[j]])
            qexpected = sorted([q(alpha),q(alpha),q(alpha*t),q(alpha/t)])
            assert qvalues==qexpected
            for k in range(0,11):
                cached_direct = sum(z[3]**k for z in d[j])/4
                cached_formula = (2*q(alpha)**k+q(alpha*t)**k+q(alpha/t)**k)/4
                fresh_direct = (sum(z[3] for z in d[j])/4)**k
                fresh_formula = ((2*q(alpha)+q(alpha*t)+q(alpha/t))/4)**k
                assert cached_direct == cached_formula
                assert fresh_direct == fresh_formula
                n_checks+=2
        if alpha < 2:
            # Cached stability condition and the exceptional amplification mode agree.
            assert (q(alpha/t)<1)==(rho>alpha/(2-alpha))
            n_checks+=1

# Exact rational witness, independent of any stability inequality derivation.
d=data(F(1,4), F(1,2))
assert set((s,t,g) for s,t,g,_ in d[0])=={
  (0,0,F(1,2)),(0,1,F(1,10)),(1,0,F(1,2)),(1,1,F(5,2))}
assert {z[3] for z in d[0]}=={F(5,8),F(181,200),F(13,8)}
assert sum(z[3] for z in d[0])/4 == F(189,200)
# The polynomial of the refreshed default factor obeys 32(M-1)=s^2-4s-8.
rho=F(1,4);t=rho/(1+rho);s=t+1/t
M=(2*q(F(1,2))+q(t/2)+q(F(1,2)/t))/4
assert M==(s*s-4*s+24)/32
assert M==F(189,200)
print('PASS: exact arithmetic checks',n_checks, 'plus rational witness, default phase polynomial')
