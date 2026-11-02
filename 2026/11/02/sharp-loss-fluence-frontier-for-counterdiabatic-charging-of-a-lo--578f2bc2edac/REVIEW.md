# Scientific assessment of the loss–fluence frontier

## Correctness — PASS

The coherent-state preservation and exact-tracking formula are reconstructed from the dissipative cavity Lindblad generator. The full complex drive satisfies \(U=f+f'/\gamma\); its intensity contains the endpoint-dependent mixed term \(aA^2/G^2\), so the optimal-control reduction uses the *whole* field. The fixed cumulative cavity energy loss is proportional to \(\int f^2\), not to the derivative cost. All quantities are dimensionally and mathematically normalized by \(f(t)=A F(t/T)\).

The optimality proof is global and does not rely on the Euler–Lagrange equation alone. The hyperbolic and sine branches use an exact energy-defect identity and the sharp two-endpoint Poincaré inequality. For the plateau branch the one-endpoint Dirichlet–Neumann Poincaré inequality is combined with the physical cap \(F\le1\) to prove positivity and equality rigidity. Branch parameter monotonicity proves every normalized budget is represented exactly once. The included checker validates branch integrals, the complete complex-field fluence and independently integrated coherent-state trajectories; bounded checks are explicitly non-substitutes for the analytical proof.

## Originality — PASS, qualified

The principal 2026 full text, arXiv:2610.32610v1, covers the model, the CD tracking rule and optimization in the selected \(\sin^2\) pulse family. It does not present the universal fixed-loss envelope minimizer, the two normalized-loss thresholds, or global uniqueness over all monotone ramps. Abah et al. (2019) already optimize CD control costs, but the inspected full-text passages treat Landau–Zener ramps and parametrically driven quantum harmonic oscillators with a different norm objective, not the fixed-loss coherent-state cavity obstacle problem. Cavina et al. (2018) establish a general variational approach for open systems and explicit two-level examples, not this completed constrained spectral/obstacle classification. Other optimal quantum-control work remains a possible source of an equivalent more general theorem. Semantic published-result searches under coherent-state, fixed-loss, global-optimality, sine-plateau and parameter aliases produced no implication-level match; retrieval failure is not taken as mathematical proof of novelty. The accessible historical mathematical claims were checked only for overlap; no new equivalence was identified.

## Value — PASS

There are two independently motivated operational resources: total field intensity in a driven circuit-QED cavity and energy leaked to the environment during exact tracking. Fixing dissipated energy and final stored energy while minimizing microwave fluence is a natural, measurable two-resource question. The unexpected transition from a delocalized sine ramp to a strictly positive plateau at exactly one-half of the normalized loss distinguishes saturated control from a conventional smooth pulse; the hyperbolic-to-sine transition at one-third distinguishes low-loss control regimes. The complete infinite-dimensional global optimum and equality classification provide actual design bounds, not merely a numerically tuned parameter or a minor endpoint improvement. At the source's natural dissipation fraction \(3/8\), the improvement in the derivative component is approximately \(17.49\) percent, showing the bound matters at an existing physical protocol.

## Limits and closest comparisons

The result is exact within the linear Markovian cavity model, unbounded complex quadrature controls and nondecreasing \(H^1\) ramps. Hardware amplitude/slew constraints, finite thermal occupation and model nonlinearities may change it. Broader control-theoretic prior claims could imply its variational structure, and publication priority has not been independently audited. General physical work accounting differs from control fluence; those quantities are not conflated.

Self-review: passed. Independent audit: not yet performed.
