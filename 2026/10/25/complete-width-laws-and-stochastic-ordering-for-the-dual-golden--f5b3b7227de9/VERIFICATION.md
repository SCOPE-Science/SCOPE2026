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

Run `python3 verify_golden_widths.py` beside these files. The Python-standard-library program independently enumerates the Cartesian vertices of both Platonic solids, draws 220,000 isotropic directions for each, and compares direct support maxima with seven analytically predicted survival probabilities per solid. It also verifies all support and transition boundaries, the exact common-normalization geometry, a 1,999-point ordering grid, the analytic order derivative conditions, and both lower-tail constants. The proof of global stochastic order, including the uncountable set of thresholds, is in `RESULT.md` and is not inferred from the grid test.

Direct numerical checks completed successfully. The integral formula for spherical segment loss and the analytic sign argument are mathematical parts of the proof, not computer-generated external certificates. There has been no independent mathematical audit.
