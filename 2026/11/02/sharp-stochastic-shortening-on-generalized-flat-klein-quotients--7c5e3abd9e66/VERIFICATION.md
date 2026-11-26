---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The theorem follows from the analytic proof in `RESULT.md`, including the independent horizontal costs, integration over the vertical gap, and the two limiting period families at fixed horizontal dimension. The unchanged `check.py` can be run with Python 3 without third-party packages. It contains sample checks on the direct deck minimum and cutoff in higher dimensions. Its ordinary-bottle integral and regularity checks are contextual comparisons only, not claims of the narrowed result. Finite samples and numerical quadrature cannot establish the universal statements.
