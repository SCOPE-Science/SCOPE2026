---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS. Each factor polygon satisfies A>=4 and L>=8 under the published planar face-distance estimates; every interval length>=2. Inradius-one triangle has perimeter L>=6sqrt(3) by tangent-plane tightening and convexity of tan in three exterior normal gaps, equality for equilateral tangent triangle. Multiplicative codimension face polynomial C_P(z)=prod(A_i+L_i z+v_i z²)prod(s_j+2z) counts orthogonal product face measures exactly. Taking z² coefficient and only lowering nonnegative A_i and s_j gives Φ_{n-2}/2^n -binom(n,2)≥sum(v_i/4-1)+2(n-2)sum(L_i/8-1)+4sum_{i<j}(L_i/8-1)(L_j/8-1). Nontriangles give nonnegative terms, while triangle contributes -1/4 offset by n>=3 perimeter excess >=(3sqrt3-4)/4, yielding (6sqrt3-9)/4 per triangle. Equality in total ridge bound requires no triangles and tangent squares/perimeter8 plus length-two intervals, hence precisely centered cube. In n=3 triangle×[-1,1] reaches the triangle-deficit coefficient; its vertices satisfy distance≥sqrt2. Independent product-polynomial checks m<=3, ell<=5 with triangles/squares and intervals passed; uniform theorem is by coefficientwise proof, not finite checking.

## originality

PASS

PASS best knowledge with visible prior dependence. Zwierzyński 2026 announces ridge conjecture and partial cases, the known surface/volume factor bounds, and a face-product polynomial for other codimensions. The stated arbitrary products of possibly asymmetric planar polygons and sharp triangular compensation are not established by the prior orthotope or tangential symmetric cases on the evidence read. The general 3D ridge inequality is credited as old; the dimension-general product theorem and quantitative remainder survive.

## value

PASS

PASS. A sharp, dimension-independent positive resolution on a broad family of a named higher-dimensional ridge-skeleton conjecture is motivated by factor geometry and the difficult local triangle-vertex deficit. The factorwise quantified sharp gap and all equality cases extend beyond orthotopes and familiar three-dimensional general edge bounds; no claim to settle indecomposable polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
