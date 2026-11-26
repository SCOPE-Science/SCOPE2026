---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write K=3-M_0. The product of means uses binomial marginal probabilities; the joint term sums only distinct boxes, with the unused mass (1-p_i-p_j)^{n-r}. At r=n a zero mass to the zero power means there are no remaining allocations, so the factor is one. The common binomial and denominator factors are positive, leaving the sign of H. Independent ordered-allocation dynamic programming produced all fourteen signs ++++-+++++---- at n=14. Separate integer maximization of the positive and negative bases reproduced the four displayed pairs and checked that the certified ratios to the powers t,2t,2t,t exceed the appropriate opposing term counts 6 or 9 already at t=15. Since all ratios exceed one, this proves the signs for every later integer t. The strict inequalities persist simultaneously by continuity after normalization of the positive weights (the max of finitely many continuous bases is continuous), preserving the same lower bounds and hence the same cutoff uniformly. Two boxes have M_0 M_r=0 for r<n and positive means of M_0 and M_r; M_n=M_0 gives strict negative covariance at n for n>=2 and positive box probabilities. One box has constant K. The infinite claim is at least three sign reversals witnessed by the sampled signs (sign variation ignoring zeros), not an exact sign sequence or a claim of exactly three switches for all large n. Replay: python3 -B /workspace/branches/frozen_review_replay.py 4. Frozen script inspected, not executed.

## originality

PASS

The elementary multinomial moment identity is not new. The strongest local overlap is a distinct later-path finite three-species witness with different probabilities and n, and the same minimum box count. Neither it nor the earlier homogeneous law gives the quantitative robust infinite family, and no exact three-box match was found in the inspected primary passages. Path dates establish neither provenance nor priority; this pass concerns the materially stronger distinct persistence claim with its stated finite certificate and scope.

## value

PASS

The result tests whether a natural uniform one-switch law is stable when box probabilities differ. The three-box boundary is minimal and the exact signs show that failure is neither a finite-n accident nor restricted to one exceptional vector. The dominant-base bounds supply an explicit cutoff and common-neighborhood stability, not just isolated enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
