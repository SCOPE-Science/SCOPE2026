# Self-review

## Correctness

**PASS.** The counterexample stays inside the feasible set of qubit density operators and two-outcome POVMs. The source objective contains the joint term \(\log\operatorname{tr}(\rho_i\Pi_i)\) plus calibration terms depending on the state and fixed prior measurement. On the displayed slice the label-\(2\) term is constant, the label-\(1\) mixed second derivative is exactly \(4\), and the chosen valid calibration data contribute only \(-4\) to the \(p\)-curvature. The determinant \(-16\) is exact, so the interior Hessian is indefinite.

## Originality

**PASS.** The direct source states the convexity-based uniqueness claim but does not identify the bilinear joint-curvature obstruction. Searches by source identifier, title, joint concavity, convexity, global maximum, and simultaneous state/measurement likelihood did not locate an implication-equivalent correction. Fixed-measurement maximum-likelihood work does not cover the simultaneous bilinear optimization.

## Value

**PASS.** The convexity sentence is the source's explicit justification for a global maximum or plateau of its simultaneous reconstruction/discrimination iteration. The obstruction removes that global certificate in the smallest commuting quantum model, requiring an independent convergence or optimality argument rather than a cosmetic correction.

## Closest literature and limitations

Ježek's 2002 article is the direct source. Later maximum-likelihood work with a given measurement has a different optimization geometry. Modern self-calibrating tomography is broader but the inspected public material did not expose this source-specific Hessian. The finding does not assert algorithmic failure or multiple local optima for every data set.

Self-review: passed. Independent audit: not yet performed.
