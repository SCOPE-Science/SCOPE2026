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
The short-radius formula follows from the exact midpoint change of variables, a uniform positive chord-root inversion, and integration of a periodic second derivative. For a unit circle, exact arcsine expansion checks both correction coefficients. The Python 3 script `space_curve_distance_check.py` (NumPy and SciPy) gives independent computational checks using an exact trigonometric chord for a nonplanar closed four-dimensional loop and direct numerical arclength derivatives of embedded wavy circles. Example outcomes: the nonplanar fifth coefficient is 0.0003922254585; a scaled finite-radius remainder at radius 0.12 is 0.000392909797, converging as radius decreases. The wavy-circle value divided by frequency moves toward the asserted constant \(-1/(1440\pi)\). The numerical experiments are finite corroboration and do not prove a universal asymptotic; the analytic derivations are in `RESULT.md`. No independent audit has been performed.
