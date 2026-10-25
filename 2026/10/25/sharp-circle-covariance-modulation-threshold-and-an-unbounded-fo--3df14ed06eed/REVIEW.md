# Self-review

## Correctness: PASS

For the kernel on the unit circle, the exact Fourier integrals give strictly positive unmodulated coefficients and a neighboring-frequency convolution under cosine modulation. The Fourier positivity criterion then yields an exact ratio minimum. A rational derivative proves one continuous minimizer and reduces the integer search to at most four frequencies; the frequency-zero comparison is strict. The proof also treats the endpoint, strict positivity on finite distinct sets via Vandermonde invertibility, both asymptotic regimes, and the arbitrarily high unique active indices. The standalone checker reproduces selected calculations; analytic proofs, rather than finite tests, establish the universal quantifiers. No extension to higher-dimensional spheres is claimed.

## Originality: PASS with residual priority risk

Gneiting (arXiv:1111.7077, sections 3 and 4.5) gives the general Schoenberg/Fourier criterion and the unmodulated powered exponential, not the explicit signed first-harmonic cutoff. Feragen–Lauze–Hauberg (arXiv:1411.0296, Theorem 4) gives positivity of unmodulated geodesic Laplacian kernels. Porcu–Bevilacqua–Genton (DOI 10.1080/01621459.2015.1072541, Eq. (19)) uses an exponential great-circle baseline in spherical covariance modeling. Accessible historic claims and published mathematical record searches were compared by domain, family, parameters and implication; the closest records concern other geometry or different spectral constraints. No checked result supplies the four-frequency coefficient formula, its asymptotics, or the active-frequency staircase. Gneiting's 1998 circle criterion has been examined only through its abstract because full text was not obtained; this is a specific unresolved priority risk, and a search miss is not evidence of uniqueness.

## Mathematical value: PASS

The object is a natural signed first-harmonic modulation of the basic geodesic Laplace covariance model. The exact allowable negative coefficient matters in covariance admissibility and periodic interpolation, and the frequency at which validity first fails changes without bound with scale. The finite four-frequency formula, included equality boundary, and nontrivial \(\sqrt{5/3}\)-slope frequency law distinguish the result from a generic Fourier-positivity test or a single numerical example.

## Limits and scope

This statement is specific to \(\mathbb S^1\). No higher-sphere analogue, general harmonic multiplier, or complete tie locus has been established. Independent validation and independent priority review remain unperformed.

Self-review: passed. Independent audit: not yet performed.
