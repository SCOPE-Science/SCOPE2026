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
# Verification of Gaussian directional-width crossover

The accompanying `verify.py` is standalone, using Python 3 with NumPy and SciPy. Invoke `python verify.py` from a directory containing that file. It computes the exact finite support maximum by enumerating each permitted graph edge and each diagonal vertex, comparing the result with the four-term formula, and checks that translating normals into the two-block zero-sum tangent space preserves width.

The checker also tests the logarithmic centering expansion at progressively larger log-sizes, compares the explicit limiting CDF integral with independent Gumbel Monte Carlo draws, and tests the diagonal-versus-cross type decision. Successful local execution returned `VERIFY_OK support= 602 asymptotic_shifts= 15 cdf= 5 angular= 360`.

These checks do not certify uniform integrability, asymptotic joint independence, or the limit theorem. Those are established in the mathematical argument through Gaussian pair-exceedance estimates, Mills bounds, and chi-radius concentration. Independent review has not been performed.
