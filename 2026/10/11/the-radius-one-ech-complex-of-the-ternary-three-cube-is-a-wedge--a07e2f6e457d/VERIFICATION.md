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

# Reproducible verification

Execute `python3 hamming3_checker.py` under standard Python 3. The script uses no nonstandard packages, no remote resources, no other result files, and no externally supplied observations. It creates 27 ternary triples, 27 radius-one closed neighborhoods, all 2,889 nonempty simplices, and 11,097 Hasse covers; it checks all 1,377 matching pairs are disjoint and checks that the directed Hasse graph is acyclic by processing all 2,889 nodes. The surviving critical-cell profile is one vertex and 134 two-simplices. Actual stdout is embedded separately as `CHECKS.txt`.

The exact conclusion follows from discrete Morse theory and the absence of one-cells in the Morse CW complex. No claim is made about a uniform formula for all Hamming graphs, other filtration scales, equivariance, or independent review.
