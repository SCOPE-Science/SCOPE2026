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

# Verification instructions and limits

Execute `python3 verify.py` with Python 3.10 or later. The program reconstructs the local domination/private-witness predicate from the Cartesian grid, then exactly calculates the optimal weight and count for each four-column state. It confirms the state-support equality, translated maximum-weight vectors and zero second differences of optimal-prefix counts at three specified lengths, and checks zero final-count slopes in four residue classes. These finite identities plus the stated linear induction prove the all-order claims.

Two independent formulations are used for finite cross-checks: the column-state recurrence and an exhaustive original-vertex-bitmask test. Each listed family of extremizers is also tested using direct vertex neighborhoods, and small exact counts are compared against the number of distinct patterns. The finite brute-force checks alone would not prove an infinite statement; they are secondary verification.

The implementation uses exact Python integers and no external dependencies. Computer-independent formal proof checking and independent historical-priority research have not been performed. The claim excludes grid heights above three.
