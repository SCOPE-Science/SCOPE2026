# Scientific review

## Correctness

The successor map is forced to be a binary bijection at each length-\((k-1)\) middle word. Each crossing choice therefore induces a permutation of all binary length-\(k\) states, and its single-cycle condition is exactly the de Bruijn condition. A length-\((k+1)\) factor from an uncrossed pair has the same first and last symbol; a crossed pair gives the two explicitly tested words. The all-order weighted formula follows. Each flip of a crossing bit composes the rotation permutation with a transposition, proving the necklace-based lower and parity constraints. For order five, exhaustive feedback-mask checking and a distinct direct cyclic-word generator both gave the exact same eight-cell table and all \(2048\) cycles; weight and moment assertions were replayed from `verify.py`. No finite experiment is used to claim the all-order formulas without proof.

## Originality

The 2015 unbordered-factor paper was inspected in full-text sections on definitions, expected maximal factor length, proofs, and algorithms; it does not give de Bruijn-cycle transition spectra. The author-supplied full text of Kari–Xu treats multi-shift and antimorphic de Bruijn generalizations and their overall counts. The relevant 2021 locally constrained de Bruijn article discusses window uniqueness, codes, and an enumeration of the \(2048\) order-five cycles for a different statistic, but not an unbordered-factor histogram. Related extant order-five palindrome and cycle-overlap statistics do not imply the current weighted unbordered-factor law. Searches returned no directly matching distribution; this is not absolute evidence of absence.

## Value

Order \(k+1\) is the first circular factor length not forced to be complete in every order-\(k\) de Bruijn cycle, so border-freeness at that scale is a natural structural measure of pattern diversity. The theorem gives an all-order feedback interpretation and a complete, nonconsecutive order-five spectrum, sharp bounds, and exact moments, rather than a numerical sample or a predicate swap applied to a previous census.

## Residual risks and scope

This is a self-review only. No independent audit was performed. Specialized unpublished or unindexed enumerations of border-free patterns could exist; the novelty search is not exhaustive. The numerical distribution is confined to binary order five, and the proof gives no general-order spectrum.

Self-review: passed. Independent audit: not yet performed.
