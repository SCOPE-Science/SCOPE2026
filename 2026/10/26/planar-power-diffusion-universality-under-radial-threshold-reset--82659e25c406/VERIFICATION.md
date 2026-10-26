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
Run `python verify.py` with SymPy and mpmath installed. The accompanying `verify.out` is the recorded output from this package. It verifies chain-rule drift and diffusion terms, the stationary adjoint and normalizations, the planar return-time moment differential equations, low-order hypergeometric coefficients, and specified finite test families. No numerical calculation establishes the infinite-dimensional path-law equivalence, the renewal functional central limit theorem, or historical originality; those depend on the written proof and source comparisons.
