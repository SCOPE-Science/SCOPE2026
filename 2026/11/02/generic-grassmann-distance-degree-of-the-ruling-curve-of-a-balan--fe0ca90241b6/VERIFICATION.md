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

Run `python3 checks/verify.py` using Python 3 and its standard library. With its fixed seed and the prime 1000003, the checker tests 18 pairs of degrees and ranks. It computes each numerator and its Wronskian, checks the expected polynomial degree and squarefreeness, verifies the coprimality with the denominator and cut factors, and computes the augmented Jacobian rank to cross-check the dominance mechanism. Observed output ends with `VERIFY_OK`.

The finite-field checks are evidence for the algebraic identities and help detect mistakes; they are not an exhaustive proof in n and d, nor do they prove that a polynomial vanishes identically in characteristic zero. The uniform assertions follow from the characteristic-zero coprimality, differential-dominance and generic-open arguments in RESULT.md.

No independent audit or external certification has been performed.
