# Scientific review: sixth-power golden-ratio Beatty conductor

## Correctness — PASS

The statement uses exactly eighteen **positive-index** Beatty values and ordinary sumset multiplicity. Pongsriiam's proved Theorem 4.3 gives every integer from \(93042\) onward. For a supposed expression of \(93041\), the floor-of-sum inequality restricts the total indices to \(5185\) or \(5186\). The Pell identity \(2889^2-5\cdot1292^2=1\) yields an exact ceiling formula valid for every relevant positive index. Its residue sum is respectively \(17\) (too small for eighteen positive residues) or \(18\cdot323-1\), which forces an index total at least \(5509\), contradicting \(5186\). The proof is exhaustive in the quantifiers. Exact integer checks and a separate bounded sumset enumeration corroborate the argument without standing in for an infinite proof.

## Originality — PASS relative to inspected literature

The closest source is Pongsriiam (2022), Theorem 4.3, Corollary 1 and Conjecture 1. It already gives the upper threshold, but states sharpness only for \(m\le5\), leaving the \(m=6\) exclusion open. Shallit (arXiv:2006.04177) treats lower/upper Wythoff generators; Schaeffer–Shallit–Zorcic (arXiv:2402.08331), Theorem 12, proves computability of a basis order without evaluating this conductor. OEIS A004921 contains the summand sequence but no eighteen-fold sharp bound. Phunphayap–Pongsriiam–Shallit (2022) deals with related two- and three-summand problems; a freely accessible complete text was not confirmed, so this remains a limited access risk, not affirmative evidence of noncoverage. Targeted scientific-result searches and comparisons against available earlier claims found no equivalent. Search exhaustiveness or independence is not claimed.

## Value — PASS

The statement resolves a specifically formulated published exact-Frobenius conjecture in its first unverified even exponent. The exact conductor is a natural finite invariant of an already-studied additive basis; the mechanism supplies a new algebraic certificate for a global sharp boundary, not a small arbitrary numerical slice or a recomputation of an existing table. The resulting precision concerns the natural \(18\)-summand count for \(\varphi^6\). No all-exponent resolution is asserted.

## Literature, dependencies and residual risks

The conclusion depends on the published infinite coverage theorem; it adds only the missing sharpness side. The available papers were read at the mathematically relevant statements and proofs, while the related Phunphayap–Pongsriiam–Shallit publication was compared from its available abstract. An unindexed equivalent proof or dataset is possible. This self-review does not establish independent expert validation.

Self-review: passed. Independent audit: not yet performed.
