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

The attached `verify_pattern_covariance.py` uses independent exact fixed-composition enumeration and ordered placement probabilities. On execution it completed `79723` assertions, printed the zero pairs `[(4, 3), (9, 4)]`, and terminated with `ALL_DONE`.

The mathematical proof is the falling-factorial placement identity plus the exact rational simplification and modular divisibility argument in `RESULT.md`. Enumeration is deliberately bounded and cannot establish an unrestricted mathematical statement. The code depends only on the Python standard library. No independent audit has been performed.
