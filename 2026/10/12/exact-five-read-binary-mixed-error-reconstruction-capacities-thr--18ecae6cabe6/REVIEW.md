# Scientific assessment: Exact five-read binary mixed-error reconstruction capacities through length eight

## Correctness — PASS

The finite claimed range is fully specified. The deletion-then-at-most-one-substitution balls and independent substitution-then-deletion balls coincide at every vertex. The problem reduces exactly to clique number on completely enumerated admissibility graphs. Both separately written exhaustive coloring-pruned searches prove the upper bounds and verify explicit optimal codebooks, giving \(5,5,6,8,12\) for \(4\le n\le8\). Greedy color classes are independent sets, so pruning by color count is rigorous; no timeout, sampling or infeasibility guess is used. Source files and run commands are supplied.

## Originality — PASS, with residual risk

Li–Sun–Ge (2026), arXiv:2604.25294v1, Theorem IV.6, gives an asymptotic redundancy construction for five reads, but not these exact finite maxima. Li–Sun–Ge (2025), arXiv:2505.04232v1, Table I, concerns seven and larger reads. Song–Cai–Quek (2025), arXiv:2501.03833v4, bounds longer-word ball intersections under different hypotheses, not the finite codebook optima. The inspected primary results do not imply the claimed upper bounds. Exact earlier unindexed finite computations remain possible.

## Value — PASS

Five distinct reads is a motivating fixed-budget reconstruction regime. This sharp first-short-length capacity profile includes all four earliest fully operational lengths \(n=5,6,7,8\), giving exact finite performance benchmarks and an explicit boundary case at \(n=4\). This fills a meaningful finite optimum gap; it does not claim a general construction or asymptotic rate improvement.

## Limitations

Only binary alphabets, lengths \(4\) through \(8\), one deletion, at most one substitution, and read budget five. No classification of all extremal codebooks or larger-length capacity. Exhaustive finite search establishes no infinite family theorem. Residual originality risk from unavailable unindexed earlier computations.

Self-review: passed. Independent audit: not yet performed.
