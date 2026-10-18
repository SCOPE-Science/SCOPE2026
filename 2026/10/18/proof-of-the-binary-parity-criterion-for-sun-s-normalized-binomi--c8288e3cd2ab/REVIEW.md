# Review of the binary-parity criterion

## Correctness

**PASS.** The proof derives the exact normalized summand valuation \(s_2(3n)+2c_n(k)\) directly from Legendre's formula; there is no reliance on numerical extrapolation. Guo's published Theorem 1.2 guarantees integer normalization for each summand. Carry-free terms are exactly the \(2^{s_2(n)}\) submasks of the binary expansion of \(n\). Reflection has no carry-free fixed point for positive even \(n\), and contributions of higher-carry pairs and the central term have strictly larger valuation. The resulting parity congruence holds for all positive \(n\), including \(n=1\). Exact-integer computations through \(n=512\) support, but do not replace, the proof.

## Originality

**PASS under accessible evidence, with residual priority risk.** Sun's original archived sequence and OEIS A189286 explicitly record the parity criterion as a conjecture. Guo's 2013 full paper proves the termwise integrality used here and cites Sun's eight-divisibility, but does not state the parity criterion as a theorem. The 2026 Appendix A.1 entry on A189286 in arXiv:2608.11941v2 also explicitly proves only integrality, not parity. Related search results for Thue–Morse valuation, other binomial supercongruences, and unrelated parity results do not imply this criterion. Accessible historical claim summaries in three archives were screened for the same source ID, formula, and conjecture aliases, without a direct match. Incomplete historical coverage and unlocated publications remain risks; absence of a search hit is not a uniqueness certificate.

## Mathematical value

**PASS.** The exact oddness condition is a pre-existing natural open question about a named 2011 binomial-convolution sequence arising in Ramanujan-type series. The proof resolves all positive indices, and the digit-sum inequality supplies an infinite strengthening rather than a fixed finite computation or arbitrary slice.

## Boundaries

This work does not establish exact valuations at non-power-of-two indices, and does not claim to reproduce Guo's proof as a new result. Independent priority and correctness checks remain outstanding.

Self-review: passed. Independent audit: not yet performed.
