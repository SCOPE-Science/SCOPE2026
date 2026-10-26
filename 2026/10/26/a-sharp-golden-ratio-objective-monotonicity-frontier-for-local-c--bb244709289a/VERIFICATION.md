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

# Reproducible verification

Run `python3 verify.py` with Python 3.9 or newer; no external libraries or network are needed. The script checks the two piecewise formulas, witnesses in both regimes, the condition-number boundary, 6006 endpoint-grid objective ratios and 3200 reproducible higher-dimensional samples.

Proof dependencies are entirely in `RESULT.md`: the exact LCD3 step, the spectral chord inequality, the algebraic rational envelope and its derivative, and explicit attainment by a two-eigenspace mixture. Finite checking cannot certify the supremum, infinite-dimensional extrapolations, prior-work uniqueness, or convergence of successive LCD3 steps. No independent audit has been conducted.
