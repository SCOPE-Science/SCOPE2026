# Scientific review

**Correctness: PASS.** The stated 2–10 classification follows from the complete normalization to unbordered binary words beginning with zero and ending with one, a reversible clique characterization, and exhaustive bitset search with mathematically sound coloring and length lower bounds. Source-file verification checks all compatibility conditions and the exact candidate range; an independent integer-program formulation independently obtains 227 at the largest order. No unbounded generalization is asserted.

**Originality: PASS, subject to named residual risk.** Wang and Wang (arXiv:2402.18896, Section 4) pose the mean-length minimization problem without computing these values. Their 2021 construction, Stanovnik–Moškon–Mraz's 2023 fixed-length cardinality results, and the checked published research records do not imply the exact mixed-length minima. The publisher-only abstract of a 2025 Qin–Luo construction could not establish noncoverage; full text remains unavailable, and equivalent unindexed work may exist.

**Value: PASS.** A directly motivated natural finite extremal sequence is settled to order ten, including the exact 24-word, 227-bit optimum and an explanatory certificate. This resolves a specific length-efficiency question, not a cosmetic recomputation of fixed-length cardinalities.

**Limitations.** The proof is finite, for binary minimum word length two, upper length limits at most ten and maximum-cardinality codes only. The analysis is not independent validation.

Self-review: passed. Independent audit: not yet performed.
