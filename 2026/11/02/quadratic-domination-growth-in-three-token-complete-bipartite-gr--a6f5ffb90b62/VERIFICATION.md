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

# Reproducible checks and limits

Run `python verify.py` using Python 3 and its standard library. This script directly generates each selected three-token configuration and all legal token adjacencies; it does not rely on a graph-library isomorphism or a precomputed solution table.

Observed replay:

```
ORIGINAL_THREE_TOKEN_GRAPH_DOMINATION_OK 95
ALL_GRAPH_TRIANGLE_DELETION_AND_MANTEL_OK 33864
EXHAUSTIVE_MINIMUM_K24_OK 20
ASYMPTOTIC_BOUNDS_ARITHMETIC_OK
VERIFY_OK
```

The first test compares the explicit family with the original domination definition for every \(2\le m\le8\), \(\max\{m,4\}\le n\le18\). The second enumerates the 33,864 labelled simple graphs of orders three through six and verifies that removing at most one edge per original triangle leaves a triangle-free graph satisfying Mantel's edge bound. The third exhaustively excludes smaller dominating sets for \(F_3(K_{2,4})\) among its 20 three-token vertices. The last checks arithmetic consistency at further parameters.

These finite checks are not an infinite proof. The domain-wide lower bound and construction are established by the combinatorial arguments in RESULT.md; in particular no numerical result is used to infer the asymptotic conclusion. The exact linear correction, growing-\(m\) regime, and historical priority against unpublished work remain unresolved. Independent external audit was not performed.
