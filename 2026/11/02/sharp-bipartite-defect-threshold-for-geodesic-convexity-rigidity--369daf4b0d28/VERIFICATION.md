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

# Reproducible checks

Execute `python3 check_rigidity.py` with Python 3 and its standard library. The checker computes graph distances by breadth-first search and shortest-path intervals directly, rather than assuming the convex-set characterization. It exhausts deleted-matchings types on five-by-five and six-by-six bipartitions, tests all defects one through five in the sharpness construction, tests 185 deterministic pseudo-random graphs near the threshold, and explicitly computes online and static dimensions of one crown example. The successful final output is recorded in `CHECK_OUTPUT.txt`; rerun the checker to reproduce the marker. Code and output are supplementary finite validations and do not replace the proof.

A direct independent mathematical proof in RESULT.md supplies all integer values of the defect parameter, both unbalanced part orders, and the strict boundary example. The complete published full texts of the closest g-minimal and online-learning sources were not reviewed; historical priority is not independently certified.
