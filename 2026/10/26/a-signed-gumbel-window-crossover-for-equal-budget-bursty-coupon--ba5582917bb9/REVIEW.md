# Scientific review

**Correctness (C): PASS.** Inclusion--exclusion identifies the exact two completion CDFs, and a coupon-tape/negative-binomial coupling gives the positive finite mean penalty. A root-of-unity calculation establishes the fixed-batch parity and residue asymptotics. Bonferroni truncation at a logarithmic number of missing-coupon terms justifies the critical-window expansion with its signed Gumbel derivative; it is not inferred solely from a limiting distribution. Independent exact-rational state recursions passed 249 comparisons over the declared finite ranges. Finite checks are corroborative only.

**Originality (O): PASS under available evidence, with priority risk.** Betken--Thäle (arXiv:2202.07485v1) explicitly use fixed-size groups without replacement and study marginal empty-count Poisson/normal approximations. Kobza--Jacobson--Vaughan (2007) already treat random sample sizes and Markov-chain computations of distributions and means, so those generic tools are not new contributions. Their full article was unavailable here, making exact specialization a residual priority risk. The assessed contribution is the signed relative \(\log n/n\) critical-window comparison between two equal-budget policies, combined with opposite early/late completion order and an exact rounding mean penalty. Actual semantic searches and implication comparisons are recorded in the accompanying audit.

**Value (V): PASS.** Equal expected throughput does not determine completion-time performance: burstiness causes a bounded but strictly positive expected delay, an early/late stochastic-order reversal, and a sharp universal transition profile at the collection cutoff. This provides a direct decision criterion for interpreting finite-time service policies with batch deliveries, rather than a single unmotivated numerical case.

**Limitations.** Fixed integer batch size in asymptotics; no assertion of a unique finite crossing. The finite-time expectation and CDF forms lie within previously studied random-sample-size coupon models, and priority for the signed correction remains to be verified independently.

Self-review: passed. Independent audit: not yet performed.
