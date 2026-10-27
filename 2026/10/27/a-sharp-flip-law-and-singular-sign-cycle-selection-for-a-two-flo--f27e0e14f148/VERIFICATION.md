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

Run `python3 VERIFY.py` using only the Python standard library. On the packaged script, the program prints `VERIFY_OK 2207 checks`. The checks comprise exact-fraction verification of the denominator derivative gap, independently computed symmetric cycles and Floquet multiplier on seeded parameter families, critical-time scaling, matched local-order coefficient, and convergence of the regularized cycle to the sign-map midpoint.

The proof in `RESULT.md` establishes the universal statements. Finite tests are diagnostics and do not certify all parameter values. No external independent audit was performed.
