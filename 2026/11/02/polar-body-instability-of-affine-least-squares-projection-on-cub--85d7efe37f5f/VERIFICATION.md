---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For normalized uniform solid measure and the degree-one orthogonal L2 projector, symmetry/second moments give K_D(x,y)=1+[(d+1)(d+2)/2] x·y on the cross-polytope and K_Q(x,y)=1+3x·y on the cube. For any x the L∞ row norm is E|K(x,Y)|; convexity in x forces a maximizing vertex, and a positive-volume region with opposite signs of K(v,y) and K(w,y) for distinct vertices makes convexity strict for any nonvertex. At a cross-polytope vertex, the one-coordinate beta density d(1−t)^{d−1} gives 1+(d+2)/2[1−2/((d+1)(d+2))]^{d+1}; the cube row is an Irwin–Hall truncated-power sum 1+12/(d+1)!Σ_{k≤floor((3d−1)/6)}(−1)^k binom(d,k)((3d−1)/6−k)^{d+1}. The signed kernel input attains the norm, while its negative part gives sharp positivity loss (norm−1)/2. Beta asymptotics yield normD/d→1/2; the CLT with uniform integrability gives normQ/√d→√(6/π), hence divergence of normD/normQ. Independent exact rational calculations in dimensions 1..9 reproduce all formula values and special cases d1=5/3,d2=233/108,d3=10561/4000 versus 415/162; small d checks do not prove asymptotic/strict vertex claims.

## originality

PASS

The published full Resultary simplex projector theorem gives a sharp positivity defect for a different uniform domain; it does not establish the paired central symmetric cube/cross-polytope constants in d≥3. The published full Hanner-polytope isotropic constant theorem supplies both covariance matrices but not the absolute kernel row integrations nor L∞ norms. Oswald 2006 studies globally coupled spline projectors and mesh dependence, not one solid affine projector. Tensor-product Legendre projection literature may encode the cube expression and is an explicit priority risk; the pairwise exact polar growth separation is assessed original at best knowledge.

## value

PASS

The cube and cross-polytope are canonical polar solids, yet their local affine projection constants have different order in dimension (sqrt d versus d). The sharp all-dimensional norms, unique spatial maximizers and positivity deficits provide a meaningful intrinsic stability comparison relevant to high-dimensional least squares, beyond reusing the elementary covariance matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
