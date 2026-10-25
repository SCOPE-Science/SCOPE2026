# Review

**Correctness — PASS.** The signature map is injective exactly when the query family identifies all vertices. The eight-query case contradicts the ball volume, and the nine-query case forces pairwise ball intersections of 29. The exact distance-dependent intersection table contains no 29.

**Originality — PASS (best-knowledge).** The closest literature defines the same ball-search parameter and studies identifying/separating codes in binary Hamming spaces. The inspected 2015 source treats the Q7 radius-three construction and general estimates; the literature searches found related but different invariants rather than this Q8 lower bound. A related Hamming-space article was not read end-to-end, and that residual risk is retained.

**Value — PASS.** The bound strengthens the information-theoretic lower bound from eight to ten queries for a natural fixed-radius search problem. It is a precise boundary result useful for subsequent constructions; it does not purport to determine the exact optimum.

## Closest literature and limitations

- Y. Kim et al., *Identifying codes and searching with balls in graphs*, arXiv:1405.7508; DOI 10.1016/j.dam.2015.03.018.
- *New identifying codes in the binary Hamming space*, arXiv:0804.3029; DOI 10.1016/j.ejc.2009.03.032.

The proof establishes only \(M(Q_8,3)\ge10\). No ten-query construction or exact value is established, and the second source was not inspected in full.

Self-review: passed. Independent audit: not yet performed.
