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

The proof was checked by direct reconstruction from the standard closed-neighborhood definition. For each \(v\in V_i\), the neighborhood sum was reduced to \(w-s_i+f(v)\), and minimization within each part yields the exact criterion \(w-s_i+\mu_i\ge1\).

The packaged `verify.py` exhaustively enumerates every \(\{-1,0,1\}\)-labeling of every nondecreasing complete-multipartite profile through order \(9\). It compares the literal graph definition against the criterion, recomputes every coefficient of the displayed weight enumerator, and verifies the published scalar minimum. Replay output:

`VERIFY_OK profiles=87 labelings=748341 valid_functions=138302 coefficient_checks=641 gamma_checks=87 max_order=9`

The exhaustive computation is finite evidence only. The theorem for arbitrary part sizes is established by the symbolic neighborhood identity and the exact partition of local labelings into the three minimum-label cases.
