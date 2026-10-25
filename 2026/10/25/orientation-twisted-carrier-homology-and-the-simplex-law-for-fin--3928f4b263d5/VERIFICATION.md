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

# Verification of the orientation-twisted carrier formula

The general conclusion is proved by comparing the integer facet-compatibility matrix with the top twisted normalized boundary. Finite examples do not establish the theorem.

Run `python verify.py` in this directory (requires Python 3 and SymPy). For the ten faces `012,013,024,035,045,125,134,145,234,235`, the program checks 6 vertices, 15 edges, 10 facets, two facets per edge, five-cycle vertex links, Euler characteristic 1, and nonorientable monodromy. It constructs the ordinary signed boundary and the oppositely signed, local-orientation-twisted boundary. It obtains ranks 10 and 9 respectively over exact rationals, and block-diagonal results for one through five disjoint copies. Each repeated-copy scenario is a direct covering by identity maps, so its simplex dimension can also be checked without homological assumptions.

Expected final line: `VERIFY_OK`. Scientific limits: the calculation only covers the displayed real-projective-plane triangulation and its disjoint-copy covers; the proof in RESULT.md covers arbitrary closed triangulated manifolds and finite-fiber simplicial maps with supported bundle scenarios. No external or independent validation has been performed.
