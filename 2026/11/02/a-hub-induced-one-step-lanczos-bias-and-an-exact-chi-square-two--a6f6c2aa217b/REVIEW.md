# Scientific review

## Correctness

**PASS.** The star spectral projections give three explicit weights, and direct Lanczos moment computation gives the Jacobi coefficients. A shared-denominator argument yields the exact nonnegative two-step quadrature error. Binomial concentration, the central limit theorem, and a uniform sub-Gaussian moment bound prove the two asymptotic regimes and moment convergence. The bundled exact-rational verifier passed 1,410 finite check groups when executed from the complete extracted package. Finite tests support but do not replace the proof.

## Originality

**PASS, with publication-priority qualification.** Chen–Trogdon–Ubaru (2022) and Ubaru–Chen–Saad (2017) explain general stochastic Lanczos quadrature, moment matching and error analysis, but the inspected portions do not state the exact star-Laplacian Rademacher two-step identity or its shifted chi-square error limit. Chen–Trogdon–Ubaru (2021) address spectral distributions primarily with uniform-sphere probes, and Chen–Hallman (2022) address Krylov-aware deflation. The closest searchable published two-step Lanczos exponential-positivity result concerns a matrix-vector exponential and a sign-change time, not a trace of a shifted inverse nor the stochastic star limit. An earlier specialized graph/Lanczos analysis may still imply some or all of these facts; neither search failure nor a subject partition proves uniqueness.

## Value

**PASS.** Star Laplacians are canonical growing-outlier graph matrices, and inverse trace estimation is a standard application of matrix-free quadrature. The result identifies a concrete mechanism by which one Krylov node retains a nonvanishing first-moment contribution from a vanishing spectral weight, while a second node detects the outlier and changes the absolute error scale from linear to constant. Exact error signs, finite distributions and limiting noise floors form a reproducible diagnostic for short-Krylov trace estimators; this is more than a routine finite example.

## Limitations and closest literature

The theorem is only for unweighted combinatorial stars, one iid Rademacher probe, fixed positive shift and exact arithmetic. It does not prove uniformity across arbitrary graphs, or floating-point performance. General theory of Gauss quadrature already supplies sign and moment-matching principles, so those are not novelty claims. The strongest source-specific residual risk is that specialized graph spectral trace literature not accessed in the searches could contain an equivalent exact star calculation. Independent validation and publication-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
