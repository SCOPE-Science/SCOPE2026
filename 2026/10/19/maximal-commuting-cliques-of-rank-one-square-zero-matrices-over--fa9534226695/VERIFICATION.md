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

# Reproducibility and scope of checks

Run `python checker.py` with Python 3. No external packages are required.

The checker constructs actual matrices over prime fields, tests square-zero and rank-one status, verifies adjacency by matrix multiplication, independently lists inclusion-maximal cliques with an explicit Bron–Kerbosch algorithm, enumerates all subspaces to construct the proposed maximal cliques and compares their exact sets, then counts all cliques of sizes one through four by distinct search to compare with the closed finite sum.

Cases checked are `(n,q)=(2,2),(2,3),(3,2),(3,3),(4,2)`. Their respective `(number_of_vertices,number_of_maximal_cliques,maximum_size)` are `(3,3,1)`, `(8,4,2)`, `(21,14,3)`, `(104,26,8)`, `(105,65,9)`. The two cases with dimension two test a boundary outside the main novelty scope.

A successful run prints `ALL_EXACT_CHECKS_PASSED` after every assertion. This proves only that the script's explicitly enumerated finite test cases agree, not the infinite parameter theorem. The written proof provides the argument over every finite field, including extension fields.

No independent mathematical audit has yet occurred.
