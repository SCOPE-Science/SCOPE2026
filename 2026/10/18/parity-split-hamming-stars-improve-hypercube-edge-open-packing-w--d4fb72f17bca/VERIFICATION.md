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

# Reproducibility and finite limits

Execute `python3 verify.py` with Python 3 supporting `int.bit_count()` and no third-party packages. The verifier reconstructs the original eighty cube edges, defines compatibility directly from their vertex coordinates, builds the full bitset graph, and uses two independent exact enumerations. The first is an anchored maximum-clique branch-and-bound bounded by greedy proper colorings, with 96 recursive nodes. The second is an ordered exact maximum-clique enumerator with color and cardinality pruning, visiting 1,393 recursive nodes and finding twelve maxima containing the canonical cube edge. Edge-transitivity and incidence counting give eighty global maximum edge sets. An explicit geometric family of eighty distinct feasible maximizers supplies the matching classification.

The code also directly checks all specified Hamming-lift edges for \(Q_3\), \(Q_5\), \(Q_7\), and \(Q_9\). These larger-dimensional checks verify specific constructions only, and do not enumerate all potential edge-open packings. The infinite inequality is a formal consequence of the parity-split Hamming-code proof in `RESULT.md`.

Recorded successful output:

```
PASS: Q5 maximum = 12; optimal subsets = 80
PASS: anchored maximum nodes = 96 ; anchored counting nodes = 1393
PASS: all maxima belong to the 80-member parity-lift family
PASS: Hamming constructions Q3=3, Q5=12, Q7=56, Q9=224
```

The result has passed the present self-review only. No independent mathematical audit has been carried out. The exact five-cube certificate depends on the correctness of the disclosed exhaustive search implementation and its clique-bound logic; it does not certify a bound for every cube dimension.
