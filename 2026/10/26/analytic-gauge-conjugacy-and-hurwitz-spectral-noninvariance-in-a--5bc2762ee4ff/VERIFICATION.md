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

Run `python3 verify.py` with the standard Python library. The checker uses rational arithmetic to obtain the characteristic coefficients and Routh-Hurwitz determinant at the exact witness, and checks the analytic conjugacy differentiation identity on nine deterministic vectors. Its finite numerical tests only corroborate the identity; the displayed algebraic proof establishes the universal result. The global pointwise Hurwitz property of the positive parameter reference member is Theorem 1/Lemma 3 of the cited 2026 primary paper. This reference's large global discriminant computation is not replayed here. No independent audit was performed.
