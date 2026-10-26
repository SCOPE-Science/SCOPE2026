# Review: full-support rank-one entry histograms

## Correctness — PASS

For the rank-one nonzero-entry stratum, the \(q-1\)-fold factorization gauge gives a uniform product of independent nonzero row and column vectors. Pairwise entry independence yields the exact finite covariance. Multinomial centering cancels the linear histogram terms exactly; the multivariate multinomial CLT then gives a centered Gaussian bilinear convolution. Character orthogonality determines its full joint characteristic function, including complex-conjugate multiplicities. The standalone checker exhaustively validates finite rational moments and checks the Fourier determinant formula in small cyclic groups. Finite computations alone are not evidence for asymptotic convergence.

## Originality — PASS in examined coverage

The most relevant antecedent is Sanna (2023, arXiv:2307.14172v1), notably Lemma 5.4's general bilinear Fourier decomposition. Its stated theorem concerns unconditioned fixed-rank entries and a Gaussian law; it does not state the full-support-conditioned joint non-Gaussian limit, exact finite histogram covariance, character-product characteristic function, or the product-normal and Laplace specializations. Chan and Xiong (2024, arXiv:2409.10412v1) similarly study unconditional matrix counts. Migler, Morrison and Ogle (2006) enumerate total nonzero matrix weight, constant in this ensemble. The available mathematical research records and accessible related historical claims did not yield the same conditional law. The factorization and Fourier mechanism itself are **not** claimed new. An equivalent conditional law in unindexed prior literature remains possible; the reviewed priority conclusion is limited to inspected coverage.

## Mathematical value — PASS

Conditioning on full support of a rank-one finite-field matrix eliminates the dominant zero-mask fluctuations, revealing a natural second-order non-Gaussian universality class across all fixed finite fields and all joint diverging row/column dimensions. Pairwise independence of individual entries coexists with non-Gaussian histogram fluctuations, and the joint law and two sharply different small-field marginal types are explicit rather than merely qualitative.

## Scope and limitations

The theorem assumes rank one, fixed field size, nonzero entries, and both dimensions diverging. No general higher-rank law, quantitative convergence rate, or exhaustive historical priority is asserted. The fourth cumulant is positive for all \(q\ge3\), but the degenerate binary case must be treated separately.

Self-review: passed. Independent audit: not yet performed.
