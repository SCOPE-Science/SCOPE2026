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

The standalone `verify.py` uses SymPy and NumPy and reproduces the recorded `verify_output.txt` when executed in an environment with those packages. It constructs the exact five-dimensional state transition matrix from the specialized original recurrence, symbolically verifies the characteristic polynomial, checks selected thresholds, and samples 300 deterministic parameter combinations to detect mistakes. It also compares fixed-time trajectories for constant history to the independently derived continuous exponential solution.

The general Schur stability theorem follows analytically from the three quadratic inequalities in `RESULT.md`. Numerical samples are consistency checks only; they do not prove a universal quantifier. Symbolic factorization verifies polynomial algebra and does not verify that the original operator specialization is appropriate; that derivation is displayed in `RESULT.md` and compared to equation (5.4) of the primary source. The code does not establish novelty or extend the model to PDE discretizations.

Independent audit has not been performed.
