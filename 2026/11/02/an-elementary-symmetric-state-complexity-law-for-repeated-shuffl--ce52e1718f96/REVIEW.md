# Scientific review

## Correctness — PASS
The claim specifies the alphabet, distinct symbols, positive block lengths, finite number of copies, complete DFA and all boundary cases. Every shuffle satisfies the prefix-capacity inequalities; the explicit greedy assignment proves their converse. Every feasible count vector has a reachable prefix and an accepting completion. Different vectors have different mandatory remaining letter-composition vectors, making their nonempty right quotients distinguishable. The residue-level decomposition counts all feasible vectors exactly, including saturated boundaries, and yields the elementary-symmetric polynomial. `checker.py` directly enumerates ten shuffle languages and their right quotients and separately verifies 600 count-vector instances. Finite evidence supports but does not replace the proof.

## Originality — PASS, qualified by priority risk
In the inspected 2009 Biegler–Daley–McQuillan primary text, Theorem 12 concerns a two-word quadratic upper bound, and Theorem 10 gives an exact special-case formula for periodic inputs with an underlying non-repeating word. Neither implies the exact all-copy elementary-symmetric formula: a big-O upper bound gives no coefficients, and the exact two-word periodic formula does not classify arbitrary finite numbers of copies of ordered-block words. The inspected 2015 Brzozowski et al. primary source gives broad worst-case bounds for two-language shuffle, not this family-specific equality. The 2021 Hoffmann paper addresses unbounded shuffle closure and commutative inputs, not this finite ordered shuffle. Targeted research-record and literature searches did not identify a covering theorem. This absence does not prove absolute priority. Other lattice-path or concurrent-trace terminology could conceal a prior equivalent result.

## Value — PASS
The family is a natural model of interleavings of identical sequential-stage processes. The result gives a closed exact minimum-state law simultaneously in the number of stages, the stage lengths and the number of processes, rather than just upper bounds. Its elementary-symmetric formula exhibits a hidden full permutation-invariance of complexity that is not apparent from the ordered languages, and yields exact polynomial growth in the number of processes. These structural features distinguish the result from routine substitution into a general shuffle bound.

## Closest literature and limits
The relevant primary comparisons are arXiv:0907.5111 (Theorems 10, 12), arXiv:1512.01187 (general shuffle bound), and arXiv:2103.09587 (different iterated-shuffle regime). The assertion is confined to identical ordered-block words with pairwise distinct letters; broader repeated-stage skeletons and heterogeneous shuffles are not resolved. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
