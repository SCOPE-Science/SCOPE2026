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
# Reproducibility and boundaries

The standalone code `verify_minimum_token_domination.cpp` builds the graph from its token-adjacency definition, with no precomputed adjacency table. It directly enumerates all labelled subsets of the claimed minimum cardinality for \(n=3,4,5,6,7\), applies closed-neighborhood domination, and classifies every feasible subset by the two explicit families.

Build: `c++ -std=c++17 -O3 verify_minimum_token_domination.cpp -o verify`.

Run: `./verify`.

Observed output:
```
n=3 ordinary=9 exceptional=0 total=9
n=4 ordinary=18 exceptional=36 total=54
n=5 ordinary=30 exceptional=0 total=30
n=6 ordinary=45 exceptional=0 total=45
n=7 ordinary=63 exceptional=0 total=63
VERIFY_OK complete_enumeration_n=3..7 with exact family classification
```

The total number of candidate sets examined is \(47,432,132\). All computations use unsigned 64-bit bitmasks and exact integer equality; the largest graph enumerated has \(45\) token vertices. The universal assertion for every \(n\ge3\), including the minimality assertion, is proved symbolically in `RESULT.md` rather than extrapolated from these finite tests. No independent mathematical audit has been performed.
