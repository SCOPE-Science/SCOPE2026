# Same-model review

## Correctness
PASS. Conditional on the multinomial bootstrap counts, the bootstrap displacement and the sample-mean error are orthogonal Gaussian linear forms. This gives an exact Cauchy ratio and hence the stated conditional coverage. The identity \(Q_n=2C_n/n\), the occupancy generating function, strict concavity argument, and collision-indicator moments were reconstructed independently. The packaged exact-arithmetic occupancy recurrence reproduces exhaustive labeled resampling for small \(n\), verifies normalization and the second through fourth central moments through \(n=30\), and reproduces all quoted numerical values.

Risk: the exact reduction is special to Gaussian observations and to one resample. Those boundaries are stated in the claim and result.

## Originality
PASS. The focal Cheap Bootstrap paper defines the \(B=1\) interval and proves asymptotic exactness; its higher-order section gives a general \(O(n^{-1})\) expansion whose coefficient is described as a multidimensional integral not generally available in closed form. The later finite-sample paper gives upper bounds for linear and Gaussian/sub-Gaussian models, not an exact occupancy mixture or a strict sign for every finite sample size. Searches for the exact Gaussian-mean specialization, Cauchy/occupancy formulation, collision-count formulation, and closed-form \(1/n\) coefficient did not locate a covering statement. A 2026 studentized extension changes the interval through an extra calibration layer and therefore does not imply the claim.

Residual risk: older bootstrap literature may contain an equivalent normal-mean identity under unrelated terminology. The targeted searches and inspections did not resolve every historical source exhaustively.

## Value
PASS. The source method is explicitly motivated by inference with as few as one resample. The finding gives an exact finite-sample calibration diagnostic for that extreme-computation regime: even in the most favorable Gaussian mean problem, the nominal interval is always slightly anti-conservative, with a closed-form first-order deficit and dramatic degeneration at very small \(n\). This sharpens both the source paper's asymptotic expansion and the follow-up paper's finite-sample bounds without requiring a broader downstream theorem.

Same-model review: passed. Independent audit: not yet performed.
