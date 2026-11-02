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

# Verification and reproduction

Run `python3 CHECK.py` with Python 3 and the standard library, from the directory containing this document and `CHECK.py`.

The checker builds each of 27 exact Fourier-convolution coefficients in four formal Laurent variables, recomputes the moment from them, and proves polynomial equality with the displayed sum-of-four-squares expression. It computes the exact Hessian matrix and verifies, using integer arithmetic, the eight parity vectors with quadratic value 16 in a finite bounding cube; the global lattice exhaustion is proved analytically in RESULT.md. It then evaluates the proposed 24 minimizing configurations as exact Laurent polynomials and checks that each equals the asserted cosine expression. Supplementary independent complex convolution enumerations for odd orders 3,5,7,9 are floating-point checks and are **not** used to infer infinite-order validity. All theoretical quantifiers, including the existence of an unspecified odd threshold, are discharged by the proof in RESULT.md.

Independent auditing is not performed. No externally certified proof status is asserted.
