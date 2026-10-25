---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The torus weights make both monomials x^2y and z^3w^2 product_i u_i^2 invariant. On x != 0, normalization x=1 identifies the quotient with A^(n+2), and this covers the complement of the divisor x=0. On x=0 the equation forces u_1 != 0, so the u_1 chart has coordinates q=xu_1,b=y/u_1^2,c=zu_1^2,d=w/u_1^2,U_i=u_i (i>=2) satisfying q^2 b+c^3d^2 product U_i^2=1. The divisor q=0 is parametrized globally by b, s=(c d product U_i)^(-1) and U_2..U_n, with c=s^2 and d=s^(-3) product U_i^(-1), proving D ≅ A^1 x (C*)^n and a trivial normal line defined by invariant q in a whole neighborhood. Both chart normalizations also establish trivial stabilizers. The homotopy-pushout Y=U union N(D), U contractible, identifies Y with Thom of that normal line; triviality gives Sigma^2 (D_+) ≃ wedge_r binom(n,r) S^(r+2). This yields all integral cohomology, vanishing positive cup products and pi_1=0. I independently verified the monomial weights, q/c/d coordinate identities and binomial ranks for small n; the all-n result uses standard tubular neighborhoods and suspension splitting, not numerical extrapolation.

## originality

PASS

Nikitina's 2026 primary paper constructs exactly the same smooth quotient, torus weights and invariant divisor and proves generic but non-full flexibility; those are prior and credited. Her actual full arXiv HTML Section 3, including invariant-ring results and the divisor, was read. It does not supply the affine-space complement, explicit torus cylinder structure of D, trivial normal bundle or integral homotopy wedge classification. Gaifullin's earlier family differs in defining geometry and singularity. The Thom-space and suspension-product principles are classical; the contribution is their exact geometric application to this new natural affine quotient family. An equivalent unindexed computation remains a priority risk.

## value

PASS

The homotopy type and torsion-free integral cohomology of a geometrically motivated family of smooth generically flexible but non-flexible affine quotients are natural topological invariants that can aid comparison and obstruction arguments. The two-chart description yields an entire all-n wedge-of-spheres classification, not merely low-degree Betti numbers or generic smoothness; this is a meaningful structural refinement of the original algebraic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
