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

Run `python verify.py` with a standard Python 3 interpreter. The actual run returned `VERIFY_OK exact_or_asymptotic_assertions=21421`.

The program computes exact-rational covariance from the unsimplified sum of indicator covariances and compares it with the claimed compact formula across sample sizes and rational radius grids. It also checks positivity/sign cases, monotonicity on discrete radius grids, the exact negative three-point example, and selected sparse asymptotic comparisons. These are finite consistency checks; they do not certify infinitely many real radii or substitute for the proof in RESULT.md. Independent audit has not been performed.
