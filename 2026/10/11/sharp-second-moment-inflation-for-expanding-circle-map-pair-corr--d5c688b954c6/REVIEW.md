# Review

**Correctness — PASS.** For fixed integer \(b\ge2\) and radius \(s>0\), the proof computes a covariance kernel using Fourier coefficients and the periodic Bernoulli polynomial, bounds all unequal-lag terms through a gcd-of-repunits estimate, and evaluates the equal-lag geometric series. The leading constant and \(O_{b,s}(\log N/N)\) remainder are controlled by this decomposition. A self-contained exact-arithmetic checker independently integrated event arcs and matched finite variances, with 153 checks passing; finite experiments are not used as a substitute for the proof.

**Originality — PASS with residual risk.** Baker–Todd (arXiv:2606.17880, introduction and Sections 3–4) and Rudnick–Zaharescu (arXiv:math/9912103, Section 4) establish Poissonian pair-correlation convergence and second-moment bounds, but their inspected statements do not give an exact leading variance for unsmoothed shrinking circular arcs. Rudnick–Technau (arXiv:2001.08820, Section 2.2) and Chaubey–Yesha (arXiv:2108.00431, Section 3.1) likewise give bounds rather than this factor. Search coverage is not a proof of novelty; an older unindexed formula remains possible.

**Mathematical value — PASS.** Pair-correlation convergence alone does not determine finite-sample fluctuation size. The proved factor \((b+1)/(b-1)\) gives a sharp, nontrivial dynamical departure from the independent-point fluctuation benchmark throughout a natural family of expanding maps. The precise scale and factor can calibrate second-moment bounds for geometric lacunary trajectories.

**Limitations.** The result covers integer-expanding circle maps, fixed radius, and variance over one Haar-uniform initial point; no full fluctuation distribution, noninteger extension, or non-circular-distance assertion is made.

Same-model review: passed. Independent audit: not yet performed.
