---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For all integers N≥2 and all positive normalized fixed unoriented planar directions, derived the worst-body perimeter-normalized Cauchy quadrature error E(µ)=½ max{2/π−rµ,Rµ−2/π} from the planar surface-area integral; thin rectangles realize the sup norm. The associated symmetric zonogon Z=∑w[-u,u] has perimeter 4. A tangential m-gon bounded by its 2k≤2N facet normals and origin-centered inradius r gives 2r∑tan(Δ_i/2)≤4; Jensen and monotonicity of m tan(π/m) yield r≤cot(π/(2N))/N=rN. Equality forces all Δ_i=π/N and regular Z and equal weights. The regular N-rule has R=1/(N sin(π/(2N))) and R+rN<4/π, making the lower discrepancy sharp and E_N=π^{-1}(1−x cot x), x=π/(2N). The global strict-convexity tangent deficit yields ∑(Δ_i−π/N)^2≤24δ/[x rN(rN−2δ)] for 0≤δ<rN/2; ≤48δ/(x rN²) for δ≤rN/4. A symmetric ±t gap deformation has δ=c_N t²+O(t⁴), so angular deviation scales as √δ. Independently evaluated small-N exact formulas and numerical perturbed geometry; these are corroboration, not the all-N proof.

## originality

PASS

Best-of-knowledge new finite positive N-direction sharp minimax/uniqueness and sharp angular stability. An (2026) gives the general exact support-discrepancy identity, and classical polygon perimeter/tangent inequalities are used rather than claimed new. Different width and tangential torsional-rigidity theorems do not imply the exact Cauchy quadrature criterion.

## value

PASS

Optimizing finitely many positive Cauchy projection directions against ALL convex bodies is a classical concrete integral-geometry quadrature problem. Sharp closed worst-case constant, uniqueness of equally spaced angles, and quadratic angular stability with proven sharp exponent give an exact design and robustness statement that general Cauchy defect identities alone do not state.

The dated certificate retains the supplied scientific assessment, sources and limitations.
