# Scientific review

## Correctness — PASS

The source definition of AWVC blocks a target with positive support only when a coalition of disapprovers has \(|S|/s>1-b_S/m\). Each copy of \(d\) adds exactly one alternative to the universe and exactly \(\chi_S\) to the unanimously superior set, yielding the stated affine inequality with strict/equality boundaries handled correctly. Strict-majority support makes the two possible slopes unambiguously positive or negative, hence their intersection an exact integer interval. For the five-voter family, all and only the three nonempty disapprover coalitions are evaluated, producing the exact conditions \(t\le3h-2\), \(t\ge1\), and \(t\ge7-3h\); the last is redundant for \(h\ge2\). The proof covers all quantified parameters and does not infer infinity from computation. The independently coded direct criterion agreed with the affine and constructive versions in 25,270 exact-integer comparisons.

## Originality — PASS with residual risk

The 2026 primary paper defines AWVC and proves majority-threshold and disapproving-voter monotonicity properties, but neither states an exact candidate-cloning interval nor constructs arbitrarily long exclusion–inclusion–exclusion windows. A highly relevant predecessor, Ianovski and Kondratev (2023), *already proves non-independence of clones* for ordinary proportional veto-core-consistent rules (Proposition 15). That qualitative phenomenon is explicitly credited and excluded from the new claim. The new statement compares **fixed target membership under arbitrary numbers of repeated copies of one other alternative** for the approval-weighted denominator, together with an exact, unbounded five-voter profile family. Searches for alias terms, clone-independence, candidate duplication, proportional-veto reductions, and the source-paper exact rule did not locate a stronger statement covering the complete theorem. An unindexed prior derivation of this interval calculus, or a general clone-response result specialized to AWVC, remains a publication-priority risk.

## Value — PASS

When a consent rule is used to decide which proposals remain eligible, its sensitivity to introducing synonymous or near-identical proposed options is a practical structural question. The theorem supplies a complete quantitative bound on that dependence, rather than merely observing that some clone can change an outcome. A particularly severe nonmonotone response occurs with only five fixed voters and 60% target approval: cloned alternatives cause temporary acceptance for an arbitrarily long interval, followed by renewed exclusion. The family is mathematically natural because it isolates competing singleton veto coalitions and keeps the voter environment unchanged; this is a substantive new sensitivity boundary beyond a textbook rephrasing of the blocking definition.

## Scope and evidence risks

The result uses finite normalized counting measure, coherent top-prefix approvals, and adjacent perfect copies. A different continuous alternative measure, an approval reelicitation after candidate insertion, or a downstream winner-selection rule is not covered. Finite regression tests support the proof but are not themselves a proof. No independent scientific audit has been conducted.

References: Dong et al., arXiv:2609.10759v1, Definition 8 and Theorem 4; Ianovski and Kondratev, arXiv:2003.09153v4, Proposition 15.

Self-review: passed. Independent audit: not yet performed.
