# Scientific review

## Correctness: PASS
The claim is reduced to a local deletion-equality lemma: identical outputs from two possible adjacent-pair deletions force two-periodicity, and the second palindromic window forces this entire interval to be constant. This yields exact grouping of inverse operations by marked run. The length budget proves the sharp maximum and an alternating run construction attains it for every received length. Counting nonconstant palindromic windows and starts of long constant runs gives the incidence identity. Independently enumerated parent sets match the structural prediction for 59,420 words across 19 parameter cases. The finite check corroborates, but does not substitute for, the proof.

## Originality: PASS, subject to stated residual risk
The 2020 primary article by Zeraatpisheh–Esmaeili–Gulliver examines overlaps among length-two palindromic squares and deduplication priorities. That overlap discussion is acknowledged, rather than claimed as original. Its inspected discussion does not supply the complete distinct-parent run-count theorem or global/aggregate formulas. The 2023 Yohananov–Schwartz article addresses asymptotic capacity under arbitrarily many such errors rather than one-step inverse lists. The 2017 duplication-coding work concerns another optimization. Targeted comparison against associated research records finds nearby coding optima and tandem/noisy duplication inverse counts, but not this transformation's exact one-step theorem. Residual risk: an implicit or unlocated general-formula specialization may already cover it.

## Mathematical value: PASS
A one-step inverse-list cardinality is the exact local ambiguity faced by a decoder of a palindromic duplication, not an arbitrary statistic. The marked-run characterization makes it computable directly; the maximum is an exact worst-case list-decoding constraint; and the incidence count measures the entire error relation for every alphabet size and length. The result explains the collapse of many apparently distinct deletion positions into one parent, including a sharp extremal construction. It is a self-contained structural classification beyond tabulation of small examples.

## Scope and risk
Only one palindromic duplication of span two, with no substitution or additional edits, is considered. No code capacity is inferred. The close 2020 overlapping-square material is not subsumed or claimed to be new. Finite verification is not an all-length proof.

Self-review: passed. Independent audit: not yet performed.
