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

# Reproducibility

Run `python checker.py` from a standard Python 3 installation. The script uses only standard-library exact rational arithmetic and enumerates all competing words for the documented small parameters. It verifies stochastic matrix entries, determinants, direct matrix-product scores, unique optimum gaps, the rational common-denominator bound, and the enumerative formula. `check_output.txt` contains a reference result from an actual run.

The proof in `RESULT.md` does not rely on finite extrapolation: the upper-envelope switching and perturbation estimates hold for arbitrary finite alphabets and word lengths. Finite tests do not independently establish originality or an infinite theorem. Independent audit has not been performed.
