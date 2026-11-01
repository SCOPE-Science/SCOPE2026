# Scientific review: rank-two Gaussian localization shape Hessian

## Correctness — PASS

The domain has exactly fixed area because the squared radial cutoff is affine in the mean-zero deformation. The Fock Toeplitz operator is trace-class analytic in the deformation parameter near positive squared radius. Its disk eigenvalue cluster \(\{\lambda_0,\lambda_1\}\) is separated from the rest by \(e^{-t}t^2/2\). Differentiating the exact matrix elements and applying the cluster eigenvalue-sum formula yields the displayed coefficient. The \(k=1\) contribution cancels, while a strictly decreasing consecutive Poisson-weight ratio proves the exact higher-mode ordering and sharp \(k=2\) constant. The independently computed finite-section checker passed 24 assertions; no infinite claim rests on numerics.

## Originality — PASS (best-knowledge, not independent priority certification)

The 2017 accumulated-spectrogram results supply the partial eigenvalue-sum motivation and Gaussian-disk spectral formulas, not a second variation of the rank-two sum. The 2023 quantitative Gaussian Faber–Krahn theorem concerns the largest eigenvalue alone. The 2025 Fock partial-sum isoperimetric theorem assumes circular symmetry and expressly leaves nonradial optimality open. The 2026 existence theorem provides no local Fourier Hessian. Searches for equivalent Ky-Fan, accumulated-spectrogram, nonradial shape-derivative and Toeplitz formulations did not locate this statement. A rank-one coherent-state Hessian concerns a distinct spectral functional; it is not a rank-two implication. The continuing risk is unindexed or otherwise unlocated shape-calculus literature.

## Value — PASS

The spectral sum measures how well an *orthonormal pair* of Gaussian time-frequency signals can be jointly localized. Its nonradial optimality had only radial evidence in the closest 2025 theorem and remained open globally. Exact positivity of each transverse angular Fourier mode establishes a motivated, full local second-order result, exhibits the translation symmetry kernel, and identifies the sharp, least-penalized quadrupole perturbation. This is not a routine evaluation of individual radial eigenvalues or a bare numerical constant.

## Limits

The claim is local to each fixed smooth perturbation and to the first two eigenvalues. It does not prove global optimality for nonradial measurable sets. Residual historical-priority uncertainty and lack of independent validation persist.

Self-review: passed. Independent audit: not yet performed.
