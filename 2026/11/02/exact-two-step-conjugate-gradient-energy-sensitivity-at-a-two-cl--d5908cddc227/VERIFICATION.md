---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

At t=0 the CG polynomial p0(z)=(1-z/beta)(1-z/gamma) annihilates the two active spectral components. Since the 2x2 Gram matrix of z and z² under positive spectral weights is invertible, the optimum residual polynomial coefficients are analytic in t. The Fréchet derivative of p0(C0) multiplies a cross-cluster F block by p0[beta,gamma]=0, cancelling it exactly. Independent linear adjustments q(beta),q(gamma) remove components along u and v; the first residual derivative is the orthogonal within-cluster perturbation vector scaled by (beta-gamma)/(beta gamma). Squaring in the C0-inverse norm yields the two denominators beta³ gamma² and beta² gamma³, with O(|t|³) error and O(t⁴) when the leading vector vanishes. For symmetric blocks the norm budget for the off-diagonal component z costs 2||z||², giving the exact Frobenius supremum and attaining rank-two block. This proof covers arbitrary finite positive eigenspace dimensions, fixed right hand side with both components nonzero and sufficiently small symmetric perturbations; finite checks are only corroboration.

## originality

PASS

Best-of-knowledge originality for the directional exact leading constant and Frobenius optimum at a spectral collision. The nearest 2026 Diouane et al bound concerns separated spectral placements and leaves an uncomputed second-order remainder. The classical CG residual-polynomial characterization is background, not claimed new. A more general matrix-polynomial perturbation source may imply the formula; version-dependent numbering in the cited Diouane theorem is a citation check risk.

## value

PASS

The formula resolves a natural sensitivity problem of exactly terminating two-step CG near a two-eigenvalue collision, identifies the directional zero set and sharp matrix-perturbation robustness, and explains why between-cluster mixing does not dominate first-order loss. These depend on actual Krylov energy sensitivity, not a routine spectral-condition-number substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
