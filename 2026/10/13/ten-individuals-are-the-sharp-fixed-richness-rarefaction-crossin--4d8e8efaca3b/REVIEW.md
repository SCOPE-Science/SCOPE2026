# Self-review

## Correctness
**PASS.** The individual-based expectation is reconstructed directly from the hypergeometric miss probability. Every strictly positive abundance multiset through \(N=10\) is generated in two independent ways, and every unordered pair at common \((N,S)\) is compared for every interior sample size using exact fractions. No crossing occurs through \(N=9\), while \(N=10\) has exactly one unordered crossing pair, \((6,2,2)\) versus \((5,4,1)\). The package independently checks all witness values and the endpoint identities \(R_2=2-\sum_i n_i(n_i-1)/(N(N-1))\) and \(R_{N-1}=S-f_1/N\).

Risk: the theorem changes if the sampling convention or comparison domain changes; incidence rarefaction, unequal richness, unequal census size, and extrapolation are excluded.

## Originality
**PASS.** Existing ecological literature establishes that species-accumulation and rarefaction curves can cross and explains abundance-shape mechanisms behind such crossings. The closest checked sources do not state the smallest fixed-\((N,S)\) positive-integer census, do not exclude every crossing through \(N=9\), and do not classify the unique \(N=10\) first-layer pair. Exact witness searches and semantic database searches also did not locate this finite boundary.

Risk: one older closely related article was available here through bibliographic and abstract material rather than inspected article body, and an unindexed pedagogical example or software test could contain the same ten-individual pair without asserting the minimality theorem.

## Value
**PASS.** Rarefaction is specifically used to compare richness at standardized sampling effort, and prior literature warns that sampling curves can cross. Fixing both observed richness and total abundance removes the most immediate comparison confounders. The sharp first crossing identifies the smallest possible finite community in which the chosen rarefaction depth alone can reverse a biodiversity ranking, while the endpoint formulas give a transparent ecological mechanism: pairwise evenness favors one profile early, but the singleton tail favors the other near census completion.

Self-review: passed. Independent audit: not yet performed.
