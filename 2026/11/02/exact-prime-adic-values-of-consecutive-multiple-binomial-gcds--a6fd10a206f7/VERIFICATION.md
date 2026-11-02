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

The executable `verify.py` computes exact base-prime carry counts rather than calling the symbolic formula, and checks all multipliers for small inputs plus the constructed minimizing multipliers. It also computes direct integer gcds of binomial coefficients for smaller cases. Run `python3 verify.py` with Python 3 standard library. The infinite result depends on the explicit carry proof, not on finite enumeration; priority has not been independently assessed.
