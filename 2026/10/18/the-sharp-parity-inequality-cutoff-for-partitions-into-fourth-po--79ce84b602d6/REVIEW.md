# Scientific review: strict parity for fourth-power partitions

## Correctness — PASS

The exact signed generating function factors into the distinct-subset product over \(2^\ell u^4\), with \(u\) odd and \(\ell=0\) or \(4\nmid\ell\). Cancellation is legitimate in formal power series, because every coefficient depends on finitely many factors. The ten-weight base certificate consists of exactly 64 integer intervals and covers \([145,661]\), but omits 144; the complete zero set below 145 follows from the same interval decomposition. All later selected weights have consecutive ratio at most two, by explicitly bridging each missing dyadic power. The interval-extension induction therefore proves all indices beyond 661, without extrapolating numerical tests.

The verifier reconstructs the 64 intervals from all 1,024 subsets and compares 2,049 signed and distinct-part coefficients from separate recurrences. No unproved asymptotic or computational extrapolation is used.

## Originality — PASS within inspected evidence

Ciolan's 2020 paper proves eventual strictness and an all-index nonnegative generating-function reformulation; its concluding discussion allows exceptional small equality cases. It neither supplies the exact fourth-power zero set nor the sharp threshold. The earlier squares-only paper concerns a different exponent. Specific mathematical-record and literature searches for the equality set, the cutoff 145, the equivalent subset-sum spectrum, and broader statements found no dominating theorem. Nearby mathematical-record hits concern unrelated Fourier moments, Waring-semigroup exceptions, or different partition statistics, and do not imply this coefficientwise sharp classification. The closest accessible historical result solves the square exponent, not the fourth-power exponent. Novelty cannot be inferred from absence of search hits alone: a hidden, unindexed equality table remains a residual risk.

## Mathematical value — PASS

The fourth-power case is the first even exponent beyond squares in Ciolan's established family of parity-bias problems. The result computes a natural and previously non-explicit sharp invariant, the last equality index, and classifies every exceptional index. The finite interval is supported by an unbounded structural induction, replacing asymptotic eventual strictness with an optimal all-index theorem. This is a substantive exact-boundary result, not a change of notation or a finite table standing alone.

## Relationship and limitations

Primary source: A. Ciolan, *Equidistribution and inequalities for partitions into powers*, arXiv:2002.05682, first version 2020-02-13, sections 2, 3, and 8 and conclusion. The paper's general nonnegative sign mechanism is credited, not claimed new. The finite 35-equality classification and cutoff 145 are the new assertions. Other exponents are not classified, and independently published overlap cannot be categorically excluded.

Self-review: passed. Independent audit: not yet performed.
