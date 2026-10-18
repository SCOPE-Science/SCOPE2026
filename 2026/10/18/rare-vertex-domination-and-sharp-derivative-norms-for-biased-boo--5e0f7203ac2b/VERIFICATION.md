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

# Verification

The reproducible script `check.py` uses only the Python standard library, notably `fractions.Fraction`, to produce all finite-matrix entries and their derivatives exactly, avoiding floating-point tolerances.

Execute `python check.py` to run 1,698 exact checks: heterogeneous Bernoulli marginals at five parameter values, all derivative orders up to full finite degree and all input rows, plus independent homogeneous binomial finite-difference formulas and peak-mass formulas through eight coordinates. It prints `PASS 1698 exact rational comparisons` if successful.

A separate high-\(n\) floating-point diagnostic was performed for the first derivative, comparing two interior biases/correlations at sizes 100, 1000, 10000 and Poisson edge values \(\lambda\in\{0.5,1,1.25,2,2.3\}\) at sizes 5000 and 20000; all ratios approached one. These diagnostics are not proofs of asymptotic limits.

The full unrestricted proof is the stochastic-channel construction, signed kernel contraction, binomial differentiation, and Gaussian-Hermite/Poisson limiting argument in RESULT.md. Parameter endpoints are handled by one-sided polynomial differentiation. No externally performed or independent audit has been carried out.
