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

Execute `python verify.py` using Python 3 and the standard library. The code independently evaluates the conditional chord-length survival integral for seven shape profiles and compares it with the closed initial affine branch, verifies inverse reconstruction by bisection, and checks the exact cusp and rectangular square-root asymptotics numerically. Execution returned `ALL_CHECKS_PASSED`.

The proof of the infinite family of identities is analytic, through a width-biased affine-line integral, a convolution of two uniform projected generator coordinates and strict monotonicity of a scalar trigonometric function. Finite midpoint quadrature and finite bisection do not certify asymptotic limits or historical novelty. No formal theorem prover or independent scientific audit was used.
