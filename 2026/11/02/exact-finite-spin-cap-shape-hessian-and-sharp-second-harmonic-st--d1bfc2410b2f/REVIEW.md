# Scientific review: exact finite-spin cap-shape Hessian

**Correctness — PASS.** The exact binomial upper-tail formula for cap eigenvalues yields a strictly simple principal eigenvalue for every integer \(N\ge2\) and \(0<p<1\). Differentiating the exact finite matrix, using simple-eigenvalue perturbation theory, and comparing consecutive binomial probability ratios establishes the whole Fourier Hessian, its strict ordering, and the second-harmonic sharpness. The Gaussian limit follows from binomial-to-Poisson convergence and dominated convergence. A separate numerical matrix-integration checker passed 163 assertions. Its finite calculations supplement rather than replace the proof; no uniform nonlinear large-degree assertion is made.

**Originality — PASS, with residual priority risk.** Frank (arXiv:2210.14798v1) determines coherent-state concentration optimizers but not their angular shape Hessian. García-Ferrero and Ortega-Cerdà (arXiv:2408.07424v1) prove polynomial concentration stability with nonsharp geometry controls, rather than the exact Fourier coefficients in this theorem. Related Gaussian STFT stability does not imply finite-spin binomial-tail coefficients. The Gaussian disk Hessian has Poisson rather than binomial coefficients, and its limiting statement does not determine fixed finite-degree curvature. A broader implicit perturbative calculation may exist in specialist literature and remains the historical-priority risk.

**Value — PASS.** The new curvature spectrum resolves which angular deformations most weakly disrupt optimal finite-spin concentration and gives a dimension- and cap-size-dependent sharp constant, including the exact translation nullspace. The finite-spin family is not reducible to a statement about the high-spin limit; it provides exact stability information for every integer dimension and every cap size.

**Limitations.** Only local, smooth, exactly area-preserving boundary perturbations are covered. Numerical checking is not a proof for all degrees. Independent mathematical review is not claimed.

Self-review: passed. Independent audit: not yet performed.
