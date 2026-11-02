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

The mathematical statement and proof are in `RESULT.md`; `check.py` is a standalone Python 3/SymPy verifier. From a directory containing both files, run `python check.py`. It should print `Exact symbolic/rational assertions passed: 1127` and exit successfully.

The verifier reconstructs the two equiprobable affine scenarios; symbolically checks their mean, variance, cost gap, curvature, and the exact general coexistence threshold; then checks the rational instance's endpoint thresholds, discriminant, two root formulas, and all boundary factorizations. Independent exact rational root-counting covers every phase and the boundary cases. A seeded rational parameter test checks the general strict-intercept interval against endpoint Wardrop conditions and counts the unique mixed root when both pure endpoints are strict. All displayed full-parameter claims are proved algebraically in `RESULT.md`; checking finitely many rational inputs alone would not establish them.

The result is not independently audited and does not claim empirical validity, stochastic-dominance consistency of mean-plus-variance preference, or uniqueness under unrelated risk criteria. Literature priority is limited to the specifically identified works and comparisons.
