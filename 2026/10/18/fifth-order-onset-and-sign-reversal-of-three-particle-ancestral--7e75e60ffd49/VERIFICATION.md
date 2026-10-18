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

# Exact verification and limits

Run `python check_fv_quintic.py` with SymPy. The script constructs the count-chain and founder matrices directly from the transition rules with exact rational entries, replaces one stationary and one founder equation by their justified normalizations, and inverts the two augmented constant matrices. For every Taylor order from zero through seven, it checks the full unmodified stationary and founder equations as exact matrix identities, their normalizations, and the current convolution formula.

The computed three-particle current coefficients at orders zero through seven are exactly `0, 0, 0, 0, 0, 89/56010528, 0, -410017/1524382530048`. The script independently solves a colored absorbing Markov chain, verifies the published three-particle current at killing vector `(1,2,4)`, and evaluates the current at the rational perturbations `1/2` and `1/3`. It also reproduces the published four-particle cubic coefficient `-1/157300`.

These finite exact calculations certify the stated Taylor coefficients, not a global current-sign inequality. The infinite local statement follows separately from analyticity of the finite uniquely normalized systems and site-reflection oddness. No floating-point simulation or external certification is assumed.
