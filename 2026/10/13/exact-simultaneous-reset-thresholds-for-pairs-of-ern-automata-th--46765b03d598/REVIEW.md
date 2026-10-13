# Self-review

## Correctness — PASS

Every nonempty pair of subsets of the two state sets is a possible vertex in an explicitly bounded transition graph. The edge actions are letter-by-letter deterministic images. A common reset word corresponds bijectively to a path from the pair of full sets to a pair of singleton sets. Breadth-first search therefore determines the exact shortest length, and its exhaustive reachable-state traversal is a finite lower-bound certificate, not merely experimental upper-bound search. A dictionary-based Python traversal and an independent integer-encoded C++ traversal agree on every one of 45 thresholds and their lexicographically earliest witnesses. Both replay all witnesses. Table-derived assertions hold precisely within the displayed domain. The elementary divisible-size observation uses the known optimal single-automaton reset word.

## Originality — PASS, with residual risk

Classical single-automaton shortest reset lengths and known shortest-word algorithms are not new. The 2012 shortest-reset algorithm (arXiv:1203.2822) and 2016 automata census (arXiv:1607.04025) do not give shortest words in intersections of two different-size Černý reset languages. The 2014 reset-language equality paper (arXiv:1405.3576) introduces the direct-product intersection identity and a different PSPACE-type comparison problem, but the relevant text contains no exact thresholds for these pairs. The 2014 random-input Černý analysis (arXiv:1404.6731) considers merging two states of one automaton. A bibliographic overlap with unindexed or inaccessible earlier tabulations remains possible; a negative search result is not a proof of novelty.

## Value — PASS

A shortest **shared** control word is a natural resource constrained by two independently initialized cyclic state machines, distinct from either separate reset length. The full triangular 45-pair finite classification quantifies its possible overhead, shows a sharp finite worst-case delay of \(n-3\) for each \(3\le n\le11\), and identifies nonmonotone and zero-overhead behavior across smaller partners. Every result has an explicit reconstructible witness and exact finite exclusion of all shorter words. This is a natural self-contained finite atlas, not a routine restatement of the single-system optimum.

## Limits and closest coverage

The published product identity itself is not claimed new. No assertion about general \(n>11\) shared thresholds follows from finite enumeration. Inaccessible older specialist computations and alternative index terms remain bibliographic risks. Scientific acceptance is an internal consistency judgment; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
