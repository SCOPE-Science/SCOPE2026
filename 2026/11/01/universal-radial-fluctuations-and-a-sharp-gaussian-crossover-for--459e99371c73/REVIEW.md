# Scientific review

## Correctness — PASS

The precise assertion is for two-dimensional random Minkowski sums of independent line segments with uniform directions and positive, direction-independent lengths. The geometric area and perimeter identities establish the nonnegative, absolutely convergent Fourier-square deficit formula. Conditional angular orthogonality supplies exact finite-size means and variances; the two required spectral sums evaluate exactly. Finite-dimensional multivariate central-limit arguments plus the uniform nonnegative Fourier-tail bound give the universal non-Gaussian law and asymptotic independence from the normalized perimeter. The bounded radial triangular array has an *exact* area–perimeter–deficit identity; direct overlap counting verifies the limiting variance, while Slutsky's theorem establishes the complete finite-critical and Gaussian-dominant crossover. The algebraic argument holds for every specified integer sample size and all specified laws, not just the simulated cases. The standalone checker reconstructed independent geometry and checked all constants without relying on prior run outputs.

**Risk/limits:** The proof requires a finite second radial moment, and its exact finite-sample variance requires a fourth moment. The triangular-array marks are bounded with zero mean and unit variance. No nonisotropic extension is proved; a numerical simulation is not an infinite proof.

## Originality — PASS (historical priority provisional)

The expected intrinsic-volume results and a generic nondegenerate central limit theorem appear in R. Schneider, *Random zonotopes and valuations* (arXiv:2202.06774v1). That theorem applies to a different first-order normalization when the length variance is fixed and nonzero; it does not determine the perimeter-cancelled second-order law or the simultaneous vanishing radial-variance crossover. A previously available fixed-unit-length, direction-biased result, opaque identifier `474c5a5f-f684-4deb-8225-2bcddca2d7a3`, **already gives the isotropic Fourier series and Laplace transform**; these are expressly attributed rather than presented as discoveries. The newly assessed assertions are the arbitrary independent radial-mark universality, exact finite-radius variance/covariance formulas, asymptotic decoupling with the perimeter, and the critical area-law interpolation. The deterministic zonotope decompositions of Joós–Lángi, the lattice-generator model of Buffière–Marchal, and the fixed-orientation Feret-reconstruction framework of Rahmani–Pinoli–Debayle do not give this combined law in the inspected material.

**Risk/limits:** A stronger unindexed stochastic-geometry result or a different degenerate-U-statistic formulation may already imply the package. The named prior fixed-length result is an actual partial overlap, and the original claim is deliberately scoped away from it. A search without a hit is not proof of historical priority; independent literature review remains desirable.

## Mathematical value — PASS

The shape-size decomposition is natural for randomly generated zonotopes and distinguished by a genuine change of fluctuation scale. Exactly subtracting the random isoperimetric perimeter term uncovers a non-Gaussian positive spectral shape fluctuation that persists for every finite-second-moment independent radial distribution, while radial length disorder alone supplies an independent Gaussian scale fluctuation. The precise critical length-standard-deviation threshold separates the two, with an explicit continuously interpolating family of centered-area laws. Exact finite-\(n\) deficit and area variance formulas make the result useful for finite samples as well as limits, including polygonal shape-versus-size variability in stochastic geometry. Its content is more than the known one-distribution Fourier calculation or a generic central limit theorem.

**Limit:** No application beyond the specified stochastic zonogon model or higher-dimensional analogue is asserted.

## Source comparisons

R. Schneider, arXiv:2202.06774v1 (sections on expectation/valuation and central limit); A. Joós and Zs. Lángi, arXiv:2206.03204v1 (definitions, decomposition and isoperimetric statements); T. Buffière and P. Marchal, arXiv:2303.18045v1 (lattice-generator model and fluctuation theorems); S. Rahmani, J.-C. Pinoli and J. Debayle, doi:10.15559/16-VMSTA70 (random zonotope and Feret-diameter sections). Full historical priority outside the compared sources has not been established.

Self-review: passed. Independent audit: not yet performed.
