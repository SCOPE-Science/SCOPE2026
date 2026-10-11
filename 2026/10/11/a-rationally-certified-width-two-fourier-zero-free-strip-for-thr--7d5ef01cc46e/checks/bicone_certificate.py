"""Exact rational Taylor-grid certificate for bicone Fourier positivity (standalone)."""
from fractions import Fraction as F
from math import factorial

J=10
K=40
factorials=[factorial(k) for k in range(102)]
coeff=[]
for k in range(1,K+1):
    a=sum((F((-1)**j*(2*j+1)*factorials[2*j], factorials[j]**2*factorials[2*j+2*k+1]) for j in range(J+1)), F(0))
    coeff.append((-1)**(k+1)*a)

def cert_eval(u):
    v=u*u
    y=F(0)
    for c in coeff[::-1]:
        y=y*v+c
    return v*y

# Auxiliary rational bounds explicitly used in the analytic argument.
assert sum((F(2*j+1, factorials[j]**2) for j in range(11)), F(0)) < 6
assert F(1)-F(3)+F(5,4)-F(7,36) == -F(17,18)
assert F(1)-F(1)+F(1,4)-F(1,36) > F(11,50)
assert F(7,30) == F(1,3)-F(1,10)
assert F(23)>F(729,32)
assert F(84,383)<F(2,9)
N=260
values=[cert_eval(F(1)+F(i,20)) for i in range(N+1)]
m=min(values)
argmin=values.index(m)
print('N=',N,'min evaluated=',float(m),'at u=',float(F(1)+F(argmin,20)))
err=2*F(23,factorials[11]**2)+6*F(14**81,factorials[81])
# derivative bound |H_u| <= 3/2, grid max dist 1/40 -> 3/80.
print('Taylor error upper', float(err),'derivative interpolation upper',3/80)
assert m > F(1,20)
assert err < F(1,10**10)
assert m - F(3,80)-err>0
print('BICONE_ZERO_FREE_S2_OK')
