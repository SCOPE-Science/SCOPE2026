---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The finite theorem is analytic for every \(m,n\ge2\) and \(0\le r\le n\).

`checker.py` exhaustively enumerates all allocations for a grid of small \((m,n)\), evaluates the occupancy spectrum, collision count, and Pearson statistic with exact rational arithmetic, and checks every displayed finite covariance. A second exact loop verifies the Pearson variance, the \(K_r\) variance formula, both occupancy-spectrum conservation identities, and singleton orthogonality at \(n=2m\).

A separate numerical loop compares large finite exact formulas with the stated fixed-load limits. These finite and numerical checks are supplementary; the proof in `RESULT.md` establishes the universal finite statement and derives the asymptotic limit symbolically.
