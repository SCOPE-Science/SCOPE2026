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

# Reproducibility

Execute `python3 check_locating_hop.py` from the directory containing this file and the standalone verifier. The program enumerates all \(87{,}360\) vertex subsets for the six values \(n=3,\ldots,8\); it computes shortest-path distances by breadth-first search, tests both the nonemptiness and distinctness conditions for all unselected vertices, compares the closed classification and the two claimed generating polynomials, and tests inclusion-minimality through removal of each selected vertex. The observed terminal result was `ALL PASSED: 87360 vertex subsets; complete BFS-based predicate, classification, two generating polynomials`.

The finite experiments do not prove the statements for larger orders. The full general proof consists of the distance-two signature reduction, case analysis by the smaller layer occupancy, correction counting, and deletion classification in `RESULT.md`. External independent mathematical audit and validation have not been performed.
