# Review

## Correctness
**PASS.** The local inverse condition is exactly the defining length-two reverse-complement duplication rule. If adjacent starts are both valid, involutivity forces the two deletions to produce the same parent. Selecting one start per distinct parent therefore injects the parent set into an independent set of the \(n-1\)-vertex path, giving the sharp upper bound \(\lfloor n/2\rfloor\). The period-four complement-pair construction has precisely the even starts valid, and the resulting parents differ at a coordinate that is a complement pair. The fixed-point-free hypothesis is explicitly used in the distinctness step. The bundled verifier independently reconstructs forward and inverse channel relations over twelve exhaustive parameter cases.

Risk: the finite verifier cannot establish the all-parameter theorem by itself. The accepted correctness rests on the symbolic proof, and no statement is made for duplication length other than \(2\) or for complements with fixed points.

## Originality
**PASS.** The closest primary full text is Ben-Tolila--Schwartz, arXiv:2112.11811 / IEEE TIT 2022. Its Lemma 16 proves a different odd-length uniqueness statement: for a fixed parent and odd duplication length, the duplication location producing a given descendant is unique. The proof relies on odd parity and therefore does not cover the even-length case here; moreover, fixed-parent location uniqueness is not the same invariant as the number of distinct parents of a fixed received word.

The 2025 coding-capacity paper studies arbitrary numbers of duplications and states that single-duplication coding capacity is one, without an exact inverse-degree formula. The 2026 Sun--Ge paper gives redundancy bounds and constructions. The September 2026 Zabokritskiy abstract establishes an even-length reverse-complement/palindromic correspondence and studies multiple-error bounds and a two-error *forward descendant* maximum. That correspondence makes the present inverse-degree question equivalent to a palindromic one but does not, from the material available, supply its exact answer. The 2020 palindromic-duplication paper proves uniqueness properties for irreducible roots, which do not bound the number of immediate one-step parents.

Targeted published-result searches under reverse-complement, palindromic, inverse-ball, parent, preimage, and deduplication aliases returned no statement implying the formula. This negative evidence is not treated as a proof of novelty. Residual risk remains for an unindexed source and especially for an unstated lemma in the September 2026 preprint whose full text was not retrievable in the bounded comparison.

## Value
**PASS.** The maximum inverse degree is the exact worst-case uncoded list ambiguity of the one-error channel. It also pinpoints a parity boundary left visible by the foundational odd-length uniqueness lemma: length \(2\) can have linearly many distinct parents, with exact coefficient \(1/2\). The result is all-alphabet and all-block-length, has a sharp construction, and concerns a natural channel invariant rather than an arbitrary finite slice.

Risk: this invariant alone does not determine optimal code sizes or multi-error capacity, and those stronger consequences are not claimed.

## Closest literature and limitations
The closest sources are arXiv:2112.11811, arXiv:2312.00394, arXiv:2602.01151, arXiv:2609.00779, and the 2020 IEEE Access palindromic-duplication paper. The principal access limitation is that only the abstract of arXiv:2609.00779 was available during the bounded comparison.

Same-model review: passed. Independent audit: not yet performed.
