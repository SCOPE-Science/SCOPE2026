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
# Reproducible checks

The mathematical claim is universal in integer length; finite computations are additional cross-checks and not the reason the universal statement is true.

- `python3 verify.py` independently forms word strings and their complete sets of distinct single-deletion outputs. It verifies the explicit lower-bound code for every length from 3 to 120 and verifies the two-output upper-bound transversal against every candidate weight-two word from length 3 to 65. It separately checks the formulas for code and transversal sizes through length 120.
- `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify` constructs the compatibility graph from literal deletion-output intersections and enumerates all maximal cliques for lengths 3 through 12, confirming exact maxima \(1,2,3,4,4,5,6,7,7,8\). The exhaustive verifier uses a Bron–Kerbosch style search with pivoting; its finite completeness follows from branching over all possible maximal compatible sets.
- The general proof requires no extrapolation from these tests: the dual output set contains at least two distinct outputs from every allowed input, and the construction has pairwise disjoint output sets.

No external validation or independent audit is asserted. The results do not cover any input alphabet or weight other than those in the stated theorem.
