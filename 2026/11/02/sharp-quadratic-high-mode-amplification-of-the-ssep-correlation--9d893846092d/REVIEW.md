# Scientific review

## Correctness — PASS

The claim is derived independently from the motivating paper's squared lag, dissipative form factor and ratio definition. The factor \(F(s)\) is strictly positive because its numerator contains a function with positive derivative, and both small- and large-frequency endpoint expansions are proved. The exact factorization separates the index dependence from a one-variable rational optimizer. Global endpoint estimates prevent escaped maximizers; the derivative polynomial is strictly monotone in squared frequency and yields the unique limiting maximizer. Uniform twice-differentiated expansions near the optimizer prove the two-term growth and optimized frequency. Symbolic identities, numeric optimizations, and their finite-only limits are recorded in `verify.py` and `verification_output.json`.

## Originality — PASS (qualified best knowledge)

The motivating 2026 SSEP study explicitly supplies \(Q_n\), the slow-mode inequality, and finite-mode overshoots including the \(n=2\) value. This finding does not claim those formulas as new. It establishes the distinct, globally frequency-optimized **large-mode** sharp envelope and its two-term asymptotic with the unique optimal frequency. The full accessible study and appendices were inspected. Bodineau–Dagallier treats time-averaged correlation large deviations, while Dechant et al. and Kolchinsky et al. concern differently defined thermodynamic speed limits; none of the inspected material states or analytically dominates this particular frequency–mode variational theorem. Searches of published mathematical findings and relevant literature did not identify a covering result. Searches cannot prove priority: hidden papers or an overlooked optimization of the known source formula remain a risk.

## Value — PASS

The motivating paper emphasizes that some higher modes violate the proposed mode-normalized dissipation comparison and plots only small modes. Showing the sharp envelope grows as \(C_*n^2\) establishes that the violation is not bounded by any universal constant and quantifies exactly how it scales with spatial resolution. The optimal frequency is not arbitrarily chosen; it is a unique asymptotic multiple of the diffusive relaxation rate. The first subleading term distinguishes finite-mode trend from the quadratic limit and gives a reproducible extrapolation. This is a structural finite-frequency spectral statement rather than a restatement of the source's isolated numeric overshoots.

## Prior comparisons and limitations

Closest source: https://arxiv.org/abs/2610.07964 , Sec. III.3 and appendices E–G. Other literature considered: https://arxiv.org/abs/2212.11561 , https://doi.org/10.1103/PhysRevLett.131.167101 and https://doi.org/10.1103/r48t-dghl . This is a theorem within the continuum weak-drive formulas, and no uniform finite-lattice high-mode limit is established. The novelty assessment is best knowledge rather than certification, and no external priority determination has occurred.

Self-review: passed. Independent audit: not yet performed.
