# Review of degree-sequence reconstruction for graded Gorenstein rings

## Correctness

PASS. In the stated class a nondegenerate symmetric bilinear form controls all positive-degree multiplication. Its zero-divisor graph has exactly \(q-1\) universal socle vertices, and the remaining degree split differs by one according to whether the corresponding linear form is self-orthogonal. Counting isotropic vectors over finite fields recovers the form's similarity type; the induced graded multiplication recovers the ring. The argument covers odd and even characteristics, both parity cases for the embedding dimension, and arbitrary finite extension fields. Independently executed brute-force adjacency checks across 13 small prime-field test cases agree with the complete formulas. The computations do not prove the all-field statement, which relies on the general algebraic and finite-field-form arguments in RESULT.md.

## Originality

PASS, with a meaningful prior-art caveat. Proposition 3.6 of Kadu (arXiv:2010.06924v1) already identifies the bilinear zero-product relation and Gorenstein nondegeneracy; these steps are explicitly prior, as is classical classification of finite-field forms. Kadu–Tanpure (arXiv:2609.36021v1) studies whether an Artinian ring is Gorenstein using a comparison of associate-class and annihilator-compressed zero-divisor graphs. Arunkumar et al. (arXiv:2207.11741v1) establish different universality and threshold results. The additional theorem here is reconstruction of the entire ring from the ordinary *simple graph's degree multiset* in a naturally restricted graded family, using the self-loop correction to read its finite-field Witt/symmetry type. Neither primary source inspected states this reconstruction result. Searches of related research records concerning chain rings, dot-product graphs, and other finite-ring graph invariants found no matching implication-level coverage. Because the theorem combines several known ingredients, an equivalent older synthesis remains a genuine historical risk, not resolved merely by unsuccessful searches.

## Value

PASS. Ordinary zero-divisor graphs generally fail to determine the underlying ring. This result gives a full positive reconstruction classification, for all residue-field sizes and all embedding dimensions at least two, in a canonical Gorenstein family with one-dimensional socle. The one-step degree split is a mathematically motivated invariant: excluding loops remembers self-orthogonality, so the graph sees the square class of the even-dimensional multiplication form or the alternating/nonalternating divide in characteristic two. The result is not merely a computation of a small example or a restatement of bilinear zero-product equivalence.

## Residual limitations and closest sources

No assertion is made beyond standard graded commutative Artinian local Gorenstein rings with Hilbert vector \((1,d,1)\) over a finite field. General Artinian local rings may have different coefficient-field and higher-product structure. The relevant 2020 preprint gives a stronger *premise* (the bilinear reduction) but neither the full simple-graph degree census nor the finite-field ring reconstruction; an older overlooked formulation remains possible. A related paper on adjacency matrices for selected finite rings was only accessible in excerpt and was not used to justify a novelty conclusion.

Self-review: passed. Independent audit: not yet performed.
