# Scientific review: critical epsilon-outside RMSProp

## Correctness — PASS

For the exact step \(h=2\varepsilon/L\), the smoothness inequality leaves the strict decrement \(h\sum_i g_i^2\sqrt{w_i}/(\varepsilon+\sqrt{w_i})^2\), with \(w_i\ge(1-\beta)g_i^2\). Strong convexity supplies compact spatial sublevels, and the memory filter remains bounded, so convergence of the decreasing objective forces every spatial limit point to be its unique minimizer. The gradient filter then vanishes. Bounds on objective sublevels and the memory filter also prove full-state Lyapunov stability.

On scalar quadratics, the exact no-hit multiplier is \(-(\varepsilon-\sqrt{v_{k+1}})/(\varepsilon+\sqrt{v_{k+1}})\). An eventually contractive equation for \(v_k/(a^2|x_k|^2)\) proves that ratio tends to one; consequently the reciprocal-amplitude increment tends to \(2a/\varepsilon\). Cesàro's lemma gives both stated inverse-time limits, with finite-hit exceptional initial data explicitly exhibited. Exact-rational and numerical checks are corroboration, not a replacement for this infinite-time argument.

## Originality — PASS under inspected evidence

Loh, Mireles James, Xu, and Tao, arXiv:2610.30078v1 (first public 2026-10-21), analyze this exact dynamical update, but their Sections 4–5 state globally attracting behavior for the **strict** subcritical bound and nontrivial cycles or instability strictly beyond the frontier. No conclusion about global attraction at equality follows from either strict inequality. Dimitrieski et al., arXiv:2603.15823, likewise use a strict stability bound. The rate statements inspected in arXiv:2504.19426 and arXiv:2608.30382 involve different optimizers or step conditions. Related published search records concern other adaptive methods, and the closest published period-two records do not address the neutral equality case. The exact \(k^{-1}\)/\(k^{-2}\) limits were not covered in the statements inspected. A wider historical normal-form implication remains a residual priority risk; no claim of exhaustive historical uniqueness is made.

## Mathematical value — PASS

The endpoint is a natural missing boundary in the established stability/bifurcation phase diagram. The theorem decides convergence there for all smooth strongly convex objectives and identifies a sharp nongeometric rate on an exact scalar model. The universal constants, lack of leading-order dependence on memory retention, and exceptional finite-hit mechanism distinguish this from routine strict-rate interpolation. No quantitative general-dimensional convergence rate is asserted.

## Limitations

Only the epsilon-outside, uncorrected and deterministic update with \(0<\beta<1\) is treated. The polynomial rate is for nonterminating scalar quadratics. Further historical priority checking and independent audit remain open.

Self-review: passed. Independent audit: not yet performed.
