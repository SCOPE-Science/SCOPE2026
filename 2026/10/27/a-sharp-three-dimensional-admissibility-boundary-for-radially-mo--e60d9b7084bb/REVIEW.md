# Independent mathematical audit

## correctness

PASS

Under the stated unnormalized forward Fourier transform on R³, the radial transform is 4π/s times the sine integral of r times the profile. Taking the imaginary part of (a−ik)⁻²+2a(a−ik)⁻³ gives 8a³k/(a²+k²)³ for the envelope's sine integral. Product-to-sum yields the stated shifted odd rational functions with prefactor 16πa³/s. Clearing the two cubic denominators gives 2s times the monic cubic in s²; independently, writing B=a²+s²+ω² and u=2sω gives the numerator 2s(B³+3Bu²)−2ω(3B²u+u³), which expands to the recorded polynomial. At s=0 its constant term is (a²+ω²)²(a²−5ω²); at s=ω the polynomial is a⁶. Above the threshold the nonconstant coefficients are positive; at equality with ω>0 the coefficient of s² is 100ω⁴, confirming an isolated quadratic zero. Below threshold the descending coefficient sequence has exactly one variation whatever the linear coefficient's sign. Descartes and the endpoint values give one simple zero in 0<s<ω, with the asserted signs. The transform is continuous and integrable (tail O(s⁻⁶)); inversion and uniqueness of the Bochner measure give both implications. Strictness on distinct sites follows by restricting the exponential sum to a line with distinct projected points, where the derivatives at zero and a Vandermonde matrix rule out an identically zero sum. Its squared modulus is therefore positive on a neighborhood that intersects the strictly positive density region, also at equality. The one-dimensional even envelope has transform 4a³/(a²+s²)² and the two half-weighted shifts are positive everywhere. This includes ω=0 under a>0. Replay in RESULT.md Steps 1–5 or by the B,u expansion above. VERIFICATION.md and check_spectrum.py were inspected, not executed; the finite quadratures are corroboration only.

## originality

PASS

The supported distinct contribution is the sharp three-dimensional classification for this specific profile and the complete radial sign obstruction, not the standard Matérn envelope or unconstrained oscillatory kernel construction. The closely related planar result is credited explicitly.

## value

PASS

The smooth Matérn envelope is a canonical useful covariance, and radial rather than coordinatewise modulation is natural when retaining isotropy. The exact threshold tells when negative spatial correlations can occur without losing Gram positivity; strictness at the threshold and the single low-frequency negative band resolve what the sharp obstruction is. The contrast with R shows that validity cannot be inferred from shifted one-dimensional spectra. This is a useful family-specific design boundary, not a claim for other dimensions or smoothness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
