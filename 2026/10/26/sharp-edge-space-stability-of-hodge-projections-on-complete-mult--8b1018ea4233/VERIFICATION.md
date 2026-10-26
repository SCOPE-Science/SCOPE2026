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

Run `python3 verify.py` from the directory containing the standalone Python script. It requires no external packages or downloaded data. The exact-rational checker constructs the unnormalized graph Laplacian of each complete multipartite graph, grounds one vertex, inverts the grounded matrix using fractions, builds the canonical edge projection, and checks every predicted row formula and the maximizing-part reduction. The observed output was:

```text
MULTIPARTITE_GRADIENT_EXACT_OK 174858 configurations 128 edge_rows 2926
```

The tests enumerate all unordered positive part-size vectors with \(2\le N\le10\), not all graphs with arbitrary numbers of vertices. They also verify symmetry, a projection identity, and the closed form for every tested entry. Their success does not establish the all-\(N\) theorem; the latter rests on the explicit Poisson solution, algebraic row-sum identities, monotonicity factorization, and strict concavity proved in `RESULT.md`. The only external data in the research are cited published mathematical sources; the checker does not retrieve literature. Independent validation has not been performed.
