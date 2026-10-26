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

Run `python verify.py` with Python 3, SymPy, and mpmath installed. Successful output is `PASS 204 exact/symbolic/high-precision checks`.

The script checks exact beta integrals in 32 integer effective dimensions, five moments in each dimension, a symbolic derivative inequality, seven high-precision noninteger integrals, and four asymptotic cases. The continuum-dimensional and real-exponent claims depend on the analytical proof, not finite testing. No formal proof assistant or external mathematical audit is claimed.
