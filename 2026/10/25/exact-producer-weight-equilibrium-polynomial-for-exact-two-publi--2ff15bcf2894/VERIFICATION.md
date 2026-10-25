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

Run `python3 verify_prism.py` using Python 3 and the standard library. The exact Bareiss determinant checks the 16-by-16 transfer-matrix factorization at 561 grid points. The degree bounds (at most 16 in the first variable and 32 in the second) make this a complete proof of the polynomial identity, not an extrapolation from finitely many prism sizes. Direct enumeration independently tests every profile on prism networks with 3 through 9 rungs, or 349,504 profiles. The proof for all network sizes then uses the trace identity and formal logarithmic expansion in RESULT.md. These checks do not assess every possible alternative game model or guarantee originality against inaccessible literature. No independent audit has been performed.
