# Review: exact cyclic reciprocal-adjacent-sum multiplicities

**Correctness — PASS.** Every oriented circular permutation is represented exactly once by rotating the label \(1\) to the first position and selecting the direction with second entry less than last. The exhaustive finite permutation recursion checks the exactly equivalent LCM-weight integer equality, and all sums fit unsigned 64-bit arithmetic. `verify_counts.c` generated the full table for \(3\le n\le13\); `crosscheck.py` independently verified the first two nonzero multiplicities using exact fractions. The claim has no unproved infinite extension.

**Originality — PASS with residual risks.** Ai–Hu–Yan (2026) prove existence of a suitable circular order for every \(n>7\), which is weaker than specifying all dihedral multiplicities. The highly relevant OEIS A322070 **already contains the analogous linear counts**; none of those data is claimed as new. OEIS A040018 instead counts circular orders with distinct adjacent sums. Targeted mathematical research and database searches revealed no cyclic multiplicity table with the claimed six successive values. Only excerpts of the most relevant primary manuscript were available, and other implicit or unindexed tables remain possible.

**Value — PASS.** This supplies a complete natural initial cyclic census immediately following the existence threshold, including the two exact orbit representatives at the first admissible size. The data distinguish uniqueness, rarity, and multiplicity and are meaningful benchmarks for further counting theory, without claiming a universal formula.

**Limits.** All counts stop at \(n=13\); no global growth law follows. The external independent audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
