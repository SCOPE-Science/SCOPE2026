# Scientific review

## Correctness — PASS
The claim is for each integer \(m\ge2\), each \(d>m\), positive \(h,\lambda\), a unit signal vector, and deterministic \(\tau>0\). The Sherman–Morrison reduction gives the exact two spectral means and the necessary regularizer for simultaneous matching. Gamma integration by parts plus strict Cauchy–Schwarz proves the signal mean falls short at that sole candidate; the exact nullspace relation proves the opposite sign. Dominated convergence proves both sharp orders without extrapolating from numerical samples. The accompanying program reconstructs actual sketches and verifies 893 finite computational tests.

## Originality — PASS with residual risk
The motivating source, Romanov–Zhang–Pilanci, arXiv:2410.01374v1, §§1–3 and Appendix I, provides the estimator and its effective-dimension correction, asymptotic bias results and Gaussian concentration; its inspected material does not state an exact finite-sample scalar-impossibility theorem or the two sharp signed coefficients. Zhang–Pilanci (PMLR 202, 2023), §§2,5 and appendix, treat related covariance-resolvent shrinkage and iterations rather than this same expectation. LeJeune et al., arXiv:2211.03751, §§4–5, prove asymptotic equivalences and include rank-deficient isotropic spectra but do not assert the finite rank-one Gaussian two-direction theorem. Targeted mathematical-record and literature searches did not identify a logically dominating result. The possibility of an equivalent result in an unlocated Wishart-resolvent proof or appendix remains real; absence of search matches is not a novelty proof.

## Value — PASS
Scalar shrinkage of inverse-Hessian sketches is used specifically to reduce systematic Newton-step bias. The result determines an intrinsic finite-sample limit of such one-parameter correction, rather than an arbitrary isolated statistic: both eigendirections cannot be corrected simultaneously, and the effective-dimension choice induces opposed eigenvalue biases with distinct and sharp decay rates. Increasing the number of independent workers removes variability but cannot remove these nonzero fixed-sketch-size mean biases. This informs whether spectral or non-scalar debiasing is required. It is not a statement that the adaptive implementation is defective or that convergence fails.

## Limits and comparisons
The result does not cover randomly selected regularization, additional scalar scaling, full-rank Hessians, non-Gaussian sketches, or entire algorithms. The source's high-dimensional guarantees remain compatible with the proved vanishing biases. Inverse-Wishart identities may offer previously published equivalent forms; the comparison remains best-knowledge, not independently verified.

Self-review: passed. Independent audit: not yet performed.
