---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

All retained exponent vectors are exposed grid vertices. The graph is connected bipartite so its edge semigroup is normal, and exponent differences span the full rank a+b−2 lattice in each chart: obtain missing coordinate axes as differences of a mixed generator and an available axis. An ordinary chart is an orthant. At a special row the absent column coordinate is nonnegative and bounded by the total row mass, with the transposed condition at a special column. At a cross chart with missing axis coordinates x,y, the mass on the mixed generator can range from max(0,x−Σc,y−Σr) to min(x,y), so the two extra inequalities in the proof are also sufficient. Each displayed inequality is an actual facet: there are relative-interior witnesses with only that inequality an equality (at a cross, for a zero ordinary row or column adjust x−y slightly with the sign giving strict slack in that extra inequality). The primitive coordinate normals give a lattice direct summand of the divisor map, so its cokernel is free with rank the number of extra facets. For the Zariski local assertion, localization is surjective on classes. An invariant divisor class killed there gives an M-graded divisorial module free at the fixed maximal ideal. A homogeneous lift of a basis of its one-dimensional fiber generates the localized module by Nakayama. This lift is a monomial, which therefore makes the divisor principal along all invariant primes (they all meet the point), proving injectivity as well. The coordinate normals force the all-ones character even over Q; the extra values are a−2, b−2, and both, respectively. This gives each stated boundary, and the vertex charts cover, so the joint global boundary is (3,3). The nonordinary counts sum to 2(a+b−3). Independent /workspace/branches/8f81efef-e391-465a-928d-8427d5845f4d/independent_chart_check.py checked 292 charts for 3≤a,b≤6 and exhaustively found the facets for all seven 3×3 charts; finite validation only. The packaged code was inspected, not executed.

## originality

PASS

The supported distinct claim is the local class-group and canonical Cartier table, notably the rank-two cross charts and their joint obstruction. Edge adjacency, normality and the divisor-sequence method are not new; the matching-deleted homogeneous ring result also has the same global numerical boundary in the two-deletion case but does not give the local table.

## value

PASS

Two independent omitted coordinates are the first matching-deletion setting in which a single fixed chart can exhibit two missing axes. The precise local group and Cartier data detect the resulting rank-two divisor obstruction, invisible from adjacency or from the one-deletion determinantal model, and give a sharp varied-parameter distinction between singular and non-Q-Gorenstein points. These data are usable in studying toric birational modifications of the projection family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
