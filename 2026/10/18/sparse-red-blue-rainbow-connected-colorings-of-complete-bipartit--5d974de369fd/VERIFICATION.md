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

Run the embedded standalone Python 3 script `rainbow_sparse_verifier.py` without external packages:

```
python3 rainbow_sparse_verifier.py
```

The script independently enumerates binary edge-coloring masks and, for each pair of same-side graph vertices, looks directly for a two-edge path containing one edge of each color. It computes the least red-edge count and number of optimizers and compares them with the theorem for the nine labeled complete bipartite graph sizes \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4)\). It also computes the complete red-edge polynomial via set-partition Möbius coefficients and independently via brute enumeration, for six of those sizes. Both test families must terminate with `PASS` and `FULL WEIGHT ENUMERATOR PASS`.

The infinite statements follow from the separately given signature-separation and Möbius-inversion proofs. Exhaustive finite masks neither establish an infinite identity nor certify novelty. There has been no independent external audit.
