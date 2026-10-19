# Scientific review

## Correctness — PASS

The Fourier multiplier is derived directly from the specified kernel, and every horizon-dependent condition number is bounded by the continuum spectral ratio. Density as the horizon approaches zero proves sharpness across all horizons. Exact derivative-sign and tail inequalities isolate the unique coefficient; the strict comparison of maxima in \([0,2\pi]\) and minima in \((2\pi,\infty]\) proves unique minimax optimality. The standalone checker reproduces the derivative, stationary-point, endpoint, and comparison computations; finite numerical samples are not treated as an infinite proof.

## Originality — PASS with bibliographic uncertainty

Lu–Nie–Zhang–Zhang (arXiv:2609.24143, first public September 21, 2026) already establish the additive preconditioner family, mass-selected scale, and general uniform spectral equivalence, which are excluded from the novelty claim. Their inspected full accessible manuscript does not optimize the exact worst-horizon continuum condition number over the mass coefficient. Related nonlocal \(\tau\)-preconditioner descriptions and indexed scholarly comparisons do not yield the displayed b*-formula or unique minimax characterization. Search indexing gaps and incompletely inspected older papers remain actual priority risks; nonmatching titles or absent hits alone were not used as uniqueness evidence.

## Value — PASS

The exact minimax coefficient and condition number resolve a natural robustness-design question. For the constant unit-mass kernel the mass-prescribed \(b=1/2\) gives a condition number at least \(4.01355\), whereas free robust tuning achieves \(1.70021\) or less (the stated exact scalar optimum), an improvement factor above \(2.36\). The proof also identifies the precise oscillatory-frequency lobe governing the coefficient. This is a continuum periodic benchmark, not a claim of superiority in finite-element work complexity.

## Scope and risks

The theorem does not cover finite elements, Dirichlet volume constraints, higher-dimensional kernels, different norm models, or finite-precision convergence. Partial access to secondary papers leaves nonzero novelty uncertainty. All supporting formulas are self-contained in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
