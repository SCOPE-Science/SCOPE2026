# Scientific review: weighted-tree heat-flow variation contractivity

## Correctness — PASS

The proof establishes that the oriented tree incidence map is surjective, so the weighted edge-gradient variables span the **entire** edge \(\ell^1\) space. In those coordinates the generator is exactly \(-WBM^{-1}B^{\mathsf T}CW^{-1}\), and each absolute column sum equals \(-c_e\kappa_e/w_e\). The finite-dimensional logarithmic-norm bound and its first-order converse prove the all-time criterion and small-time necessity. Perron–Frobenius theory gives the uniform-mass classification; a degree-sum argument gives the uniform-variation classification. These are analytical arguments for every finite weighted tree, not inferences from finite test cases. The runnable finite checker passes 18,248 labeled-tree cases and 150 weighted rational-generator tests. Potential limitations: the key surjectivity fails on graphs with cycles; finite tests do not prove the general case.

## Originality — PASS with stated uncertainty

Ollivier's 2007 preprint (Journal of Functional Analysis 2009, §2.5, Proposition 29) provides the general Markov **Lipschitz** contraction/transport-curvature equivalence. It is a methodological predecessor, not an exact formula for the operator norm in the distinct edge-\(\ell^1\) **total variation** seminorm on trees with three independent weight arrays. Bauer et al. (arXiv:1306.2561, §1) analyze quadratic gradient and heat-kernel inequalities rather than sharp total-variation contraction. Kolmogorov–Pock–Rolinek (arXiv:1502.07770, abstract available) investigate nonlinear tree-TV minimization, not linear heat flow. Earlier exact variation contraction criteria or equivalent curvature reformulations could exist; one related full text was not obtained. No assertion of global priority is made.

## Mathematical value — PASS

The sharp local inequality distinguishes three physically natural positive weights: vertex heat capacities, edge conductances, and spatial variation penalties. It reduces an all-time semigroup norm statement to finitely many local algebraic tests and proves the **non-obvious independence** of the contractivity boundary from conductances. Two different permissible topology classes arise according to which weights can be selected: paths/claws for free variation weights with fixed masses, versus all stars/paths for free masses with fixed variation. This distinction is structurally informative for graph diffusion and variation stability, not a numerical table or a small parameter improvement.

## Scientific limitations and closest literature

The criterion is tree-specific, assumes strictly positive static finite weights, and controls a one-step linear heat semigroup rather than nonlinear TV-gradient flows. It does not give exact long-time peak amplification in noncontracting regimes. Ollivier's contraction framework is the closest conceptual predecessor and may contain equivalent formulations not identified here. An associated tree-TV optimization paper could only be assessed at the abstract level. Independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
