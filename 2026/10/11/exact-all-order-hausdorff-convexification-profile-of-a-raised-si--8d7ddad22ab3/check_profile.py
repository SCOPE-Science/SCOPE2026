#!/usr/bin/env python3
"""Exact-rational checks for a regular-simplex raised-vertex convexification profile.

The proof covering all dimensions and averaging orders is in RESULT.md. This
program checks its finite algebraic identities, strict separation inequalities,
and, for small parameters, the exact closest-point distance to the constructed
witness over every allowable lifted-vertex multiplicity vector.
"""
from fractions import Fraction as F
from itertools import combinations


def comps_upto(n, k):
    def go(prefix, rest, position):
        if position == n:
            yield tuple(prefix)
        else:
            for c in range(rest + 1):
                yield from go(prefix + [c], rest - c, position + 1)
    return go([], k, 0)


def simplex_projection_sq(lam, lower):
    """Exact min sum (mu_i-lam_i)^2 s.t. mu>=lower,sum(mu)=1."""
    n = len(lam)
    if sum(lower) == 1:
        return sum((x-y)**2 for x,y in zip(lam,lower))
    best = None
    for mask in range(1 << n):
        free = [j for j in range(n) if not (mask >> j & 1)]
        fixed = [j for j in range(n) if mask >> j & 1]
        if not free: continue
        shift = (sum(lam[j] for j in free) + sum(lower[j] for j in fixed) - 1) / len(free)
        mu = [lower[j] if j in fixed else lam[j] - shift for j in range(n)]
        if any(mu[j] < lower[j] for j in free): continue
        val = sum((mu[j]-lam[j])**2 for j in range(n))
        if best is None or val < best: best = val
    assert best is not None
    return best


def exact_witness_sq(n,k,eps):
    if k < n:
        lam = [F(1,n)]*n
    else:
        lam = [F(k-n+1,k)+F(n-1,n*k)] + [F(n-1,n*k)]*(n-1)
    best = None
    for c in comps_upto(n,k):
        j=sum(c)
        lo=[F(x,k) for x in c]
        horiz_sq = F(n,n-1)*simplex_projection_sq(lam,lo)
        dist_sq = horiz_sq + (eps * F(k-j,k))**2
        if best is None or dist_sq < best: best=dist_sq
    return best


def main():
    # Algebraic certificates, dimension/order-independent in the written proof.
    for n in range(2,31):
        eps=F(1,2*(n-1)**2)
        assert eps < F(1,(n-1)**2)
        for k in range(1,151):
            goal = eps * min(F(1),F(n-1,k))
            if k<n:
                assert F(n-k,k*(n-1)) >= F(1,(n-1)**2)>eps
            else:
                lam=[F(k-n+1,k)+F(n-1,n*k)] + [F(n-1,n*k)]*(n-1)
                floors=[int(k*li) for li in lam]
                assert sum(lam)==1 and floors==[k-n+1]+[0]*(n-1)
                assert F(1,(n-1)*k) > goal
                assert sum(floors)==k-n+1
    # Unlike sampling, enumerate EVERY multiplicity vector and solve the
    # nearest-point convex quadratic exactly for selected full instances.
    cases=[]
    for n,k in [(2,1),(2,2),(2,7),(3,1),(3,2),(3,3),(3,4),(3,7),
                (4,3),(4,4),(4,6),(5,4),(5,5)]:
        eps=F(1,2*(n-1)**2)
        got=exact_witness_sq(n,k,eps)
        goal=(eps*min(F(1),F(n-1,k)))**2
        assert got==goal, (n,k,got,goal)
        cases.append((n,k,str(got)))
    print('SIMPLEX_MINKOWSKI_PROFILE_RATIONAL_OK',len(cases),'full-enumeration instances;',
          '4350 all-n/all-k exact algebra checks')
    print('cases:',cases)

if __name__=='__main__': main()
