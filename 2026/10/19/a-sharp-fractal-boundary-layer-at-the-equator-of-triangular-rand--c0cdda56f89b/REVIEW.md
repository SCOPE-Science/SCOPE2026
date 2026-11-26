# Independent mathematical audit

## correctness

PASS

Reconstructed the claim from RESULT.md:5–47,49–85 and inspected VERIFICATION.md and checker.py. Left multiplication gives S_n=ξ_n+ρS_{n−1}; the normalized output vector is exactly (r_n,1+r_n S_n/λ), r_n=cρ^((t−1)n). The operator norm is comparable uniformly to λ^n, and the determinant gives the smaller singular-value rate log μ. A separate rational calculation reproduced 558 norm-square identities for three parameter pairs and all words through length five at t=1,2,3, without running the source script; the word (−1,1) distinguishes the two multiplication orders. The real-t argument is analytic: bounded S_n makes the error O(r_n) when t>1; at t=1 the normalized norm is F_c(S_n); for t<1 the top-scale normalization is within r_n^{-1} of H(S_n). Reversal in distribution couples S_n to the forward limit with deterministic tail bound ρ^n/(1−ρ); the Lipschitz constants c/λ and 1/λ give the stated W1 bounds. This coupling is not a samplewise convergence claim. Independent repeated block trials put every reversed finite prefix arbitrarily late on one probability-one event, and the two tails differ by at most 2ρ^k/(1−ρ); extending the current prefix gives the converse limit-set inclusion. Strong separation gives cylinder covering and mass bounds with dimension log 2/log(1/ρ). The critical map has derivative bounded below on the hull under the strict c hypothesis. The even top-scale map is bi-Lipschitz on the positive first-level piece and has at most two preimages, so dimension and nonatomicity are not lost on folding. The exact support follows from the positive masses of all cylinders and continuity of the maps. Normalized norms are uniformly bounded above and asymptotically bounded away from zero, so the exponential rates hold on every sequence. At λ=2, μ=1/2 both Cantor images have dimension 1/2; only the t=1 regime is critical in the strict sense.

## originality

PASS

The distinct result supported is the exact finite-time, moving-input norm crossover in this specific reducible Bernoulli cocycle, including normalized weak laws and full pathwise norm limit sets. The affine recursion, stationary Cantor measure, generic support machinery and its dimension are not claimed as new.

## value

PASS

This is a nonuniformity example at a natural quantitative scale, the exponential gap between the two singular-value rates. It shows that nondegenerate law convergence of normalized output can coexist with almost-sure oscillation over a specific fractal set, and distinguishes two different images of the same stationary support on and below the scale. The useful content is that combination, not a new proof of the classical Cantor dimension or an assertion about arbitrary matrix products.

The dated certificate retains the supplied scientific assessment, sources and limitations.
