# Self-review

## Correctness — PASS

The definitions use standard open neighborhoods and private selected witnesses. The five-column test is logically equivalent to the super domination definition because candidate witnesses lie at column distance at most one and their full neighborhoods at most two; genuine boundaries explicitly forbid virtual witnesses. The exact max-plus recurrence uses complete state supports, not scalar extrapolation. The verified identities \(V_{11}=V_9+3\) and \(V_{12}=V_{10}+3\) propagate to all later widths by transfer homogeneity. The verified first twelve widths establish the formula by induction. Independent direct graph-based enumeration for widths up to six agrees. The even-width minimum-set classification follows from perfect-matching cuts and four-cycle propagation; no numerical experiments are used to prove its infinite scope.

## Originality — PASS (best knowledge, residual risk)

The closest directly relevant paper is Klein, Rodríguez-Velázquez and Yi, *On the super domination number of graphs*, arXiv:1705.00928v2, Theorem 24, which already gives **all even-width numerical values** (so those numerical values are not original) but gives bounds, not the exact odd-width three-row formula, and does not classify the two even-width minimum sets. The full accessible primary text was examined. Full-text checks of Ghanbari, Jäger and Lehtilä (arXiv:2209.01795v3) and Bujtás, Ghanbari and Klavžar (arXiv:2302.08862v1), plus completed semantic mathematical-record searches, found no covering statement. Other invariants of the same grids, including integer \(\{2\}\)-domination, are not equivalent. The residual possibility of a missed or differently named independent exact result is recorded.

## Value — PASS

Odd Cartesian products are precisely the regime left between bounds by the 2017 foundational result; the theorem resolves an infinite natural constant-height family with a genuine small-width exception. Even widths exhibit strong rigidity not determined by the known cardinality equality: exactly two optimal vertex sets, contrasting with the variety seen in odd small widths. Both are exact natural invariants of a standard grid family, with a reusable local-state proof method.

## Limitations and review state

This is a three-row theorem, not a general grid-width formula; minimum-set counts for odd widths are not claimed. The finite-state proof is entirely supplied and checkable but has not undergone independent scientific audit. Literature coverage cannot guarantee that no unindexed equivalence exists.

Self-review: passed. Independent audit: not yet performed.
