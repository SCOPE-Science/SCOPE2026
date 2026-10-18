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

# Reproducibility and limits

Execute `python3 verify_gt4.py` from the directory containing this file. The checker uses only standard-library exact arithmetic and reconstructs the primitive facet normals and endpoint vertices from the interlacing inequalities. It separately checks every one of the 924 possible six-facet linear systems and confirms all feasible basic solutions match the forty endpoint vertices. It enumerates every nonempty intersection of the twelve facets; checks the \(f\)-vector \((40,132,186,139,57,12,1)\); records the singular face counts \((16,28,16,3)\); checks that exactly three inclusion-maximal singular faces cover all singular faces; verifies their pairwise intersections; and certifies that each generic transverse four-ray cone has rank three, a saturated lattice, and the primitive square relation. The observed execution ended with `VERIFY_OK: 40 vertices, 567 faces, 63 singular orbits, three conifold strata in a chain`.

The finite enumeration is exhaustive because every face is an intersection of the twelve named facets and every vertex solves some six independent facet equations among the 924 combinations and the checker shows those feasible solutions equal the 40 distinct endpoint assignments. The checker does not directly prove total unimodularity or the correspondence between smooth toric orbits and unimodular cones; these steps are supplied in the mathematical proof. The checker does not address the Jacobian scheme or analytic structure where two components intersect.
