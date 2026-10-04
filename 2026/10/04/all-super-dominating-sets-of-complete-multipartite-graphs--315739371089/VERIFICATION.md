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

The proof is symbolic and valid for arbitrary finite order. The standalone checker `verify.py` is an independent finite stress test of the literal definition against the claimed structural criterion.

It enumerates every nondecreasing complete-multipartite part profile of total order from \(2\) through \(10\), every vertex subset for each profile, and checks:

- literal super domination versus the complement classification;
- every coefficient of \(\mathcal S_G(x)\);
- the minimum-size formula;
- the number of minimum super dominating sets;
- complete-graph, star, and nontrivial complete-bipartite boundary cases.

Exact replay output:

`VERIFY_OK profiles=128 subset_checks=64916 criterion_checks=64916 valid_sets=2505 coefficient_checks=339 gamma_checks=128 special_checks=34 max_order=10`

The exhaustive computation is finite evidence only. The arbitrary-order result is established by the proof in `RESULT.md`.
