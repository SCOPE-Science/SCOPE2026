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

The checker constructs \(K_n\square K_2\) from two complete graphs and a perfect matching, computes all-pairs shortest-path distances, and evaluates mixed distance vectors for every vertex and every edge.

For each \(5\le n\le9\), it exhaustively tests every vertex subset of size below \(n\) and confirms that none is mixed resolving. It then tests every \(n\)-vertex subset and compares the direct result with the structural criterion: exactly one endpoint from every matching edge and at least two selected vertices in each clique layer.

Recorded output:

```text
VERIFY_OK
complete_prisms_checked = 5
vertex_subsets_checked = 207641
minimum_mixed_bases_checked = 912
parameters n = 5..9
all smaller subsets failed directly
all size-n mixed bases matched the matching-transversal classification
all basis counts matched 2^n - 2n - 2
```

The finite computation is corroborative only. The theorem for every \(n\ge5\) follows from the proof.
