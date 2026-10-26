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

# Reproducibility and boundaries

Run `python verify.py` with the standard Python 3 library and compare its complete JSON stdout with the packaged `certificate.json`. The verifier uses exact fractions, enumerates all binary hidden and observed paths for three seasons, computes observed moments independently of the reconstruction identities, and verifies exact recovery for 12 admissible interior parameter choices, one involving negative temporal memory. It additionally constructs two distinct strictly interior parameter vectors sharing all six observed first and pairwise second moments when the outer detection rates coincide.

The mathematical proof is in `RESULT.md`; finite tests are consistency evidence only. The standalone code has no third-party dependencies. The empirical precision of moments inferred from finitely many surveyed sites is not assessed. No external or independent audit was performed.
