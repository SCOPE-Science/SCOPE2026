# Scientific assessment

## Correctness — PASS

The exact right derivative of the maximal active edge difference is bounded by the explicit scalar coefficient in the theorem. Internal clique edges have at least the required negative contribution from every common neighbor; hub–blade edges additionally receive at most one positive unit per vertex in other blades. The scalar minimization of \(s^{p-1}+(1-s)^{p-1}\) on \([0,1]\) is elementary and sharp at endpoints for \(p\le2\) and at the midpoint for \(p\ge2\). A single feasible vertex signal attains the upper bound. Global well-posedness follows from the maximum principle and monotonicity of the flux; the active-edge differential inequality yields nonincrease exactly for nonpositive coefficient, while the attaining signal proves failure otherwise. Scaling proves unbounded *instantaneous normalized* growth only for the nonlinear failing cases.

The full finite-family phase diagram follows by ordering the blade sizes. The standard-library checker reconstructs edges and derivatives directly from the graph rather than using the closed formula, with 108 exact sharpness tests, 2536 finite grid cases and 384 sampled phase configurations. These finite tests corroborate but do not replace the analytical proof.

## Originality — PASS, qualified

Mugnolo, *Parabolic theory of the discrete p-Laplace operator* (arXiv:1207.1996), proves order preservation and contraction in vertex-function norms (not a graph-edge seminorm). Hua–Mugnolo (arXiv:1410.1584) treats solution time regularity, extinction and conservation, not the blade-by-blade edge-gradient classification. Münch–Wojciechowski (arXiv:1712.00875) associates linear heat Lipschitz decay with curvature; the nonlinear exponent-dependent threshold is not an implication of a linear result. Exact-semantic comparisons to earlier claims in related areas distinguish the new *individual nonlinear graph-edge maximum* from both linear edge-total-variation decay and two-input edge-Lipschitz stability. The searches and source inspections recorded in the structured assessment did not identify an evaluated theorem covering the same coefficient and phase diagram. This is a best-knowledge originality judgment, not a guarantee of first publication. Unindexed equivalent coverage remains a risk.

## Mathematical value — PASS

The problem compares a familiar nonlinear graph heat flow with a natural, very concrete seminorm not controlled by order preservation alone. The answer classifies an infinite standard graph family, including the complete-graph boundary, a three-leaf exceptional case, all two-blade asymmetries and a genuine critical exponent for balanced blades of size at least three. It identifies exact short-time optimal growth and distinguishes the qualitative fact of contraction from failure by an unbounded normalized instantaneous rate for nonlinear exponents. This is a structural phase diagram, not an arbitrary finite graph calculation.

## Scope and scientific risks

Only finite unit-mass, unit-conductance clique bouquets and one-input edge gradients are covered. The critical normalized-rate divergence has no fixed-positive-time implication. Broader literature may contain a previously unnoticed equivalent criterion, particularly under Markov-semigroup curvature or nonlinear graph-diffusion terminology. The full primary texts inspected provide important general principles but do not directly establish the evaluated blade formula.

Self-review: passed. Independent audit: not yet performed.
