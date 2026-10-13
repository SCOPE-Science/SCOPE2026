# Review

## Correctness

PASS. Direct inner-product expansion of the exact two-task PCGrad update gives \(\langle g_i,d_{\rm PC}\rangle=\|g_i\|^2(1-\rho^2)\) for each task. The aggregate norm and the raw-sum common-descent window follow from exact algebra, including both boundaries and exact antiparallelity. Randomized and boundary-controlled replay agrees with every formula.

Risk: the statement is first-order; finite learning rates require additional smoothness and step-size control.

## Originality

PASS. The defining paper contains the projection rule, two-task aggregate, and convergence analysis, but the inspected full text does not state the equal relative task attenuation, squared gradient-norm progress invariant, or sharp raw-sum amplitude-ratio window. Later work separating magnitude and directional negative transfer supplies motivation but does not imply these identities. Focused published-record searches found no implication-equivalent statement.

Residual risk: an equivalent elementary derivation may exist in unindexed notes or implementation documentation.

## Value

PASS. The source itself identifies both directional conflict and magnitude disparity as important. The theorem cleanly separates them: PCGrad repairs common descent for all positive norm ratios except exact antiparallelity, yet exactly preserves squared magnitude imbalance in infinitesimal task progress. The raw-sum window and quadratic near-antiparallel slowdown make the distinction quantitatively sharp.

Self-review: passed. Independent audit: not yet performed.
