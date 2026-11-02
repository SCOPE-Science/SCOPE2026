# Review of the sharp two-defect quadrature positivity frontier

## Correctness

**PASS.** Exactness on the original Dirichlet cardinal basis reduces the changed-site equations to scalar and symmetric two-by-two calculations. The derived formulas determine the sign of every weight for all odd grid sizes \(K\ge5\). The one-site case remains positive for every permitted signed displacement; the two-site case has exactly one sign-changing center weight. The unique crossing follows from monotonicity in displacement and strict convexity of the inverse-sine function. The proof includes the exact condition-number identity and a justified large-grid expansion. A standalone checker independently solves complex Fourier moment equations on finite samples and passed 5100 grouped assertions. Finite tests are corroborating checks, not a substitute for the proof.

## Originality

**PASS, qualified.** Austin's 2016 thesis section 3.5.2 numerically investigates trigonometric quadrature weight sums and contains partly unperturbed grids; the relevant section was read, and it does not give a two-moved-node sign classification. Austin and Trefethen (2017) establish convergence bounds. Yu and Townsend (2022), section 4.1 and Appendices A–B, prove a negative-weight construction with many moved sites for arbitrarily small displacement and global size lower bounds; these do not imply a two-site support optimum or the present exact threshold. Published-record searches found nearby work on unrelated weight-positivity problems. Historical-priority uncertainty remains possible.

## Value

**PASS.** Sparse node jitter is a motivated design distinction: whether one or two sampling sites fail to meet a prescribed grid is not captured by a uniform amplitude bound alone. The sharp all-order crossing, one-site impossibility and explicit \(\ell^1\) stability gap identify when the positive-weight property first becomes possible to lose under local corruptions. The result does not claim a global minimax two-site threshold.

## Limitations

Only exact odd-order trigonometric interpolatory quadrature, the stated two-site symmetric geometry, and analytic real arithmetic are covered. Unrestricted two-site arrangements and floating-point sign effects are not analyzed. Priority and scientific validation have not been independently assessed.

Self-review: passed. Independent audit: not yet performed.
