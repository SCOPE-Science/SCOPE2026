# Review of the binary-step midpoint damping theorem

## Correctness — PASS

The result is an exact global classification on \(h>0\) at each fixed \(a\ge0\) and \(\lambda>0\). The midpoint amplification is derived directly from the implicit update, and independence yields the all-horizon mean-square formula. Hyperbolic addition converts the objective to the rational function \(Q_c(y)=1-2(1+cy)/(y+c)^2\) over \(y\ge1\). Its derivative has at most one admissible zero, giving the unique central optimum, the two asymmetric optima and the explicit value formulas. The critical quartic, square-root split and distinct zero-atom almost-sure extinction are independently derived. A standalone symbolic/numerical verifier passes 6,847 check groups, but numerical checks do not substitute for the proof. No unresolved critical lemma remains within the stated scalar model.

## Originality — PASS, with priority risk

Abdulle and Garegnani (arXiv:1801.01340, Sections 2, 6–7 and numerical examples) treat random positive time steps and midpoint geometric conservation, but do not derive mean-square optimal binary-step scale bifurcation or a sharp \(7+4\sqrt3\) ratio. Lie–Stahn–Sullivan (arXiv:2103.16506; published Calcolo 2022) study general strong error bounds, including nonuniform grids, primarily with additive solver randomization. Neither claim implies a classification of geometric two-atom step designs on scalar dissipative modes. A related earlier mathematical result, *Three sharp optimal stage laws for mean-preserving randomized implicit Runge–Kutta damping*, optimizes the **stage parameter law** at fixed scaled step, whereas the present theorem fixes two physical step-length ratios and optimizes their **common scale**; the different feasible sets and update maps preclude an immediate implication. Other accessible midpoint works concern oscillatory dynamics, injected noise or stage coupling. A published scalar Polyak analysis contains the same number \(7+4\sqrt3\), but that numerical coincidence is not a proof of overlap. Relevant specialized older variable-step/multiplicative-process literature has not been exhaustively inspected.

## Value — PASS

Random-time-step integration and pseudo-time relaxation motivate a natural binary uncertainty model: the two lengths have a fixed geometric ratio and each numerical update has comparable solve cost. The finding completely solves the optimal mean-square damping-per-step design, determines a sharp qualitative transition from one to two global optimizers, and isolates the critical quartic sensitivity and square-root splitting. Its exact contrast with an almost-sure finite-termination design warns that pathwise and mean-square criteria can choose different scales. These are not consequences of standard \(A\)-stability alone. The result is deliberately restricted to the scalar model and does not claim broader solver dominance or fixed-physical-time accuracy.

## Residual limitations

Independent validation was not performed. Equal probabilities, independent choices, scalar curvature, exact arithmetic and fixed-iteration-count objective are material. The relationship to niche historical studies of random rational recursions remains a publication-priority uncertainty, not an unresolved mathematical step.

Self-review: passed. Independent audit: not yet performed.
