"""Reproducible checks of the stated discrete-hyetograph infiltration theorem.

The analytic proof applies to general positive nonincreasing capacity functions;
these computations check a strict rational witness and finite numerical cases.
No finite set of tests is used as proof of the theorem.
"""
from fractions import Fraction
from itertools import permutations
from math import exp, log
import random

# f(F)=max(1,3-F): exact high-stage exponential transfer.
q = Fraction(3,4)
initial=Fraction(0)
d=Fraction(1,4)
high_first=Fraction(3)*(1-q)+d
low_first=Fraction(3)-(Fraction(3)-d)*q
assert high_first==1
assert low_first==Fraction(15,16)
assert high_first-low_first==Fraction(1,16)
assert 0<low_first<high_first<2
# During high stages, f(F) <=3<4, during low stages f(F)>=2>1.

# High-accuracy standard-library RK4 integration for decreasing capacities.
def travel(x,r,d,f,steps=720):
    h=d/steps
    for _ in range(steps):
        def g(y): return min(r,f(y))
        k1=g(x)
        k2=g(x+h*k1/2)
        k3=g(x+h*k2/2)
        k4=g(x+h*k3)
        x+=h*(k1+2*k2+2*k3+k4)/6
    return x

def solve(blocks, f, x):
    for r,d in blocks: x=travel(x,r,d,f)
    return x

rng=random.Random(20261029)
checks=0
families=[
    (lambda x: 1+2/(x+1),0.25),
    (lambda x: max(1.0,3.0-x),0.0),
    (lambda x: 0.7+4*exp(-0.6*x),0.2),
]
for capacity,x0 in families:
    for trial in range(35):
        intensities=[rng.uniform(0.3,5) for _ in range(4)]
        durations=[rng.uniform(0.05,0.8) for _ in range(4)]
        blocks=list(zip(intensities,durations))
        vals=[solve([blocks[i] for i in perm],capacity,x0) for perm in permutations(range(4))]
        maximum=solve(sorted(blocks,reverse=True),capacity,x0)
        minimum=solve(sorted(blocks),capacity,x0)
        for v in vals:
            assert minimum-5e-7<=v<=maximum+5e-7,(capacity,blocks,v,minimum,maximum)
            checks+=1
        assert maximum>=minimum-5e-7
        checks+=1
print(f"PASS exact witness and {checks} finite numerical bounds for 3 decreasing-capacity families")
