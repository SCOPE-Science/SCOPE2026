# Scientific review: adaptive institutional reward phase diagram

## Correctness

**PASS.** The normalized ODE exactly reproduces equation (6) of Hua and Liu (2023). With \(1<r<N\), \(k=c(1-r/N)>0\) and the finite geometric sum \(S_N\) is strictly decreasing. The root comparisons yield strictly ordered \(\delta_0<\delta_1<\delta_2<\delta_3\) and the five selected states, including endpoints. The proposed integral Lyapunov function is well defined on the open rectangle, has a precise derivative identity with three nonpositive terms, and its sublevels cannot meet any nonselected boundary face. Every zero-derivative invariant trajectory must be stationary at the selected point; LaSalle therefore proves global convergence for arbitrary \(\varepsilon>0\), with no appeal to finite simulations or boundary hyperbolicity. A standard-library checker checks algebraic identities and finitely many regimes; it is not an infinite certificate.

## Originality

**PASS on inspected evidence, with residual literature risk.** The closest source, Hua and Liu (2023), already derives the equilibria and their local Jacobians and reports five numerical scenarios. Neither the complete Lyapunov integral nor a quantified, ordered **all-parameter** convergence theorem including four equality thresholds is given in its Section 4 or Appendix. The 2022 environmental-game and 2023 collective-risk papers concern different payoff/feedback structures and in general admit cycles. The 2024 collective-risk/dilemma-strength model has a nonmonotone binomial payoff component and a distinct sign for feedback, and may be multistable; its results do not imply monostability for this strictly decreasing reward isocline. Literature and mathematical-result searches did not identify a dominating same-model theorem; indexing gaps and possible uninspected general theorems remain residual risks rather than proof of absolute novelty.

## Value

**PASS.** An exact phase diagram matters because local stability at each fixed point and finite phase portraits cannot exclude persistent cycles or distant competing attractors. The all-parameter Lyapunov law supplies a mathematically substantive global guarantee despite arbitrary feedback-speed separation, while the four sharp thresholds identify precisely when stationary behavior switches between full defection, high reward partial cooperation, a feedback-set fraction, low reward partial cooperation, and full cooperation. Endpoint cases are often nonhyperbolic and are included rather than inferred from linearized stability. The result isolates the structural monotonic-payoff mechanism behind the absence of recurrent oscillations, distinguishing it from nearby collective-risk models where multistability occurs.

## Limitations and literature relation

The finding is confined to Hua–Liu equation (6) for \(N\ge2\), \(c>0\), \(1<r<N\), \(\delta,u,\varepsilon>0\), \(0<\alpha<\beta\), and strictly interior initial conditions. Full bibliography, exact formulas and proof are in `RESULT.md`. No independent validation or audit has yet occurred.

Self-review: passed. Independent audit: not yet performed.
