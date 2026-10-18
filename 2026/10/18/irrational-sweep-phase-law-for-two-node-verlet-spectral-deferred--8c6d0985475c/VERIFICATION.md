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

# Reproduction and verification

Execute `python verify.py` from a directory containing the companion source file. Dependencies are SymPy and mpmath. No external data downloads, random seeds, network operations or compiler are required.

The verifier independently integrates the two Gauss–Legendre cardinal polynomials, constructs the cumulative explicit and implicit velocity-Verlet substep matrices, and checks the exact \(2\times2\) compression. It checks the compression trace, determinant and \(2\cos(2\theta)=\sqrt3-1\), constructs the two-stage Gauss collocation endpoint, and verifies its exact unit determinant. For each of six successive correction counts, the exact determinant polynomial has zero coefficients below the predicted \(z^{k+1}\) order and the correct nonzero leading coefficient. Nine high-precision full-stage forward-substitution calculations independently check the leading sign and scale.

Actual result: `PASS: quadrature, Verlet matrices, complex compression, Gauss collocation, six determinant-leading identities, and nine independent high-precision sweeps`. The observed leading signs at correction counts 1 through 9 are negative, positive, positive, negative, positive, negative, positive, positive, negative.

The infinite-density conclusion is proved by irrational circle-rotation equidistribution and the algebraic-conjugate obstruction to roots of unity; finite code checks are not a substitute for that proof. The small-step bound may depend on the correction count. No external or independent validation has been performed.
