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

The claim is proved for all integers \(n\ge3\) by adjunction, geometry of a general pencil and local ordinary-node analysis. The first-jet class and Euler characteristic computations agree algebraically.

Run `python3 verify_dual_unprojection.py` (stdlib only). On execution, the exact checker returned `VERIFY_OK: independent coefficient-extraction and closed forms agree for 99 values n=2..100; Euler-fibration, genus parity, exceptional nodal contribution, and four base examples all check.`

These finite comparisons are auxiliary, not a proof for all parameters; genericity of the pencil and conormal birationality are proved geometrically in RESULT.md. No independent expert or external audit has been performed.
