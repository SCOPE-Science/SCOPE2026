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
# Reproducible verification

Run `python3 VERIFY_GP2_OCT.py` in the same directory. No external libraries, external papers, or network access are required.

The verifier reconstructs the seven permissible signed-or-zero columns and all 41 permissible ordered pairs, enumerates every arc, verifies the integer reduced-cost inequality, identifies the sole cyclic strongly connected component of equality arcs, verifies its 22 vertices and its modular four-level labelling, and checks cyclic witnesses and their repeated concatenations. It independently constructs graph adjacency and brute-forces all deletion subsets smaller than the bound and all subsets at the bound for each \(5\le n\le12\), testing residual bipartiteness by graph traversal.

Observed output in the scientific review:

```
CERTIFICATE_OK states=41 tight_arcs=58 recurrent_states=22
INDEPENDENT_BRUTE_OK n=5 minimum=3 attaining_sets=30
INDEPENDENT_BRUTE_OK n=6 minimum=4 attaining_sets=132
INDEPENDENT_BRUTE_OK n=7 minimum=4 attaining_sets=196
INDEPENDENT_BRUTE_OK n=8 minimum=4 attaining_sets=162
INDEPENDENT_BRUTE_OK n=9 minimum=5 attaining_sets=540
INDEPENDENT_BRUTE_OK n=10 minimum=6 attaining_sets=3240
INDEPENDENT_BRUTE_OK n=11 minimum=6 attaining_sets=2783
INDEPENDENT_BRUTE_OK n=12 minimum=6 attaining_sets=1458
VERIFY_OK
```

The theorem's infinite scope rests on the finite potential and cyclic witness arguments, not on extrapolating the brute-force checks. Stronger claims concerning all optimal configurations, uniqueness, or other step sizes have not been checked. Scientific originality may be affected by unindexed earlier work; no independent validation has occurred.
