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
# Finite verification and proof boundaries

The supplied standalone Python 3 program `verify_clique_corona.py` uses bitmask adjacency construction for the ordinary clique corona of each labeled core graph. It independently enumerates every possible dominating subset, tests both domination and the outside-neighbor capacity bound, computes the cardinality distribution directly, and compares it with the distinct coefficient formula built by summing the private-clique occupancy contributions. It also compares the actual minimum cardinality and count with the component-factor and bounded-core-cut predictions. All of the reported comparisons passed.

Run with `python3 verify_clique_corona.py`. The resulting standard output must equal `verification_output.txt` byte-for-byte. Testing covers 75 labeled core graphs, 857 graph-parameter cases and 1,877,184 candidate vertex subsets, including the attached-single-leaf boundary as an auxiliary check. The theorem is unbounded in graph order and capacity: finite tests do not prove that unbounded claim. Necessity, sufficiency and the minimum-set classification are established by the mathematical proof in `RESULT.md`; the program tests the implementation independently and is not an external certification.
