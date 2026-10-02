# Mathematical audit — 2026-10-01

## Final claim assessed

Sharp minimax relaxation frontier for scalar Newton under derivative-sector bounds

## Correctness — PASS

PASS. The root-relative error identity is exactly \(1-\gamma a/d\), where the root secant slope \(a\) and current derivative \(d\) both lie in \([m,L]\). Endpoint maximization gives the exact one-step envelope and continuous boundary layers attain its extremes in the closure. Equioscillation gives the optimal constant damping. At \(\kappa=2\), equality in one step would require an impossible continuous derivative profile, so every nonroot error strictly decreases and compactness rules out a positive limiting error. The explicit even derivative profile yields a genuine two-cycle for every \(\kappa>2\). The derivative-aware minimax reduces pointwise to the two-endpoint Chebyshev problem and correctly cancels the Newton denominator.

## Originality — PASS

PASS to the best of current knowledge. Heid's complete open-access article was inspected through Theorem 2.1 and the damped-Newton framework; it gives a sufficient convergence condition with damping strictly below \(2\alpha_{F'}/L\), which specializes to the strict scalar bound already excluded from novelty. It does not state the exact root-error envelope, the sharp \(\kappa=2\) boundary with explicit beyond-boundary two-cycle, the optimal constant factor, or the derivative-aware minimax collapse. Resultary and targeted Newton/minimax searches found no earlier theorem containing that combined exact frontier.

### equivalent_formulations

Searches: Resultary: scalar Newton derivative sector exact minimax damping condition number threshold two cycle; web: relaxed Newton derivative bounds sharp scalar minimax

Evidence: The exact semantic search returned the assigned theorem; inspected general damped-Newton theory supplies only sufficient convergence under broader assumptions.

Reasoning: Root-error envelope, relaxation-factor and derivative-aware fixed-slope formulations were all compared; no prior exact equivalence was located.

### broader_coverage

Searches: Heid 2023 complete open-access article, Theorem 2.1; Ortega--Rheinboldt damped Newton context

Evidence: Heid proves convergence for damping below a strict general bound, not the exact scalar minimax envelope or sharp boundary classification.

Reasoning: The broader convergence theorem is prior coverage for one sufficient inequality only and does not dominate the final claim.

### exact_database_or_table

Searches: Resultary exact scalar Newton sector-minimax search

Evidence: No database is relevant and no earlier exact theorem record was found.

Reasoning: The quantities are derived worst-case constants over an infinite function class.

### claim_vs_prior_implication

Searches: Heid Theorem 2.1 versus exact secant/current-derivative envelope; Newton/Kantorovich error-bound literature

Evidence: The prior strict damping guarantee does not imply the endpoint \(\kappa=2\) theorem, two-cycle sharpness, optimal constant factor or derivative-aware minimax rule.

Reasoning: The final theorem contains genuinely additional sharp worst-case statements.

## Scientific value — PASS

PASS. The result turns a standard qualitative damping question into a sharp robustness classification: it identifies the exact worst one-step factor, the precise undamped global boundary, an explicit failure mechanism immediately beyond it, and the information-theoretic fact that derivative-aware multiplicative damping is minimax-equivalent to discarding the local derivative. These are natural algorithmic structure results.

## Source inspections

- **A short note on an adaptive damped Newton method for strongly monotone and Lipschitz continuous operator equations** — https://doi.org/10.1007/s00013-023-01858-x. Material read: Complete open-access HTML was inspected through the assumptions, damped scheme, Theorem 2.1 and its proof discussion. The theorem requires a damping upper bound strictly below \(2\alpha_{F'}/L\). Assessment: PARTIAL_PRIOR_COVERAGE_NOT_EXACT_FRONTIER. Evidence: It covers a sufficient strict damping inequality but not the exact scalar root-error minimax results.
- **Published-record search for scalar Newton sector minimax** — Resultary semantic search. Material read: Ranked semantic results for scalar Newton, derivative-sector bounds, damping, condition thresholds and two-cycles. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: The assigned record was the only exact match among inspected results.

## Checked sources

- Complete assigned Git package and deterministic verifier artifacts.
- Independent endpoint, equioscillation, boundary and two-cycle calculations.
- Complete relevant Heid open-access theorem context.
- Resultary and targeted literature searches.

## Limitations and residual risks

Scalar real equations only; exact arithmetic; global \(C^1\) derivative-sector bounds and a root are assumed. The derivative-aware class is memoryless multiplicative relaxation; line searches, systems and history-dependent methods are outside scope.

- Older scalar relaxed-Newton or nonlinear-equation literature may contain an equivalent minimax statement under different terminology.

## Disposition

**passed**
