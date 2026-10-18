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

The package contains `check_split_face.py`. Execute `python check_split_face.py` with Python 3, `numpy`, and `sympy`. The program constructs exact rational stochastic transition matrices and tests eigenvector identities, nonnegativity, fixed row sums, extremal internal-edge budgets, symbolic characteristic polynomials for six small graphs, and illustrative non-invariant optimal cores. It prints four PASS messages on success. Its checks span the sizes stated in RESULT.md.

Analytical proof, not sampling, establishes the universal claim. In particular, a full trace compression and spectral saturation argument is needed to prove cross-edge rigidity for all graph sizes. Prior work supplies the scalar optimum, while the complete all-optima characterization is justified independently here. No separate or independent audit has been performed.
