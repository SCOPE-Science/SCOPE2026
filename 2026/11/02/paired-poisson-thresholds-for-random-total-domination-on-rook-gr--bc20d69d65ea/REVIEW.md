# Scientific review: paired Poisson rook-domination thresholds

## Correctness

**PASS.** For selected incidence indicators \(A_{ij}\), the open-neighbor count is \(d_i+e_j-2A_{ij}\). The proof verifies joint independent-Poisson convergence of the numbers of \((r-1)\)-degree rows and columns by mixed factorial moments and bounds the expected number of low-degree occupied crossing exceptions by \(O_r((\log N)^3/N)\). It explicitly deduces the odd/even truth events and uses a monotone coupling with binomial selection-count concentration to transfer the conclusions to uniform fixed-cardinality samples and exposure times. This is an infinite-family proof, not extrapolation from the finite tests. The independent open-neighbor implementation agrees with the row/column criterion on 2,608 exhaustive small-board cases; a separate seed-controlled simulation illustrates the distinctions and retains finite-size deviations.

## Originality

**PASS with documented residual priority risk.** Carballosa–Wisby (arXiv:2001.07850, January 22, 2020) studies deterministic minimal total \(k\)-domination of Cartesian products of complete graphs; Pahlavsay–Palezzato–Torielli (arXiv:1807.08104) studies minimal total \(3\)-domination of rook graphs. The degree-count identity is available in this subject and is expressly not claimed as new. Neither inspected primary treatment establishes an independent-Bernoulli random placement window, the joint Poisson deficiency count with different odd/even Boolean events, or the induced hitting-time laws. Standard low-degree Poisson limit arguments are previously known tools and not claimed as independent discoveries. Six semantic mathematical-record searches, targeted primary-literature searches and accessible own-history claim comparisons revealed no exact implication of the claimed paired result. Unindexed or differently phrased random bipartite-incidence literature may still overlap.

## Mathematical value

**PASS.** The paired result quantifies a nontrivial discrete parity phenomenon: at the same \(N\log N\) random-placement threshold, neighboring total-domination requirements have different transition laws. Their joint probabilities, an explicit maximum separation of one half, and equivalent random-order stopping-time distributions describe the reliability of random placements, a different and naturally motivated object from previously studied optimized minima. The proof isolates precisely which low-degree incidence obstructions control the phenomenon and why occupied-cell corrections disappear. It is neither a mere scalar restatement nor a parameter substitution.

## Limitations and closest literature

Fixed \(r\), fixed real \(c\), and balanced square rook graphs only. No claim of complete prior-literature coverage. Source inspections and search comparisons are itemized in `AUDIT.json`. The 2018 rook graph degree identity and 2020 deterministic extremal theory are credited. The finite checker does not verify convergence or priority.

Self-review: passed. Independent audit: not yet performed.
