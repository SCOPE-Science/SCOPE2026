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

# Reproducibility checks

Run `python check_coherence.py` in a Python environment with NumPy and SciPy. The program independently calculates one-source phase coherence using the exponential of the complex two-state Markov generator and compares it with the closed form. The Gaussian benchmark is compared with numerical integration of its covariance. Numerical grid tests cover parameters both below and above the proven sharp boundary, several source counts, and the analytic post-zero envelope bound.

The program was executed successfully and reported 3229 passed deterministic comparisons/inequalities. These computations neither explore all parameters nor validate the universal quantifiers; the full proof is in `RESULT.md`. The code uses only its own stated input formulas, requires no external files, and has no stochastic sampling.

The review of mathematical correctness, originality and value was not an independent scientific audit.
