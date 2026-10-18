# Review of a covariance reversal for uniform occupancy

**Correctness (C): PASS.** The exact covariance is reconstructed from pairwise multinomial occupancy indicators, then analytically continued. The distinct exponential bases provide a zero-count theorem with at most four real roots; two known roots, the derivative sign, the two-draw sign and eventual positivity prove one and only one additional root above one. The limiting threshold follows from a uniform expansion and a unique positive root. The two-box boundary is enumerated analytically. The independent standalone program checks rational identities and small exhaustive allocations but does not substitute for the infinite-parameter proof.

**Originality (O): PASS on inspected evidence.** The 2026 public *A one-switch covariance law for occupancy richness and frequency counts* is closest: its exact-frequency covariance formula implies the raw covariance here after summing over frequency indices. The distinct sample-size one-root classification, analytic interpolation, and universal limiting critical load are not given there. Derbazi, Gnedin and Marynych (arXiv:2308.01739v1), and Barbour and Gnedin (arXiv:0809.4387v1), study record-process limits and exact-frequency asymptotics, respectively, without this finite uniform sign transition. Targeted public-record searches included the closest hit and implication comparison. Not all classical sources were assessable, so an unindexed equivalent remains a genuine residual risk.

**Value (V): PASS.** The crossover is a natural dependence boundary between first-hit and second-hit occupancy counts, not an arbitrary statistic. It gives a complete all-integer sample-size single-reversal theorem for every fixed number of boxes and a universal critical load as boxes grow, revealing a sharp structural distinction between sparse and saturated fixed-size samples. The bivariate two-box exception is explicit.

Scientific limits: equal box probabilities are essential; whether a finite threshold is an integer for any number of boxes at least three is left open. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
