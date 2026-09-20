# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The objective ratio follows by exact expansion of one scaled Polyak step:
\[
R=1-\gamma+\frac{\gamma^2}{4}
\frac{(e^TAe)(e^TA^3e)}{(e^TA^2e)^2}.
\]
After reweighting the spectrum by \(p_i\propto\lambda_i e_i^2\), the remaining
factor is \(\mathbb E[\Lambda^2]/\mathbb E[\Lambda]^2\). The endpoint inequality
\(\lambda^2\le(\mu+L)\lambda-\mu L\), followed by a one-variable maximization in
\(m=\mathbb E[\Lambda]\), gives the sharp bound
\((\mu+L)^2/(4\mu L)\). Equality requires endpoint support with
\(p_\mu=L/(\mu+L)\) and \(p_L=\mu/(\mu+L)\), realized by
\(A=\operatorname{diag}(1,\kappa)\), \(e=(\kappa,1)^T\). This verifies both the
constant and sharpness without a dimension-dependent assumption.

The monotonicity condition is exactly \(Q_\gamma(\kappa)\le1\), yielding
\(\gamma\le16\kappa/(\kappa+1)^2\). Solving the corresponding quadratic in
\(\kappa\) gives the stated frontier. Substitution independently recovers the
special thresholds \(7+4\sqrt3\) and \(3+2\sqrt2\). Differentiating the exact
quadratic envelope in \(\gamma\) gives the minimax scale
\(8\kappa/(\kappa+1)^2\) and factor \(((\kappa-1)/(\kappa+1))^2\).

Limiting cases were checked: at \(\kappa=1\), the envelope becomes
\((1-\gamma/2)^2\); for the classical step it grows asymptotically as
\(\kappa/16\); and the explicit \(\kappa=20\) witness increases objective while
decreasing Euclidean distance. A deterministic NumPy check reproduced the equality
family and found no violation in randomized SPD tests. Numerical evidence is
supporting evidence only; the proof is analytic.

## Originality

**PASS, to the best of our knowledge.** Polyak (1969) establishes the target-value
stepsize principle. Barré, Taylor and d'Aspremont (2020) analyze classical and
modified Polyak steps and explicitly separate distance-oriented and descent-oriented
variants. Huang and Qi (2024), in an accessible theorem-level quadratic analysis,
prove a sharp Euclidean-distance contraction for the Polyak family; their
Corollary 1(ii) is a distance statement, whereas Corollary 1(i) gives objective
contraction for generalized steepest-descent steps, not for the Polyak step.

Recent work was also checked for present-day coverage. Orabona and D'Orazio
(2025/2026) give surrogate-function and negative-result perspectives. He et al.
(2025/2026) establish tight global convergence results and explicit worst-case
PolyakGD trajectories. Wang et al. (2026) study adaptive estimation of the optimal
constant stepsize for quadratics. Searches also covered target-value steps,
objective/function-value monotonicity, overshoot, quadratic specializations,
condition-number thresholds, exact constants, and the synonymous doubled-Polyak
parameterization. No checked source states the exact all-state envelope
\(1-\gamma+\gamma^2(\kappa+1)^2/(16\kappa)\), the two sharp monotonicity
thresholds, or the minimax scaling result.

Residual originality risk is retained. The downloadable copy advertised for
Polyak's 1969 article was not available for complete theorem-level inspection in
this review, and the older target-value/subgradient literature is broad. A simple
spectral two-moment inequality equivalent to the present result could therefore
exist under different weighted-norm or relaxation terminology. The accessible
modern sources provide no concrete indication that the claimed frontier is already
covered.

## Value

**PASS.** Polyak steps are usually motivated by distance-to-solution control, so an
exact boundary for objective monotonicity answers a distinct stability question.
The result shows quantitatively that Euclidean progress does not prevent a function-
value spike, identifies the precise condition-number range where this cannot
happen, and shows that the spike can become arbitrarily large with conditioning.
The scaled-family theorem also determines the unique minimax calibration of the
Polyak formula for one-step objective control and connects its sharp factor to
exact-line-search steepest descent.

## Scientific limitations

The result assumes exact real arithmetic, a real SPD quadratic objective, the
Euclidean gradient, and exact knowledge of the optimum value. It is a sharp
one-step class result, not a complete trajectory characterization. It does not
cover inaccurate target values, nonquadratic smooth strongly convex functions,
constraints, stochastic or inexact gradients, alternate metrics, or floating-point
effects. The exact-line-search comparison concerns equality of worst-case objective
factors only. Historical prior-coverage risk remains because some older target-value
and subgradient sources were not fully inspected theorem by theorem. Independent
audit has not been performed.
