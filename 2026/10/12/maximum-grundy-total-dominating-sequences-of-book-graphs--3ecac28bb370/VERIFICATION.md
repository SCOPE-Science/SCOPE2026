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

The proof is analytic and valid for every integer \(n\ge1\). Its critical steps are: the bipartition-side independence of legality, the exact length-\(n\) classification on each side, and the binomial interleaving count. No finite experiment is used to extend a claim beyond the range checked.

The bundled `verify.py` independently reconstructs \(B_n\) from its edges, applies the open-neighborhood definition directly, and uses memoized dynamic programming on dominated-vertex masks. For each \(1\le n\le7\), it verifies the maximum length, counts all maximum ordered sequences, reconstructs all underlying maximum sets, and compares those sets with the claimed complements of one vertex from each bipartition class.

Expected replay output:

`VERIFY_OK n_range=1..7 maximum_sets=203 dp_states=21844 n7_sequences=348713164800`

The computation is a finite corroboration only. It does not constitute a proof for arbitrary \(n\); the all-orders proof is given in `RESULT.md`.
