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

# Verification of the exact CoCD stability theorem

The mathematical result and proof appear in `RESULT.md`. The corresponding standalone Python file `verify.py` uses SymPy to construct the exact elementary refresh/decay matrices, multiply them, eliminate the freshly overwritten stored coordinate, expand the characteristic polynomial, and factor every displayed Schur quantity. It also verifies exactness of centered finite differences on the quadratic for an arbitrary nonzero perturbation.

The executable checks sampled parameter configurations on both sides of the derived threshold (576 spectral calculations), six critical-boundary eigenvalue tests, and symbolic special cases. Run `python verify.py` using Python 3.10+ with NumPy and SymPy installed. The expected success message is:

`VERIFY_OK symbolic identities; 576 matrix-root checks; 6 boundary checks; central differences`

The software checks have been executed successfully on the included source file. Symbolic equality checks confirm algebraic identities; finite numerical samples do not certify an uncountable stability region. Exact inequalities in `RESULT.md` prove the complete domain and include determinant and zero-coupling boundary cases. No independent third-party audit is represented.
