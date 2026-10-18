# Scientific review

## Correctness — PASS

The theorem covers every dimension and finite alphabet in the specified GF(2) parity-acceptance model. Expanding the matrix-monoid Hankel kernel and separating the two endpoint-normalization cases gives the exact rank \(n^3-n^2+n\). The lower bound follows from explicit ternary matrix generators of the full monoid. A standalone exact-bit verifier checks the monomial bookkeeping through dimension eight, independently reconstructs full Hankel ranks at dimensions two and three, and certifies the binary size-six minor. The symbolic proof, not finite extrapolation, justifies the infinite quantifier.

## Originality — PASS within examined evidence

Onishchenko, arXiv:2605.02957v1, proves a sharp \(n^3\) bound for ordinary Boolean-semiring NFAs, a different path-aggregation model. Chistikov et al., arXiv:2607.00742v1, study XOR-path automata and decision complexity, without the claimed square-root state bound in examined sections. Berstel--Reutenauer, Ch. 2, supplies the classical minimal-rank machinery, not this exact monoid rank. Searches for equivalent weighted-series formulations, dominating statements, exact tables, and the characteristic-two formula found no decisive covering result. Earlier unindexed equivalent work is an acknowledged priority risk; the XNFA article appendix and the complete book chapter were not examined.

## Value — PASS

The result determines an exact complexity function for a natural regular-language operation on a whole automaton model, with witnesses over only three letters. It explains the saving from the ordinary NFA cubic cost through explicit characteristic-two cancellation and provides a binary sharp witness in dimension two. These are structural, independently motivated state-complexity facts, not routine finite census increments.

## Limitations

The assertion does not extend to Boolean-semiring NFAs or to coefficient fields other than GF(2), and it does not determine whether two letters always suffice above dimension two. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
