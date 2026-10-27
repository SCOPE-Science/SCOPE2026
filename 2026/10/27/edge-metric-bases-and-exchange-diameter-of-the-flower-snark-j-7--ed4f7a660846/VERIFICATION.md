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
# Reproduction

Use the self-contained `verify_distances.py` with Python 3 and the standalone `verify_signatures.cpp` with a C++17 compiler. The outputs `verify_distances.out` and `verify_signatures.out` capture successful actual executions. The two programs build the same abstract cubic graph by distinct vertex numberings, compute distance matrices using BFS versus Floyd–Warshall, test edge resolution with pair-cover masks versus injective distance signatures, and construct exchange adjacency by generated replacements versus intersection cardinality. Both independently check every one of the \(3276\) three-subsets and \(20475\) four-subsets and BFS from every one of the \(1932\) exchange states.

These are exhaustive finite checks because each relevant set appears once in a complete lexicographic enumeration and each BFS traverses every graph edge. The records do not certify any statement for flower snarks other than \(J_7\); no external audit is claimed.
