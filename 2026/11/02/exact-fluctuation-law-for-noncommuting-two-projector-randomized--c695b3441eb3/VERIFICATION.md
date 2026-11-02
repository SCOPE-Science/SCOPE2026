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

Run `python verification/check.py` in the extracted package directory. The verifier uses Python standard library only and tests rational projector resolvents, all equiprobable sign paths through seven steps at nine parameter settings, exact mixed moments, and 45 finite-refinement comparisons to the proved leading coefficient. Output beginning with `PASS` indicates the checks succeeded.

These calculations support, but do not replace, the parameter-uniform analytic proof. They do not constitute an independent audit or independent verification of the infinite-step limit.
