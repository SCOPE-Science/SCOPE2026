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

The proof is analytic. The finite computation independently checks the defining maximality condition.

`artifacts/verify.py` generates every nondecreasing complete-multipartite part profile of total order \(2\) through \(8\). For each labeled graph it recursively enumerates every matching. A matching is declared maximal only if no graph edge has two unmatched endpoints. The script compares the resulting size distribution with the residual-perfect-matching formula.

It also verifies the stated size-spectrum condition and compares the direct first moment with \(\mathcal A_G'(1)/\mathcal A_G(1)\).

Expected replay output:

`ALL CHECKS PASSED; profiles=58; matchings_examined=9543; maximal_matchings=2448; orders=2..8`

The finite check does not prove the theorem for unbounded part sizes. Its role is to probe parity, perfect and near-perfect cases, highly unbalanced profiles, complete graphs, bicliques, and multipartite profiles with repeated part sizes.
