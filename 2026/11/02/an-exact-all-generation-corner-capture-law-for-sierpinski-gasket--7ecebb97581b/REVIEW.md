# Scientific assessment

## Correctness

**PASS.** The result uses a precisely defined triangular subdivision graph and a three-corner block-Krylov space. Eliminating newly introduced midpoints gives an exact rational boundary Schur complement with the quadratic spectral map \(R(z)=z(z-3)\). Its two symmetry-channel rational functions have rigorously counted reduced numerator degrees, including all exceptional cancellations at \(z=-1,2\). The spectral theorem then turns those degree counts into the full boundary-generated rank without requiring distinct eigenvalues between channels. Positive local loss damps exactly the complementary modes, and corner-supported Hermitian perturbations preserve the invariant span. Two-prime finite ranks and direct rational Green-function inversions provide independent, bounded checks.

## Originality

**PASS on examined evidence, provisional.** The closest source is Darázs et al. (2014, arXiv:1405.5078), which gives the *same* three-corner trapping observable for a graph-Laplacian walk and tabulates finite dark-mode counts. The present work does not claim those counts or the known qualitative localization effect. Their full text, including equations defining the Hamiltonian and the entire gasket-results section, presents numerical eigenvalue calculations rather than an all-level formula. The new claim is an exact result for every generation, established by a separate Schur-complement recurrence, with a calculated asymptotic coefficient and absorber/corner-perturbation invariance. Novo et al. (arXiv:1412.7209) supply the general invariant-subspace approach but not the gasket-specific count in their examined full text. A residual priority risk is that older fractal spectral-decimation results may contain an equivalent hidden formula for the same boundary-visible spectral multiplicities. Search absence alone is not evidence of uniqueness.

## Mathematical value

**PASS.** This resolves the exact all-size capture fraction for a natural highly symmetric fractal transport network previously studied numerically, explains the rapid loss of accessible modes by an explicit quadratic spectral recurrence, and gives an invariant and reusable distinction between absorbing corner subspaces and interior dark modes. It is a complete infinite-family formula, not a routine extra numerical generation or a minor precision improvement.

## Scope and limitations

The statement is for a finite coherent, uniformly coupled, single-excitation model with all three outer corners absorbing at positive rates and a maximally mixed initial state. It does not give finite-time capture, dephasing robustness, or all-size two-corner rankings. Existing finite-level numerical results and general Krylov methods are explicitly credited; historical priority still requires independent checking against the broader spectral-decimation literature.

Self-review: passed. Independent audit: not yet performed.
