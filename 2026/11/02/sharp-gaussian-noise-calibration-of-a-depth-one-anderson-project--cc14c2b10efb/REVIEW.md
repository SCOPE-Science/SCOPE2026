# Scientific review: sharp Gaussian noise calibration of a depth-one Anderson projection

## Correctness — PASS

The statement concerns one regularized **projection** from two distinct scalar evaluations. The proof computes the independent Gaussian difference and midpoint exactly, expresses the projected error as a rational function, and derives the exact risk and derivative. Positivity of the derivative's expectation establishes a unique global risk minimum at \(\lambda=2\sigma^2\). Normal density positivity at the denominator's zero gives the moment threshold, while conditional density integration yields the tail constant. The companion verifier reproduces exact pointwise algebra and checks numerical consequences. No finite experiment is used to establish the general theorem.

## Originality — PASS, qualified

The Anderson projection and ridge penalty predate this work; their introduction is not claimed. Wei, Bao and Liu (arXiv:2110.01543v1, equations (4a), (5), (10)–(13)) provide the closest exact algorithm. Pollock–Rebholz (arXiv:2211.12953) address conditioning safeguards, and Lupo Pasini–Laiu (arXiv:2206.03915) treat inaccurate evaluations. Their accessible materials do not identify this simultaneous exact finite-noise tuning identity and model-specific sharp error tail. Independently, ratio-of-Gaussian variables are well known to produce reciprocal tails, so this underlying probability fact is credited and not claimed as new. Searches of available published mathematical research records, the relevant primary paper, and accessible historical descriptions found no claim with the same optimizer. The filtering and approximate-evaluation primary full texts were not completely available; they remain specific priority risks. Independent priority verification is outstanding.

## Value — PASS

Regularization of Anderson least squares is a natural numerical stability decision, but convergence and conditioning safeguards need not indicate a risk-minimizing scale. The theorem gives a **parameter-free relative calibration** \(\lambda=2\sigma^2\) on a precisely defined noisy local benchmark, independent of unknown affine slope or probe distance. It additionally shows that suppressing the penalty creates infinite first and second error moments even under arbitrarily small Gaussian noise, and quantifies that rare-event instability by an exact tail coefficient. This isolates a substantive noise-versus-regularization tradeoff not answered by generic deterministic contraction or conditioning bounds. The result is a local diagnostic, not a globally optimal solver or a claim that root-centered probes can be selected in practice.

## Closest literature and residual limits

Wei, Bao and Liu (2021) introduce and regularize the Anderson mixing projection; their stochastic convergence statements operate on different objectives. Pollock and Rebholz (2022) analyze filtering and condition numbers; Lupo Pasini and Laiu (2022) analyze inaccurate evaluations and convergence-preserving error tolerances. No inspected material states the exact Gaussian risk minimizer or this two-point tail coefficient. An independently unnoticed equivalent in general noisy-secant/ridge-risk literature is a remaining risk. The closed-form optimum applies only to independent equal-variance Gaussian noise, a root-balanced affine scalar pair, and the projection stage. Its assumptions do not support assertions about complete multi-step Anderson mixing, nonlinear maps, unbalanced probes, or finite precision.

Self-review: passed. Independent audit: not yet performed.
