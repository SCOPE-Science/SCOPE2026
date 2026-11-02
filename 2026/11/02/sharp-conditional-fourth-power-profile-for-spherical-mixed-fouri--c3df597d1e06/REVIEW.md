# Self-review

## Correctness: PASS

For unnormalized surface measure on the unit two-sphere, the angular Fourier–Bessel identity gives an exact nonnegative quadratic form in the squared masses of all spherical-harmonic projections. Legendre orthogonality, Fourier inversion at the endpoints of a supported self-convolution, and Plancherel give the all-order constant-to-degree moment \(M_{0k}=1/[\pi(2k+1)]\). The degree-one self-moment is computed exactly as \(M_{11}=7/(15\pi)\). Xu's Theorem 1.2 (arXiv:2610.19648) supplies the necessary strict all-degree diagonal order. Cauchy–Schwarz then bounds all positive-degree cross moments, with strictness for any degree at least two. The resulting mass-polynomial has equality exactly in degrees zero and one, and every fixed mass is realized. CHECK.py verifies the polynomial-convolution identities and 4,424 rational assertions, not the infinitely many strict modal inequalities. Normalization, the zero input, endpoints, complex values and the dependence on Xu's theorem are explicit.

## Originality: PASS relative to inspected evidence

Xu, arXiv:2610.19648, first posted 2026-10-14, proves the sharp linear deficit for the squared mixed norm and strictly ordered diagonal modal moments. Its full HTML text, especially Theorems 1.2–1.3 and the Section 4 proof, was compared with the conditional fourth-power claim: it does not give the exact constant-to-arbitrary-mode mixed Bessel moment or the fixed-mass optimal quartic. The earlier full preprint arXiv:1710.10365 proves unrestricted constant-mode extremality and works with the same norm, but not the conditional profile. DLMF §10.59 supplies classical spherical-Bessel identities rather than the extremal inequality. Searches of published mathematical research records for conditional spherical Fourier extension fourth moments, first-mode cross moments, sharp stability, and algebraically equivalent profiles returned no equivalent result; the closest result on degree-two spherical harmonics concerns a different, ordinary sphere \(L^4\) norm. A published or unindexed equivalent conditional inequality remains a residual risk, and a negative semantic search does not prove originality.

## Value: PASS

The question of how the best radial–angular extension constant deteriorates when a specified fraction of input energy lies outside the constant spherical harmonic is a natural quantitative refinement of the newly sharp unrestricted extension and stability theorems. The exact nonlinear profile, all fixed-mass equality cases, and all-order cross-moment identity supply information not implied by the linear squared-norm deficit. In particular the positive first-harmonic energy is allowed in every equality case, giving a complete nontrivial family rather than an arbitrary finite cutoff.

## Limits and closest prior literature

The sharp all-degree diagonal order is a cited input from Xu (2026); it is not independently established here. The theorem is specific to dimension three, exponent four, and the radial–angular mixed norm. Independent external assessment and unindexed literature checks remain open. No claim is made for the ordinary full-space \(L^4\) norm.

Self-review: passed. Independent audit: not yet performed.
