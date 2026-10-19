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

# Reproducible finite-state checks

Run `python3 verify.py`. All transition intensities and all stationary masses are rational. The program verifies detailed-balance identities, stationary normalization and symmetry, strict upper-half transition-ratio comparison at adjacent positive noise parameters, strictly decreasing upper polarization tails, and radial likelihood-ratio comparisons for \(6\le N\le30\). It additionally checks the exact \(N=4,5\) anticonformist non-irreducibility witnesses and the binomial noise-only endpoint for the independence model. The run passed 24,477 exact identities and comparisons for 400 tested stationary distributions.

At \(N=6\) an independent symbolic generator linear-system solve for \(p=1/4\) yielded exactly the same stationary masses in both models. This is a check of the finite formulas, not an independent mathematical review or infinite-range certification.

The all-population, all-noise conclusion follows from the explicit algebraic derivatives of successive stationary ratios, and not from enumeration. The model is a continuous-time interpretation of single-step gain–loss coefficients, not the original simultaneous four-spin update chain.
