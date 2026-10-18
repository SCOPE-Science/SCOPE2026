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

# Verification and scope

Run `python verify_spider.py` with Python 3; it uses only the standard library. The verifier explicitly constructs each spider, calculates breadth-first-search distances and edge-to-vertex distances, exhaustively tests the resolving-arm lemma on 2,688 subsets of four spiders, enumerates all vertex subsets for 51 bounded instances, and compares the independently computed simultaneous domination-and-resolution minima with both theorem formulas. It additionally checks 42,294 arm-length profiles for modular equality and consistency of the closed expressions.

The mathematical proof is independent of the finite numerical checks: the arm-resolution lemma and complete case split for edge coverage appear in `RESULT.md`. No claim of independent external validation or formal proof certification is made. The full proof addresses only spiders with at least three arms of lengths at least two.
