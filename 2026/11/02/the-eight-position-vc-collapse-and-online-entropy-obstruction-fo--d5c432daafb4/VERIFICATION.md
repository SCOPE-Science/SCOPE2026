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

Run `python eulerian_certificate.py verify certificate.json` with Python 3 and no dependencies. Two genuinely different permutation enumeration routes (full permutations versus maximum-insertion) agree at every \(n\le8\); the VC support search is exhaustive, and the adaptive version-space recurrence checks every feasible split. The witness tree has 2047 internal nodes and 2048 distinct leaf permutation indices. Both the source code and the witness are standalone. Direct-sum amplification is a symbolic argument and has no infinite computational claim.

The checked eight-position result is: 4541 concepts, VC=6, Littlestone=11, cardinality bound 12, 31827 VC-search nodes and 77182 adaptive memoized subproblems. The depth-twelve failure is an exhaustive Boolean recurrence result; it is not an unsuccessful search or timeout. No independent scientific audit was conducted.
