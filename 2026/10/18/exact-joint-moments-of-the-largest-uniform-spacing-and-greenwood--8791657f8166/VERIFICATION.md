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
# Reproducible mathematical checks

Run `python verify.py` using Python 3. The implementation uses only the Python standard library (`fractions` and `math`) and checks exact rational binomial-harmonic identities, endpoint and rational-threshold values of the mixed tail polynomial, positive covariance, the positive-definiteness constraint on both variances, and exact mixed moments for every integer size from 2 through 39. The checker also records the separately integrated low-dimensional benchmark values 25/48 for two spacings and 349/1080 for three spacings. An additional numerical experiment with independent normalized exponential variables for dimensions 2, 3, 5, 9, and 25 agreed to Monte Carlo accuracy; random simulation is not a formal certificate.

**Unproved or untested beyond the theorem:** no complete joint distribution, no asymptotic independence claim, no nonuniform-null guarantee, and no independent external audit. The full parameter-range statements are justified by the proof in `RESULT.md`, not by the finite checks.
