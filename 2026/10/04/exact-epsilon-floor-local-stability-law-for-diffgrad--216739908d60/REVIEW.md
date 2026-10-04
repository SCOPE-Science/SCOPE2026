# Review

## Correctness

PASS. The source formulas were reconstructed with bias correction, the gradient-difference friction, and epsilon outside the square root. At the zero orbit, \(\xi_t-1/2=O(|x_t-x_{t-1}|)\), so its product with the first moment is second order. The adaptive denominator similarly differs from \(1/\varepsilon\) only by a higher-order contribution. The limiting optimization block has determinant \(\beta_1\) and trace \(1+\beta_1-(1-\beta_1)\alpha\lambda/(2\varepsilon)\); the exact Jury inequalities give the stated ceiling. The remaining limiting eigenvalues are \(\beta_2\) and \(0\).

Risk: the equality boundary is not assigned a nonlinear stability status, and global dynamics outside the local neighborhood are not classified.

## Originality

PASS. The defining diffGrad paper states the friction rule, its \(1/2\) floor, and a regret theorem, and reports reduced oscillation experimentally; it does not give a quadratic local-stability spectrum. The adaptive-edge-of-stability literature gives the exact frozen EMA-heavy-ball threshold for Adam-like momentum but does not analyze diffGrad's gradient-difference factor. The Adam limit-cycle literature demonstrates broader nonlinear phenomena but likewise does not imply the first-order disappearance of diffGrad's gradient-difference sensitivity.

Focused searches for diffGrad local stability, scalar quadratics, Jacobians, epsilon-floor curvature, and asymptotic equivalence to half-step Adam identified no covering result.

Residual risk: a generic adaptive-optimizer linearization framework may imply the calculation after substituting diffGrad's friction coefficient, even if no diffGrad-specific statement is indexed.

## Value

PASS. diffGrad's defining mechanism is intended to change friction according to short-term gradient variation, especially near optima. The theorem separates two effects that are otherwise conflated: the fixed floor \(1/2\) doubles the local curvature margin, while the actual gradient-difference sensitivity contributes only at nonlinear order. This gives a sharp mechanistic boundary, a direct comparison with established frozen-Adam stability theory, and a precise warning that first-order local stabilization is not dynamically responsive to gradient differences.

Same-model review: passed. Independent audit: not yet performed.
