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

Run `python3 verify.py` beside `maxima.json`. The verifier independently reconstructs the 90 balanced ternary words and the Hamming-compatibility graph, exhaustively enumerates every maximal clique, and checks the packaged list of 12 maxima. It also recomputes the five-perfect-matching decomposition for each maximum, verifies that these matchings partition the 15 edges of \(K_6\), counts six labeled 1-factorizations with two maxima each, and exhausts the full \(S_6\times S_3\) action.

Expected final line:

```text
VERIFY_OK words=90 maximum=15 labeled_maxima=12 factorizations=6 maxima_per_factorization=2 orbit_size=12 stabilizer=360 maximal_cliques=90627
```

The verification is exact finite computation over integer bit sets. It does not establish or claim any result for other FPA parameters.
