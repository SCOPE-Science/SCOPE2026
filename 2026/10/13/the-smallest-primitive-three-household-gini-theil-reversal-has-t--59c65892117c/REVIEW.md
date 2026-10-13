# Self-review

## Correctness
**PASS.** For sorted three-household incomes with fixed total \(S\), the Gini coefficient is exactly \(2(a-c)/(3S)\), so its ordering is range ordering. Theil's \(T\) equals a fixed constant plus \(S^{-1}\ln\prod_i x_i^{x_i}\), so its ordering is certified by exact integers. Two independent complete generators exhaust all positive integer partitions through total \(13\), proving no strict reversal through \(12\) and a unique reversal at \(13\). The infinite family is not inferred from computation: differentiating its log-ratio gives a strictly positive derivative for \(x>3\), and the exact \(x=6\) base comparison closes the proof.

Risk: the minimum-total statement is a primitive-lattice statement and should not be interpreted as assigning significance to a particular currency denomination.

## Originality
**PASS.** Prior literature explicitly treats Gini and Theil as distinct inequality measures with different conceptual foundations and recognizes that alternative inequality indices can yield different judgments. The accepted claim is narrower and sharper: the first primitive equal-total three-household strict reversal, its uniqueness at total \(13\), and an infinite reversal family. Searches by aliases, exact vectors, Lorenz-crossing language, and minimal-witness language did not locate equivalent coverage.

Risk: search failure is not proof of bibliographic uniqueness. An unindexed exercise, historical table, or software example could contain the same pair.

## Value
**PASS.** Gini and Theil are standard economic inequality measures and are routinely reported side by side precisely because they weight distributional structure differently. A smallest rational equal-mean witness makes that abstract index dependence concrete, while the infinite family shows the effect is structural rather than an isolated numerical accident. The pair also has crossing Lorenz curves, so it is a compact benchmark for the limits of scalar inequality rankings.

Self-review: passed. Independent audit: not yet performed.
