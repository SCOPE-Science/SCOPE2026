# Review of exact-count scattered-pair automata

## Correctness

**PASS.** The concatenation identity separates prefix, suffix, and cross-boundary occurrences. The proof explicitly handles the empty prefix, already-accepted prefixes, over-counted prefixes, impossible deficits, and each reachable positive-deficit pair. A one-one suffix distinguishes different deficits; a two-one suffix distinguishes every remaining pair of active types. Consequently the \(\lfloor k^2/4\rfloor+\lceil k/2\rceil+3\) listed reachable residuals are pairwise inequivalent and exhaustive. A separately minimized saturated-counter DFA and direct word tests confirm small parameter instances. Finite computations are corroboration, not proof for all \(k\).

## Originality

**PASS, subject to residual literature risk.** The closest inspected paper is Mansour–Rastegar–Roitershtein (2019), Section 2.2: its continuation equivalence preserves all low occurrence counts rather than only exact-\(k\) membership, and the inspected constructions do not identify the minimal exact-count quotient, its collapsing one-future-one classes, or its quadratic-plus-linear state formula. Leroy–Rigo–Stipulanti (2017) and Renard–Rigo–Whiteland (2024) study underlying binomial coefficients but not this automaton-minimization question in the inspected materials. An equivalence potentially implicit in unindexed work or general minimization theory remains a risk. Distinguishing a published method from a published consequence is essential; the complete description of the quotient, not the existence of a finite automaton, is the claim.

## Value

**PASS.** Exact-frequency pattern languages are natural finite-state counting objects. The family here is infinite in its occurrence threshold; the result gives not only a state count but every Myhill–Nerode residual and an explicit distinguishing continuation. The transition between one-future-one and multiple-one residuals produces a nontrivial linear correction to quadratic growth. It does not purport to resolve arbitrary patterns or prove new generic state complexity bounds.

## Checks and limitations

Independent implementation confirms 60 small-to-medium thresholds with a partition-refinement algorithm and validates the canonical residual map. The infinite claim rests on the case-split and distinguishability proof. Literature comparison was concentrated on cited preprints, so an alternative specialization outside these sources remains possible.

Self-review: passed. Independent audit: not yet performed.
