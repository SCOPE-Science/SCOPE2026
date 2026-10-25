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

# Reproducibility checks

The file `verify.py` exhaustively constructs all transitive ordered tournament simplices and all induced supports on at most five vertices. It checks exact mod-two boundary ranks for small supports, direct signed fundamental cycles of all 55 spheres, affine orbit equality, the signed global chain boundary identity, 45 integral unit pivots giving a verified unimodular kernel basis, and the Smith normal forms over the integers.

The degree-two integer boundary presentation has Smith invariant factors `1` repeated 54 times and `2` once; adjoining 55 sphere cycles gives 65 unit Smith factors. This establishes an integral surjection from the sum of sphere homologies, not a finite-field inference.

The local mod-two test excludes other five-vertex supports; integral torsion-freeness of those small tournament complexes also follows from Govc's published complete classification for tournaments on at most ten vertices. The script's success marker is `VERIFY_OK_PALEY11_MINIMAL_SPHERE_GENERATORS`.

A finite exact certificate applies to the particular eleven-vertex complex; no larger-parameter generalization or independent external audit has been performed.
