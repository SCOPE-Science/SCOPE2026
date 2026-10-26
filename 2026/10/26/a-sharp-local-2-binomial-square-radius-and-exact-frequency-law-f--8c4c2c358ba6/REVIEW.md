# Self-review

**Correctness — PASS.** The proof independently derives the equivalence signature, checks all 512 possible aligned length-72 cases using a supplied executable certificate, and derives limiting pair frequencies and densities. The length-128 morphism-block cover is an exhaustive infinite-word reduction, not a sample. Every allowable index and smaller root is handled; the least possible universal bound 36 is attained already at index 19.

**Originality — PASS against inspected sources.** Rigo–Salimov (2013) develops 2-binomial equivalence and global factor-complexity; Rao–Rigo–Salimov (2015) studies avoidance of squares and cubes using other morphisms; Lejeune–Leroy–Rigo (2020) computes the number of Thue–Morse binomial classes. These results do not give all-start least adjacent-root values or their exact position densities. Searches for equivalent first-moment/Parikh-matrix formulations, stronger global statements, and existing exact 36-root tables identified no covering result. An earlier unindexed calculation remains a historical-priority risk.

**Mathematical value — PASS.** A sharp worst-case local radius, a complete rational frequency law, and an explicit characterization of the exceptional positions are mathematically motivated refinements of square existence under subsequence equivalence. The result distinguishes global possible-root lengths from minimal local roots at every start. The required finite calculation is complete and independently reproducible. The theorem is limited to this specific morphic word; arbitrary sequences and longer roots remain outside scope.

The attached verification code uses two distinct equivalence computations, but this does not constitute an independent scientific audit. Detailed checks, source comparisons and residual risks are in `AUDIT.json` and `VERIFICATION.md`.

Self-review: passed. Independent audit: not yet performed.
