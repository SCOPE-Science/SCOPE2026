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
# Verification

The symbolic proof reduces the process to the connectedness pattern of the current white induced subgraph. When whites lie in at least two partite classes, they form one connected component, so the first-force condition is exactly an outside-white-neighbor count. Once that force occurs, all remaining whites lie in one independent part and are cleared as singleton white components.

The bundled `artifacts/verify.py` reconstructs the graph and positive semidefinite color-change rule directly. It exhaustively tests all initial subsets for every ordered part-size profile with two, three, or four parts, each part size between one and four, subject to total order at most eleven. It then compares the brute-force cardinality counts against the closed enumerator coefficient-by-coefficient and checks the minimum-size corollary.

Replay command:

`python3 artifacts/verify.py`

Observed output:

`VERIFY_OK profiles=269 subset_checks=182540 criterion_checks=182540 coefficient_checks=2529 minimum_checks=269 max_order=11`

The finite replay is not an infinite proof. The all-parameter claim rests on the explicit first-force argument in `RESULT.md`; the computation is a boundary and implementation check.
