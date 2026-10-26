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

Exact identity check: execute `python verify.py` with Python 3 and no third-party packages. The verifier constructs bivariate rational polynomials and asserts the determinant identity, the two trace factorizations, the factor difference identity, and two rational test instances. It prints `VERIFY_OK: four exact polynomial identities and two rational witnesses` on success.

The unbounded-orbit and full boundary conclusions are obtained from the determinant-one Floquet classification and strict monotonicity of the off-diagonal ratio; finite parameter tests do not establish them. The resonant small-modulation limit follows from the trace Taylor expansion and the inverse hyperbolic cosine. No independent audit or higher-dimensional numerical experiment has been performed.
