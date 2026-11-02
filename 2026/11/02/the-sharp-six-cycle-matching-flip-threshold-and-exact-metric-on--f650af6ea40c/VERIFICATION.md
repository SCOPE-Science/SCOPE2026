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

# Reproduction and boundaries

Run `python code/check_primal.py` and `python code/check_dual.py` in a standard Python 3 interpreter. Neither program imports third-party libraries. They were run on their actual saved contents with assertions enabled, and both printed their PASS markers.

`code/check_primal.py`: builds the icosahedral graph from two 5-cycles and poles, recursively visits every perfect matching, compares every pair for legal one-cycle 4/6 flips, calculates all components, degrees and all-pairs BFS distances; verifies the five frozen matchings partition all 30 edges and that any two are at distance two after length-six flips.

`code/check_dual.py`: constructs the 20-vertex dodecahedron as a generalized Petersen graph, enumerates exactly 12 pentagonal faces, builds their icosahedral dual, recursively enumerates all 125 matchings and independently enumerates all simple cycles of length four and six; adjacency is determined by actual alternating-cycle toggles, not symmetric-difference pair classification. Asserts the same full graph metrics and the frozen-matching properties.

The two independent finite checks are exact; their exhaustive enumeration covers every perfect matching and legal short flip by the described recurrences. They do not establish global literature novelty or any infinite-family statement. No independent scholarly audit has been performed.
