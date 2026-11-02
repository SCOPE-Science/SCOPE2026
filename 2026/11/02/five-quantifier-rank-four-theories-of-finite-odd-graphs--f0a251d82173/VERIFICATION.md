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

# Verification protocol

Run `python3 verify_odd_graphs.py` with Python 3.9 or newer; only Python standard-library modules are required. The committed output `verification_output.txt` is the recorded result of that command.

The checker uses two independent constructions: an orbit enumeration using the eight Venn regions and exact binomial inclusion-exclusion for fourth-vertex atomic patterns, and a direct graph-adjacency bitset method. The two yield identical pair extension types for every \(1\le k\le6\). The orbit calculation also checks the number and equality of all rank-four classes through \(k=12\). A separate interval-profile cross-check verifies the five rows for \(5\le k\le60\).

The universal conclusion for all \(k\ge5\) is not a computational extrapolation. Its proof is the exact subset-feasibility equivalence (1), the fourth-vertex common-neighbor classification, and the five symbolic interval-profile matrices in RESULT.md. The checker does not claim to establish an unbounded fact by finite sampling. Historical priority and mathematical audit remain independent and unperformed.
