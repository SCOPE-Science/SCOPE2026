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

The algebraic proof uses only exact fractions, maximum-degree-two graph topology and elementary counting. The included standalone checker uses exact integer cross multiplication to compare the full set of unilateral deviations with the stated local conditions; it does not infer infinite validity from the exhaustive cases.

Replay from the extracted package root: `python3 checks/verify_cycle_nash.py` (Python standard library only). Expected final line: `PASS: 172620 unrestricted partitions on paths, cycles and disjoint degree-two graphs; no singleton or adjacency omissions`.

The largest tested cycle order is ten. The checker also verifies the sharp component number at each tested size and the eight-vertex threshold; all larger sizes and the general if-and-only-if claim rely on the written proof. No external audit has been performed.
