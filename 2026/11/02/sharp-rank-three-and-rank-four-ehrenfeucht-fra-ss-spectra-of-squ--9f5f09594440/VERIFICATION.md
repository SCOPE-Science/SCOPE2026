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

# Reproducibility

The rank-three classification can be checked directly from the pair-extension table in `RESULT.md`: count ordered differences of two elements of \(\{-2,-1,1,2\}\) modulo \(n\), and evaluate positivity of the common, exclusive and neither-neighbour counts. The row for all sizes at least eleven is derived symbolically. No execution of a supplied program is necessary to establish the finding.
