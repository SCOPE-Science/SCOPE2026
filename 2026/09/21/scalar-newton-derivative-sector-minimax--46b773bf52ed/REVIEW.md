# Scientific review

## Correctness

**PASS.** The main identity is exact: for a nonroot state, the secant slope from the root is an average of f' and therefore lies in [m,L], while the current derivative also lies in [m,L]. The relaxed Newton error multiplier is consequently 1-gamma*a/d. Its supremum over the admissible ratio interval [1/kappa,kappa] occurs at an endpoint, giving the stated envelope. Continuous boundary-layer derivative profiles approach both endpoint ratios, so the envelope is sharp as a supremum.

The optimal constant relaxation follows by equioscillation of the two endpoint errors. The kappa=2 boundary argument was checked separately: equality in the upper ratio would force a continuous derivative to attain its maximum almost everywhere on the entire root-to-state segment while taking its minimum at the endpoint, which is impossible. Strict pointwise error decrease plus continuity on the resulting compact orbit proves global convergence. For kappa>2, the displayed continuous even derivative integrates to exactly twice the endpoint derivative on [0,1], yielding the stated Newton two-cycle.

For derivative-dependent multiplicative relaxation, the closure of feasible (root-secant slope, current derivative) pairs is [m,L]^2. The minimization therefore separates pointwise in the current derivative and reduces to the standard two-endpoint scalar minimax problem. The unique minimizer is Gamma(d)=2d/(m+L), producing the fixed-slope update and the factor (kappa-1)/(kappa+1).

A deterministic verification artifact checks representative boundary witnesses, exact two-cycle parameter choices, random admissible sampled derivative profiles, and the derivative-aware formula. Numerical checks support but are not used in place of the proof.

## Originality

**PASS, to the best of our knowledge, with material historical-equivalence risk.** Classical Newton convergence theory is extensive. Ortega--Rheinboldt covers Newton processes, relaxation and contractions. Gragg--Tapia and Potra--Ptak give sharp bounds under Newton--Kantorovich/majorant hypotheses. Polyak--Tremba develops damped/pure Newton hybrids and one-dimensional specializations. Heid's Theorem 2.1 gives, in a more general strongly monotone Lipschitz operator setting with additional structure, the sufficient damping condition that specializes to gamma<2m/L here.

That sufficient inequality is therefore treated as prior coverage, not as a novelty claim. The checked sources do not state the exact scalar one-step root-error envelope max(|1-gamma/kappa|,|1-gamma*kappa|), its sharp boundary-layer realization, the no-uniform-rate but still globally convergent kappa=2 endpoint, the explicit monotone C1 two-cycle for every kappa>2, the optimal constant factor (kappa^2-1)/(kappa^2+1), or the minimax theorem showing that derivative-dependent multiplicative relaxation optimally cancels the Newton denominator.

The principal residual risk is older scalar nonlinear-equation, relaxed-Newton, nondiscrete-induction, and stationary-iteration literature, where the elementary sector argument may have appeared under different notation. The 1970 Ortega--Rheinboldt monograph was checked at the chapter/summary level available online rather than exhaustively theorem-by-theorem, and the broader pre-digital literature was not exhaustively inspected. This residual risk is scientifically material but no concrete checked source was found to imply the full claimed package.

## Value

**PASS.** The result gives an exact robustness frontier rather than only a sufficient convergence condition. It identifies a sharp global-conditioning transition for undamped scalar Newton, supplies an explicit two-cycle immediately beyond it, quantifies the best possible fixed damping, and explains a counterintuitive minimax fact: under derivative-sector uncertainty alone, the optimally robust derivative-aware Newton relaxation discards the local derivative and becomes a simple fixed-slope iteration. This distinguishes local Newton acceleration from global black-box robustness in a transparent model.

## Limitations

The theorem is scalar, exact-arithmetic, and root-error based. It assumes global derivative-sector bounds and a root. It does not cover systems, nonmonotone functions, finite precision, residual monotonicity, adaptive line searches, trust regions, or history-dependent algorithms. The derivative-aware minimax class is restricted to memoryless multiplicative relaxations based on the current derivative and known sector endpoints. Historical-equivalence uncertainty remains for older relaxation literature.

Same-model review: passed. Independent audit: not yet performed.
