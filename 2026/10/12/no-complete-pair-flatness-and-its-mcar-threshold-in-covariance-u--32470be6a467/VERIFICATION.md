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
The included `verify.py` checks the algebraic and numerical consequences of the complete-pair trace identity under a fully specified synthetic missingness mask.

For \(n=6\) and \(p=2\), every row has one missing coordinate, all 15 unordered row pairs are active, the frozen-covariance missing-coordinate design has full column rank six, and its column-mean initialization has a strictly positive covariance determinant. Two distinct completions preserve all observed values, yield positive-definite sample covariance, and both give the identical nonlinear Mahalanobis sum \(60\).

For each completion, the program verifies at two positive ridge strengths that the direct pairwise sum equals the eigenvalue formula, while the values can depend on covariance spectrum once ridge is inserted.

For independent cellwise MCAR at \(n=1599\), \(p=45\), and \(q=0.2\), the checker reproduces the exact binomial mask event probability \(0.9976857362296532\) to working precision. It also checks representative numerical regimes on either side of the dimension threshold. The exact general theorem rests on the trace identity and elementary binomial analysis, not on numerical enumeration.

No assertion is made about the exact probability that the completed covariance is invertible for a particular data-generation model; the all-pairs mask event and the invertibility condition are kept distinct.
