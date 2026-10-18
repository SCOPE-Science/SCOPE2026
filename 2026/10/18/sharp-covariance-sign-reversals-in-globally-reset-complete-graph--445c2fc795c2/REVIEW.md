# Scientific review

## Correctness
**PASS.** With exactly \(k\) particles, the complete-graph exclusion generator closes on first and second occupation moments. The explicit generator identities yield unique stationary means and pair products, and subtracting their products gives the three covariance fractions. Denominators are positive, so the asserted one-time sign thresholds follow directly from their numerators. All boundary cases \(k=1\), \(k=2\), \(N-k=1\), and \(N-k=2\) were included. Independent unreduced generator computations agreed in 2,766 covariance comparisons; symbolic factorization and exact-rational boundary checks corroborated the proof.

## Originality
**PASS within checked coverage, with residual risk.** Borcea–Brändén–Liggett establish negative association for fixed-time symmetric exclusion, whereas stochastic resetting mixes observation ages and is not an assumption of that theorem. Evans–Majumdar's renewal scheme is a general technique, not an evaluated complete-graph pair-correlation/sign theorem. The full accessible 2019 single-configuration SSEP-reset paper studies a nearest-neighbor ring, density profiles, and currents; the full 2020 dichotomous-reset ring paper studies correlations in a different symmetric two-reset ensemble. Neither examined primary document implies the all-size single-reset complete-graph formula or sharp integer filling thresholds without additional work. Relevant published-result searches did not locate a matching statement. An unindexed equivalent Bernoulli–Laplace resetting specialization remains possible.

## Value
**PASS.** The finding answers a natural statistical-mechanics question raised by negative dependence of conservative exclusion systems: global Poisson resets can reverse stationary correlation signs even while particle number is fixed. It identifies the exact minimal particle/vacancy requirements and thresholds, while proving that mixed pairs cannot reverse. This complete finite-volume classification provides a benchmark for nonequilibrium resetting models and distinguishes strong temporal mixing from instantaneous exclusion repulsion.

## Closest literature and limitations
The closest primary sources are arXiv:0707.2340 (fixed-time strong Rayleigh property), arXiv:1906.11801 (single-reset SSEP on a ring), and arXiv:2004.00951 (two-reset ring correlations); arXiv:1102.2704 supplies the general resetting mechanism. This theorem does not generalize to arbitrary graph geometries and does not prove negative association when all pair covariances are nonpositive. A first-pass bibliographic originality assessment cannot rule out inaccessible or unindexed equivalent formulas.

Self-review: passed. Independent audit: not yet performed.
