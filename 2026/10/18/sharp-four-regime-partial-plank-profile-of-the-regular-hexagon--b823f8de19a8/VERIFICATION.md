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

# Reproducibility and verification

Run `python3 check_hex_planks.py` with Python 3 (only the standard library). Successful output from the actual packaged code was:

`HEX_PLANK_PROFILE_OK fan_clips=2400 orientation_grid=32400 translated=1500`

The script evaluates exact polygon geometry independently of the cap formulas using two oriented halfplane-clipping passes and shoelace area. There are 2,400 seeded random checks for the three cap formulas, 32,400 checks of predicted maxima against an 81-angle grid at 400 widths, and 1,500 checks of centered-strip improvement over translated strips. These are finite diagnostics only.

Symbolic algebra independently verified (with all residuals exactly zero) the derivative formulas for all cap branches, strict monotonicity derivative for the auxiliary \(\kappa\), and continuity at both cap transition boundaries. The proof in `RESULT.md` establishes the global continuum inequalities; no machine or independent theorem certification is asserted.
