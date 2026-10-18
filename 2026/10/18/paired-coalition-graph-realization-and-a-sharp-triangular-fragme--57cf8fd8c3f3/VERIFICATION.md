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

# Verification and reproducibility

Execute `python3 verify.py` in a directory containing the accompanying script. It uses only Python's standard library and finishes with `ALL_FINITE_CHECKS_PASSED` when every assertion succeeds.

The direct computation enumerates each **unlabeled** set partition of the ten or fewer labeled vertices exactly once, constructs the graph's full adjacency relation, checks domination and perfect matching without using the signed-imbalance shortcut, creates each coalition graph and checks each connected component is complete bipartite, then compares the joint component-and-block count to the formal generating function evaluated with exact rational coefficients. It covers all pairs \((m,n)\) with \(1\le m,n\le5\). The complete \(K_{5,5}\) count is \(14{,}637\). It verifies the sharp component cutoff and the triangular equality for \(T_c\in\{1,3\}\); separately the formula's \(K_{6,6}\) coefficient at three components equals \(3{,}600\). The \(K_{6,6}\) coefficient is formal-series evidence only, **not** an exhaustive graph-partition census.

The all-parameter results rely on the full combinatorial argument in `RESULT.md`. Finite tests do not certify unbounded parameters or publication novelty. Independent scientific audit has not been performed.
