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

# Reproducibility and verification
Execute `python verify_triac.py` with Python 3, NumPy and SciPy available. Integer-pair arithmetic in \(\mathbb Z[\varphi]\) checks 32,768 signed sums, 105 spherical-arrangement pair intersections, distinctness of all extremal rays, 20 nonzero generator triple products and the four pair-cosine classes with exact comparisons. Separately, two-dimensional projected convex hull areas from 64 generator sums agree with the determinant area identity for 100 independently sampled directions, and 2,000 random directions satisfy the exact sharp inequalities up to floating-point tolerance. The analytic spherical identity (2) and the classification of extrema require the mathematical argument in RESULT.md in addition to any code results. No independent mathematical audit has been performed.
