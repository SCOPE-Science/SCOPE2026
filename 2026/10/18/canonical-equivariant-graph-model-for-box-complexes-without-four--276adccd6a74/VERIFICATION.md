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

The included `verify.py` constructs all Hom cells, exact mod-two boundary matrices, component actions on the canonical double cover, and chain Lefschetz traces. Execution: `python verify.py`. The saved output `checks.txt` records success on cycles five through eight, the triangle, a four-degree windmill graph, the Petersen graph and the Heawood graph. It tests all 120 Petersen automorphisms with coordinate swap/no swap. Finite tests confirm specified cases, not the universal topological theorem, whose proof appears in `RESULT.md`.
