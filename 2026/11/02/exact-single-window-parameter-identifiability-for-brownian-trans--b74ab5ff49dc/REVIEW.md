# Self-review

## Correctness: PASS

The final statement fixes an invariantly initialized Poisson-reset Brownian mobility, independent observed Brownian drivers, and strictly positive rate/scale. Its invariant symmetric-Laplace distribution gives \(\mathbb E D=2\Lambda^2/\alpha\) and \(\operatorname{Cov}(D_0,D_u)=20\Lambda^4e^{-\alpha u}/\alpha^2\). Conditional Gaussian mixing implies \(\operatorname{cum}_4(X_t^j)=12\operatorname{Var}(\int_0^tD_u\,du)\), yielding the exact claimed fourth cumulant. Direct differentiation proves strict monotonicity across the whole domain, not merely a sampled interval. Disjoint increment computations use independence of Brownian increments conditional on mobility and exact covariance integration. The stationary age calculation, Feynman–Kac PDE, two renewal kernels, Fourier–Laplace quotient, and ergodic central limit argument are explicit. The packaged independent checks passed; finite numerical comparisons are corroboration, not proof. Weak Gaussian convergence and exact population-level inversion are claimed, not finite-sample accuracy.

## Originality: PASS, qualified

The inspected Santra–Basu–Sabhapandit 2022 paper resets both mobility and position, not the mobility alone, and explicitly notes the alternative as an open question. Olsen–Löwen 2024 proves a general partial-reset Fourier–Laplace quotient; this **already contains the renewal architecture** and it is excluded from novelty. Miyaguchi–Akimoto–Yamamoto 2016 Appendix E derives a **general** fluctuating-diffusivity non-Gaussian parameter relation; this is likewise excluded from novelty. The narrower evaluated all-duration inverse map, its strict one-to-one range \((0,5)\), and the jointly evaluated volatility-increment law require the model's specific invariant fourth moment and a separate global monotonicity/identifiability argument; they are not stated or calculated in the inspected sources. Accessible earlier research findings and published similarity results were also checked for the specific map and nearby aliases. General results could subsume parts of the claim and definitive publication-priority verification is not established. The generic conditional-Gaussian and renewal identities are explicitly prior.

## Mathematical value: PASS

The same observed mean-square displacement can arise under infinitely many hidden rate/scale combinations; this theorem supplies the precise additional observable required for **unique parameter recovery at any duration**. This is an invariant-level inverse problem for a physically motivated partial-reset alternative left open in the original study. The exact dimension-free shape and disjoint-increment correlations give independent, interpretable signatures of the hidden environment. The finite-time strict boundary and the exponential lag law are natural rather than arbitrary small-parameter slices. Reproducible algebraic checks support their use. The theorem does not establish statistical robustness under noisy experimental measurement.

## Nearest prior implications and residual risks

The 2024 general partial-reset quotient gives the transform's form but does not by itself give the inverse-kurtosis strict bijection or evaluated coefficient in the squared-Brownian mobility model. The 2016 arbitrary-diffusivity parameter expresses non-Gaussianity by a covariance functional but leaves the covariance and monotonicity to be evaluated here. The 2022 no-reset harmonic oscillator gives the fresh kernel but not stationary-initialized partial-reset observables. A broader inverse-identifiability result may still provide coverage. Independent audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
