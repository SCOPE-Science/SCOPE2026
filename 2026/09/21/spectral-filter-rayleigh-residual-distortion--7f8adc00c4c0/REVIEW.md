# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

PASS. In an orthonormal eigenbasis of a normal matrix, the squared Rayleigh residual is exactly the variance of the eigenvalue-valued random variable under spectral weights \(|c_i|^2\). A spectral filter followed by normalization changes those weights by the likelihood factor \(|\phi(\lambda_i)|^2\). Comparing the weighted variance-minimization formula pointwise between the minimum and maximum gains gives the stated \(m/s\) and \(M/s\) bounds. A two-eigenvalue construction gives the exact ratio \(mM/((1-p)m^2+pM^2)\), proving the global \(M/m\) and \(m/M\) constants sharp. The zero-gain construction is valid because an input can approach a killed eigendirection while the normalized filtered image remains a fixed non-eigenvector in two retained eigendirections. The universal nonexpansiveness classification follows by exhausting the nonzero-unequal, constant-modulus, single-eigenspace-support, and zero-plus-two-retained cases.

The separation tradeoff is an immediate sharp consequence of the exact distortion law: if \(\alpha\) is the smallest wanted gain and \(\beta\) the largest unwanted gain, then \(M\ge\alpha\), \(m\le\beta\), hence \(M/m\ge\alpha/\beta=1/\eta\). Two-level gain magnitudes attain equality. The generalized Hermitian definite extension follows by viewing \(B^{-1}A\) as self-adjoint in the \(B\)-inner product.

Deterministic numerical checks found no violations in 5,000 random complex normal spectral instances and reproduced the exact two-point, power-iteration, and exact-zero formulas to floating-point precision.

## Originality

PASS, to the best of our knowledge, with residual historical-equivalence risk.

The closest filtered-subspace theory explicitly measures filter quality through the ratio of unwanted to wanted spectral gains. In Gopalakrishnan--Grubišić--Ovall, the rational filter maps eigenvalues componentwise and their condition (6)--(7) requires the wanted gains to dominate unwanted gains through a supremum/infimum ratio below one. Their theorems concern filtered-subspace convergence, eigenspace discretization error, and eigenvalue error; the exact one-vector Rayleigh-residual distortion law was not located there.

Polynomial-filtered Lanczos, Chebyshev--Davidson, and least-squares rational filtering papers were checked for the same or equivalent residual statement. They analyze filter design, component amplification, convergence, and eigenspace extraction. No theorem matching the exact \(M/m\) worst-case Rayleigh-residual factor, the zero-gain dichotomy, or the reciprocal \(1/\eta\) minimax tradeoff was located.

Two recent sources were checked because their terminology is especially close. Di Napoli--Wu (2026) analyzes the condition number of the *array of filtered vectors* to select stable QR variants in Chebyshev subspace iteration; this is a different conditioning quantity. Kodali--Ramakrishnan--Motamarri (2025/2026) reformulates Chebyshev filtered subspace iteration in terms of residuals to tolerate inexact matrix-vector products; its analysis addresses approximation-error propagation and convergence rather than the exact pure-filter Rayleigh-residual gain law.

Ipsen (1997) is a particularly important near-neighbor: for normal matrices, fixed-shift inverse iteration has strictly monotonically decreasing residual norms. The residual in that theorem is the fixed-shift quantity \((A-\hat\lambda I)x_k\). The inverse-iteration corollary in this record instead recomputes the Rayleigh quotient and studies \((A-\rho(x_k)I)x_k\), so the two statements are compatible and scientifically distinct.

Searches also covered power iteration residual convergence, Rayleigh-residual bounds, spectral transformations, polynomial/rational filters, restarted filtering, and synonymous component-amplification language. No exact equivalent was found. Nevertheless, the proof is an elementary variance comparison after spectral decomposition, and old simultaneous-iteration, spectral-transformation, probability variance-comparison, and textbook literature is too broad to claim exhaustive theorem-level coverage. This is the principal residual originality risk.

## Value

PASS. The result isolates a sharp diagnostic limitation that is not captured by standard eigenspace-convergence factors. The same gain contrast that makes a spectral filter selective is exactly the quantity controlling its worst possible raw Rayleigh-residual spike. The minimax identity shows quantitatively that demanding a separation factor \(\eta\) costs at least \(1/\eta\) in worst-case one-step residual amplification before extraction. The exact-zero dichotomy also identifies a discontinuous limiting phenomenon: a true rank-one spectral projector solves the eigenvector residual exactly, while arbitrarily small but nonzero unwanted gain can admit arbitrarily large relative spikes as the gain ratio diverges.

The power-method corollary makes the effect concrete: for invertible normal matrices, the exact worst-case one-step factor is \(\kappa_2(A)\), and for a two-eigenvalue SPD system the precise state threshold between residual increase and decrease is explicit. The result therefore clarifies why a residual used as a stopping diagnostic need not improve monotonically during a pure filtering stage even when spectral separation improves monotonically.

## Scientific limitations

- Main theorem: exact arithmetic, finite-dimensional normal matrices, exact application of the spectral filter, Euclidean Rayleigh residual.
- Nonnormal matrices, finite-precision filter evaluation, inexact shifted solves, and rounding are not covered.
- Full filtered eigensolvers add orthogonalization and Rayleigh--Ritz extraction; their output residuals are not claimed to obey the one-step pure-filter law.
- Unbounded statements concern relative amplification as the input residual tends to zero, not absolute blow-up.
- The minimax statement does not impose polynomial degree, rational pole, sparsity, or evaluation-cost restrictions.
- Older spectral-transformation and simultaneous-iteration literature remains a plausible source of an unlocated equivalent formulation.
