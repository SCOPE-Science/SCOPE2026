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

# Reproducibility and mathematical limits

Execute `python verify_cycle.py` with Python 3, without third-party libraries. The script performs 648 exact rational matrix trace identities (eight values of the weighting parameter and 81 rational nonnegative weight quartets), compares rational candidate branches, and checks a finite simplex grid. Successful output includes `CYCLE_WEIGHTED_SCHATTEN_FOUR_EXACT_TRACE_AND_GRID_CHECK_OK 648`.

The decisive claims are proved in `RESULT.md`: (i) a trace expansion with the phase-sensitive winding term, (ii) strict negative definiteness in the opposite-pair product variables away from the central parameter, (iii) exhaustive corner and scalar branch comparisons, and (iv) direct endpoint control. The finite checker does not establish any continuum uniqueness or global theorem by enumeration. No machine-checkable infinite proof or independent validation is claimed.
