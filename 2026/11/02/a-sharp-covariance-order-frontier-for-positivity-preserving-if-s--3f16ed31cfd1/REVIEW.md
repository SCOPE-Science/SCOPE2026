# Scientific review: stationary covariance order for IF-SSPRK2

## Correctness — PASS

The source's actual three-stage map (equation (5) in arXiv:2606.15703v1) collapses for constant forcing to \(\Phi_h(X)=DXD+h(DQD+Q)/2\), where \(D=e^{hA}\). Its componentwise attracting fixed point and the continuous Lyapunov stationary matrix differ by the stated Langevin kernel. A complete strict-concavity proof establishes the necessary midpoint inequality, and a signed \(2\times2\) determinant provides necessary and sufficient Loewner-order criteria including boundary forcing cases. Both small-step and large-step formulas follow from analytic expansions. Reproducible checks are implemented in `verify.py`. No simulation is substituted for an infinite-dimensional or all-step proof.

## Originality — PASS under inspected evidence; priority risk remains

The entire accessible primary manuscript (Zhang, Lan, and Jing, 2026, arXiv:2606.15703v1, Sections 1–5 and references) contains positivity-preserving stages and finite-time error estimates but not the stationary correlation threshold. The 2023 Chen–Borzì exponential Euler/midpoint construction and Gillis–Diehl 2013 collocation construction are different methods, based on the inspected previews. Broad and exact-formulation scholarly searches, published mathematical-record searches, and available neighboring claims did not identify equivalent or stronger coverage. Inaccessible full texts and older results about matrix quadrature kernels remain a genuine priority risk; negative search results are not proofs of uniqueness. Previously known scalar trapezoidal error and Gramian identities are credited rather than claimed.

## Value — PASS

An explicit positivity-preserving method can return a stationary covariance that neither upper- nor lower-bounds the true covariance in matrix order. The exact forcing-correlation frontier and all-timestep rank-one obstruction directly inform uncertainty-bound interpretation and long-time control-covariance calculations. The result is a complete and motivated two-mode classification rather than an arbitrarily selected entrywise estimate. It does not claim general nonlinear or high-dimensional applicability.

## Closest literature and scientific limits

Primary: Zhang–Lan–Jing (2026), arXiv:2606.15703v1, eq. (5), Thms. 3.2 and 3.4. Neighboring methodologies: Chen–Borzì (2023), DOI:10.1007/s10915-023-02275-6; Gillis–Diehl (2013), DOI:10.1109/CDC.2013.6761121; Chen–Borzì (2025), DOI:10.1007/s10444-025-10228-w. Their inspected accessible content does not imply the fixed-point result for this specific stage map. The 2013 and 2023 primary full texts were not completely available. The proof and claims apply to constant \(Q\succeq0\), two stable symmetric modes, and exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
