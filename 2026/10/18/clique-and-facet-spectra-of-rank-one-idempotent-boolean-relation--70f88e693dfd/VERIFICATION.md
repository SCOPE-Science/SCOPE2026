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

# Reproduction

Run `python3 artifacts/verify.py` with Python 3 (standard library only). The program builds literal Boolean matrix products and verifies each rank-one idempotent and each edge via products for \(2\le n\le4\). It enumerates all cliques/facets and graph distances through \(n=5\); it also checks predicted integer formula boundary cases through \(n=13\). Success marker: `VERIFY_OK_BOOLEAN_RANK_ONE_IDEMPOTENT_CLIQUES`.

The tested integer clique vectors for \(n=2,3,4,5\) are \((7,1)\), \((37,24,1)\), \((175,385,66,1)\), \((781,5160,2725,165,1)\). Facet vectors are \((5,1)\), \((19,21,1)\), \((65,295,62,1)\), \((211,3465,2405,160,1)\). No computation certifies all infinitely many dimensions; the RESULT.md proof is uniform.

Self-review: passed. Independent audit: not yet performed.
