---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Cox–de Boor stencil has identity endpoint rows, first and last interior diagonals 5/8, and pure interior diagonals 3/4. In particular the n=2 middle equations persist with no pure interior rows. Checkerboard conjugation gives a positive diagonal minus a nonnegative matrix with strictly subunit row sums after diagonal scaling, so the inverse is nonnegative by the Neumann series and its row sums give the absolute inverse row sums. Endpoint values are 1. Subtracting 2 from the other row sums leaves the homogeneous recurrence with roots q and q^(-1), and the reflected boundary equations give multiplier (sqrt(2)-1)/(1-q^n) on q^(j-1)+q^(n-j). Symmetry and strict convexity give only j=1,n as maxima; alternating data attain all row sums in modulus and work over either field. The correction is positive and strictly decreasing, and the n=2 equations give 5/2. For the cardinal comparison, the checkerboard row-sum equations have ghost values z_0=z_(m+1)=0 and solution z_j=2-2(q^j+q^(m+1-j))/(1+q^(m+1)); hence strict inequality at finite m and convergence in the middle. Independent exact rational Cox–de Boor and Gauss–Jordan checks at n=2,3,4 yielded maxima 5/2, 17/7, 29/12, with the correct positions and alternating witness.

## originality

PASS

Best of current knowledge: exact coefficient recovery, its maximizing positions and the finite boundary correction are distinct from the strongest actual statement matches. The cardinal reference and the later same-stencil spectral result are not equivalent inverse max-row-sum statements. The Marsden risk remains explicitly unresolved.

## value

PASS

The coefficient max norm is the worst amplification of bounded sampling error into control coefficients. The exact formula distinguishes the persistent clamped excess sqrt(2)-1 over the cardinal limit, identifies the two coefficients responsible, and gives the sharp bound 5/2 including the minimal mesh. This is a natural finite-size stability benchmark for the standard clamped discretization, not an arbitrary slice or just a bound from diagonal dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
