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

The proof has two components: a mathematical gap-preservation lemma giving an all-order tail, and exact enumeration of all ordered four-move atomic diagrams over a finite set of graphs. The exhaustive finite recursion is explained in RESULT.md and implemented by `checks/types.cpp`. An independent implementation `checks/types.py` verifies its finite partition on overlapping instances, including all sharp thresholds and exceptional diagrams.

Run `python3 checks/reproduce.py` in an environment with Python 3 and a C++17 compiler. The recorded output `checks/reproduction.txt` was generated from the packaged source files. Checks include repeated choices, equality, both directions of each back-and-forth extension, distinctness of the 33 rank-four classes, and stabilization across the ranges 16–40 and 17–40. The mathematical gap lemma proves all remaining indices; checking only up to 40 would not suffice on its own.

No proof assistant, outside mathematical referee, external formal certification, or independent audit is claimed. Literature-priority checks are incomplete, as identified in RESULT.md and REVIEW.md.
