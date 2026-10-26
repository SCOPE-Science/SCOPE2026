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

# Reproducibility

Run the included `verify.py` with `python3 verify.py` in a clean Python 3 installation. It requires no third-party packages. It prints `VERIFY_OK` if all exact characteristic-three polynomial-identity and sample rational-fiber tests succeed.

The proof of completeness and the assertions for every algebraically closed characteristic-three field are the explicit algebraic arguments in `RESULT.md`; the verification script checks the critical universal identity in a polynomial ring and three finite-field specializations, and does not purport to enumerate an infinite field. Independent external audit has not been performed.
