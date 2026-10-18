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

# Reproducible numerical and exact checks

Use `python3 verify_capped_crown.py` with standard-library Python 3. The checker builds the bounded-crown poset directly, enumerates all monotone Boolean assignments as order-polytope vertices, constructs true facet vertex masks, closes under facet intersections, and ranks active incidence columns by integer connected-component counts.

The expected output is:

```
n=3 vertices=20 faces=1615 singular_components=7 by_dimension={3: 1, 5: 6}
n=4 vertices=37 faces=18447 singular_components=18 by_dimension={5: 4, 6: 8, 7: 6}
n=5 vertices=70 predicted_components=50 all_candidate_cones_exact
VERIFY_OK
```

For \(n=3,4\), every nonempty face is inspected; every nonsmooth cone is identified by excess primitive active normals over incidence rank, and inclusion-minimal nonsmooth cones are compared as sets with the stated indexed families. For \(n=5\), the checker verifies each candidate equality block gives exactly the claimed active normals and dimensions, as well as all torus-fixed vertices; **it does not enumerate the entire face lattice**. The all-parameter completeness argument and local semigroup isomorphisms are mathematical proofs in `RESULT.md`, not certified by these finite tests. No independent audit is asserted.
