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

The attached `CHECKER.py` performs the following checks on the stated two-periodic spline projection:

- Exact symbolic divisibility of the rational-expression identity for the kernel row integral, using the genuine quadratic equation for the decaying Bloch root; this is a polynomial certificate in the two positive cell lengths and the root variable.
- Exact rational Gram inversions for finite circles with 4, 6, 8, 10, 14, 20 and 24 knots, each in five rational cell-length ratios; exact integration of the signed affine reproducing kernels without quadrature.
- Agreement of all nodal absolute-row integrals under the mesh's reflection symmetry, strict finite-circle upper bounds, and finite-section convergence comparisons.

The code's finite sampling does not prove the claims for all lengths or circle sizes. Analytic details about Bloch inversion, the kernel norm, and periodization are supplied in `RESULT.md` and are essential to the universal argument. No external independent validation is claimed.
