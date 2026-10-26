# Scientific review

## Correctness

**PASS.** The method coefficients match Table 1 of Jensen--Ketcheson--Lóczi. The cubic discriminant is strictly negative and the Vieta/root calculation determines the exact threshold. A unique real-plus-complex spectral decomposition proves the positive-history cone dichotomy, and the exponential-start coefficient is explicitly nonzero above the threshold. The exact critical factorization, derivative \(96/125\), and bounded-waiting irrational-rotation argument establish the first-negative-index limit, not just numerical evidence. The packaged standard-library checker checks rational identities and selected trajectories. The asserted statements are strictly within the scalar, fixed-step, exact-arithmetic scope.

## Originality

**PASS, subject to normal historical risk.** The 2026 primary manuscript establishes the optimal BDFL3 formula, A/L stability, accuracy, and numerical tests, but does not state a sharp positivity-history threshold or a first-negative-index asymptotic. The accessible 2010 NASA primary full text gives the earlier BDF2OPT(4) formula and investigates A-stability and aerodynamic performance, not the positive-history classification. A published BDF2 sign-delay result concerns a distinct two-step recurrence with another spectral mechanism and does not imply this three-step result. Exact-coefficient, equivalent-formulation, broader-coverage, and table searches in mathematical records did not identify direct prior coverage. Unindexed older work on positive discrete semigroups or optimized multistep schemes remains a risk; searching is not a proof of priority.

## Mathematical value

**PASS.** The source explicitly motivates stiff-mode damping and long-time integration. The new sharp threshold reveals a structural contrast: decay stability persists, but the set of robustly positive initial histories collapses from a set with interior to one ray. The explicit \(1/(s-s_*)\) delay and constant quantify why finite-time positivity tests near the transition can be misleading. This is more than a one-step sign test or a restatement of A-stability. It does not claim broad nonlinear or variable-step consequences.

## Limits and closest literature

The published coefficient and standard recurrence theory are essential antecedents. Unlike arbitrary positive-history positivity, subcritical perpetual positivity is asserted only for a nonempty open cone; the exact-start law is asserted at and above the critical value. Historical equivalents cannot be conclusively excluded through database searches alone. Independent mathematical review has not occurred.

Self-review: passed. Independent audit: not yet performed.
