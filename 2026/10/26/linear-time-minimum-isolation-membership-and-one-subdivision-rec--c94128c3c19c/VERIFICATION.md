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

# Computational reproducibility

Run `python3 verify_isolation_reroot.py` with Python 3 and the standard library. Expected final line:

`VERIFY_OK independent_bf_tree_cases= 18729 subdivision_trees= 1441`

The verifier builds trees directly, independently checks vertex-subset isolation by examining each edge's dominated endpoints, computes both forced-selection and forbidden-selection optima by brute force, and checks them against the associative rerooting algorithm. It tests every labelled tree with at most seven vertices, another 480 deterministic pseudorandom trees of orders 8 through 13, and every labelled tree with two through six vertices for the published single-edge-subdivision criterion. It also supports reuse of `solve(n, edges)` for arbitrary tree inputs.

A test of all trees through seven vertices is a finite correctness check, not a substitute for the induction proof. The infinite-time and space bounds come from the constant per-directed-edge state size and the sum-of-degrees accounting in `RESULT.md`. The single-subdivision corollary invokes the cited tree characterization and applies only to nonstar trees.
