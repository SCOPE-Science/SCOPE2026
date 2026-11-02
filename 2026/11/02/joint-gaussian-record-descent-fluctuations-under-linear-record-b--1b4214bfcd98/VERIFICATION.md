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
# Verification and reproducibility

Run `python3 checker.py` with Python 3.9 or later. It uses only the standard library (`fractions`, `itertools`, `math`). The checker enumerates all permutations of sizes 2 through 7 for each of four rational weights, and compares exact weighted averages to the formulas for single and consecutive descent probabilities, both expectations, both variances, and record–descent covariance. It also makes asymptotic numerical probes for the positive ratios 1/2, 1 and 2 at sizes 300, 1000 and 3000, and tests positivity of the proposed limiting covariance determinant. A normal output is `PASS: 318 exact identities and asymptotic probes; 23648 enumerated weighted permutations`.

The exact symbolic formulas and all quantifiers appear in RESULT.md. The finite computations are sanity checks rather than an infinite certificate. The central limit theorem follows from independence of the rank code, exact local moments, positive definiteness and independent-block Lindeberg argument. External mathematical validation has not been performed.
