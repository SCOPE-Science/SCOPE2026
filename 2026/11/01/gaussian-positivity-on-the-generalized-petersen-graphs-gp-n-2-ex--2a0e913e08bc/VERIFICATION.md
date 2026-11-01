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

# Verification of the graph-metric classification

The self-contained Python 3 standard-library script `verify.py` reconstructs the \(2n\)-vertex generalized Petersen graph from its edge definition, computes unweighted shortest-path distances by breadth-first search, forms anchored Gram matrices, and obtains exact integer characteristic polynomials by Newton power sums. It checks all four surviving characteristic-polynomial factorizations and the associated ranks without a floating-point eigensolver. For each listed finite excluded order, it reconstructs the explicitly given zero-sum coefficient vector and verifies the exact strictly positive distance quadratic value. It also checks the universal eight-vertex witness and its exact quadratic value \(2\).

The script compares the independent shortest-path matrices with the two-layer infinite-cover distance formula for \(5\le n\le50\), a total of **171580** individual distance entries; it verifies nontrivial winding cannot shorten the eight-vertex certificate for all \(n\ge18\) by the analytical displacement bound \(n-7\ge11\). The final success marker from direct execution is `GP_GAUSSIAN_POSITIVITY_EXACT_CHECK_OK`. The full all-orders claim follows from the analytical cover argument and uniform winding inequality, not merely the finite script checks.

The historical originality comparison covers the primary sources in RESULT.md and relevant publicly searchable prior statements. It does not certify independence or exclude every differently worded historical theorem. No independent audit has been performed.
