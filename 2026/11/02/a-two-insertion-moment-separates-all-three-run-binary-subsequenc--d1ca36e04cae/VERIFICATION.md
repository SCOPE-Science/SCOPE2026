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

Execute `python3 verify.py` with Python 3 and only the standard library. The program constructs all size-two embedding-complement sets, counts compatibility for each of the six disjoint shape patterns, and independently enumerates binary hosts with a subsequence-count dynamic program.

Actual execution returned `pair-and-shape checks: 216`, `independent direct-host checks: 81`, `example (1,2,3)/(1,3,2)/(2,1,3): 592/594/598`, and `VERIFY_OK`.

The first exhaustive check covers all triples of run lengths from 1 to 6; the second covers all such triples whose total length is at most 9. Exact integers are used throughout. The checks do not establish any claim beyond those finite ranges; the general result depends on the position-compatibility and run-multiset proof in RESULT.md. Independent scientific validation has not been performed.
