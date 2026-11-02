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

# Reproducing the finite checks

The two supplied programs examine the same finite graph using different constructions and data structures. Python 3.10 or later is required. The direct graph-isomorphism checker additionally uses NetworkX 3.x; the generalized-Petersen bitset checker needs only Python's standard library.

Execute the scripts from the directory containing them:

```
python verify_dodeca_total_direct.py
python verify_dodeca_total_gp.py
```

The expected success markers are `DODECAHEDRON_DIRECT_TOTAL_DOMINATION_PASS` and `DODECAHEDRON_GP_BITSET_PASS`, respectively. Each script raises an assertion error on any disagreement; neither uses files not included in this package.

The direct checker enumerates every possible size-seven and size-eight candidate, all minimum-set exchanges, each shortest-path eccentricity, all twelve-subsets for induced-cycle recognition, and the full automorphism group. The second checker independently constructs the edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\) of \(\operatorname{GP}(10,2)\), and checks the complete candidate, transition, distance, and cycle ranges using bit operations.

These are exact exhaustive finite checks for the twenty-vertex graph. They do not certify analogous results on larger generalized Petersen graphs, nor do they constitute external scholarly review.
