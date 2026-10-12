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

The mathematical proof appears in `RESULT.md`. It derives the Lie automorphism parametrization from the characteristic derived ideal, the shift-cycle fixed-space contribution, the exact translation compatibility correction, and the finite-subspace Möbius inversion formula. All dimensions, field characteristics and cardinality normalizations are explicit.

Execute `python verify.py` in a standard Python 3 environment. The program constructs prime and quadratic-extension finite fields, enumerates invertible matrices, builds complete Lie automorphism block matrices including the free translation column, calculates ranks of their differences with the identity, and compares observed fixed-space profile coefficients against the closed formula.

A successful execution returns the final line `FINITE_CHECKS 25 VERIFY_OK`. The checks include \(q=2,3,4,5,7,9\) and arbitrary spectral supports when the direct enumeration size is manageable. Certain larger cases use formula-level consistency checks and do not claim exhaustive construction. The proof is general; computational samples are not a certification of all instances.

Independent audit has not been performed. No external verification or specialized proof assistant is claimed.
