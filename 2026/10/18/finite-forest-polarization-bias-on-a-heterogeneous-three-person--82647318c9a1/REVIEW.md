# Scientific review

## Correctness

**PASS.** The out-degree Laplacian is a rank-one perturbation of the identity and its inverse yields contribution-independent centered equilibrium opinions. Exactly sixteen directed rooted forests exist on three labeled vertices; grouping them by the number of vertices with root 3 proves the exact one-draw polarization moment. Independence across sampled forests gives the quadratic plug-in bias identity. The cross-sample estimator is unbiased because its factors come from different independent forests. The stated absolute-error tail follows from the bounded centered norm and McDiarmid's inequality. A standalone exact rational enumerator independently checks the forest law and matrix inverse for 1,230 assertions. Its finite scope is not mistaken for proof of the all-real-parameters statement.

## Originality

**PASS with publication-priority uncertainty.** The closest direct source is Xu–Zhang, arXiv:2310.05689v1: its forest sampling construction and coordinate unbiasedness are established prior art, while its squared plug-in polarization step is not accompanied by this precise three-person influence-dependent bias calculation. The later NeurIPS 2025 Sun–Sun–Zhou–Zhang paper uses a related squared plug-in estimator in an undirected-network setting and proves additive-error control. Neumann–Dong–Peng, arXiv:2404.16464v1, uses other sublinear estimation mechanisms. Mathematical record searches did not identify an equivalent statement. Generic variance decomposition, matrix-forest enumeration and cross-product U-statistics are standard: originality attaches to their exact interaction in the specified directed three-person example and the unbounded high-coupling relative distortion, not to those ingredients separately. A specialized prior analysis may remain unindexed.

## Value

**PASS.** A quantitative study of influence heterogeneity based on sampled polarization can misattribute a sampling effect to an underlying change in equilibrium polarization, even in the smallest genuine group-interaction model. The exact factor both explains the mechanism and determines its worst high-influence scaling for any fixed sampling budget, and the companion unbiased estimator provides a concrete control. This is a motivated limitation of a published social-network computation method rather than an arbitrary choice of three numerical parameters. Absolute bias still vanishes as influence grows, and the correction can have negative finite realizations.

Self-review: passed. Independent audit: not yet performed.
