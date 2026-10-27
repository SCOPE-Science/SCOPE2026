# Self-review

**Correctness — PASS.** The two unit-cell integrals reduce exactly to the scalars \(2\), \(3\), \(p_\varepsilon=2+\varepsilon^2\), and \(q_\varepsilon=1-2\varepsilon^2\). Every nonresidual iterate reaches the exact alternating pair; the residual version contracts by \(2\varepsilon^2/3\). Smooth cutoff existence, all parameter bounds, tie choices, and finite versus infinite reasoning are treated in the proof. A separate exact-rational checker is supplementary rather than a replacement for analysis.

**Originality — PASS, with residual uncertainty.** Hall–Smears–Süli–Wells (arXiv:2606.24806v1) already demonstrate nonconvergence under nonmatching quadratures and slower residual-form convergence. The distinct contribution is the all-small-perturbations impossibility in a fixed smooth one-unknown finite-element example with two positive affine-exact rules, plus the exact phase criterion, cycle amplitude, biased limit and contraction rate. The earlier exact Howard convergence theory of Bokanowski–Maroso–Zidani (2009) is not applicable to the inconsistent branch-selection/forcing pair. An unindexed exact equivalent remains possible.

**Mathematical value — PASS.** The theorem gives a structural no-tolerance boundary, not just a single erratic numerical trajectory, and precisely explains why two superficially similar finite-element assembly variants behave differently. The discrete policy tie is the essential mechanism, so the result is not asserted for all strictly complementary regimes or complete nonlinear PDE solvers.

Self-review: passed. Independent audit: not yet performed.
