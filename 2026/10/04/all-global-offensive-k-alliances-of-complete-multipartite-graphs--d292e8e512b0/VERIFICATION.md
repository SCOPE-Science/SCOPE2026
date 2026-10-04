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

For an omitted vertex in part \(V_i\), the literal graph definition gives selected-neighbor count \(s-s_i\) and unselected-neighbor count \(N-n_i-(s-s_i)\). The symbolic proof in `RESULT.md` reduces the alliance inequality to the displayed threshold exactly.

The bundled `verify.py` independently constructs every nondecreasing complete-multipartite profile of total order from \(2\) through \(9\). For every \(k\) in the standard range \(1\le k\le\Delta\), it enumerates every vertex subset, tests the literal neighborhood inequality, and compares the answer with the profile criterion. It also recomputes every coefficient of the cardinality enumerator. For complete bipartite profiles it checks the minimum value against Remark 2.1 of arXiv:0812.1528, and for \(k=1\) with both parts non-singleton it checks the all-set condition against Cabahug–Isla Theorem 3.8.

Replay result:

`VERIFY_OK profiles=87 parameter_checks=524 subset_checks=162612 criterion_checks=162612 coefficient_checks=4626 bipartite_gamma_checks=90 bipartite_k1_set_checks=2736 max_order=9`

The exhaustive range is a finite stress test only. The unbounded theorem is established by the exact neighbor-count argument in `RESULT.md`.
