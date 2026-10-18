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

# Verification of the conditional phase-selection theorem

The standalone `verify.py` uses `fractions.Fraction` and polygon clipping, not floating-point simulation, for all finite-level first-entry and capture areas. For each integer \(3\le n\le18\), it independently constructs the lower-branch survivor triangle, first-entry polygon, and its portion entering the exact permanent upper trapping strip. It checks the survivor area \(2/(a_{n-1}b_{n-1})\), the first-entry area as the difference of consecutive survivors, and strict positivity of both captured and uncaptured portions.

The last ratios agree with the analytic limit to within the declared floating-point tolerances; exact upper-branch eigen-coordinate relations and cancellation of signed-phase biases are also checked. Running the extracted package script as `python verify.py` produces `VERIFY_OK`. The script is a reproducibility and error-detection aid only; it does not enumerate every initial condition for every \(n\), establish historical priority, or constitute an independent audit. All infinite and universal assertions rely on the proof in `RESULT.md`.
