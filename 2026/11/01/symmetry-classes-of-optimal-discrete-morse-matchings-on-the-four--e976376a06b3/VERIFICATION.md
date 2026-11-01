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

The theorem concerns all optimal acyclic Hasse matchings of the nonempty faces of the five-vertex simplex. There is no random or truncated stage.

Run `python3 verify_vpaths.py` to enumerate every matching of the 30 noncritical faces by the smallest-unmatched-face recurrence. Its independent cycle test uses directed Forman \(V\)-paths at equal rank. It prints exact permutation-fixed counts, all stabilizer types, and the orbit count; assertions require all reported counts to agree.

Compile and run `c++ -std=c++17 -O2 verify_hasse.cpp -o verify_hasse && ./verify_hasse`. This implementation enumerates by the same completeness-preserving first-face recurrence but detects cycles through reversed Hasse arrows and Kahn's topological sort, not through \(V\)-paths. Its 24 individual fixed counts agree with the cycle classes of the Python checker. Both checkers enumerated exactly 117837 perfect pairings, 76025 of which are acyclic.

The proof's finite exhaustive component rests on the elementary recurrence's one-to-one correspondence with graph perfect matchings; neither output alone establishes completeness without that recurrence argument. Known cross-check: 5 times the rooted acyclic count is 380125, equal to the reported total in Scoville's work. The result is not independently audited and makes no statement for larger simplices.
