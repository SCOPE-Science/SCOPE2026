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

# Verification and reproducibility

Run `python3 verify_escape.py` with Python 3 standard library. It performs exact-rational interval intersection and inverse-image iteration, avoiding floating-point rounding. Recorded output:

```text
VERIFY_OK closed_form_cases= 315 upper_edge_cases= 4 max_exact_horizon=34
```

Nine rational hole parameters cover the subcritical, threshold and supercritical-within-window regimes at integer horizons from zero through 34. Four rational parameters just outside the window verify the independent two-step expression and its strictly positive excess. This procedure is a finite consistency test. It does not establish the theorem for all real parameters or all times; those quantifiers follow from the explicitly justified inverse-branch inclusions and the closed recurrence in the proof.

The map is discontinuous at the middle point, which lies strictly inside the excluded hole for every parameter used. Measure-zero endpoint choices do not affect any check. No independent scientific audit has been performed.
