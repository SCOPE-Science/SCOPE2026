# Independent audit — 2026-09-28

Record: `2026/09/10/042`  
Audited tree: `323a51863ed40c29c3fab468d2b9b51192527874`  
Disposition: **passed**

## Correctness
I independently reconstructed the counting proof. Let `T` be the number of loose-triangle edge triples and `h` the number of 6-sets containing one. A loose triangle spans exactly six vertices, so `h <= T`. For a fixed corner vertex `v`, an unordered pair of incident edges has disjoint off-`v` pairs by linearity. A completing third edge must choose one point from each off-`v` pair, giving at most four choices, and linearity permits at most one edge through each chosen pair. Summing over the three corners of every triangle gives `3T <= 4 sum_v C(d(v),2)`. Since `2d(v) <= n-1`, this yields `T <= n(n-1)^2/6`, hence

` t(H) <= 120(n-1)/((n-2)(n-3)(n-4)(n-5)) -> 0.`

The threshold arithmetic at `n=15` and `n=20` is also correct. The proof is stronger than needed because it does not use Fano-freeness.

## Originality
The closest literature I located treats loose-triangle-free subgraphs or Fano-plane edge extremal problems, not the fraction of 6-sets containing loose triangles in arbitrary linear hosts. I did not locate this exact bound or the `T*=0` conclusion. That is positive evidence for originality, not an exhaustive proof of novelty; the short counting lemma could conceivably have appeared in a differently phrased source.

## Scientific value
The theorem decisively refutes the admitted positive-density interval and provides a closed-form uniform bound with an `O(n^-3)` rate. That is a useful constraint for any later linear-hypergraph density optimization.

## Limitations
It does not determine the sharp finite-`n` maximum or an edge-density extremum.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/042
- https://arxiv.org/abs/2004.10992
- https://arxiv.org/abs/1804.07673
