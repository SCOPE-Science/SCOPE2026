---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For any d>=3, q=d-1, a C^3 strictly convex full-dimensional body with finitely many diameter pairs, positive curvature radii and G_j=D I-R_{j,-}-R_{j,+} positive definite: boundary graphs at each pair yield a chord deficit Q(v,y)+O(||(v,y)||^3). The 2q-dimensional quadratic form is positive definite exactly under G_j; computing its determinant gives 4^{-q}D^q det(B_-)det(B_+)det(G). An independent exact noncommuting rational q=2 test (D=7, B_-=[[5,1],[1,4]], B_+=[[4,2],[2,6]]) gave det M=789439/16 equal to the closed expression, and G leading minors 1233/190 and 16111/380 positive. Localization to the finite diametral lines, ellipsoid sublevel volume, and Cauchy line normalizer κ_q S(K)/2 produce the epsilon^{d-1} exponent and coefficient. Finite ellipsoid quadrature in source verify.py corroborates, not proves, universal tails. Degenerate/continuous diameter sets and d=2 are not asserted.

## originality

PASS

Best-of-knowledge originality PASS for the all-d>=3 tensor-radius endpoint coefficient with finite nondegenerate diameter pairs; both the normalizer and the general existence of chord CDFs are classical, not the claimed new content. The complete Ren (2014) paper could not be accessed, so its possible curvature-endpoint analysis is a material priority risk rather than evidence of noncoverage.

## value

PASS

Sharp near-diameter tails under natural invariant-line sampling are a substantive local-to-global stereological invariant: a universal exponent, explicit noncoaxial endpoint curvature matrix coupling, finite multiple-maximizer superposition, and proper surface-area conditioning. These facts can be used without a global chord CDF calculation; the radius determinant is not a known-table reproduction for arbitrary smooth bodies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
