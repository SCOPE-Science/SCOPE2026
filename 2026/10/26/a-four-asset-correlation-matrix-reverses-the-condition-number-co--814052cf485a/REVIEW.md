# Review

**Correctness — PASS.** The exact characteristic polynomials give the spectra of the signed matrix and its entrywise absolute value. These imply positive definiteness of the proposed correlation matrix and give the Euclidean ratio exactly. A rational Taylor enclosure proves the nuclear-norm ratio is strictly below \(0.989\); the included verifier reproduces the polynomial and inequality checks.

**Originality — PASS.** The primary source already defines global balance and studies a trace-norm ratio. The new claim is narrower: it gives an explicit admissible correlation matrix on which that ratio and the induced Euclidean condition-number ratio have opposite signs. Published-literature comparisons found no same matrix/norm-comparison claim. The closest signed-network literature concerns balance indices or spectral properties, not this condition-number sign reversal.

**Value — PASS.** The result identifies a qualitative norm-dependence in an argument intended to interpret a network statistic as perturbation sensitivity. It gives a concrete check that users can apply before reading a trace-norm surrogate as a Euclidean worst-case sensitivity measure.

**Closest literature and limitations.** Bartesaghi et al., arXiv:2407.14272, §4.2–4.3, define the global-balance and trace-norm quantities; the present result does not claim either definition as new. It does not challenge the paper's empirical correlations or establish a general ranking for all networks.

Self-review: passed. Independent audit: not yet performed.
