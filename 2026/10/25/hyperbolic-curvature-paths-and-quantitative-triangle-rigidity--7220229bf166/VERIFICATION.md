---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Outer Steiner mass-moment expansion q(t)=A+Lt+pi*t^2 and M(t)=AG+LtH+pi*t^2 S follows by adding outward polygon edge strips and exterior circular sectors, with cubic normal moments cancelling, then convex approximation. Barycentric weights lead to lambda_H^2=(L^2/A*pi)*lambda_G*lambda_S and a strictly hyperbolic conic when centers are noncollinear (strict isoperimetric inequality). Differentiating confirms determinant 2AL*pi*det(H-G,S-G)/q(t)^3 and noninflection. For triangles, physical center determinant is A/(6L*pi)*det(1,a_i,alpha_i). The sine law and strict sine concavity give scalene iff curved, with Hermite-Genocchi second-divided-difference lower bound by min sin(alpha)/2. Direct apex-coordinate ordering gives monotone straight paths for nonequilateral isosceles triangles. Eighty independently sampled triangle configurations and curvature identities were checked; universality follows from the analytic derivation.

## originality

PASS

Best-of-knowledge original remainder after separately excluding known component formulas and narrower/other-object antecedents. The primary article supplies the rational second-order centroid formula already, so that identity is NOT novel; its indicated result neither deduces the full geometric conic locus nor the scalene/isosceles rigidity and quantitative angle-gap bound. Algebraic closeness of the hyperbola deduction remains an explicit priority risk.

## value

PASS

The complete triangle shape classification, signed noninflection, and quantitative degeneration bound are motivated geometric properties of a known path, distinguishing curved from straight regimes; no claim of a new centroid formula or globally optimal bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
