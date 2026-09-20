# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked as a self-contained endpoint argument rather than as an extrapolation of the supercritical annular proof.

The key identity is obtained by squaring the extension operator and applying Plancherel in the coordinate in which the monomial graph is linear. The endpoint radial weight is dominated by a one-dimensional weight. Its Laplace representation is a positive mixture of exponentials, whose Fourier transforms are positive Poisson-type kernels. At beta=(k-1)/k the resulting kernel has small-frequency singularity |xi|^{-1/k} and large-frequency decay |xi|^{-2}.

The central Schur estimate was checked in both geometric regimes. When s <= R^{-1/k}, scaling reduces the row integral to a uniformly integrable power singularity; the worst collision is the quadratic stationary point and has exponent 2/k<1. When s >= R^{-1/k}, the two-point monomial phase is comparable to s^{k-2}|x^2-y^2|. Scaling at h=(R s^{k-2})^{-1/2} reduces the row bound to an auxiliary integral J(A), and the kernel's two asymptotic regimes give J(A) <= C_k/(1+A). The resulting denominator is s^{k-2}x + R^{-1/2}s^{(k-2)/2}, exactly comparable to the normal gap plus Vergara's terminal cutoff. Symmetric Schur then gives the source energy after the change of variables s=t+v and the source's normal-parameter comparison.

Checks of edge cases found no hidden failure at the flat point, at the symmetric stationary point, for noninteger real k >= 3, or for s>1. The singularities are locally integrable because k>2. Translation of the spatial center is a unimodular modulation and leaves the energy unchanged. For general L2 data, bounded phase-preserving truncation and Fatou/monotone convergence justify the density step. No empirical computation is used as a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** Vergara's arXiv:2609.20643v1 was read in the relevant primary-source sections. The introduction states that the monomial weighted estimate holds for iota>(k-1)/k, fails below, and that the endpoint remains open; Section 4.4 repeats this after Corollary 4.8. The source's proof at supercritical exponents uses annular summation and explicitly converges only for iota>(k-1)/k.

Repository overlap searches used the source identifier, monomial/power-curve terminology, weighted Fourier extension, endpoint language, and normal-direction-energy formulations. No existing SCOPE record covering this endpoint was found. External searches used the same exact and synonymous formulations and did not locate an equivalent theorem or a stronger result that visibly implies it.

Relevant primary theorem statements were checked in Bulj--Inami--Shiraki (arXiv:2602.03167), Schippa (arXiv:2408.07248), and Bennett--Gutiérrez--Nakamura--Oliveira (Forum Math. Sigma 2025). Those works concern reverse square functions, adapted decompositions, Strichartz/local-smoothing applications, or a different phase-space weighted-extension framework, and do not state the endpoint normal-direction-energy inequality proved here. Bulj--Shiraki's strip estimates concern nonvanishing-curvature strip concentration and do not provide the monomial endpoint statement.

No inaccessible paper was identified as especially likely to contain this exact endpoint. The principal residual originality risk is temporal: the direct source is very recent, so an unindexed contemporaneous follow-up may exist. Some related papers were inspected at theorem or abstract level rather than exhaustively line by line. The originality assessment is therefore deliberately phrased as to the best of our knowledge.

## Value

**PASS.** The result closes an endpoint explicitly left open in a recent direct theorem and converts the monomial threshold from a strict supercritical sufficiency/subcritical failure dichotomy into the exact closed threshold iota >= (k-1)/k. The proof also identifies why the logarithmic failure of annular summation is artificial in the monomial model: retaining oscillation in the linear coordinate produces a positive endpoint Fourier kernel whose Schur scale is exactly the terminal angular cutoff. This mechanism may be useful when testing which more general finite-type curves admit endpoint estimates.

## Limitations

- Only the monomial model is settled; the general fixed finite-type endpoint remains open.
- The argument uses a global graph coordinate and exact power-law two-point geometry; no invariant generalization is established.
- Constants are not optimized.
- No weak/Lorentz endpoint refinement, stability result, or extremizer theorem is claimed.
- A contemporaneous unindexed overlap remains possible because the source problem is very recent.
- Independent audit has not been performed, and no independent validation is claimed.
