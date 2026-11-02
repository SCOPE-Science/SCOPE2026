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
# Reproducibility and scope

Run `python verify.py` using Python 3.9+; no external packages are required. The script computes exact `Fraction` matrix products for multiple rational parameter choices, checks the determinant and trace formulas for all six balanced words, tests exact Schur inequalities against the theoretical thresholds, and verifies two rational witnesses and an exact rational enclosure of the crossover root. The check must be run from the embedded `verify.py` as extracted from the saved scientific package; its terminal success message is reproduced only after actual execution.

These tests establish finite algebraic consistency, not historical originality, arbitrary-word results, nonlinear stability or an infinite mathematical proof. The all-parameter correctness argument is in `RESULT.md`, based on exact algebra, the degree-two Schur criterion and monotonicity. Independent audit has not been performed.
