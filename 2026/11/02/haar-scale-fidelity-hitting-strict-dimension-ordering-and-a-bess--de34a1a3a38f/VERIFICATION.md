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

# Reproducibility and limits

Run `python verify.py` with Python 3 and its standard library. An execution of this exact script returned `PASS: 927 exact-rational coefficient identities, strict comparisons and bounded numerical checks.`

The checker evaluates positive rational Taylor coefficients of the finite-dimensional hitting-transform function, verifies their exact second-order differential-equation recurrence at multiple dimensions and degrees, proves selected coefficient and mean inequalities by exact fractions, and tests the moment and finite-size-correction identities numerically at specified bounded parameters. The exact domain is the projective Brownian radial generator with fidelity initially zero, positive fixed diffusion coefficient, integer dimension at least two, and a target less than one.

The script **does not** enumerate every dimension, prove monotonicity of complete infinite sums, prove convergence in distribution, or certify either infinite limit. Those are analytical conclusions in `RESULT.md`, with the positive power-series comparison, dominated convergence and the large-threshold product bound providing the needed reasoning. Numerical tests are only independent finite consistency checks for calculations that also have explicit proofs. The original Brownian model and generic CIR/Kummer first-hitting methods are prior literature, not independent certifications. No independent audit has been conducted.
