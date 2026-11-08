# Scientific review: cap-conditioned spherical right-angle graphs

## Correctness

**PASS.** The result is stated for fixed graph order and two exact cap-height sequences, with separate phase-transition convergence for general sequences. The radial-tangent spherical factorization is exact. The fixed-size tangent Gram law has the determinant density whose Taylor expansion has cubic signed-triangle coefficient one; on a logarithmic central region the remainder has integrated order smaller than the claimed first correction, and the complement is exponentially small. In the fourth-root window, scaled radial cap overshoots converge with moments to independent exponentials, contributing the boundary shift \(2+\lambda^4\). In the equatorial window, scaled radial coordinates converge in moments to truncated Gaussians, contributing \(\mu_a^2\). Rectangular Gaussian integration produces the displayed labelled motif coefficients and the signed triangle term. The standalone checker corroborates these coefficients and their normalization; finite tests are not an infinite-dimensional proof. All limiting regimes and fixed-parameter restrictions are explicit.

## Originality

**PASS under best-knowledge historical comparison, with residual priority risk.** Bubeck, Ding, Eldan and Rácz (arXiv:1411.5713, 2014) work with full-sphere high-dimensional geometric graphs and signed triangle statistics, but not cap-conditioned fixed-axis point sampling or its two different boundary corrections. Bárány, Hug, Reitzner and Schneider (arXiv:1505.04672, 2015) study random convex hulls from halfspheres, not edge-pattern probabilities. Bangachev and Bresler (arXiv:2402.12589, 2024) analyze Fourier coefficients for rotation-invariant full-sphere geometric graphs; they do not provide the stated cap laws. Independent searches for hemisphere, spherical cap, Gram, edge motifs, and fixed-size graph expansions did not identify implication or exact duplication. The classical Gaussian and spherical ingredients are inputs, not novelty claims. A specialized cap-conditioned graph expansion could remain unlocated; independent historical review has not been done.

## Mathematical value

**PASS.** A high-dimensional spherical cap is the natural conditioned model for geometrically clustered orientations. The precise fourth-root transition quantifies when its right-angle graph changes from an unbiased independent-edge model to a nearly complete graph. More than a basic law-of-large-numbers limit, the full labelled pattern expansion separates a shared cap bias from irreducible three-way geometric dependence and locates a distinct equatorial boundary layer. This informs the interpretation of signed-triangle statistics in non-rotation-invariant geometric sampling.

## Verification and limitations

The executable checker directly samples spherical radial coordinates using the beta survival function, independently samples the tangent Gram matrix, and compares four triangle-pattern orbit types in two dimensions and four cap regimes. It checks correction normalization for every labelled pattern on three and four vertices. The analytic theorem is asymptotic for fixed graph order; it does not give a uniform error for all cap heights or growing graphs. No independent proof review or external mathematical certification is asserted.

Self-review: passed. Independent audit: not yet performed.
