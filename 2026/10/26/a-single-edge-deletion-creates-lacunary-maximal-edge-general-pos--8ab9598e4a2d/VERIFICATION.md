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

# Reproduction and proof coverage
The verifier is a self-contained standard-library Python 3 file, \(\texttt{verify.py}\). It creates the graph for each \((p,q)\), discovers all three-edge geodesics using graph distances computed by breadth-first search, tests all selected-edge subsets against this original definition, and identifies each inclusion-maximal set by trying every one-edge extension. It compares the two direct-enumeration distributions to the coefficient formulas. The nine cases from \((2,2)\) through \((4,5)\) with graph edge count at most twenty agree exactly.

The proof independently establishes the formulas for all integer \(p,q\ge2\); exhaustive examples do not certify an infinite result by themselves. Independent external scientific audit and validation have not been performed. The accessible abstract of a relevant 2025 paper does not permit complete priority exclusion.
