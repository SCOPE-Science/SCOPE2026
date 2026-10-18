# Scientific review

## Correctness — PASS

The proposed claim is one combined exact theorem about rooted intuitionistic fork theories and their minimal-variable branching cutoff. The proof specifies the exact frame, all allowed persistent valuations, and the full intuitionistic implication clause. A structural induction establishes that the pair of root and distinct leaf colors determines every rooted formula; explicit negated minterms recover every leaf color and atoms recover the root color. This gives an exhaustive bijective count, while an explicit finite disjunction is valid at every world on the smaller frame and false at the root of the larger frame. The finite checker directly evaluates the semantics and corroborates all tested counts and distinguishing formulas; it is not substituted for the general proof.

## Originality — PASS, with stated residual risk

The closest inspected source, Almeida's 2026 *Uniform Local Tabularity in Intuitionistic Logic*, develops colored models, bisimulation and examples using the two-fork, but its explicit results address uniform implication-depth logic rather than all rooted \(n\)-types of arbitrary finite forks and the sharp \(k\)-versus-\(n\) threshold. Related material in Almeida's dissertation was checked in the universal-model and uniform-tabularity chapters. Hyttinen et al. (2024) obtain exponential color-count bounds for a different layered infinite Esakia construction; it does not establish the exact finite-fork census or the formulas giving each sharp transition. Searches for equivalent fork terminology, bounded branching, full rooted-type profiles, and minimum-variable separation did not identify a dominating theorem. A previously unindexed equivalent specialization of the standard bisimulation theory remains possible.

## Value — PASS

The full classification makes a motivated model-theoretic question exact: how many genuinely different rooted theories can a finite branching frame realize in a restricted propositional language, and precisely when does additional branching become invisible? The binomial census determines the whole natural type spectrum, not one small instance, while the formula construction proves that the cutoff is optimal at every finite level. Such finite-variable compression is relevant to analyzing tabular intermediate logics and generating finite-model test collections; no speculative stronger general theorem is claimed.

## Boundaries

The count is not the number of elements of a free Heyting algebra; intermediate levels, arbitrary posets and richer languages are not covered. The result is subject to the usual risk of unindexed equivalent results. The code's finite checks are not independent or infinite certification.

Self-review: passed. Independent audit: not yet performed.
