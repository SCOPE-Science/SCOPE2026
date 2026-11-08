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

Run `python3 verification/check_demicube.py` with Python 3.10 or later. It requires no third-party packages and returns `EXACT_OK 7927`. The exact-fraction checks cover dimensions four through eight, partial facet families, selected exact rational combinations, all tied nearest witnesses encountered, and the three-dimensional simplex boundary. The universal conclusion is proved by the inequalities and facet argument in RESULT.md; a finite checker cannot establish it for unbounded dimension. No independent mathematical audit has been performed.
