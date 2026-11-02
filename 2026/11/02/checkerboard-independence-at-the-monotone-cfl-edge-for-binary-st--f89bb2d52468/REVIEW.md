# Scientific review

## Correctness — PASS

The model is a well-defined unbiased binary rounding of the complete exact Euler step on its stated parameter intervals. A positive Perron-weighted coupling contracts the finite-state laws at all grid sizes for the monotone interval. Conditional independence yields a diagonal-noise covariance Lyapunov equation with an absolutely convergent nonnegative path expansion; strictly positive boundary noise supplies the strict inequalities. At the limiting step, two-step kernel factorization and uniqueness of the two-step invariant law prove independence of **entire** parity blocks. The exact two-site formula follows from a closed stationary moment equation and is checked separately on its larger admissible interval. The included rational Markov-chain check corroborates small instances, but infinite-parameter claims rely on these proofs.

## Originality — PASS (qualified)

The closest numerical-analysis source is Croci–Giles (arXiv:2010.16225), which studies floating-point rounding-error accumulation for heat stencils, not stationary laws of a fixed binary quantizer. The closest voter comparison is Gastner (arXiv:1502.02883), studying a periodic synchronous noisy-voter chain with an Ising mapping and correlation functions; his periodic model has no pinned fair Dirichlet reservoirs and does not state the unique checkerboard-factorized invariant law or its sharp two-cell continuation. Ben-Ari et al. (arXiv:2004.10187) develop discrete voter duality and complete-bipartite quasi-stationarity for a different absorbing process. Published mathematical records related to heat positivity, stationary correlation, binary dynamics, and rounding were searched for covering implications. No inspected statement directly supplies this theorem, but specialized synchronous-voter or quantized-heat literature not located could contain an equivalent formulation. Priority is not independently established.

## Value — PASS

The result distinguishes spatial independence of **fresh rounding draws** from long-run spatial independence of the numerical field. It finds an exact CFL parameter at which entire checkerboard blocks decouple while correlations within a block survive, proves strict spatial correlation below that point at every grid size, and shows a boundary-enabled two-cell sign reversal within its stable parameter range. These are structural diagnostics for a concrete fixed-grid stochastic finite-difference discretization, not just a recomputation of a general Markov transition table.

## Scope and residual limitations

The scheme deliberately quantizes to two fixed levels and rounds only after the full stencil is evaluated exactly. It does not model arithmetic-by-arithmetic floating-point rounding, nonlinear PDEs, arbitrary grids, or general forcing. Standard voter duality may offer alternative proofs. Only the explicitly formulated model has been classified.

Self-review: passed. Independent audit: not yet performed.
