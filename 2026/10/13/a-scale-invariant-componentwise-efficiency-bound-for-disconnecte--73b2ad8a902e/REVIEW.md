# Self-review

## Correctness
PASS. The proof uses the exact detailed-balance identity and the source's decompositions of social cost and rescaled potential. No cross-component pair terms remain under Assumption 2, so both optimization and social cost decompose. On each nontrivial component, player-specific coefficient ratios are \(q_i\) and pairwise ratios are \(q_iq_j/(q_i+q_j)\); nonnegativity gives the two-sided coefficient comparison. Summation yields the global bound. The optimization over component scales has matching lower and upper constructions, so the normalization optimum is exact.

## Originality
PASS. The full source text was inspected at Assumption 2, Theorems 4.4–4.5, Proposition 4.7 and Corollary 4.8. The source allows disconnected groups and states a global rescaling-vector efficiency bound, but does not state the componentwise gauge invariance or optimize that bound over independent component scales. published-finding corpus searches for the title, detailed balance, disconnected components, component rescaling, social efficiency, and equivalent formulations returned no covering result. The related 2025 general \(\alpha\)-potential framework does not supply this source-specific componentwise efficiency normalization.

## Value
PASS. The distinction is structurally relevant because the selected exact-potential policies do not change under component scaling while the source's displayed global certificate can become arbitrarily large. The componentwise result turns that non-intrinsic certificate into a finite scale-invariant one and identifies its exact optimal normalization. This is directly useful for disconnected vehicle groups, a case the source explicitly admits.

## Closest literature and limitations
The closest source is arXiv:2609.38731v1 itself: its Corollary 4.8 is the coefficient bound being normalized, while Assumption 2 supplies the disconnected-component setting. Guo, Li and Zhang (2025) provide the broader \(\alpha\)-potential framework but not this componentwise social-efficiency conclusion. Residual risk is that a general potential-game text may contain an abstract product-game decomposition; no inspected source was found that states the exact detailed-balance normalization result here. The claim does not assert sharp actual price of stability and is limited to the exact, nonnegative-cost setting.

Self-review: passed. Independent audit: not yet performed.
