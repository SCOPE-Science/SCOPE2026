# Self-review

## Correctness
PASS. The shift identity reduces the five-point resolvent exactly to a quadratic polynomial in \(X=T+T^{-1}\). At and above \(r=1/3\), both factors are second-order resolvents with strictly positive geometric kernels, and preservation of constants gives a stochastic convolution kernel. Below \(1/3\), the factor parameters form a nonreal conjugate pair, forcing the decaying Green sequence to be a nonzero damped cosine; elementary rotation arguments force a negative coefficient. The bundled checker reproduces the exact factorization and a robust subthreshold sign witness.

## Originality
PASS with a stated residual risk. Classical finite-difference weight construction, general inverse positivity, pentadiagonal Toeplitz inverse formulas, and modern fourth-order maximum-principle constructions were treated as prior work. The closest full-text maximum-principle source uses a different \(Q^2\)-derived fourth-order operator and proves a lower time-step restriction for that scheme. The closest pentadiagonal Toeplitz source gives general inverse formulas but its full text was unavailable. Searches under five-point stencil, inverse-positive resolvent, pentadiagonal Toeplitz, maximum principle, backward Euler, and the \(1/3\) threshold did not locate the present if-and-only-if infinite-lattice classification.

## Value
PASS. The result isolates a natural and practically interpretable boundary for a textbook high-order spatial stencil: backward Euler does not automatically repair its lost maximum principle, but it does so exactly after a computable lower step-size threshold. The factorization explains the transition structurally and provides a reusable test for distinguishing monotone and oscillatory Green kernels.

Self-review: passed. Independent audit: not yet performed.
