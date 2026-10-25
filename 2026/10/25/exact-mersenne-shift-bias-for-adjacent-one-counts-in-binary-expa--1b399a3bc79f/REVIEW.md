# Mathematical review: exact Mersenne-shift adjacent-one bias

## Correctness — PASS

The complete proof reconstructs the conditional law for the change in the `11`-block count after adding one, including its infinite geometric tail. The split at a \(k\)-digit boundary is exact. The binary-valuation cases \(0\le j\le k-3\), \(j=k-2\), and \(j=k-1\) partition all nonzero low words without overlap. Their rational weights yield the exact geometric identity \(P_k=83/128\) for every \(k\ge4\); the three smaller shifts are separately evaluated. Exact rational and direct integer verification corroborate, but do not replace, the general proof.

## Originality — PASS within inspected evidence

The closest primary work is Sobolewski–Spiegelhofer, arXiv:2309.00142, especially the still-open comparison (2.4) and the general fixed-shift distribution recurrences. Sobolewski's later arXiv:2412.15851 treats arbitrary block patterns and many-run Gaussian limits; this theorem instead gives an exact one-run family. Sobolewski's arXiv:2204.05287 has identical Mersenne step sizes but studies parity monochromatic progressions, a different statement. OEIS A014081 supplies the underlying block-count sequence, not this uniform density. Search comparisons did not locate the plateau formula. **Limitation:** the general recurrences might admit an implicit or previously derived specialization, and unindexed priority remains possible.

## Mathematical value — PASS

The published question asks whether the count of `11` patterns weakly increases under addition more often than not. The theorem proves a uniform positive answer for every Mersenne shift and identifies the exact plateau \(83/128\), which persists at arbitrarily large shift lengths despite there being only one run of ones. That solves a motivated infinite subfamily outside the reach of the paper's many-run approximation, not merely a finite table or a recoding of an existing arithmetic sequence.

## Scope and remaining risks

Only shifts \(2^k-1\) are covered; the full all-shift question and complete change distributions remain open here. Finite experiments do not establish the infinite theorem. The general prior distribution recurrences warrant independent priority comparison.

Self-review: passed. Independent audit: not yet performed.
