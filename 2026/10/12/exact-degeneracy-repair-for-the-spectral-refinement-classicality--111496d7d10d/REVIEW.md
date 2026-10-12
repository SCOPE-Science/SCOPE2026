# Self-review

## Correctness
PASS. The existential equivalence follows directly from product-basis diagonalization and marginal partial traces. The universal characterization follows because all rank-one product projectors inside a fixed \(P_\alpha\otimes Q_\beta\) block generate the full matrix algebra on that block, so their commutant is scalar; cross-block terms are excluded by the block projectors. The converse is immediate. The two-qubit witness is exact.

## Originality
PASS. Later literature already covers the ambiguity of spectral-eigenbasis choices for degenerate marginals, including Bell-diagonal and Werner-type examples. The accepted claim is deliberately narrower and different: it repairs the logical quantifier in the general rank-one spectral classicality criterion and classifies exactly when all refinements give the same classicality verdict. Statement-level searches and full-text comparison of the closest sources did not locate that general block-scalar if-and-only-if theorem. Residual risk remains because the proof is elementary and could appear in an obscure note.

## Value
PASS. Degenerate reduced states occur systematically in symmetric quantum states. The theorem separates three notions that are easily conflated: being classical-classical, being classical in one compatible marginal eigenbasis, and being invariant under every marginal eigenbasis. It therefore gives an exact criterion for when the common spectral-measurement shortcut is logically safe without optimization.

## Closest literature and limitations
The defining 2008 paper was inspected through its classicality theorems and spectral-measurement construction. A 2009 analysis explicitly discusses ambiguity from degenerate marginals and basis dependence in symmetric states. A 2011 analysis explicitly discusses Bell-diagonal ambiguity and optimization. These sources cover the phenomenon, but the inspected statements do not give the general existential repair together with the universal block-scalar characterization. The remaining risk is a poorly indexed source containing the same elementary commutant argument.

Self-review: passed. Independent audit: not yet performed.
