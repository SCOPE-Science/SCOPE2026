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

# Verification of sharp cyclic-cover length

Run `python3 verify.py` under Python 3 (standard library only). The program independently constructs the prescribed extra-zero paths, checks their sink bijection and balanced multigraph degrees, generates an Euler circuit, and verifies the exact set of all cyclic factors for each integer \(2\le n\le12\). It also runs exhaustive covering-closed-walk breadth-first searches for \(2\le n\le5\) to verify the sharp minimum without using the constructive theorem.

The resulting length/repeated-occurrence pairs for orders \(n=2,3,4,5,6,7,8\) are respectively \((3,0),(6,1),(10,2),(17,4),(28,7),(46,12),(75,20)\), agreeing with the Fibonacci formula. The program reports `CONSTRUCTION_AND_FORMULA_2_TO_12_OK` and `EXHAUSTIVE_CLOSED_WALK_BFS_2_TO_5_OK` when all assertions succeed.

The finite checks cannot establish the claim for arbitrary \(n\), and exhaustive search is carried out only through order five. The complete all-order proof is the combinatorial flow lower bound, explicit source-to-sink bijection, and generating-function count in `RESULT.md`. Independent external auditing has not been performed.
