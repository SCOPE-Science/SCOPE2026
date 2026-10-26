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

# Reproduction and limits
Run `python verify.py` using Python 3 with NumPy and SciPy. Checks performed include 300 numerical Lyapunov/propagator/antisymmetry/KL/aliasing comparisons over independent positive rates and random rotations/projections, 240 additional zero-normal-projection reversibility checks, and 100 small-time pairwise information-rate comparisons. Random seed: 20261024. All tested assertions passed. An independent algebraic 2-by-2 Gaussian block test was also compared in 500 random positive-definite cases and passed to floating-point precision.

The infinite parameter classification is justified by the displayed exact Rodrigues matrix identity, the Gaussian covariance criterion for path reversal, the entropy-production current integral, and the exact block-inverse formula. Finite numerical checks cannot establish novelty or substitute for the analytical arguments. No independent scientific audit has been performed. The full text of one related nonreciprocal-information article was unavailable, leaving a residual priority question.
