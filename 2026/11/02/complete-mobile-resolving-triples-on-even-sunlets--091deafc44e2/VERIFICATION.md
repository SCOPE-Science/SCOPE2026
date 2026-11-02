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

# Reproduction and mathematical scope

Run `python3 verify_sunlet.py` using Python 3's standard library. The program constructs every edge of each even sunlet of circumference \(4,6,8,10,12,14,16\), computes distances by fresh breadth-first searches, and independently evaluates resolvingness of all vertex pairs and all three-core sets using distinct distance signatures for every vertex. It compares the latter with the closed gap bound and count, verifies the exceptional four frozen two-landmark cases, and exhaustively explores each initially labelled triple's core-only resolving moves to confirm individual robot reachability at every core position; all permitted core-to-leaf detours are checked against resolvingness.

Recorded output:

```
EVEN_SUNLET_OK n=4 two_resolving=4 core_triples=4 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=6 two_resolving=0 core_triples=14 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=8 two_resolving=0 core_triples=32 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=10 two_resolving=0 core_triples=60 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=12 two_resolving=0 core_triples=100 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=14 two_resolving=0 core_triples=154 triple_each_robot_all_core=YES
EVEN_SUNLET_OK n=16 two_resolving=0 core_triples=224 triple_each_robot_all_core=YES
VERIFY_OK complete-mobile lower bound and core-gap classification checks n=4..16
```

These finite tests are corroboration only. The quantified theorem follows from the distance-difference localization lemma, arithmetic count, pair-landmark obstruction, gap-transfer argument, cyclic patrol and resolving-preserving pendant replacement proved in `RESULT.md`. No computer-generated infinite certificate or independent external audit is asserted. Historic originality remains qualified by possible differently formulated work.
