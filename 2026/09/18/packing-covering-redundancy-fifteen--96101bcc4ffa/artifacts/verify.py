#!/usr/bin/env python3
"""Exact-integer checks for the redundancy-15 generalized packing-covering result."""
from math import comb

RHO = 15
Q = (2, 3, 4, 5, 7, 8)
EXCEPTIONAL = {(3,4), (3,5), (4,5), (4,6)}


def cap_K(q, rho, t, r):
    a = rho - 2*r + t - 2
    b = rho - 2*r - 1
    vals = []
    for h in range(a+1, rho+1):
        num = (q**h-q**(h-a))*h - b*(q**h-1)
        den = q**(h-a)-1
        vals.append((num//den, h))
    return min(vals)

rows = []
for q in Q:
    for t in range(3, RHO-4):
        for r in range(t+1, (RHO+t-3)//2 + 1):
            if not (q < r and 3*r < 2*RHO and (t,r) not in EXCEPTIONAL):
                continue
            K,h = cap_K(q,RHO,t,r)
            if K <= 5*t-2:
                status = "low-dimension"
            else:
                lhs = comb(RHO+K,r)
                rhs = q**(t*(RHO-r))
                status = "ball-binomial" if lhs < rhs else "remaining"
            rows.append((q,t,r,K,h,status))

remaining = [x for x in rows if x[-1] == "remaining"]
print("rho=15 reduced tuples:", len(rows))
print("low-dimension exclusions:", sum(x[-1]=="low-dimension" for x in rows))
print("binomial exclusions:", sum(x[-1]=="ball-binomial" for x in rows))
print("remaining tuples:", remaining)
assert len(rows) == 62
assert remaining == [(2,3,6,78,6,"remaining")]

# Special binary tuple. A counterexample has d_4(C^perp) >= k+2.
# Shorten nine independent coordinates, retaining the other N=k+6 coordinates.
# The resulting binary [N,6] code E satisfies d_4(E)>=N-4.
# Therefore every 2-dimensional subspace of F_2^6 contains at most four
# generator columns, counted with multiplicity (including the zero column).
# There are 31 two-dimensional subspaces through any fixed nonzero point,
# and they pair the remaining 62 nonzero points.
nonzero_points = 2**6 - 1
lines_through_point = (nonzero_points - 1)//2
assert nonzero_points == 63 and lines_through_point == 31

# If zero multiplicity z and multiplicity m at a chosen point satisfy z+m>=2,
# summing the 31 line inequalities gives
# N <= 31*4 - 30*(z+m) <= 64.
line_bound = 31*4 - 30*2
assert line_bound == 64
# If z=0 and every nonzero point has multiplicity at most one, N<=63.
print("binary projective-multiplicity length bound: N <=", max(63,line_bound))

# Hence k+6=N<=64, so k<=58 and original length n=k+15<=73.
kmax = 64-6
nmax = RHO+kmax
assert kmax == 58 and nmax == 73
print("special tuple dimension bound: k <=", kmax, "and n <=", nmax)

# Exact generalized covering-ball inequality for q=2,t=3,r=6,rho=15 requires
# V_8(n,6) >= 2^(3*rho). It already fails at the largest possible n=73.
V = sum(comb(nmax,i)*7**i for i in range(7))
need = 2**(3*RHO)
print("V_8(73,6) =", V)
print("2^45 =", need)
print("strict inequality:", V < need)
assert V == 20282523983828
assert need == 35184372088832
assert V < need
print("PASS")
