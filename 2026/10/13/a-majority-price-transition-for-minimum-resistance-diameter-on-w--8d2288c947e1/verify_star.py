"""Reproducible finite checks for optimal resistance diameter on a priced star.

No numerical experiment here replaces the analytical proof for all positive prices.
Run with Python 3 standard library: python verify_star.py
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product, combinations
from math import isclose
import random

getcontext().prec = 70

def optimum(prices):
    """Return predicted optimal diameter and conductances as Decimals."""
    c = [Decimal(str(x)) for x in prices]
    C = sum(c)
    i = max(range(len(c)), key=lambda k: c[k])
    if 2*c[i] <= C:
        return 2*C, [1/C]*len(c)
    a = c[i].sqrt()
    b = (C-c[i]).sqrt()
    w = [1/((a+b)*b) for _ in c]
    w[i] = 1/((a+b)*a)
    return (a+b)**2, w

def diameter(w):
    v = [1/x for x in w]
    return max(v[i]+v[j] for i,j in combinations(range(len(v)),2))

def grounded_solve(w, right):
    """Exact Gaussian elimination of grounded star Laplacian, hub=0."""
    m = len(w)
    # Grounding the hub leaves the diagonal matrix of leaf conductances.
    A = [[Fraction(w[i]) if i==j else Fraction(0)
          for j in range(m)] for i in range(m)]
    b = [Fraction(x) for x in right]
    for k in range(m):
        piv = A[k][k]
        assert piv != 0
        for j in range(k,m): A[k][j] /= piv
        b[k] /= piv
        for i in range(m):
            if i == k: continue
            t=A[i][k]
            for j in range(k,m): A[i][j] -= t*A[k][j]
            b[i] -= t*b[k]
    return b

# All parameter branches, including the boundary where a price is exactly half.
tests = [[1,1], [1,2], [1,1,1], [2,1,1], [5,2,1,2],
         [10,1,1,1], [16,4,4,1], [9,4,3], [1,5,3,2,4]]
rng = random.Random(651025)
for _ in range(250):
    m = rng.randrange(2,9)
    tests.append([rng.randint(1, 25) for _ in range(m)])
for p in tests:
    goal,w = optimum(p)
    budget=sum(Decimal(x)*y for x,y in zip(p,w))
    dia=diameter(w)
    assert abs(budget-1)<Decimal('1e-60'),(p,budget)
    assert abs(dia-goal)<Decimal('1e-59'),(p,goal,dia)
    # The formula is strictly better than uniform exactly in the majority branch.
    C = Decimal(sum(p))
    if 2*max(p)>sum(p): assert goal<2*C
    else: assert goal==2*C

# Compare exact electrical-network solves with the series-law effective resistance.
for m in range(2,7):
    for _ in range(35):
        w=[Fraction(rng.randrange(1,9),rng.randrange(1,9)) for _ in range(m)]
        for i,j in combinations(range(m),2):
            b=[Fraction(int(k==i)-int(k==j)) for k in range(m)]
            x=grounded_solve(w,b)
            R=x[i]-x[j]
            assert R==1/w[i]+1/w[j]

# Exhaustive small rational grids in the *normalized resistance* dual problem.
# For each u_i>0 with u_i+u_j<=1: sum(c_i/u_i) >= asserted optimum.
meshes=0
for m in (2,3,4):
    for prices in product((1,2,4),repeat=m):
        goal,_=optimum(prices)
        for parts in product(range(1,7),repeat=m):
            if any(parts[i]+parts[j]>7 for i,j in combinations(range(m),2)):
                continue
            f=sum(Fraction(c*7,u) for c,u in zip(prices,parts))
            assert Decimal(f.numerator)/Decimal(f.denominator)>=goal-Decimal('1e-55')
            meshes+=1

# A genuinely nonuniform rational exact certificate.
prices=[16,4,4,1]
goal,w=optimum(prices)
assert goal == 49
assert all(w[i]==Decimal(1)/Decimal(21) for i in range(1,4))
assert w[0]==Decimal(1)/Decimal(28)
print(f'VERIFY_OK {len(tests)} full-budget cases, '
      f'{sum(35*m*(m-1)//2 for m in range(2,7))} grounded-network cases, '
      f'{meshes} exact dual-grid inequalities')
