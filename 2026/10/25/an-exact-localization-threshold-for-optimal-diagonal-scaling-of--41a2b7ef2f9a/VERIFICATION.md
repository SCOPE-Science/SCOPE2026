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

The theorem is established by the exact Löwner-averaging argument and a two-dimensional eigenvalue optimization in RESULT.md. The optional standalone `verify.py` uses only Python's standard library, and can be run with `python verify.py`; its deterministic tests cover many numerical nonsymmetric scalings, the optimal two-level scaling, and the exact five-dimensional Jacobi comparison. A finite test cannot certify global optimality; that comes from the proof. Reproducibility is in exact arithmetic apart from these numerical sanity checks. No independent audit has been performed.
