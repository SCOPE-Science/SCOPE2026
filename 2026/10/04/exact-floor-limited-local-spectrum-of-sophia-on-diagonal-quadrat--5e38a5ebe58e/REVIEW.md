# Review

## Correctness

PASS. The exact Hessian estimator makes each refreshed Hessian state
\[
h_i^{(j)}=\lambda_i(1-\beta_2^j),
\]
so the preconditioner transient is explicit and geometric. In the local unclipped regime, the limiting two-state mode has determinant \(\beta_1\) and trace
\[
1+\beta_1-(1-\beta_1)\chi_i.
\]
The Jury inequalities give the exact strict stability interval, while the discriminant gives the exact complex-root plateau. The identity
\[
\chi_i=\min\{\eta/\gamma,\eta\lambda_i/\varepsilon\}
\]
then yields the exact flat-curvature threshold.

Risk: this is a local exact-Hessian result; stochastic Hessian estimation and clipping-active global dynamics are not covered.

## Originality

PASS. The defining Sophia paper gives the practical momentum, Hessian-EMA, floor, and clipping update. Its theoretical section proves a condition-number-independent rate for a substantially simplified full-Hessian method without the practical momentum state or max-with-\(\varepsilon\). The inspected source does not state the practical local characteristic polynomial, the exact all-curvature stability ceiling, or the denominator-floor threshold separating the curvature-independent rate plateau from flat-direction slowdown.

Focused literature and published-record searches for Sophia quadratic spectra, local stability, denominator floors, and momentum rate plateaus found no statement implying the complete claim.

Residual risk: an equivalent calculation may exist in unpublished optimizer notes or under generic preconditioned-momentum terminology.

## Value

PASS. Condition-number adaptation is a central motivation of Sophia, while the practical algorithm contains an explicit denominator floor absent from the simplified source theorem. The result identifies exactly when the practical local dynamics inherit curvature independence and exactly where the floor breaks it. It also shows that the source Hessian averaging parameters affect only the transient on exact quadratics, separating preconditioner warm-up from the limiting optimization spectrum.

Same-model review: passed. Independent audit: not yet performed.
