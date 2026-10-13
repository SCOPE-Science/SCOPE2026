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

Run `python3 verify.py` with Python 3.10 or newer (standard library only). The finite-case verifier computes the published one-coordinate local dynamics, derives exact binomial likelihood-ratio tails, and compares them to the proposed Gaussian profile at dimensions 512, 2048, and 8192 for critical, fixed overdamped, and near-critical parameters. It also checks positivity/monotonicity at selected time points and the defining scalar critical centering over much larger dimensions. The expected ending line is:

`VERIFY_OK finite_binomial_TV=passed critical_center=passed nearcritical_crossover=passed overdamped_center=passed monotonicity=passed`

## Analytic checks and limits

The infinite-dimensional conclusions do not follow from a finite sample. The proof checks exact local generator normalization and ODE, the unique critical root, uniform finite-crossover expansions at \(\theta=0\), the two exponentially separated overdamped modes, the Gaussian likelihood-ratio comparison for a triangular Bernoulli array, and monotone mixing-time bracketing. The simulation has relatively slow convergence at critical damping; it is not intended to establish a numerical error bound for arbitrary dimensions. There is no independent scientific audit, publication-priority certification or verification beyond the documented mathematical proof and finite calculations.
