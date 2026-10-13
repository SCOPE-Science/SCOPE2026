# Scientific review

**Correctness — PASS.** Exact truncated-bivariate-normal second moments are integrated by parts, then propagated along the Gaussian autoregressive Markov chain using conditional second moments. Summation produces the finite-sample covariance for every \(n\ge2\), \(-1<\rho<1\), real \(a\) and \(\sigma>0\). A positive monotone integral gives uniqueness of the threshold and both limiting statements. Independent quadrature comparisons and seeded simulations corroborate calculations without replacing proof. The boundary \(\rho=0\) and two signs of \(\rho\) have been checked separately.

**Originality — PASS, subject to residual historical risk.** Kratz (arXiv:math/0612577) develops continuous Gaussian crossing literature, not the displayed finite discrete crossing–quadratic-energy covariance. Sinn–Keller (doi:10.1137/S0040585X97984991) addresses covariances of crossing counts; complete text was inaccessible, so indirect consequences remain possible. Di Bernardino–León–Tchumatchenko (doi:10.1186/2190-8567-4-22) studies correlations between continuous-time level-crossing signals. The zero-threshold crossing/energy special case is expressly excluded from the novelty assessment. Targeted searches found no published equivalent for the all-level sharp sign classification, but negative searches cannot prove unique priority.

**Value — PASS.** Level-upcrossing frequency and empirical quadratic energy are natural, distinct descriptors of stationary Gaussian time series. The theorem yields a complete dependence sign map and a sharp universal threshold stable under changes in the sample length, quantifying when a high-level excursion event is positively or negatively associated with total signal energy. It is not just a sign calculation at a manually chosen parameter.

**Residual risks.** Hidden reformulations via Hermite-chaos projections or a general level-crossing generating functional may reproduce the result; historical comparison is non-exhaustive. No extension beyond the specified Gaussian autoregression is asserted.

Self-review: passed. Independent audit: not yet performed.
