"""Reproducible exact checks for two-choice rectangular averaging maxima.
No external dependencies; finite boxes supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import prod

for t in [F(1,5), F(1,3), F(1,2), F(3,4), F(9,10)]:
    c=t/(2-t); rho=(1-t)/(2-t)
    assert (1+c)==2/(2-t)
    for u,v in product([F(-2),F(-1),F(0),F(1),F(2),F(3)],repeat=2):
        deficit=u*u+c*v*v-max(u*u,((1-t)*u+t*v)**2)
        rhs=min(c*v*v, t/(2-t)*((2-t)*u-(1-t)*v)**2)
        assert deficit==rhs and rhs>=0
    for L in [2,4,8,16]:
        vals={j:rho**j for j in range(L)}
        vals2={j:rho**j for j in range(L+1)}
        Y=sum(max(abs(vals.get(j,0))**2,abs((1-t)*vals.get(j,0)+t*vals.get(j-1,0))**2) for j in range(-1,L+2))
        X=sum(v*v for v in vals.values())
        assert Y<=2/(2-t)*X
        # Exact geometric infinite-tail equality (geometric-series proof).
        Xinf=1/(1-rho*rho)
        Yinf=1 + ((1-t)*rho+t)**2/(1-rho*rho)
        assert Yinf/Xinf==2/(2-t)
print('CHECK_OK rational scalar identity, exact extremizers, truncation tests')
