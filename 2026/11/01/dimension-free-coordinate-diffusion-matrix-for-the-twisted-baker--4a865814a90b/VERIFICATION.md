---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the stated fixed dimension and stationary normalized product measure, both inverse branches have weight 1/2. Applying them to the centered coordinates gives the invariant affine span and matrix B. Mixing implies B^n→0 since the coordinate Gram matrix is invertible, and the displayed H satisfies (I−B)H=B (interior rows reduce to successive differences, with the two end rows giving the asymmetric coefficients). As a direct check on the joint limit, the Poisson increment on the left inverse branch at y is ((y₁−1)/2, u₂(y)+(y₁+1)/4, …, u_M(y)+(y₁+1)/4); on the right it is its negative because Pd=0. Product Lebesgue second moments give 1/3, −1/12, 1/6 and 1/12 for the four covariance-entry classes, respectively. Ergodicity gives the averaged conditional variances for the bounded reverse-martingale CLT, applied to every linear projection; the bounded telescoping corrector does not alter the limiting covariance or distribution. The passive correlations are for distinct indices, with no such pair at M=2. The two-dimensional block has trace M+4 and determinant 3M+1 in units of 1/12, giving the eigenvalues and the fixed-order versus large-M limits as claimed. Read the frozen exact-arithmetic verify.py and its recorded replay instructions; the finite range was not rerun and does not establish the all-M argument.

## originality

PASS

The supported distinct claim is the evaluated full joint covariance for spatial-coordinate sums, including exchangeability, mixed signs and dimension dependence of the eigenvalues. The dynamics, affine transfer operator, scalar first-coordinate variance, and general martingale method are not distinct contributions.

## value

PASS

The exact matrix quantifies the anisotropic spatial fluctuations of a concrete map despite its deterministic ordering of passive coordinates. A common diffusive passive mode and a negative coupling to the active coordinate cannot be inferred from scalar variance or mixing. The joint invariant is useful without claiming a new martingale theorem or a growing-dimension CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
