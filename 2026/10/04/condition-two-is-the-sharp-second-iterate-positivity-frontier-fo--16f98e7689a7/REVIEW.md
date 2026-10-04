# Same-model review

## Correctness
PASS. The first two steepest-descent updates are reconstructed from the exact residual formula, yielding the identity
\[
x^{(2)}=\alpha_0\alpha_1[(\mu_0+\mu_1)I-A]b.
\]
For a Stieltjes matrix, the off-diagonal signs of this bracket are favorable, and the Rayleigh bounds \(\mu_0,\mu_1\ge\lambda_{\min}\) prove positivity whenever \(\lambda_{\max}\le2\lambda_{\min}\). Sharpness is established for every larger condition number by an explicit diagonal three-mode family with an exact admissible interval for its third right-hand-side component. The all-iterate two-dimensional statement follows from an exact two-step residual cycle with multiplier \(\rho\in[0,1)\). The packaged rational checker independently replays the critical identities and the explicit witness.

## Originality
PASS with residual literature risk. Classical sources cover the Cauchy step, residual orthogonality, convergence-rate bounds, and two-mode spectral oscillation; those facts are treated as prior work. Searches for Stieltjes or \(M\)-matrix steepest-descent positivity, positive-orthant invariance, second-iterate sign criteria, and a condition-number-\(2\) frontier did not find an implication-equivalent result. The inspected full texts do not state the universal second-iterate positivity theorem, the all-\(\kappa>2\) diagonal obstruction family, or the all-iterate two-dimensional orthant result. Older monotone-iteration literature remains a plausible residual risk.

## Value
PASS. Stieltjes systems arise from standard elliptic discretizations and have nonnegative inverses, so a negative transient iterate is a meaningful qualitative failure even though the quadratic objective decreases. The result gives a complete sharp second-iterate conditioning frontier, identifies the minimal dimension and iteration where failure can occur, and supplies an exact low-dimensional safe formula. These are directly usable as solver diagnostics and regression tests rather than a routine convergence-rate restatement.

Same-model review: passed. Independent audit: not yet performed.
