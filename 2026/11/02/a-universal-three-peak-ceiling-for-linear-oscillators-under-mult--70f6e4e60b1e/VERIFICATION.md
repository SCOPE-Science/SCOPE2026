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

The claim is proved in `RESULT.md` by the exact derivative identities, monotonicity of expectations under positive Stieltjes weights, and the strictly negative large-frequency derivative limit. No formalized theorem prover or independent auditor is claimed.

Execute `python verify_spectral_bound.py` in an environment with NumPy and SciPy. The code runs independent state-space frequency-domain matrix inversions, checks the Stieltjes spectral expression, inspects the derivative-sign invariant for finite random ensembles, and verifies a mathematically exact witness with two positive critical squared frequencies. The checker uses finite random samples and must not be mistaken for an exhaustive argument.

At the tested parameters the independent frequency-domain transfer comparisons numbered 1080, with maximum relative difference below \(10^{-13}\). The monotone normalized derivative was sampled at 248262 neighboring pairs; sampled critical-point counts never exceeded two. The sharp one-noise example has positive critical squared frequencies near \(0.34064583403484\) and \(0.95935416596516\).

Limits: historical priority has not been independently certified; the model requires nonnegative exponential covariance mixtures and a single scalar linear oscillator. Results for signed/cross-correlated, oscillatory or non-exponential kernels cannot be inferred.
