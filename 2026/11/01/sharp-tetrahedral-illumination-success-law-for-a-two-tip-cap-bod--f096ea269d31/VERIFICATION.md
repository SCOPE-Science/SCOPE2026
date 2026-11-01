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

# Reproducibility and boundaries

Run the included `verify.py` under Python 3 with NumPy, SciPy and mpmath. The checker computes the exact tetrahedral inner-product matrix, threshold trigonometry and endpoint value; independently integrates a spherical-coordinate formula for each lens; verifies the critical power law using high precision; and compares six probabilities with seeded uniform-axis samples (280,000 axes). Successful diagnostic execution is not a replacement for the all-parameter analytic proof in `RESULT.md`. No independent mathematical audit has been performed. No covering formula is claimed on the intermediate overlap-rich radius range.
