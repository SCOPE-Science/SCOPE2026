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

The standalone `verify_cycle.py` checker directly forms the standard-coordinate cycle incidence roots and recomputes Gram determinants over every subset. It compares these sums against an independent coefficient-recurrence calculation for every integer \(3\le n\le9\) and \(1\le k\le n\), giving 42 complete finite cases. It additionally checks the small exact values, the fixed-deletion asymptotic at \(n=500\), and the positive-density local-limit ratio at \((n,k)=(300,120)\). The expected successful terminal marker is `VERIFY_OK`.

All global identities and limiting laws are proved mathematically in RESULT.md; finite arithmetic and numerical convergence checks are diagnostics, not replacements for the proof. Independent audit was not performed.
