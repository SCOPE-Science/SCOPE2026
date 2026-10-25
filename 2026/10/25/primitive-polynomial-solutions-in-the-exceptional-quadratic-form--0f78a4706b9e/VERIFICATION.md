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

Run `python3 verify.py` with Python 3. The script uses only the standard library and checks the conic identity and both square identities as exact sparse multivariate polynomials with integer coefficients; the observed output is `VERIFY_OK`. The proof supplies the all-parameter coprimality argument and is not replaced by finite tests. The claim applies to every integer \(c\) and every nonzero integer \(n\), and only to the exceptional quadratic-form family stated in `RESULT.md`.

The trusted importer initializes absent external channels as unperformed; research never assesses/authors them or resets old evidence.
