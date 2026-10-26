# Scientific review of the logarithmic-distance first-passage field

## Correctness — PASS

The normalized Mittag–Leffler law is explicitly specified by its Laplace transform, eliminating the common ambiguity between the Mittag–Leffler waiting-time law and related densities. The starting survival integral (Levit–Reuveni, supplementary S49–S51) gives a standard-logistic limit for \(\alpha\log\lambda\) by dominated convergence. Brownian scaling makes the physical first-passage clock logarithmically equivalent to \(\exp(2b/\alpha)\). Finite-prefix convergence, the absence of ties at a continuous logistic threshold, and exponential separation within the first successful refresh block establish the *joint* convergence; the proof does not infer an infinite limit from finite enumeration. Sharp outer-distance regimes follow by monotonicity.

The joint threshold process is an iid-uniform first-exceedance process, so its geometric marginals, independent increments, Poisson-jump representation, and covariance follow from exact conditioning and generating functions. The stated normalizations, first index convention \(j=0\), factor-two Brownian variance, boundary cases, and quantifiers were checked independently of the finite verifier. The accompanying deterministic and sampled tests passed all 154 assertions. This does not constitute external validation.

## Originality — PASS, with remaining historical priority risk

Levit–Reuveni's arXiv:2609.26925v1 analyzes a discrete lattice walk. In its main equation 6 it studies mean first passage at fixed \(\alpha\) and large distance; supplementary S49–S53 proves the \(\alpha\downarrow0\) zero/infinity rate dichotomy for *fixed* positive rates and its fixed-distance mean. Those conclusions do not imply the nontrivial simultaneous \(\alpha\downarrow0\), \(\alpha\log x\to b\) Brownian multi-target limit, the explicit full two-target law, or independent increments of the spatial hitting-time field. The distributional limit uses their integral rather than claiming it as an invention.

The general fluctuating-diffusivity first-passage theory of Uchida–Washizu–Miyoshi (arXiv:2502.20705), the doubly stochastic walk model of Arutkin–Reuveni (arXiv:2302.07041), and the OU-squared diffusing-diffusivity calculation of Sposini–Chechkin–Metzler (arXiv:1809.09186) supply related frameworks but no matching singular joint spatial theorem in the inspected sections. The elementary geometric-compound-Poisson identity is classical; novelty is asserted only for its probabilistic appearance as this exact multi-target limit and accompanying scale trichotomy. Keyword and implication searches did not expose prior stronger coverage. Potential equivalent record-theoretic constructions and less accessible older limit theorems remain priority risks, so originality has not been independently certified.

## Mathematical value — PASS

The model's two known, apparently incompatible descriptions — a fixed-index, ultra-broad-rate zero/infinity limit and a large-distance mean scaling like a power \(x^{2\alpha}\) — lead to the natural critical distance scale \(x=\exp(b/\alpha)\). The theorem resolves the **complete finite-dimensional spatial crossover**, including correlations across distances, an exact independent-increment description, an additive Poisson construction and sharp collapse/divergence outside that scale. These structural conclusions distinguish it from routine computation of a single fixed-parameter marginal and provide a reusable distributional benchmark for numerical simulation of fluctuating diffusivity.

## Closest sources and limitations

Primary source: Levit–Reuveni, arXiv:2609.26925v1, first publicly available 2026-09-22, particularly main equation 6 and supplementary S49–S53. Supporting time-change theory: Uchida–Washizu–Miyoshi, arXiv:2502.20705; Arutkin–Reuveni, arXiv:2302.07041; Sposini–Chechkin–Metzler, arXiv:1809.09186. A source model using a lattice walker need not share the exact finite-parameter law of the Brownian analogue used here. The proof gives only fixed finite-dimensional convergence, with no claim of convergence of prelimit first-passage expectations, path topology, rates of weak convergence, universality for alternate rate laws, or higher-dimensional absorbing targets. Full historical uniqueness cannot be guaranteed from inspected literature and database records.

Self-review: passed. Independent audit: not yet performed.
