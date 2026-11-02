"""Exact reproducibility checks for the time-reversed seasonal Beverton-Holt identity.

Only Python 3 and SymPy are needed. This program checks polynomial
identities and finite rational instances; the all-period autocorrelation
statement is established by the Fourier argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import prod
import sympy as S


def elementary(xs, k):
    return sum((prod(t) for t in combinations(xs, k)), 0)


def inverse_cycle(a, beta):
    """Exact globally attracting positive period of inverse abundances."""
    a, beta = F(a), tuple(map(F, beta))
    n = len(beta)
    y = sum(a ** i * v for i, v in enumerate(beta)) / (a ** n - 1)
    result = []
    for v in beta:
        result.append(y)
        y = (y + v) / a
    assert y == result[0]
    return result


def autocorr(cycle, lag):
    n = len(cycle)
    return sum(cycle[t] * cycle[(t+lag) % n] for t in range(n)) / n


def mean_catch(cycle, q):
    return sum(1/(y+q) for y in cycle)/len(cycle)


a,b,c,d,q=S.symbols('a b c d q')
L=(b+a*c+a*a*d, a*a*b+c+a*d, a*b+a*a*c+d)
R=(b+a*d+a*a*c, a*a*b+d+a*c, a*b+a*a*d+c)
V=(b-c)*(b-d)*(c-d)
checks=0
for k in (1,2):
    assert S.expand(elementary(L,k)-elementary(R,k))==0
    checks+=1
assert S.factor(prod(L)-prod(R)) == -a*(a-1)**3*(a+1)*V
checks+=1
Q=a**3-1
z=q*Q
EF=elementary(tuple(t+z for t in L),2)
ER=elementary(tuple(t+z for t in R),2)
PF=prod(t+z for t in L)
PR=prod(t+z for t in R)
assert S.expand(EF-ER)==0
checks+=1
assert S.factor(PF-PR)==-a*(a-1)**3*(a+1)*V
checks+=1
# Multiplying the rational response formula by both positive products
# gives a polynomial identity, independent of numerical approximations.
assert S.expand(Q*(EF*PR-ER*PF)-Q*a*(a-1)**3*(a+1)*V*EF)==0
checks+=1

assert inverse_cycle(F(2),[1,2,3]) == list(map(F,[F(17,7),F(12,7),F(13,7)]))
checks+=1
assert inverse_cycle(F(2),[1,3,2]) == list(map(F,[F(15,7),F(11,7),F(16,7)]))
checks+=1
vf=inverse_cycle(F(2),[1,2,3]);vr=inverse_cycle(F(2),[1,3,2])
assert sum(vf)/3 == sum(vr)/3 == 2
checks+=1
assert sum(v*v for v in vf)/3==sum(v*v for v in vr)/3==F(602,147)
checks+=1
assert sum(v**3 for v in vf)/3-sum(v**3 for v in vr)/3 == F(12,343)
checks+=1
assert mean_catch(vf,0)-mean_catch(vr,0)==-F(4067,1750320)
checks+=1

for growth in (F(3,2),F(2),F(5,2),F(3),F(5)):
    for n in range(1,9):
        profiles=[tuple(F(((3*t+t*t+seed*seed+t*seed)%13)+1, (t+seed)%5+2) for t in range(n)) for seed in (1,2,4)]
        for beta in profiles:
            forward=inverse_cycle(growth,beta)
            reverse=inverse_cycle(growth,tuple(beta[(-i)%n] for i in range(n)))
            for lag in range(n):
                assert autocorr(forward,lag)==autocorr(reverse,lag)
                checks+=1
for growth in (F(3,2),F(2),F(7,3),F(4)):
    for crowd in ((F(1),F(2),F(3)),(F(1,3),F(4),F(7)),(F(11,5),F(3,5),F(2))):
        f=inverse_cycle(growth,crowd)
        r=inverse_cycle(growth,(crowd[0],crowd[2],crowd[1]))
        v=(crowd[0]-crowd[1])*(crowd[0]-crowd[2])*(crowd[1]-crowd[2])
        for saturation in (F(0),F(1,10),F(1),F(7)):
            gap=mean_catch(f,saturation)-mean_catch(r,saturation)
            assert gap != 0 and (gap>0)==(v>0)
            checks+=1
for growth in (F(2),F(7,3)):
    for crowd in permutations([F(1),F(2),F(3)]):
        f=inverse_cycle(growth,crowd)
        r=inverse_cycle(growth,(crowd[0],crowd[2],crowd[1]))
        assert sum(f)==sum(r) and sum(t*t for t in f)==sum(t*t for t in r)
        checks+=1
print(f'PASS: {checks} exact assertions; polynomial identity and rational replay verified')
