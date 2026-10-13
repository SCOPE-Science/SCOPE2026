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

# Reproducibility and limitations

Run `python verify_pareto_zeno.py` in an environment with NumPy and SciPy. The script samples conditional survival probabilities, compares first and second moments with the limiting formulas, checks a non-unit amplitude, compares both deterministic regimes, and numerically integrates an independent Fourier identity. The numerical tests passed in the reported run; they use seeded pseudorandomness and fixed finite sample sizes. At the Pareto border exponent two, logarithmically slow finite-size convergence is expected, so the check uses a deliberately conservative tolerance rather than claiming high-precision asymptotics.

The exact all-exponent claims require the direct conditional-product derivation, Pareto variable substitution, Poisson Laplace functional, truncated second-moment variance bound at the critical exponent, and law of large numbers above it. None of these infinite results follows from the finite numerical checks. The infinite-product statement also requires absence of exact cosine zeros and integrability of its logarithm near zero; these are verified analytically in the proof.
