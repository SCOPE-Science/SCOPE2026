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

The reproducible check is `python3 verify_model.py` with Python 3 standard library only.

The script implements the exact count-state recursion using weights \(ab,ac,bc\), a separately constructed labeled-vertex recursion, and direct exhaustive permutations of all graph edges on three small instances. It checks 16 count-vs-labeled distributions, 40,446 exhaustive edge orders and 855 rational total-variation inequalities. Its observed outcome was PASS, without exceptions. Small-case checks corroborate the finite combinatorics; the survival product, coupling and limit arguments are proved mathematically in RESULT.md, not inferred from these computations.

The comparison literature may not exhaust all earlier formulations. No independent audit or external validation has been conducted.
