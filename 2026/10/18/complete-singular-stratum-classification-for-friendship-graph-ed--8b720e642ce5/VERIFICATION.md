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

# Reproduction and scope
Run `python3 verify.py` with Python 3 and no external dependencies. The program explicitly constructs the edge-polytope vertices and all proposed facets for \(m=2,3,4\), validates their dimensions and exact inequalities, computes all nonempty faces as intersections of facet vertex masks, derives rational face dimensions, checks normal-ray ranks, and matches every maximal nonsimple face with its proposed indexed component family. For \(m=2,3\) it additionally verifies integral smoothness of every simplicial cone by computing gcds of full-rank minors. The expected terminal line is `VERIFY_OK`.

Observed checks: \(m=2\) had 49 faces and 9 maximal nonsimple faces; \(m=3\) had 289 faces and 26 maximal nonsimple faces; \(m=4\) had 1645 faces and 72 maximal nonsimple faces. Exact facet counts were 9, 15, and 25 respectively. These are finite exhaustions for those parameters, not a proof for arbitrary \(m\).

The general proof in RESULT.md is symbolic. Key proof obligations are the polytope inequalities (including sufficiency via mixture weights), completeness of the three active-facet circuit patterns, saturation of simple cones, and identification of the affine invariant rings from the single primitive relation. The singular-scheme structure and all nongeneric analytic local equations are not determined.
