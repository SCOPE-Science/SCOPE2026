# Independent audit — 2026-09-30

## Disposition: PASSED

### Correctness
PASS. I independently reconstructed the DFS-tree geometry of `K_{a,b}`. Ancestor-comparability forces an alternating spine, with all surplus same-side vertices attached as leaves at the terminal spine vertex. Recounting the return loads gives exactly
`h_i=i(a+b+2-2i)-b-1` and `g_i=i(a+b-2i)-1`; the leaf-envelope contribution is dominated. Neighbor comparisons reduce the optimum to the concave `g_i` sequence except for the balanced odd parity correction. Its integer maximum yields the stated transition between `b≤3a-2` and `b≥3a-1`. For `K_n`, every DFS tree is a Hamilton path and the load is `i(n-i)-1`. Small exhaustive definition-level checks reproduced all tested formulas.

### Originality
PASS, qualified. Bourotte–Ducloz–Orponen–Seki introduce KLX and develop small-parameter structure and algorithms, but the accessible current source does not state exact complete-graph or complete-bipartite values. Classical spanning-tree congestion is not equivalent because it optimizes over all spanning trees. Searches found no prior statement of these formulas or the biclique phase transition.

### Scientific value
PASS. The formulas give exact dense-family benchmarks for a new parameter and show a sharp imbalance transition and a large DFS-restriction penalty.

### Evidence
- Bourotte, Ducloz, Orponen, Seki, arXiv:2606.24675; MFCS 2026, DOI 10.4230/LIPIcs.MFCS.2026.7.
- Kozawa, Otachi, Yamazaki, DOI 10.1016/j.disc.2008.12.021, for ordinary spanning-tree congestion context.

### Limitations
No complete-multipartite extension or classification of all minimizers is proved. Very recent unindexed KLX work remains a residual originality risk.
