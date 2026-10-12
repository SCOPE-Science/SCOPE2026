# Self-review

## Correctness
**PASS.** At fixed household count \(n\) and total income \(S\), Gini ranking is exactly ranking by the integer pairwise-distance sum \(D\), while coefficient-of-variation ranking is exactly ranking by the integer squared-deviation sum \(Q\). Positivity bounds the household count by \(n\le S\), so the lower-bound claim is a finite exhaustive statement. The verifier enumerates every positive integer partition and every same-\((n,S)\) pair through \(S=12\), totaling \(762\) comparisons. It finds no strict reversal through \(S=11\) and exactly one at \(S=12\), and independently checks the displayed fractions and the two-household identity.

Risk: changing the domain to allow zero incomes or unequal totals changes the cutoff.

## Originality
**PASS.** Sen and Allison establish the two measures as standard inequality indices, while Bendel et al. directly compare them and document that their empirical orderings and sensitivities can differ. The 1989 paper was inspected in full, including its constructed examples and discussion of right-tail sensitivity. Neither it nor the other checked sources states the smallest fixed-total positive-integer reversal, the unique \(S=12\) strict pair, or the unique \(S=10\) first tie split. Exact-vector, fixed-mean, integer-grid, and generalized-entropy searches did not locate those statements.

Risk: an unindexed exercise or software test could contain the same small witness even though the sharp global cutoff was not located.

## Value
**PASS.** Gini and the coefficient of variation are established inequality measures with materially different sensitivity profiles. Holding both population size and total income fixed removes scale and population-size effects, isolating the effect of distributional shape alone. The exact first tie split and first strict reversal provide a compact finite-resolution benchmark for interpreting or testing implementations of the two measures.

Self-review: passed. Independent audit: not yet performed.
