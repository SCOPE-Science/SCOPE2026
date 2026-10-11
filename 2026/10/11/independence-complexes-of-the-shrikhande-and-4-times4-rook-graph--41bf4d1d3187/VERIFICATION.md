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
# Reproducibility and verification

Run in an ordinary Python 3 environment:

```
python3 verify_twins.py
python3 verify_independence_polynomials.py
```

Both are standalone and require only Python's standard library. The first enumerates all \(2^{16}\) vertex subsets for each graph; checks six-neighbor regularity, two common neighbors for each pair, 200 and 208 nonempty faces, face-vector entries, exact dimensions and count of critical cells, and a complete topological sort of all 496 and 528 oriented face incidences. It also performs mod-two boundary-rank checks independently of the discrete Morse matching. Its successful output ends with `SHRIKHANDE_ROOK_INDEPENDENCE_VERIFY_OK`.

The second computes the full independence polynomials by the graph vertex-deletion recursion and outputs `POLYNOMIAL_RECURSION_OK (1, 16, 72, 96, 16) (1, 16, 72, 96, 24)`. The homotopy claim uses Forman's finite acyclic matching theorem, not an inference from the numerical homology ranks alone. No external independent audit or family-wide theorem verification has been undertaken.
