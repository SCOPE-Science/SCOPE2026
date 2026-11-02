# Scientific review

## Correctness — PASS
The calculation counts ordered pairs of four-position embeddings by their union size, and assigns their exact joint probability. Its proof covers every word length by a finite binomial identity; there is no finite-to-infinite extrapolation. The exact coefficient table is recomputed from the definition in a standalone program and independently cross-checked against exhaustive length-4 through length-11 text enumeration. Reversal/complement orbit coverage and the strictness threshold are checked exactly.

## Originality — PASS, qualified
The closest inspected primary source, Menon–Singh (arXiv:2306.07870v1), studies occurrence frequencies and records the common mean but not the complete variance comparison. Janson–Szpankowski (arXiv:2003.09584) supplies more general fluctuation and moment machinery, but does not explicitly establish the six-class finite-length variance hierarchy or the strict onset at six. Older general hidden-word moment methods (Flajolet–Szpankowski–Vallée, 2006) may permit re-derivation. Exact moment *methods* are known: the potentially new result is the evaluated comparative classification, coefficientwise ordering, and sevenfold limiting gap. No exact equivalent was located in the searched records. An unindexed comparison or overlooked explicit table remains a substantive priority risk.

## Mathematical value — PASS
This is a complete natural classification for the first binary pattern length supporting four alternating runs, not an arbitrary isolated sample or a routine one-number increment. Patterns of the same length have identical expected counts but six strictly ordered fluctuation laws after length five, providing an exact baseline for assessing variability in hidden-pattern matching, subsequence channels and sequence profiling. The all-length coefficientwise inequalities and the sharp \(n=6\) separation are qualitative, not merely numerical data.

## Limitations
Only four-letter patterns, fair independent binary sources, and multiplicity-counted scattered occurrences are covered. No stochastic tail or higher-moment ordering is inferred. Comparison with broad general moment formulas leaves an explicit residual originality risk; human literature verification remains warranted.

Self-review: passed. Independent audit: not yet performed.
