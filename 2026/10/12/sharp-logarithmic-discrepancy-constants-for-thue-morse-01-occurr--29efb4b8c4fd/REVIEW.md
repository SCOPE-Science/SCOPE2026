# Self-review

## Correctness
PASS. The four Thue–Morse residue identities give an exact recurrence for \(E_N=3D_N\). Reading base-\(4\) digits turns this into a two-state weighted automaton; its max-plus and min-plus dynamic programs solve exactly to
\[
\max_{N<4^k}E_N=1+\lceil k/2\rceil,
\qquad
\min_{N<4^k}E_N=-\lfloor k/2\rfloor.
\]
Explicit all-\(1\) and all-\(2\) digit patterns, with one leading zero in the opposite parity cases, attain the bounds. The asymptotic constants follow by comparing \(4^{k-1}\le N<4^k\). Direct prefix enumeration and an independent recurrence evaluator agree throughout the packaged finite stress range.

## Originality
PASS. The direct paper defines the same \(D_N\), proves \(D_N=O(\log N)\), proves its range is \((1/3)\mathbb Z\), and gives explicit unbounded subsequences, but it does not state sharp quartic-prefix extrema or the constants \(\pm1/12\). Searches under exact constants, quartic scales, recurrence aliases, and the factor-\(01\) discrepancy found no covering theorem.

Residual risk remains for an unindexed or unpublished derivation of the same elementary digital recurrence.

## Value
PASS. This sharpens the main discrepancy estimate of the source from unspecified logarithmic order to an exact scale-by-scale envelope and two sharp leading constants. The statement is an extremal law for the source's central observable, not a finite parameter increment.

Self-review: passed. Independent audit: not yet performed.
