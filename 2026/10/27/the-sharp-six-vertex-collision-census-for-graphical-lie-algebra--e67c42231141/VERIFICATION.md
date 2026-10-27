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

`verify.py` uses Python standard library only. It checks every labeled simple graph on 0 through 6 vertices, partitions them into explicit permutation orbits, then compares complete formal coefficient dictionaries. For six vertices it confirms 156 graph isomorphism types, 149 different formal polynomials, seven doubleton collision classes, and no larger collision. Its seven edge-list pairs appear verbatim in `CENSUS.txt`. It also verifies the witness symbolically and computes every possible vertex-vector commutator-matrix rank over F_2, F_3 and F_5 by exact elimination. The all-field support-rank identity is proved algebraically in RESULT.md; finite experiments do not establish a general n>6 classification. Graph-to-Lie nonisomorphism in odd characteristic uses the published theorem of Mainkar. Independent audit is not performed.
