# Fresh mathematical audit — Uniform real-root barrier for fixed-parameter heavy-ball acceleration

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** With \(t=\sqrt\beta\), the all-real-root condition is exactly \(|s_\lambda|\ge2t\) for every \(\lambda\). Since \(s_\lambda\) is an affine decreasing interval, it must lie wholly in the positive branch \(s_L\ge2t\) or the negative branch \(s_\mu\le-2t\). On the positive branch, the worst root is at \(\mu\) and the best admissible step is \((1-t)^2/L\); direct polynomial evaluation shows its factor is strictly larger than \(1-\mu/L\) for every \(t>0\). On the negative branch, evaluating the magnitude polynomial at \(q=(L-\mu)/(L+\mu)\) shows the larger root is strictly above \(q\) for every \(t>0\). The \(t=0\) minimax problem gives unique equality at \(\alpha=2/(L+\mu)\). The nonnegative-root frontier follows from the same positive branch. The package replay independently checks representative condition numbers and the Polyak endpoint/interior root pattern.

Sources checked: RESULT.md at the assigned source tree; artifacts/verify_real_root_barrier.py; Hagedorn–Jarre 2024 full open-access HTML.

Correctness risks: Finite-grid replay is corroborative only; the acceptance rests on the analytic branch proof..

## Originality

**PASS.** Classical and modern heavy-ball sources analyze optimal parameters, critical damping, and real/complex root regimes. The inspected Hagedorn–Jarre full text gives the modal spectral-radius formulas and treats real versus complex discriminants, but no inspected source states the constrained interval minimax theorem that an all-real-root tuning cannot beat optimal fixed-step gradient descent, nor the exact nonnegative-root frontier.

### Equivalent formulations

Searches/sources: Published-record semantic search: heavy ball all roots real spectral interval cannot beat gradient descent momentum complex roots; Hagedorn–Jarre DOI 10.1007/s10957-023-02261-w; Danilova–Kulakova–Polyak arXiv:1811.00658.

Evidence: The modern source explicitly separates real and complex modal root formulas and discusses heavy-ball rates. The published-record search found no earlier theorem with the same interval-wide real-root constraint and minimax conclusion.

Root-regime descriptions are ingredients, not an equivalent constrained optimization theorem.

### Broader coverage

Searches/sources: Robust-control heavy-ball optimality literature; Classical Polyak optimal quadratic parameters; stagewise-safe Richardson no-acceleration records.

Evidence: Robust asymptotic optimality establishes heavy-ball performance without imposing all-real roots. Related no-acceleration barriers concern different stagewise or algorithmic constraints.

No broader inspected theorem simultaneously imposes real roots for every curvature in a continuous interval and derives the sharp gradient-descent barrier.

### Exact database or table

Searches/sources: Resultary exact/semantic search for real-root heavy-ball barrier and complex-root necessity.

Evidence: The current record was the exact match; nearby records address different acceleration barriers.

No tabulated invariant is involved; theorem-record search is the relevant exact database check.

### Claim versus prior implication

Searches/sources: Check whether Polyak optimal tuning alone implies necessity of complex roots; Check whether Hagedorn–Jarre modal formula already optimizes over the all-real constraint.

Evidence: Polyak's tuning shows one accelerated method with complex interior roots but does not prove every strict interval improvement must do so. The Hagedorn–Jarre formulas permit the two-branch analysis but do not, in the inspected text, carry out this constrained minimax classification.

The converse necessity statement and equality classification require the new interval-connectedness and branch minimax argument.

### Source inspections

- **Iteration Complexity of Fixed-Step Methods by Nesterov and Polyak for Convex Quadratic Functions** — SUPPORTING_NOT_COVERING.
  Identifier: https://doi.org/10.1007/s10957-023-02261-w
  Trigger: Closest modern full treatment of heavy-ball modal spectral radii.
  Material read: Full open-access HTML, including the main results and Section 2.1 real/complex eigenvalue formulas.
  Method: lawful open-access full text
  Evidence: It analyzes the spectral radius and both discriminant regimes but the inspected theorem statements do not give the all-real interval minimax barrier.
- **Non-monotone Behavior of the Heavy Ball Method** — SUPPORTING_NOT_COVERING.
  Identifier: https://arxiv.org/abs/1811.00658
  Trigger: Classical optimal tuning's complex-interior behavior.
  Material read: Public arXiv metadata and cited description in the audited record.
  Method: lawful open-access material
  Evidence: It documents non-monotone behavior and classical parameter effects, not the converse interval-wide necessity theorem.

Originality risks:
- Full theorem-level text of Torii–Hagan 2002 and Zhang 2015 was not inspected; an equivalent parameter classification there remains a residual prior-art risk.

## Scientific value

**PASS.** The theorem gives a sharp structural boundary between overdamped/all-real interval tuning and robust acceleration, including the unique equality case and a stronger nonnegative-root frontier. This is a natural classification with direct interpretation for fixed-parameter quadratic optimization.

Value risks: The statement concerns continuous interval robustness and does not say every accelerated finite matrix has an actually present complex mode..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to the scientific result or slogan is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
