# Scientific review

**Correctness — PASS.** Exact inversion of the smooth clipping fixed-point condition gives a strict monotonicity and concavity argument for the unique stationary state; a monotone scalar equation proves the complete classification. Three asymptotic expansions and a discrete Jacobian perturbation establish the critical exponents, constants and conditional local stability. The included standalone checker reports `VERIFY_OK 1011`; analytic proofs establish the infinite statements.

**Originality — PASS (best knowledge).** The original SClip-EF paper specifies the algorithm and variable-parameter convergence, but the relevant inspected sections do not provide the fixed-parameter three-client equilibrium transition. Clip21 has hard additive clipping feedback, whereas the present map has smoothed relaxed feedback. Prior direct-clipping bias is credited and not asserted as original. Public research-index comparisons uncovered nearby results about other optimizers, not an identified implication of this precise claim. There remains a risk of an equivalent robust-estimation formulation or inaccessible historical result; priority is not independently validated.

**Value — PASS.** The sharp threshold at \(\varphi=2a\), persistent subcritical bias, anomalous critical cube-root recovery and supercritical square-root recovery give interpretable design information for constant clipping in distributed strongly convex problems. Three equal-curvature clients are necessary and sufficient for this bias mechanism, and a locally attracting biased state exists under an explicit feedback-retention condition.

**Limitations.** Scalar deterministic equal-curvature quadratics and one shared global iterate; attraction proven only for sufficiently small steps under an explicit sufficient condition. Parameter limit does not guarantee stability for one fixed feedback weight. No stochastic or general network convergence theorem.

Self-review: passed. Independent audit: not yet performed.
