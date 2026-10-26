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

Exact state and polynomial-vector action checks are in `verify.py` (Python 3 standard library only). The script verifies all 12 states for each modulus, both annihilating polynomials, the rational generating function identity, and a separate comparison with original Stern shells. The universal recurrence and oscillation conclusion also use the algebraic and analytic proof in RESULT.md; finite shells alone are not a proof. Independent audit not performed.
