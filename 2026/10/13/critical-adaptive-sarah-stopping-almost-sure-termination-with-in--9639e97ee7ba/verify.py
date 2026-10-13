"""Exact-rational checks for a stopped two-curvature SARAH+ inner loop.

Run with Python 3. No third-party dependencies. Finite enumeration supports
but does not prove the infinite-work and infinite-risk assertions.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

ETA=F(1,2)
MU=F(7,2)
THRESHOLD=F(1,2)  # norm threshold, squared parameter 1/4
UP=F(-2)
DOWN=F(1,2)


def first_hit_and_iterate(bits):
    # 1 means component curvature 6, 0 means curvature 1.
    v=MU
    x=F(1)-ETA*v
    first=None
    for t,bit in enumerate(bits,1):
        v*=UP if bit else DOWN
        x-=ETA*v
        if abs(v)<=THRESHOLD*MU:
            first=t
            break
    return first,x


def exact_path(h):
    bits=[1]*h+[0]*(h+1)
    first,x=first_hit_and_iterate(bits)
    assert first==2*h+1
    S=F(5,3)*(-2)**h+F(1,3)-F((-1)**h,2)
    assert x==1-F(7,4)*S
    return first,x

checks=0
for h in range(0,60):
    t,x=exact_path(h)
    if h>=1:
        assert abs(x)>=2**h
        checks+=1
    checks+=2

# Catalan first-passage probabilities, computed via independent enumeration.
for max_time in range(1,16):
    if max_time%2==0:
        continue
    hit=0
    j=(max_time-1)//2
    for bits in product([0,1],repeat=max_time):
        t,_=first_hit_and_iterate(bits)
        hit+=(t==max_time)
    assert hit==comb(2*j,j)//(j+1)
    checks+=1

# Exact lower bound for truncated sampling: stopping event T<=N only.
for N in range(1,14):
    captured=F(0)
    for bits in product([0,1],repeat=N):
        hit,x=first_hit_and_iterate(bits)
        if hit is not None and hit<=N:
            captured+=x*x/F(2**N)
    count=max(0,(N-1)//2)
    assert captured>=F(count,2)
    checks+=1

# Normal full-objective gradient descent has multiplier -3/4.
assert 1-ETA*MU==F(-3,4)
checks+=1
print(f'PASS: {checks} exact-rational path, Catalan and finite-cap checks')
print('This computation does not establish recurrence, infinite expectation, or infinite second moment.')
