#!/usr/bin/env python3
from fractions import Fraction
import math

for n in range(3,101):
    A=Fraction(n*n-n+1,n)
    rho={}
    for d in range(1,n):
        rho[d]=d*A-Fraction(d*(d+1),2)

    # Exact source shell ordering.
    for d in range(1,n-1):
        assert rho[d+1]-rho[d] == A-(d+1)
        assert rho[d+1] > rho[d]

    rho1=Fraction((n-1)*(n-1),n)
    assert rho[1] == rho1

    # Each clock distance occurs for exactly n ordered pairs.
    counts={d:0 for d in range(1,n)}
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            d=(j-i)%n
            assert 1 <= d <= n-1
            counts[d]+=1
    assert all(counts[d]==n for d in counts)
    assert sum(counts.values())==n*(n-1)

    # Squared Euclidean shell radii are exact rationals.
    facet_d2={d:rho[d]*rho[d]/2 for d in rho}
    vertex_r2={d:Fraction(2,1)/(rho[d]*rho[d]) for d in rho}
    assert facet_d2[1] == min(facet_d2.values())
    assert vertex_r2[1] == max(vertex_r2.values())
    assert facet_d2[1]*vertex_r2[1] == 1

    # Exact barycenter of outer directed-neighbor roots.
    # Sum_i (e_i-e_{i+1})/rho1 = 0 coordinatewise.
    coeff=[Fraction(0) for _ in range(n)]
    for i in range(n):
        coeff[i]+=1/rho1
        coeff[(i+1)%n]-=1/rho1
    assert all(x==0 for x in coeff)

# Representative floating values only for a visible replay check.
vals=[]
for n in (3,4,5,10,100):
    r=(n-1)**2/(n*math.sqrt(2))
    R=n*math.sqrt(2)/(n-1)**2
    assert abs(r*R-1)<1e-12
    vals.append((n,r,R))

print("VERIFY_OK clock-cyclohedral-radii n=3..100 exact_shells=yes exact_barycenter=yes")
for n,r,R in vals:
    print(f"n={n} rin={r:.12g} Rmin={R:.12g}")
