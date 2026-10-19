# Scientific assessment

## Correctness
**PASS.** The theorem's only nontrivial distributional step, \(\mathbb E[zz^{\mathsf T}/(z^{\mathsf T}z)]=K^{1/2}/\operatorname{tr}(K^{1/2})\) in dimension two, is proved by Gaussian polar coordinates and an elementary rational integral. Cayley–Hamilton yields the explicit projection moment, and the determinant, trace, derivative factorization, endpoint continuity, and sharp joint anisotropy limit are reconstructed from it. The external verifier confirms 935 independent exact-rational or numerical checks. Neither quadrature nor finite checks are used as proofs of any continuum assertion.

## Originality
**PASS, with residual priority uncertainty.** The closest covariance-aware randomized range-finding primary literature (Scotto Di Perrotolo et al., arXiv:2405.04811, Sections 3–4.4 and appendix; Boullé–Townsend, arXiv:2105.13052, Sections 2–3 and appendix) provides general bounds in oversampled settings, not the exact one-probe fixed-marginal correlation minimization or the \(\kappa\sqrt{1-\rho^2}\) crossover. The iid two-eigenvalue Nyström rank-one residual is trace-equivalent to this squared range-finder loss, so the iid specialization is already covered and expressly excluded from the originality claim. The classical iid-Gaussian and angular central Gaussian frameworks are acknowledged explicitly; the new claim does not assert invention of normalized-Gaussian calculus. Overlap searches of available related mathematical records and existing claim statements found Gaussian sketches, Nyström singular limits, and randomized matrix algorithms but no statement that implies the non-diagonal covariance correlation phase law and its sharp crossover. An equivalent special-case moment formula or angle-distribution implication in older directional-statistics literature remains possible; the Tyler article's abstract rather than full text was accessible.

## Value
**PASS.** Covariance selection is an explicit design variable in randomized low-rank approximation; the theorem completely solves the smallest nontrivial fixed-marginal covariance design problem and identifies when adding dependence reverses from helpful to harmful. Its exact double-scaling law turns an unbounded expected squared error into a bounded one without changing either sketch marginal, while exposing the \(\kappa^{-1}\) residual-correlation threshold. This is a mathematically motivated boundary, not an arbitrary instance or a claim about large matrices.

## Remaining limitations
One real sketch, two unequal positive singular values, diagonal singular coordinates, squared Frobenius loss, and exact arithmetic. Correlation-one covariance is singular. Priority uncertainty includes older projected-normal second-moment literature. No broader sketch-size or numerical implementation result is asserted.

Self-review: passed. Independent audit: not yet performed.
