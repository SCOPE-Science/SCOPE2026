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

# Verification

Run `python3 verify.py` with standard Python 3 and no third-party dependencies. The exact-integer checker directly enumerates the roots and all active signed coordinate and \(\ell_1\) inequalities. It compares the facet-wise illumination test with the heavy-pair condition for every tested designed direction, verifies that every root has exactly one illuminator, and checks the size of each illuminated class. It additionally enumerates all magnitude vectors with entries \(1,2,3,4\) for dimensions \(3\)–\(6\), asserting both pairwise intersection and the optimal per-direction upper bound.

Observed output:
```
d=3 vertices=12 directions=4 per_direction=3 exact_cover=yes
d=4 vertices=24 directions=8 per_direction=3 exact_cover=yes
d=5 vertices=40 directions=10 per_direction=4 exact_cover=yes
d=6 vertices=60 directions=12 per_direction=5 exact_cover=yes
d=7 vertices=84 directions=14 per_direction=6 exact_cover=yes
d=8 vertices=112 directions=16 per_direction=7 exact_cover=yes
EXACT_OK dimensions=3..8 incidence_checks=4328 magnitude_profiles=5440
```

These finite checks do **not** constitute exhaustive verification of arbitrary dimensions or all real directions. The proof of the infinite-dimensional-parameter statement is the active-facet criterion, intersecting-edge lemma, vertex-count weighted bound, signed optimal construction, and boundary-face argument in `RESULT.md`. A separate external audit has not occurred.
