# Self-review

## Correctness — PASS

The theorem is a finite exact statement on precisely specified deletion shadows. Every code witness, LP primal/dual feasibility inequality, and weighted-clique inequality is checked using exact rational arithmetic by the included dependency-free verifier. The 77 conflict cliques have explicit word lists and each is checked pairwise, while their total fractional cover weight is exactly \(482/23<21\). Thus the resulting integral upper bound is \(20\), matching the included length-eight twenty-word construction. The exact fractional optima and shorter integral optima are certified with matching rational primal/dual data. This checks the complete finite domain and invokes no unverifiable optimization-software output.

## Originality — PASS (historical-priority qualification)

Relevant primary literature on exact consecutive deletion bursts was compared by *implication*, not titles. Schoeny et al. (arXiv:1602.06820, Sections II–IV) supply the same channel and a general length-eight upper bound of \(24\) after integer rounding, but not the proposed twenty-word exact optimum, nor the first fractional-packing gap. Ye and Ge (arXiv:2610.05696) address stronger substring edits and asymptotic redundancy, not the particular exact finite maximum. Search results for closely related published coding claims cover other channels (two total deletions, substring edits, deletion covering, or one insertion plus deletions) and do not imply the stated result. The 1967 adjacent-deletion paper of Levenshtein could not be checked in full; this remains a real historical-priority limitation. Searches alone do not prove priority.

## Value — PASS

The number \(A_2(n)\) is the fundamental zero-error code capacity for a fixed finite binary burst-deletion channel. The small-length cutoff is not arbitrary: length eight is exactly the first strict failure of the natural deletion-shadow fractional packing relaxation, and the gap is resolved by a different, stronger family of conflict-clique inequalities. The exact integrality obstruction explains why the conventional fractional-transversal technique cannot settle the cardinality there, and gives a reproducible finite benchmark for improved channel bounds.

## Limits and comparison

No classification of every optimum, general-length theorem, or asymptotic implication is asserted. Source comparison is focused on accessible primary sections and has residual historical-priority uncertainty. All computational work is part of a finite, explicit exact rational proof, independently checkable from the package but not independently audited.

Self-review: passed. Independent audit: not yet performed.
