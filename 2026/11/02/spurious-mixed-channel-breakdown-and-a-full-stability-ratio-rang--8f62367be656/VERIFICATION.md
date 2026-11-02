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

# Verification of the mathematical claim

The analytical proof uses the identity \(A(A^{-1}v-\alpha v)=v-\alpha Av\), two orthogonal projections, a spectral sign argument, the three-eigenvalue Vandermonde determinant and two endpoint limits. These establish an all-dimensional criterion and full-range behavior, not just tested cases.

The supplied independent implementation of the Gram projector in `verify.py` uses Python's exact rational arithmetic and has no third-party dependencies. Executing `python3 verify.py` returned `EXACT_VERIFY_PASS 2317`. It evaluates the two candidate residuals independently of the closed formula, including the exact breakdown case. Exact test counts and rational computations are reproducibility evidence, not an infinite-dimensional proof.

Scope limitations: no floating-point error theorem, no performance or downstream matrix-function error analysis, and no proof of exhaustive historical uniqueness. Independent audit status: not performed.
