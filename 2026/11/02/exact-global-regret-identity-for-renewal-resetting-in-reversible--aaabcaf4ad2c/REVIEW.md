# Scientific review: global renewal-resetting regret for reversible diffusion

## Correctness — PASS

The claim's domain is a finite, one-dimensional reflected-absorbed reversible diffusion under arbitrary positive iid restart intervals of finite mean. At each fixed original launch location the renewal mean is exactly the mean duration of a single attempt divided by its success probability. The duration solves the mixed-boundary Poisson equation with the success probability as source, so it is the symmetric reversible Green transform. Pairwise symmetrization gives the stated exact nonnegative square. The strict positivity of the Green kernel and the unit hitting probability at the absorbing endpoint establish the exact equality criterion. The bound by squared log-ratio follows from elementary hyperbolic-cosine convexity. The inward constant-force half-line specialization follows from explicit killed Green and hitting transforms, with infinite-risk competitors handled separately. The standalone checker passed 479 exact algebraic and numerical assertions; finite checks are corroboration rather than a proof.

## Originality — PASS, qualified

The closest primary source, Evans and Ray, arXiv:2410.01941v1 (2024-10-02), derived the free-diffusion conjugate target law and functional stationarity, and expressly relied on restricted numerical comparisons when addressing whether the stationary clock was globally minimizing. It listed diffusion in a potential as a future direction. Its later v2 and the published Physical Review Letters version were considered by statement/implication, not merely title. The theorem here has a different mathematical conclusion: a nonnegative **all-competitor** identity for the entire renewal-clock class, weighted by the reversible speed measure for any smooth one-dimensional potential, with an equality and stability characterization. Ray–Mondal–Reuveni treat drift-diffusion and optimize a Poisson rate at a fixed target; Evans–Majumdar treat resetting site or rate optimization. Accessible related mathematical records and previously recorded findings did not contain a covering theorem. General reversible Green-potential optimization or unindexed kernel symmetrization could still entail the result, so independent publication priority is uncertain.

## Mathematical value — PASS

The 2024 source itself distinguished its variational stationarity from an unproved global minimum and named potential-driven search as an open extension. An exact global regret certificate closes that motivated mathematical gap, clarifies equality and gives quantitative perturbation stability for competing clocks. It also reveals explicit force-dependent optimal Poisson rates for a natural exponential launch law, avoiding a purely formal or arbitrarily truncated model calculation. The theorem is a structural result about all renewal protocols, rather than a finite-parameter numerical improvement.

## Closest sources and limitations

The directly checked full primary source is arXiv:2410.01941v1, including its supplementary derivation, plus v2. The 2011 optimal-resetting paper and 2019 Péclet-drift paper supply relevant but distinct baseline models; the latter optimizes fixed-site Poisson restart. The result is restricted to one-dimensional reversible gradients, independent renewal clocks, fixed per-experiment launch site and complete restarts. No all-dimensional or nonreversible result, experimental validation, or uniqueness of clock laws is claimed. A specialized unindexed potential-theoretic identity remains a priority risk, and independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
