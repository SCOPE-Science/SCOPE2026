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

# Reproducible finite verification

Run `python annular_spectral_checker.py` with Python, SymPy and mpmath installed. The checker reconstructs the derivative identity symbolically for each \(1\le k\le14\), locates the three cubic roots on their proved intervals, checks the positive-hump inequality, compares independently integrated annular densities with the boundary formula, and verifies the seven level-set crossing counts using monotone arcs.

The expected output appears verbatim in `verification_output.txt`. All 182 assertions passed. Floating comparisons use explicitly bounded error tolerances; the all-index proof is wholly analytical, and the finite tests do not certify infinitely many indices.
