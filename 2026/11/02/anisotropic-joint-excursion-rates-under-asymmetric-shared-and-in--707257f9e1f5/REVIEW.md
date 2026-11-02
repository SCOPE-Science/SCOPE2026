# Scientific review: anisotropic joint-excursion rates under asymmetric resetting

## Correctness — PASS

The stationary generator identity \((\Lambda+A k^2+B l^2)\Phi=c+a/(1+l^2)+b/(1+k^2)\) follows directly from independent Brownian diffusion and the three reset maps. The stationary marginals are standard Laplace after normalization. This gives a **positive mixture** of an exponentially aged Gaussian vector, that vector plus an independent Laplace variable on the first coordinate, or that vector plus an independent Laplace variable on the second coordinate. Positive mixture weights sum to one.

The aged Gaussian has good speed-\(t\) large-deviation rate \(\sqrt{\Lambda(u^2/A+v^2/B)}\). Contraction with Laplace costs \(|z|\) reduces the two remaining components to one-dimensional convex minimizations. Their derivatives yield the exact two non-overlapping transition rays and three-piece rate. The quadratic cost support-domain formula gives strictly nested feasible regions at fixed marginal reset rates, hence strict identifiability. Moment equations give squared-coordinate covariance \(4c/\Lambda\). The rate is \(C^1\) but not \(C^2\) at the two rays by direct differentiation. A runnable standard-library checker confirms 7,784 finite algebraic and numerical identities, including independent infimal-convolution minimization. Infinite statements rely on the written proof, not these checks.

## Originality — PASS (qualified best knowledge)

The full accessible January 2026 original arXiv article and its Supplement S3 already supply the symmetric pairwise Fourier law and density for uniformly selected resetting batches. They **cover every equal-single-rate example** and its diagonal extreme benchmark, which are not claimed here. For every such source batch, the two local-only rates are necessarily equal. The assessed result restricts to **unequal** rates and proves explicit angular rare-event sectors and strict shared-clock rate inference at fixed unequal marginals. The accessible Opitz (2015) article proves extremal asymptotics for elliptical multivariate Laplace laws, not the nonelliptical mixture with two independent one-coordinate convolution streams. The 2025 simultaneous non-Poissonian study is a related model with fully simultaneous reset events, but only bibliographic and abstract material was accessible; no full-text noncoverage conclusion is drawn from this source. General results on joint renewal shocks, Laplace convolution and multivariate gauge functions could still imply parts of the theorem; prior-art priority is qualified, not certified.

Earlier accessible mathematical findings with nonuniform batch *moments* (mixed cumulants) and stable-flight algebraic extreme tails do not imply the positive-direction **Brownian exponential** joint-excursion rate or its phase boundaries. Indexed research-result searches for common/individual Poisson resetting, shared Brownian tails and equivalent multivariate Laplace geometry found closest work on Gaussian bridge maxima, Laplace sum tails and reset coupon collectors; these have different objects and do not mathematically cover the assertion. Absence of search hits alone is not used to establish novelty.

## Value — PASS

The full three-sector rate exposes two nontrivial angular phase boundaries at which curvature changes while gradients remain continuous. It shows that an experimentally meaningful common-reset intensity changes joint extremes strictly, even when **both complete one-particle stationary distributions** are held fixed. This supplies a concrete direction-dependent probe of a hidden common shock stream rather than simply a recomputation of a scalar covariance or a symmetric source formula. The asymptotically independent pair can simultaneously have positive squared-coordinate covariance, distinguishing moment correlation from joint extremes.

## Limits and residual risks

No polynomial prefactor, nonasymptotic joint probability order, confidence interval, multitime law, interactions or non-Poisson generalization is asserted. A broad published/unpublished common-shock convolution theorem may cover a part of the exact rate, and the 2025 simultaneous-reset primary full text was not inspected. The claimed new contribution is the explicitly delimited unequal-rate theorem; the symmetric special case is covered prior art. No external independent validation or priority adjudication was performed.

Self-review: passed. Independent audit: not yet performed.
