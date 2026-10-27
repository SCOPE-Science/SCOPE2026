# Review

**Correctness — PASS.** The three transition matrices are row-stochastic, the scalar recurrence follows from the state update, and exact rational enumeration covers all 27 words of length three. The target score is \(47/54\), the largest competing score is \(23/27\), and the strict gap is \(1/54\). A one-state PFA cannot distinguish any inputs, proving the lower bound.

**Originality — PASS, bounded claim.** Gill’s binary classification and alphabet-extension corollary do not cover words using three distinct symbols. Kjos-Hanssen’s 2026 theorem gives the upper bound three and explicitly leaves the larger-alphabet two-state classification open. The exact witness is not implied by those statements. Targeted public-literature searches did not reveal a direct match; they do not establish absolute novelty.

**Value — PASS.** The example is minimal in both alphabet support and word length for a target containing three distinct symbols. It supplies a reproducible exact boundary case for the unresolved larger-alphabet classification, rather than claiming a general classification or optimal gap.

**Closest literature:** K. Gill, arXiv:2402.13376, Theorem 4.1 and Corollary 4.18; B. Kjos-Hanssen, arXiv:2607.26275, Theorem 1.2 and Remark 5.3. Residual risk: an unindexed source may already contain an equivalent small witness.

Self-review: passed. Independent audit: not yet performed.
