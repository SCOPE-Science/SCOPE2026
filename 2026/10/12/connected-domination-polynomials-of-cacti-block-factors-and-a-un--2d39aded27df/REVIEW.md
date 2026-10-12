# Scientific assessment

## Correctness — PASS

Every connected dominating set must contain all articulation vertices. A nonarticulating cycle vertex has no neighbor outside its cycle, and the block-cut tree forbids a connection bypassing that cycle. Omissions within each cycle therefore form exactly one consecutive run of length at most two, and the converse selection produces a connected dominating set. This yields an exact bijection and an unambiguous product count. For each quadratic cycle factor, the discriminant bounds distinguish \(q=2\), \(q=3\), and \(q\ge4\); the sole negative discriminant occurs for the isolated triangle cycle. The proof handles trees, bridge blocks, cut-free cycles, leaves, and small orders independently. Direct exhaustive testing checked 6,280,063 candidate subsets on 823 cactus instances, plus 7,105 independent discriminant samples. Finite checking is not treated as a proof.

## Originality — PASS, with residual uncertainty

Mojdeh–Emadi (2018) already determine the full path/cycle/corona polynomials and top coefficients for arbitrary graphs, so those facts are expressly excluded from the new contribution. Yoosuf–Kuttipulackal (2021) already determine the friendship-graph specialization, and Vijayan–Felix Nes Mabel (2016) investigate tadpoles. Ibrahim–Salih (2020) treat specific complete/wheel coalescences, not arbitrary cactus block gluing. The compared published statements do not give the general cycle-specific factorization, its exact arbitrary-cactus coefficient sequence, or the real-rootedness theorem with the unique triangular exception. The 2019 doubly connected-domination polynomial is not the same invariant. The 2026 root-density paper was not available for full-text inspection; an unindexed equivalent theorem, including one derived by a general block decomposition, remains possible. No exclusivity is inferred merely from database searches.

## Value — PASS

This solves a natural full-distribution enumeration problem for all connected cactus graphs, not a handpicked finite instance. It gives an explicit structural decomposition into independently interpretable cycle factors, supports arbitrary cactus topology, and deduces a sharp global root-location theorem and coefficient log-concavity from local discriminants. The contribution extends beyond the already known individual cycle, friendship and corona formulas.

## Scope and scientific limitations

The theorem is restricted to finite connected simple cacti. The triangle is an essential exception, and the small graphs \(K_1,K_2\) use separately stated formulas. The result makes no claim of novelty for earlier special-family formulas or of completeness for general graph roots. Residual overlap risk from one recent inaccessible full text persists. Reproducible subset counts do not establish infinite correctness or originality.

Self-review: passed. Independent audit: not yet performed.
