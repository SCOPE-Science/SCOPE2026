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

The included `verify_cycles.py` performs exact rational root-bracketing and outward-rounded rational interval arithmetic, certifying the active branch inequalities, return-map eigenvalue intervals, and strictly contracting primal period factors. Run `python3 verify_cycles.py` from a directory containing the script. All assertions pass when the script reports `PASS`.

The algebraic proof in RESULT.md is separate from numerical checks. The certificate does not prove attraction, a complete census of possible stepsize cycles, or publication priority; no independent audit has been conducted.
