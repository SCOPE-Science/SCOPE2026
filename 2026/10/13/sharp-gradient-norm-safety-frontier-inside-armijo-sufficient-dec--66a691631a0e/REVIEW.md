# Self-review

## Correctness
PASS. On an SPD quadratic, the Armijo rule for the negative-gradient direction is exactly
\[
\alpha
\frac{g^{\mathsf T}Ag}{\|g\|_2^2}
\le
2(1-\sigma).
\]
The new-gradient ratio is a convex quadratic in that normalized step. A sharp endpoint spectral-moment bound gives
\[
K_{\max}
=
\frac{(\kappa+1)^2}{4\kappa},
\]
so the interval maximum is attained at the zero-step limit or the Armijo endpoint. The two-dimensional endpoint construction simultaneously attains the moment bound and the maximal allowed step, and positive scaling realizes it at any prescribed first backtracking trial.

The packaged exact-rational checker replays the displayed witness and verifies the algebraic safety equivalence.

## Originality
PASS with stated residual risk. Classical Armijo sufficient decrease and classical exact-line-search gradient-norm oscillation are prior work. The Armijo source inspected in full controls objective decrease, while the exact-line-search source proves the known gradient-norm bound and condition-number threshold for one special step choice.

The accepted claim instead optimizes over every Armijo-admissible steepest-descent step and yields the sharp
\[
\sigma
=
\left(
\frac{\kappa-1}{\kappa+1}
\right)^2
\]
frontier. Targeted searches did not locate an implication-equivalent result or the sharp first-trial backtracking construction.

The main residual risk is older line-search literature that may encode the same Kantorovich calculation under different terminology.

## Value
PASS. Armijo decrease and gradient-norm stopping are routinely used together. The theorem identifies exactly when they are compatible on the basic SPD quadratic model and gives a concrete accepted step where the objective decreases while the gradient stopping diagnostic gets worse. The first-trial construction shows the effect is intrinsic to the acceptance rule rather than an artificial choice among admissible steps.

## Closest literature and limitations
The closest sources are the classical Armijo backtracking framework and Nocedal–Sartenaer–Zhu's exact-line-search gradient-norm theorem. The present result is restricted to quadratic steepest descent under Armijo sufficient decrease alone. Wolfe curvature conditions, nonquadratic objectives, preconditioned directions, and finite precision require separate analysis.

Self-review: passed. Independent audit: not yet performed.
