# Scientific review

**Claim reviewed:** Exact absorption-time law for fixed-increment limited-precision stochastic summation.

**Correctness — PASS.** The \(p+r\) truncation of an exact state-plus-small-increment is a binade-constant truncated increment. The induced chain has one upward neighbor per state and a common positive success probability within each binade, followed by a zero-probability absorbing boundary. The count of grid edges and independent geometric waiting times prove the negative-binomial convolution, moments, deterministic endpoint, and ideal-rounding separation. Exact rational verification of 62,496 states supports the local algebra but is not an infinite proof.

**Originality — PASS (best knowledge, not an independence certificate).** El Arar et al. (arXiv:2408.03069 and arXiv:2603.24161) supply the prior operator and finite-length error analysis. The 2025 stochastic-neuromorphic paper already identifies small-update guard-bit loss; that phenomenon is not claimed as new. Fitzgibbon–Felix compare different few-bit implementations and bias corrections. The distinctive claim is the sharp stopping barrier, at-most-\(r\)-binade classification, entire negative-binomial convolution, and exact moments for persistent fixed increments. Targeted statement/implication searches in the published mathematical literature and primary-source full-text comparisons found no dominating result. Earlier equivalent specialized probability laws remain possible.

**Mathematical value — PASS.** The finding quantifies when finite guard-bit stochastic updates will cease to accumulate altogether and exactly how many iterations precede that event. This is a natural benchmark in the design of biased limited-precision stochastic arithmetic, particularly when many small updates are accumulated. It is not claimed to generalize to sticky-bit corrected implementations.

**Limits.** Positive \(p\)-representable fixed addends in the stated interval; \(p+r\) truncation toward zero; independent draws; unbounded normal exponents; no subnormals or sticky correction. General varying-input, practical runtime, and hardware-specific conclusions are unproved. Literature uniqueness is not independently certified.

Self-review: passed. Independent audit: not yet performed.
