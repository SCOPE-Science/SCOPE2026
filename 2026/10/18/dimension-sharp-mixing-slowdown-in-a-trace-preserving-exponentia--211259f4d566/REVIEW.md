# Scientific review: Dimension-sharp mixing slowdown in a trace-preserving exponential Lindblad step

## Correctness

**PASS.** The primary integrator has the exact reduced map \(q\mathcal I+(1-q)\mathcal J\). Orthogonal Fourier and coherence decomposition gives the complete induced Hilbert--Schmidt contractions, including off-diagonal eigenmodes that cannot be omitted when assessing the full density-matrix problem. A strict scalar derivative inequality settles every dimension \(n\ge4\), while exact factorizations settle the two- and three-dimensional equality windows. The large-step spectral and trace-norm conclusions follow by limits of finite-dimensional operators. The standalone checker reproduced 341 symbolic and numerical assertions; this is supporting verification, not a proof by enumeration.

## Originality

**PASS, subject to publication-priority uncertainty.** Chen et al.'s original FREE integrator and its positivity, trace and error results are not new here. The compared Cao--Lu Kraus construction and classical directed-graph mixing literature provide important context, but no material inspected yielded the full specified dimension-sharp comparison or its trace limit. The nearest related published mathematical findings concern Padé positivity on Markov chains, not the Lindblad FREE map. Equivalence through other formulations or inaccessible random-walk literature remains a risk.

## Value

**PASS.** It is mathematically and computationally significant that a positivity- and trace-preserving numerical channel can have exponentially poor relaxation relative to a primitive Lindblad semigroup even while sharing the unique stationary density. The full-matrix equality thresholds in dimensions two and three isolate exactly when coherence modes hide population slowdown; this is a structural rather than merely a single-parameter numeric example.

## Limits

Only common jump rates, zero Hamiltonian, a directed cyclic family, an exact full-rank step, and induced Hilbert--Schmidt norms are covered. The method remains first-order convergent for a shrinking timestep at fixed final time. The displayed trace-norm limit does not imply the same error at any fixed finite step. Full-text publication-priority verification beyond inspected papers remains open.

Self-review: passed. Independent audit: not yet performed.
