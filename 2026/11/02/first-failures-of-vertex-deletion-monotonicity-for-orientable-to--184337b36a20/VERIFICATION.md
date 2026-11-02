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

The infinite-family proof is in `RESULT.md`; it holds for every integer \(m\ge5\). The finite scripts are corroboration, with exact exhaustion only where indicated.

`verify_census.cpp` enumerates every labeled six-vertex graph, every valid orientation and every subset, and all 720 relabelings of the distinguished-vertex pairs. It also checks the absence of an offending pair through five vertices. The complete result is 9000 labeled marked pairs, 5850 underlying graphs and 18 marked isomorphism classes; output finishes with `VERIFY_OK`.

`verify_family.py` independently computes both extremal orientation values for \(m=5,6,7,8\), obtaining the pairs \((5,3),(6,4),(7,5),(8,6)\); output finishes with `VERIFY_OK`.

`verify_atlas.py` uses NetworkX's complete graph atlas for the six-vertex unlabeled graphs and a distinct in-neighborhood search and marked isomorphism check. It reports `ATLAS_PAIR_CLASSES 18 ATLAS_PAIRS 25`. This optional cross-check depends on NetworkX; the C++ census is standalone apart from a C++17 compiler.

No infinite claim rests on the finite enumeration. The entire set of six-vertex graphs is finite, and the bitmask loops and canonicalization give an exhaustive certificate for that part of the claim. An independent mathematical audit has not been performed.
