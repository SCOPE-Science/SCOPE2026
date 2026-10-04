# Review

## Correctness

PASS. The source recurrence has \(s_\star=\varepsilon/(1-\beta_2)\). At the optimum, the residual square has zero derivative and denominator perturbations are multiplied by a zero numerator. The Jacobian therefore splits into eigenvalue \(\beta_2\) and a \(2\times2\) block with determinant \(\beta_1\) and trace \(1+\beta_1-(1-\beta_1)\chi\). The Jury inequalities give the exact frontier, and the discriminant gives the exact complex-root plateau.

Risk: this is a local theorem and does not classify nonlinear motion after instability.

## Originality

PASS. The defining paper specifies the epsilon placement and proves broad convergence bounds but does not state this deterministic quadratic local frontier. The official implementation confirms the same accumulated-epsilon convention. Later Aida work studies how epsilon placement changes adaptive-step ranges but does not derive the curvature ceiling or rate plateau. FastAdaBelief changes the schedule to exploit strong convexity rather than analyzing this constant-parameter local dynamics.

Focused published-record searches over AdaBelief, scalar quadratics, epsilon, Jacobians, fixed points, and local stability found no covering statement.

## Value

PASS. Epsilon is an operationally important AdaBelief hyperparameter and later work already identifies its placement as shaping adaptive-step ranges. The exact quadratic calculation shows a sharper consequence: the locally admissible curvature scales through \(\sqrt{\varepsilon/(1-\beta_2)}+\varepsilon\), and momentum creates a broad exact rate plateau. This supplies a concrete tuning and implementation diagnostic.

Same-model review: passed. Independent audit: not yet performed.
