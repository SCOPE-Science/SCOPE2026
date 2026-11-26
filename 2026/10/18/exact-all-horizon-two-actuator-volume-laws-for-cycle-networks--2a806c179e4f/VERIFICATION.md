---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Writing W=KK^T and changing the state rows to real Fourier coordinates isolates each repeated frequency into a 2-by-2 projected input block with determinant (2/n) sin(2 pi k d/n). A singular block is rank deficient for all time; otherwise factoring it out leaves two independent time-monomial channels. The constant scalar mode is symmetric; on even cycles the alternating mode is symmetric or antisymmetric according to d. This gives the four listed index ranges (and the two in odd order). The products of squared sines follow by pairing conjugate nontrivial roots in the product of 1 minus roots of unity; the gcd obstructions are exactly gcd(d,n)>1 in odd order and gcd(d,m)>1 in even order. Early zeros follow from the column count or the oversized symmetric channel; at sufficient T the moment matrices are positive by distinct-node Vandermonde rank, including lambda=0. The even parity product difference is det(G_E)^2 times the squared inner product of the endpoint residuals, so the comparison is correctly non-strict. As an independent exact check, iterating K from the two coordinate columns using (A v)_i=(v_{i-1}+v_{i+1})/2 and fraction Gaussian determinant on C_6 (a=1,b=1/2) gives at T=4 the determinants 289/262144, 289/262144 and 0 for d=1,2,3. At T=3 the values are 1/4096, 0, 0. This checks the important even-distance threshold and shows that cross-parity equality can actually occur. The frozen verifier was inspected, not executed; its 440 stated exact checks are finite corroboration.

## originality

PASS

The supported distinct content is the full-state determinant factorization and placement comparison across all horizons and both cycle parities, including the even-distance branch at T>=m+1. Earlier rank and volume results and an exact indexed minimum-horizon slice overlap but do not imply the entire classification. This is a scoped comparison, not historical priority or a claim that adjacent controllability was new.

## value

PASS

This solves a natural determinant placement problem, more finely than reachability: it shows exact ties of geometrically different separations, distinguishes full-rank even placements from optimal ones when appropriate, and proves a universal weak parity ordering over all affine parameters and horizons. These are usable design conclusions and not a re-labeling of rank or a numerical best-placement example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
