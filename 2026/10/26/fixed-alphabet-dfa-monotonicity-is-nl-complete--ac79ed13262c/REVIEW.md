# Review

## Correctness
PASS. The upward-closure automaton and complement product reduce non-monotonicity to NFA emptiness. The lower-bound encoding is fixed-length, has polynomial size, is logspace constructible, and maps DFA emptiness exactly to monotonicity. The zero-predicate boundary follows because the alphabet is a singleton.

## Originality
PASS, qualified. Kuperberg–Moreau prove NL-completeness for DFA input with an input-dependent alphabet. Their displayed hardness reduction adds a top letter above the source alphabet; it does not state the fixed-binary restriction. The one-hot block encoding supplies that restriction. Targeted literature searches did not surface this exact fixed-alphabet claim; unindexed prior art remains possible.

## Value
PASS. The result shows that the hardness of semantic monotonicity testing does not depend on an unbounded number of predicates: one predicate suffices, while zero predicates give a trivial problem. This is a precise vocabulary-size boundary relevant to the distinction between semantic monotonicity and syntactic positivity.

## Closest literature and limitations
Kuperberg and Moreau, arXiv:2406.17693, Proposition 4.5 and Appendix B.3. The theorem is for explicit DFAs; it does not address NFAs, succinct encodings, or the decision problem for positive definability.

Self-review: passed. Independent audit: not yet performed.
