# Review

## Correctness

PASS. At the source-permitted endpoint \(\beta=0\), bias correction makes the scalar second moment exactly \(g_t^2\). On the positive branch of a strongly convex scalar quadratic this cancels curvature from the normalized gradient, yielding an autonomous buffer and an affine parameter recurrence. The buffer proof gives \(b_t/t^2\to\xi^{7/2}\), which makes the multiplicative coefficient \(O(t^{-3})\) and the normalized-gradient displacement \(O(t^{-2})\). The convergent infinite product and exact variation-of-constants identity prove the threshold and positive nonstationary limit.

Scientific risk: the theorem does not classify the sign-changing dynamics below the positive-branch threshold.

## Originality

PASS. The defining source already gives the decay-factor formulas and their heuristic asymptotic motivation, so those are not claimed as new. It explicitly leaves rigorous convergence analysis to future work. Focused searches found no implication-equivalent Amos result proving that its internally generated decay can make deterministic normalized-gradient motion summable and produce a nonstationary limit on a strongly convex scalar quadratic.

Residual risk: an unindexed later optimizer note may contain the same memoryless specialization.

## Value

PASS. The source motivates Amos's internally generated decay as eliminating the need for an externally fixed terminal schedule. The finding identifies a precise robustness boundary of that mechanism: the decay can spend only finite total gradient displacement. The exact threshold \(X_\star\) makes the obstruction quantitative and directly relevant to any rigorous convergence theory or safeguard for the optimizer.

Self-review: passed. Independent audit: not yet performed.
