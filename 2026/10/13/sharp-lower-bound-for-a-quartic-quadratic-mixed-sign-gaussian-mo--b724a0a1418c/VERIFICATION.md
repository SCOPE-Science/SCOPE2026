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

# Reproduction and limitations

Run `python3 VERIFY.py` using Python 3 and its standard library. The script's exact-rational checker validates 207 identities and moment comparisons. It independently expands \(Y^4Z^2\) against even moments of three Gaussian coordinates after the negative-power tilt and checks agreement with the matrix representation. The continuous theorem is proved in `RESULT.md` by a polynomial factorization and positivity argument, not inferred from finite numerical cases. The condition \(0<u<1\), unit variances, and Gaussianity are essential to the stated proof; the excluded parameter endpoints and other powers are not covered. A singular covariance is allowed to attain equality; positive-definite approximants approach it.
