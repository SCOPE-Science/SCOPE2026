# Self-review

## Correctness — PASS

The three-state minimum-cost/count recurrence is derived from disjoint child subtrees and the exactly-one-or-more-selected-child condition for a dominated, unselected root. The base profiles and the three-phase induction establish the optimum numbers and enumerate all minimizers. The bottom support-vertex replacement lemma proves the all-pattern pruning invariance; a two-to-one exchange with the unique surviving leaf establishes the sharp one-group doubling. The `verify.py` script checks 25 full-tree cost/count values, 75 simultaneous retention-pattern prunings, 25 sharp one-group deletions, and 18 exhaustive small-instance minimality and exact-count cases, including nine explicit all-optimum-set classification cases. Computation is supporting evidence, not the proof.

## Originality — PASS (historical-priority caveat)

Allagan et al., arXiv:2601.03485v1 (January 7, 2026), already establish the binary-tree phase law, binary one-leaf doubling, and a general three-state algorithm. Those are prior work. Oyewumi, Roux and Wagner (2025) count all dominating sets in d-ary trees, a different quantity. The new contribution is a higher-branching closed optimum census, complete optimum classification, and the exact all-sibling retention threshold with a sharp one-group transition. Semantic record searches, own accessible historical claim comparisons, and targeted published-literature searches identified no statement covering those stronger specific assertions. Generic algorithms and elementary local exchange steps are not independently claimed. A potentially unindexed historical formulation remains a residual risk.

## Value — PASS

The number and structure of minimum dominating sets measure placement flexibility, while deletion of terminal leaves models changes in boundary coverage constraints. The theorem shows a sharp difference between binary trees and higher-branching trees: simultaneous removal of up to \((d-2)d^{h-1}\) leaves leaves the entire optimum family untouched, but one group reduced to a lone leaf creates exactly one new choice for every optimum. This quantitative rigidity law holds across an infinite, natural two-parameter graph family and answers a motivated question beyond minimum cardinality alone.

## Scope and limits

Perfect uniformly branching rooted trees of positive height; terminal leaf deletions only. Results do not classify multiple simultaneously exceptional sibling groups, arbitrary nonuniform branching, or internal vertex deletions. The binary special case is already established in prior work. Independent review and further historical-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
