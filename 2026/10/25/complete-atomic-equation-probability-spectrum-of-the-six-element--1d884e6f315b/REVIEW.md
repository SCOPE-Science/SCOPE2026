# Scientific review: atomic-equation probabilities in the six-element permutation group

## Correctness
**PASS.** The claim is precisely an atomic equality-probability spectrum for the fixed finite group \(S_3\), without named nonidentity parameters. The proof reduces every equation to a word identity, writes the word map in \(\mathbb F_3\rtimes\mathbb F_2\) coordinates, verifies the necessary coefficient identity by induction, and proves its sufficiency by a constructive module-spanning argument. The key nonstandard step is supported by explicit square- and commutator-word coefficient vectors, character projectors, and the local rank calculation. Counting kernel/nonkernel rotation assignments then gives all and only the asserted arity-specific probabilities. The one-variable case is treated separately. The standalone checker confirms all \(972\) two-variable word functions, \(124\) local spanning ranks, and \(828\) direct evaluations. Finite checks do not replace the arbitrary-arity proof.

## Originality
**PASS with historical-priority risk.** Cardó (arXiv:2604.08446v1, 2026-04-09), in the fully inspected relevant portions of his paper, explicitly states that the equational probabilistic spectrum of \(S_3\) is unknown. His one calculated family does not cover all equations or the new complete spectrum. Schneider–Thom (arXiv:2206.11956) study symmetric-group word maps with constants and asymptotic image size, not the fixed \(S_3\) constant-free exact probability range; their introductory/main-theorem/appendix material was compared. Separate older word-map techniques could conceivably imply this result even without the spectrum being stated. Title and keyword searches, relevant source comparisons, and checks against accessible prior finding claims did not identify equivalent or stronger coverage, but search absence cannot establish historical uniqueness.

## Value
**PASS.** A cited April 2026 paper explicitly leaves this precise small-group spectrum open; the result gives its full answer, establishes the optimal positive gap and shows all attainable values arise without gaps at each fixed arity. It is a natural exact classification of satisfaction probabilities of atomic first-order formulas in a fixed finite structure, rather than an arbitrary finite sample or an increment to an already enumerated table.

## Scope and remaining limitations
No arbitrary first-order formulas, constants naming nonidentity elements, larger groups, or minimal word-length bounds are classified. Algebraic argument and computation are included; independent replication and historical-priority review have not been performed. The main comparison with Cardó was possible in HTML full text; one related companion work was available only at abstract level and is not asserted to be wholly non-covering.

Self-review: passed. Independent audit: not yet performed.
