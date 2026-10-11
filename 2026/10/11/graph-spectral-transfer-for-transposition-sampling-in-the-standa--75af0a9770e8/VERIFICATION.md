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

# Verification and limitations

The analytic proof fixes normalized group measure and confirms the matrix-coefficient normalization \((n-1)/n!\). Its nonstandard all-graph bridge is the exact character-to-incidence identity. Complete-graph Gram positivity, principal-submatrix interlacing, unsigned-incidence rank and regular-graph spectral decomposition are checked explicitly in the proof. Empty edge sets, disconnected and bipartite graphs, and small-rank thresholds are addressed in the stated domains.

The bundled `verify.py` is a standalone Python 3 standard-library checker. Invoke `python3 verify.py`. Actual execution produced:

`VERIFY_OK complete_n=4..9 (6) arbitrary_edge_masks=424 regular_graphs=17 exceptional_n3_rank=2`

The checker compares character and incidence Gram entries exactly, tests complete-class eigenvector identities, confirms the bipartite-component rank identity on all 424 edge masks, and tests regular-graph row sums and vertex adjacency-incidence identities on 17 examples. It includes a negative sanity check: the full transposition Gram at \(n=3\) is singular, so the theorem does not extend that threshold.

These experiments are finite; none prove positivity or the spectral formula for all \(n\). Those universal steps appear in the analytic proof. No external audit or independent verification has been performed. Novelty relative to unindexed older frame literature is not conclusively established.
