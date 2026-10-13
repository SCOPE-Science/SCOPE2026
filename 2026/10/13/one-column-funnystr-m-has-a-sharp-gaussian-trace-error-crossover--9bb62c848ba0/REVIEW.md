# Self-review

**Correctness — PASS.** The exact rank-one eigenvalue follows by a rational Rayleigh-quotient computation. The Gaussian-square ratio has the stated beta-prime density. A rescaling makes the expected trace excess an explicit nonnegative integral with an integrable majorant, and dominated convergence yields the Gamma constant. The special \(\theta=1\) identity agrees with exact rational test cases; the almost-sure conclusion follows from a fixed-sketch expansion. The finite checker supplements but cannot replace the all-parameter proof.

**Originality — PASS, with literature risk.** Persson–Kressner give the algorithm and multi-column bounds rather than a one-column sharp Gaussian transformed-trace asymptotic; Gittens–Mahoney give a deterministic alignment bound on power Nyström, not an expected transformed-function trace law. The known unpowered Gaussian residual behavior is not claimed as original. A narrower earlier one-column Gaussian residual law would not determine the all-pass transformed-function asymptotic without an additional argument. Detailed statement-versus-implication searches and source inspections are in `AUDIT.json`. A specialized unindexed calculation remains a priority risk.

**Value — PASS.** The contrast-dependent separation between typical and mean error is directly tied to whether a single Gaussian matrix-function sketch gives a trustworthy expected trace approximation. The sharp \(\theta=1/2\) one-pass threshold and the universal two-pass recovery across \(0<\theta\le1\) give a concrete pass-versus-function-smoothness boundary. Even for this minimal system, bounds requiring oversampling do not answer the expectation question.

**Closest literature and limits.** See Persson–Kressner (arXiv:2209.11023) and Gittens–Mahoney (JMLR 17:117, 2016). Results are two-dimensional, Gaussian, asymptotic at fixed pass count, and exact-arithmetic only. Independent publication-priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
