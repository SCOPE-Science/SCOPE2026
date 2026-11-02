# Self-review

## Correctness: PASS
The claim quantifies over every integer \(n\ge2\) and all unrestricted partial matchings of a specified complete strict preference family. The exact circular comparison lemma partitions the clockwise arcs between matched endpoints. In odd order every matching leaves a core agent unmatched; its exact blocking degree is at least \(k\). In even order the dummy-matched and dummy-unmatched cases jointly force degree at least \(k\). The displayed explicit matchings achieve at most \(k\). This proves the all-order formula without computational assumptions. Exact enumeration independently reproduces the formula through ten agents. A separate exact finite enumeration of every symmetric acceptability graph and strict preference profile through four agents proves the smallest-size lower bound. The finite census is not extrapolated beyond its range.

## Originality: PASS, with residual publication-priority risk
The most relevant full-text comparison is Glitzner and Manlove's *A Minimax Perspective on Almost-Stable Matchings* (arXiv:2601.14195), including its distinct Theorem 3.5 (logarithmic lower bound for unrestricted complete-list roommates) and Theorem 3.7 (linear lower bound only under a maximum-cardinality restriction). Neither stronger claim subsumes the present unrestricted linear family. The preliminary proceedings article concerns the same introduced fairness objective. Earlier almost-stable roommates literature counts total blocking pairs, not worst agent blocking degree. Searches using alternate labels, cyclic preferences, and worst-case asymptotics did not locate an identical result. Absence from a searched record is not proof of first publication; an equivalent unindexed treatment of cyclic orders remains a genuine risk.

## Value: PASS
Worst-agent blocking-pair degree models concentrated deviation incentives when stable roommate assignments are unavailable. The prior general complete-preference lower-bound construction grows only logarithmically. This explicit linear-rate separation closes the worst-case asymptotic order with the universal \(n-1\) upper bound, without requiring maximum-cardinality assignments or incomplete lists. The exact five-agent onset identifies the smallest population displaying degree at least two. Neither is merely a parameter substitution in the prior recursive construction.

## Limits and references
The \(\Theta(n)\) bound is about the worst-case order, not the sharp universal leading constant. Sources: Glitzner--Manlove (2026), arXiv:2601.14195 (Sections 2--3 and Theorems 3.5, 3.7); Glitzner--Manlove, AAMAS 2026, doi:10.65109/pcde6577; Abraham--Biró--Manlove (2006), doi:10.1007/11671411_1. Primary source full text inspected; the two shorter contextual sources were reviewed by accessible abstract/metadata and not used to assert their entire contents lack the new theorem.

Self-review: passed. Independent audit: not yet performed.
