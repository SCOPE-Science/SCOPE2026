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

The package includes `verify.py`, a definition-based, finite exact-integer checker, and `verification_output.txt`, its observed standard output.

Run with `python3 verify.py`. It constructs vertices as the two-subsets of \([n]\), derives adjacency from pairwise disjointness, and tests the induced maximum-degree-at-most-one condition directly. For each \(n\in\{4,5,6,7\}\), all \(2^{\binom n2}\) subsets are enumerated, so this finite check is exhaustive within its stated range. Inclusion-maximal sets are identified by checking all one-vertex extensions. Exact coefficient-shape tests run through \(n=500\).

The recorded output is:

```
VERIFICATION_OK direct_orders=4..7 subsets=2131008 maximal_sets_checked=True shape_orders=4..500
```

The infinite statements, including persistent failure of log-concavity after order twelve and return of unimodality after order fourteen, follow from the written algebraic proof, not the finite tests. Independent scientific audit: not performed.
