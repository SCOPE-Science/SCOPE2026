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

# Reproducibility and limits

Run `python3 check.py` using Python 3's standard library. The exact expected output from the supplied run appears in `check_output.txt`. The script enumerates each admissible length-\(n\) word and the proposed additional arcs for \(2\le n\le17\), checks all indegree/outdegree equations, computes the first-one potential and validates the sharp dual value, builds an Eulerian cycle, and compares the complete cyclic window **multiset** with the required one. It independently enumerates every legal shorter cyclic binary word for \(n=2,3,4,5\) and excludes full coverage.

These checks demonstrate reproducibility only on the finite stated ranges. General correctness relies on the mathematical proof and tight potential argument in `RESULT.md`. No independently conducted scientific audit or independent validation is asserted.
