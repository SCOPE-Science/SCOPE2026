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

# Verification of the Pappus-graph minimum dominating-set classification

Use `python3 verify.py` (Python 3 standard library only) from the same directory as the result.

The verifier constructs the explicit eighteen-vertex \(\mathrm{TD}(3,3)\) graph and a separate LCF graph, then tests an explicit graph isomorphism. It enumerates all \(262144\) vertex masks, checks ordinary **closed-neighborhood** domination, and confirms minimum cardinality five and precisely eighteen optimal masks. It checks the full eighteen-set canonical family, the one-triple/seventeen-single coverage profile, all distance-four spheres, and a vertex-transitive automorphism subgroup of order 216.

Observed exact output:

```
VERIFY_OK graph=TD(3,3)=Pappus LCF_iso=18 vertices=18 edges=27
VERIFY_OK all_masks=262144 gamma=5 optimum_sets=18 point_split=9+9
VERIFY_OK unique_triple_coverage=18 canonical_centers=18 distance4_two_each
VERIFY_OK automorphism_group=216 one_optimum_orbit=18
```

These finite checks apply to this fixed finite graph only. The mathematical proof separately derives the lower bound, all possible bipartition splits, rigidity of incidence covering, distinctness and the symmetry orbit. No independent mathematical audit has been performed.
