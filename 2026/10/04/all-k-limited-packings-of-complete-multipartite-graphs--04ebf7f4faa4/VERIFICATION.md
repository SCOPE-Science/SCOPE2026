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

The proof is symbolic and covers every finite connected complete multipartite graph and every integer \(k\ge1\). The finite program is a stress test, not a substitute for the proof.

`verify.py` enumerates every ordered positive part-size profile of total order at most \(9\), every \(k\) from \(1\) through \(N+1\), and every vertex subset. For each subset it computes the closed-neighborhood condition directly from the graph and compares it with the theorem's part-count criterion. It also reconstructs the enumerator coefficients from the lower-quota formula, checks the closed form for \(L_k(G)\), and verifies the published complete-bipartite specialization.

Replay output:

`VERIFY_OK profiles=502 subset_checks=1680156 criterion_checks=1680156 coefficient_checks=42110 bipartite_checks=276 max_order=9`

Unproved by computation: no finite census can establish the arbitrary-order theorem. The infinite statement depends on the closed-neighborhood identity and the residual-capacity argument given in `RESULT.md`.
