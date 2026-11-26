# Independent mathematical audit

## correctness

PASS

Flipping either marked spin gives −2 C_n plus γ times its two neighboring separations; at n=1 the coincident product is 1, so the Dirichlet bulk operator has forcing γ at site 1. With product-symmetric initial law, the derivative is the semigroup applied to that forcing. The sine kernel gives γ exp(−2t)(I_{n−1}−I_{n+1})=n exp(−2t) I_n(2γt)/t>0. The bulk bounded semigroup contracts at least as e^{−2(1−γ)t}, so the limiting recurrence yields q^n. This supplies an invertible map of the exponential age, with no atoms, not a continuous law for an instantaneous ±1 spin product. The short-time series gives C_n(t)∼γ^n t^n/n!, hence the lower-edge density including the finite n=1 endpoint. Write D=n/√(4πγ); at fixed n, C'_n∼D e^{−λt} t^(−3/2) and its tail δ is ∼C'_n/λ by integrating against the exponential. Thus f∼a(λ/D)^a δ^(a−1)t^(3a/2), with t∼log(1/δ)/λ; the leading constant is a(D√λ)^(−a), and the density still diverges at a=1. Taking the mean and Laplace transforming the bulk equation gives the bounded geometric root with 2 replaced by 2+ρ and boundary value one. Independent replay: python3 /workspace/branches/independent_checks.py 2 (SciPy) uses the sine integral for both the derivative and the rescaled tail, not the frozen computation. The limiting density-ratio check was within 0.00056 of one at the largest sampled time for three (n,γ) and three ρ/λ values (including equality). This quadrature is bounded and not interval-certified; the analytical asymptotic is the proof.

## originality

PASS

The classical correlation evolution and the resetting pushforward principle are prior ingredients. The supported distinct result is the unbiased-product fixed-separation law with its sharp t^(−3/2) edge conversion, in particular the critical log^(3/2) divergence and exact coefficient. The closest Resultary hit also has a doubled threshold but uses all-plus preparation, and it gives a different support and a different critical logarithmic exponent. No priority inference is made from directory dates.

## value

PASS

The distribution of an age-conditioned two-point expectation is a specifically motivated next observable beyond magnetization. Its mean cannot detect either edge. The infinite-chain, fixed-distance relaxation has a power prefactor that changes the edge law qualitatively at the critical reset rate; knowing just the relaxation exponent would miss the divergence there. The preparation-dependent comparison with all-plus also shows why the exact log power matters. This is a local distributional singularity, not a thermodynamic phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
