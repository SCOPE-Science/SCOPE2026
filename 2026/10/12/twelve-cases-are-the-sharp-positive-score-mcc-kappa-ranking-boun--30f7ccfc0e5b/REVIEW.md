# Self-review

## Correctness
**PASS.** For a binary table with true margins \(P,Q\), predicted margins \(R,S\), and determinant \(\Delta=TP\,TN-FP\,FN\), the exact identities \(M=\Delta/\sqrt{PQRS}\) and \(\kappa=2\Delta/(PS+QR)\) reconstruct both statistics. The witness has common \(N=12\), common \(P=4\), all cells positive, and common \(\Delta=4\); direct substitution gives \(2/17>1/10\) for kappa but \(1/\sqrt{70}<1/8\) for MCC. Exhaustive exact enumeration proves that no positive-score strict reversal occurs for \(N\le11\), and that exactly two complement-related reversals occur at \(N=12\). The packaged verifier returns `VERIFY_OK`.

Risk: the theorem excludes zero-cell and negative-association tables; those are different finite domains.

## Originality
**PASS.** The closest primary comparison, Chicco–Warrens–Jurman, studies the mathematical relation between MCC and kappa, proves the pointwise extremeness relation, and reports that positive values are generally concordant while emphasizing negative-regime discordance. The checked full text does not state a fixed-prevalence positive-score ranking reversal, a minimum sample size, or a complete first layer. Exact-table and alias searches likewise did not locate the twelve-case boundary.

Risk: a small numerical pair could occur in unindexed instructional or software material without a minimality result.

## Value
**PASS.** The result isolates a subtle failure exactly where the closest comparison literature suggests practical concordance: both scores are positive, all four cells are populated, and true prevalence is held fixed. The witness also has equal cross-product determinant, showing that predicted-margin treatment alone can reverse model preference. This gives a compact diagnostic for the distinction between two widely used balanced binary-classification summaries.

Self-review: passed. Independent audit: not yet performed.
