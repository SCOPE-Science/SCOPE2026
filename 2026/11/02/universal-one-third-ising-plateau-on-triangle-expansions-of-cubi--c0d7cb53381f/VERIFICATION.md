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

The theorem is proved analytically in `RESULT.md` by exact bond decompositions, counting lower bounds, and a perfect-matching construction attaining each bound. `verify_ground.py` checks every spin configuration for the expanded complete four-vertex graph and expanded triangular prism, and separately counts the truncated-cube ground-state orientation classes. `verify_cube_full.cpp` runs an independent exhaustive Gray-code enumeration of all \(2^{24}=16777216\) spin states of the truncated cube. The commands and completed output are in `CHECKS.txt`; execution succeeded without discrepancies.

The arbitrary-size statement is not certified by finite computation; its proof is the edge-and-triangle counting argument. This is self-review, not independent audit or external certification. No assertions concern finite temperature, variable bond strengths, or cubic graphs without a perfect matching.
