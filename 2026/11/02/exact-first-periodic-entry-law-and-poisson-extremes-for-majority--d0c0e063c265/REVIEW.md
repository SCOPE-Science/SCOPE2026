# Scientific review

## Correctness — PASS

The Boolean identity \(F(x)_i=x_i\oplus y_{i-1}y_i\) implies monotone erosion of maximal runs of edge disagreements, proving the exact first-entry identity and ruling out hidden transient cycles. The transfer matrix has a one-to-one closed-walk encoding for each cyclic edge word containing a zero; parity projection and the two checkerboards account for all configurations. The Poisson law follows from explicit factorial moments of incompatible and independent rare run-start events. Geometric upper and lower tails yield the mean estimate. Direct exhaustive dynamics and independent matrix census checks in `verification_output.txt` match the theorem. **Risk:** an error in an untested finite case is possible, but is not used to infer any infinite result; every limiting assertion rests on stated symbolic arguments.

## Originality — PASS, qualified

Tosic–Raju (2011) empirically discusses majority-automaton convergence rates but provides no exact first-periodic-entry distribution for radius-one synchronous cyclic majority. Tosic–Agha (2004) addresses stable configuration structure; Lemoy–Mozeika–Seki (2013) addresses thermally perturbed equilibrium; Nakar–Ron (2022) provides a general stability/periodicity classification without deriving the present finite entry-time census or its Poisson limit. Related results concern distinct rules or weaker conclusions and do not imply the claimed exact count and scaling. Targeted searches for the longest alternating run, rule 232 convergence time and Poisson statistics found no covering claim. **Risk:** older unindexed analyses could independently contain these formulas; current novelty is supported by the inspected material and not independently certified.

## Mathematical value — PASS

Convergence-time statistics of the classical majority rule are a natural invariant not determined by merely classifying eventual fixed points or two-cycles. The exact all-size CDF directly resolves the distribution rather than just a worst-case bound; the logarithmic law and lattice Poisson window identify the typical rate behind previously reported empirical convergence curves. This is not a trivial reparametrization: a parity constraint, a two-cycle exceptional class and an extreme-value argument are all required.

## Scope and comparison

Only binary nearest-neighbor *synchronous* cyclic majority is covered. The limiting law is stated along integer thresholds with convergent intensity; an unconditional centered continuous Gumbel statement is deliberately not made. The four closest source families, precise domains and residual historical-equivalence risk appear in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
