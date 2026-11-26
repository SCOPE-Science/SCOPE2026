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

The frozen unrestricted 'without independence' is false at a=b=1, where R=2 almost surely; the corrected complete RESULT.md is at /workspace/repairs/2/RESULT.md and addresses exactly this case. In all other cases R=2,3 are both attainable, and their strictly different conditional variances prove dependence. Reversal gives the conditional mean for all feasible r and hence zero covariance, including the exception. Given orientation, independent uniform compositions have the stated projected covariance, and the centered linear and bilinear terms are pairwise uncorrelated. In the even case equal orientation weights yield a between-orientation variance (ab/(2k))²; in the odd case the two conditional means agree and the composition counts give weights proportional to a−k and b−k. The variance formulas and positive difference factorizations remain unchanged. /workspace/review_checks/check_2.py independently verified the three rational identities symbolically and checked exact word moments in six cases, including the degenerate independence case. The general proof, not the finite sample, covers every attainable count.

## originality

PASS

Pass for the frozen contribution's finite inversion/run second-moment formulas and the strict adjacent comparisons, retained by the repair. A distinct indexed SCOPE result demonstrably contains essentially the same theorem and proof, including the boundary comparisons, and extends it to the odd subsequence. Its recorded source is later than the bound record; it is not evidence that these formulas were already known when this finding was made, and the comparison does not establish independent discovery or priority between the underlying work. No inspected earlier primary result supplies the area/run variance profile or its ordering. The corrected independence sentence is a consequence, not a new contribution.

## value

PASS

The same two-sample labeling law supports both rank and runs tests. The exact finite conditional variance profile shows that mean independence hides a ubiquitous parity effect, rather than merely exhibiting one small counterexample. Strict comparisons at every feasible interior or boundary pair and the exact degeneracy exception give usable finite-sample information; no value is assigned merely to correcting the a=b=1 sentence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
