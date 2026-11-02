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

# Verification scope

Run `python verify.py` from this directory using Python 3.9 or later. The checker independently constructs Stirling-permutation plateau masks by adjacent-pair insertions and ordered-tree leaf masks from increasing parent arrays weighted by their number of child orderings. The two complete distributions agree through seven nonroot vertices (the largest sample has \(135135\) ordered trees). It then verifies exact joint-survival products for every subset of labels, the pairwise covariance products and signs, total leaf means and exact variances, together with additional finite exact recurrence checks through forty vertices.

The all-size claims are established by forbidden insertion-gap counting, rational product factorization, logarithmic product asymptotics and dominated Riemann-sum convergence in `RESULT.md`. The executable evidence is finite corroboration only; it is not an infinite proof. No external or independent audit has been performed. The quantitative priority assessment is necessarily limited by accessible historical literature.
