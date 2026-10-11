# Scientific review

## Correctness — PASS
The explicit cyclic-shift identity follows directly from the phase labelling of a single orbit. A nonempty proper subset of the prime cyclic group cannot be invariant under a nonidentity translation, proving the uniqueness used at each induction step. The prefix-function algorithm processes each pair of length-\(p\) words in linear time, yielding \(O(p^2)\) reconstruction and \(O(p)\) auxiliary storage. Every prime cycle was checked up to \(p=7\), with randomized larger tests. The infinite statement is proved analytically, not inferred from the tests.

## Originality — PASS (residual risk)
The full relevant Section 2 of Fuhrmann--Gröger--Passeggi (arXiv:2610.07435v1), including Lemma 2.1, proof, and Remark 2.4, states cubic reconstruction complexity; it does not present this cyclic-shift matching algorithm. Knuth--Morris--Pratt supplies linear-time matching only, not the representation of ordered orbit signatures as translates. Searches across mathematical records and the cited primary literature found no equivalent quadratic algorithm. A previously unindexed optimization of the original proof cannot be ruled out.

## Value — PASS
Reconstructing the orbit permutation is the algorithmic core of a new interval-map periodic-spectrum rigidity argument. Replacing cubic by quadratic work for an explicit quadratic-sized signature input is a substantive asymptotic improvement with an exact reproducible algorithm; this is not a new interval-map rigidity theorem or a lower bound for partial-query settings.

## Closest literature and boundaries
Fuhrmann--Gröger--Passeggi, Remark 2.4, gives \(O(p^3)\) reconstruction and proves uniqueness. The present result concerns only the table-to-permutation step. Classic linear-time pattern matching is a generic subroutine. Earlier or unpublished algorithmic improvements remain possible.

Same-model review: passed. Independent audit: not yet performed.
