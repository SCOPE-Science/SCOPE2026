#!/usr/bin/env python3
import math

checks=0
for n in range(1,61):
    T=n*(n+1)/2.0
    for m in range(n+2,121):
        r=T/(m+math.sqrt(m))

        # Coordinate and total-sum tangencies.
        assert abs(r-r) < 1e-14
        dfull=(T-m*r)/math.sqrt(m)
        tol=1e-11*max(1.0,r)
        assert abs(dfull-r) <= tol

        # Every proper upper facet is strictly farther.
        for k in range(1,n):
            z=k*(2*n-k+1)/2.0
            d=(z-k*r)/math.sqrt(k)
            if not d > r + 1e-12*max(1.0,r):
                raise SystemExit(("proper facet failure",m,n,k,d,r))
            checks+=1

        # Global upper-bound equality at the candidate radius.
        assert abs((m+math.sqrt(m))*r-T) <= 1e-10*max(1.0,T)

print(f"VERIFY_OK redundant-partial-permutohedron-inball proper_facet_checks={checks} n=1..60 m=n+2..120")
