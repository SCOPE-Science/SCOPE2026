# Scientific review

## Correctness — PASS

The model is a finite-speed velocity-jump process with two orientations and transparent interfaces; its generator is specified in RESULT.md. The invariant density, periodic Poisson corrector and martingale quadratic variation give \(D_{\mathrm{eff}}=L^2/(2IJ)\) for every starting state. The exact budget optimizer follows from a linear inequality because the higher-speed phase has the smaller reversal-cost coefficient. The speed optimizer is the sole positive root above unity of an explicit quadratic. The exact equal-half optimum, small-fast-fraction asymptotic and strict enhancement boundary are algebraic consequences with independently checked identities. The finite-state corrector implementation provides diagnostics but is not used to infer infinite-parameter truth.

## Originality — PASS on inspected evidence; priority uncertainty remains

The 2015 works by Solon–Cates–Tailleur and Angelani–Di Leonardo–Paoluzzi motivate variable motility and treat, respectively, local diffusion closure and first-passage objectives. Lutscher–Hillen (2021) supplies closely related general periodic velocity-jump homogenization, so that generality is explicitly excluded from the new-claim scope. The new statement optimizes a *jointly constrained spatial speed profile and switching-rate allocation* over all admissible two-zone coefficients, characterizes both unique optimizers and a noncompact enhancement regime, and supplies a strict finite-contrast decision boundary. No equivalent or dominating result appeared in the actually queried research records or examined accessible source material. The full 2019 Angelani–Garra paper remained inaccessible, so historical priority is provisional; absence from abstracts alone was not treated as proof of noncoverage. The mathematical statement is new relative to the inspected sources, not independently certified against all literature.

## Value — PASS

The optimization explains a potentially counterintuitive design feature: an environment with fixed mean transport speed and fixed mean reversal activity can outperform its homogeneous counterpart, by a sharp factor for equal zones, and by arbitrarily much in a singular narrow-patch family. It distinguishes local resource budgets from the time spent moving through each zone, and provides a complete fixed-fraction optimum rather than an arbitrary numerical instance. The infinite upper envelope is a mathematically structural limitation of mean-only constraints, not a prediction of unconstrained physical devices.

## Boundaries and access risks

The result does not extend to bounded speed/rate amplitudes without new work, does not include discontinuous interface reflection, and does not claim novelty of general homogenization. The inaccessible full 2019 speed-inhomogeneity paper is a priority risk; the inspected 2021 homogenization supplies much of the underlying method. No claim of external verification, peer review, or independent audit is made.

Self-review: passed. Independent audit: not yet performed.
