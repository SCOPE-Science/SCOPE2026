# Mathematical review

**Correctness — PASS.** The joint conditional construction follows from the ordered-selected-prefix and sorted-tail representation in Clay [1]. Its *joint* use is explicit, avoiding an invalid inference from separately coupled marginals. The Hoeffding projection has coefficients \(n-2t+1\) for \(t\le k\) and \(-k\) otherwise; the canonical remainder has variance \(k(2n-k-1)/24=O(n^2)\), negligible on the inversion scale. Cross-covariance between conditional descent noise and projected inversion noise is exactly \((k-1)/6\), hence vanishes upon joint scaling. The 1-dependent triangular-array central limit theorem, independent coupon-count CLT, and quadratic centering complete the proof. All 202 packaged exact checks passed; they are corroboration, not an infinite proof.

**Originality — PASS, with priority risk.** The primary 2026 source [1] provides two univariate limits, not their joint limit. Uniform permutation joint asymptotics in Dörr–Heiny [3] have zero limiting covariance in the fully mixed case, and riffle-shuffle results [4] involve a different kernel. Comparisons with accessible published records about inversion indicator covariance, fixed-point/descent correlations and occupancy richness found none with the new intermediate-time covariance. The possibility of an older, differently named multivariate shuffle theorem remains a residual risk.

**Value — PASS.** Two univariate Gaussian limits cannot determine their joint law. At every finite positive shuffle density the limiting covariance is positive and is **entirely** attributable to coupon-occupancy fluctuations; this distinguishes correlated mixing diagnostics from conditionally independent permutation-order noise. It provides a mathematically natural occupancy-canceling linear contrast and a nontrivial interpolation to asymptotic independence in the fully mixed regime.

The priority comparison does not assert that search nonhits prove uniqueness. No independent verification or audit was commissioned.

Self-review: passed. Independent audit: not yet performed.
