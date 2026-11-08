# Scientific review: housekeeping-selected charging clock

## Correctness — PASS

The claim specifies a two-state Markov charging stroke with fixed positive affinity and a constant housekeeping rate that does not feed back on the dynamics. The reduction from the relative-entropy free energy and interface work of Lin, Liu and Ma to \(\eta_h(s)=f(1-e^{-s})/(1-e^{-s}+hs)\) follows with explicit units. The identity \(f'(1)=1\) is verified from the exact logistic odds shift; strict convexity gives \(0<\rho<1\). The derivative numerator is factored into a positive ideal term and a housekeeping term. A compact positivity argument and an eventually strictly decreasing threshold function prove uniqueness of the **global** optimizer for sufficiently small housekeeping for every fixed finite affinity. Controlled expansion yields the logarithmic clock and the next efficiency term. In linear response, the exact threshold's derivative has a definite sign for all positive time beyond the unique maximum-power time, proving global uniqueness, strict parameter monotonicity and both endpoint asymptotics. The standalone standard-library verifier passed 458 deterministic consistency checks; these do not replace the proof.

## Originality — PASS, with stated priority risk

The parent preprint [1] establishes the charging dynamics, relative-entropy stored energy, fuel-efficiency expression, finite-time existence of a full-efficiency optimum, and efficiency at **maximum power**. It also supplies numerical graphs of maximal full efficiency. The mathematical statements compared here instead locate the **maximum-full-efficiency charging duration**, prove its weak-housekeeping logarithmic law including the finite-affinity coefficient, obtain the two-term optimal efficiency deficit, and globally classify the complete weak-affinity optimizer curve. The related passive RC work [2] concerns the classical power-efficiency curve and multi-step charging control without the modeled housekeeping term. Their exact forward formulas do not state these asymptotic optimizer laws or the all-housekeeping linear-response uniqueness theorem. Literature and semantic index searches using equivalent charging-clock, housekeeping, relative-entropy, and constant-voltage terminology did not identify an explicit covering result. Residual risk: a broader unindexed theorem for single-exponential charging with parasitic power might imply the linear-response component, and an independently discovered asymptotic optimum may exist. The finite-affinity logarithmic law is the principal distinctive statement.

## Value — PASS

The parent model treats the optimal full efficiency primarily numerically. Its ideal limit is attained only at infinite charging time, while any positive source-maintenance cost forces a finite optimum. The precise clock-selection rate and the sharp \(h\log(1/h)\) performance penalty distinguish practical near-ideal operation from the singular zero-cost idealization. The finite-affinity coefficient depends only on the asymptotic ideal efficiency \(\rho\), giving an explicit stopping rule from measurable model parameters. The complete weak-affinity classification explains how the optimum moves monotonically toward the maximum-power clock as fuel maintenance dominates. These are physically motivated boundaries and nonuniform limits, rather than a free parameter substitution or an arbitrary finite-data fit.

## Closest published material and limits

[1] Y.-Q. Lin, R.-H. Liu and Y.-H. Ma, *Active-Matter Battery*, https://arxiv.org/html/2610.00428v1, first public 2026-09-30; main-text equations (1), (4), (7), (9), (16), (17), Appendix A.

[2] J.-R. Lei, Y.-Q. Lin, S.-G. Ou and Y.-H. Ma, *Universal power-efficiency trade-off in battery charging*, Frontiers of Physics 20 (2025) 042202, https://doi.org/10.15302/frontphys.2025.042202; RC charging performance and multi-step control.

No general finite-affinity uniqueness claim for arbitrary positive housekeeping is made; only sufficiently small housekeeping is covered there. The all-housekeeping uniqueness claim is solely in the linear-response limiting model. The theorem does not address feedback-dependent active dissipation, leakage, optimized time-varying affinity, finite-time discharge or experimental batteries. Literature priority still requires independent verification.

Self-review: passed. Independent audit: not yet performed.
