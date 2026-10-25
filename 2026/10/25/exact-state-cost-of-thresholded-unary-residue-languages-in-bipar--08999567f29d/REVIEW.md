# Review

- **Correctness — PASS.** The lower bound uses an accepting cycle whose length is a multiple of \(\operatorname{lcm}(p,2)\), a simple shortest accepting path, and, for odd \(p\), a simple path of length \(m+p\). The path-plus-cycle construction attains the bound.
- **Originality — PASS, with residual risk.** The closest inspected result proves existence of bipartite-cactus NFAs for all regular languages, not the exact minimum for this thresholded unary family. Unary-NFA literature inspected does not impose this graph constraint. The search was bounded and is not a proof of global novelty.
- **Value — PASS.** The formula gives a complete, exact state-cost classification for a natural infinite family and isolates the parity-dependent price of the first accepted length under a structural graph restriction.

**Closest literature:** Grobler, Koziel, and Siebertz (2026), arXiv:2610.11717; Czerwiński et al. (2023), arXiv:2302.06435.

**Limitations:** The result does not classify arbitrary ultimately periodic unary languages or automata outside the stated constraints. Finite tests validate only the construction, not the universal theorem.

Self-review: passed. Independent audit: not yet performed.
