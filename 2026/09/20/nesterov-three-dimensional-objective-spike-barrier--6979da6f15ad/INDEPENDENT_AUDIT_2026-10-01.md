---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For exact-parameter strongly-convex Nesterov acceleration on real SPD quadratics with standard initialization, endpoint-only spectra are objective-monotone, so dimension two is always monotone; for every condition number above one, dimension three admits an interior curvature mode annihilated at step two and revived at step three, making the local objective ratio arbitrarily large with positive denominator.

## Correctness — PASS

Diagonalization gives the exact scalar recurrence. The upper endpoint disappears after one step; the lower endpoint has a repeated-root closed form with strictly decreasing magnitude, proving all-step endpoint objective monotonicity. The step-two polynomial has an interior zero, and direct symbolic recomputation gives nonzero step-three revival. Adding an epsilon-sized lower-endpoint mode keeps the denominator positive and makes the local objective ratio grow like a positive constant times inverse epsilon squared. The actual verifier was inspected but is only corroborative.

**Checked sources.** Assigned RESULT.md at tree 506f0db3a1e207e7352bf19033ed4ea65c68c8dd; artifacts/verify.py blob 091867ed417ef081c61b7f192176ec2c855b0cc9; Hagedorn--Jarre 2024 full open-access article; Giselsson--Boyd 2014 restart paper

**Residual risks.** Loose spectral-endpoint calibration can change the dimension-two conclusion and is excluded.

## Originality — PASS

Prior work establishes nonmonotonicity and motivates restart, and Hagedorn--Jarre provide exact quadratic spectral analysis with two-dimensional nonmonotonicity of iterate distance. Searches did not locate the sharper objective statement: endpoint-only objective monotonicity, sharp dimension-three onset, the annihilation/revival curvature, or an unbounded positive-denominator local ratio for every fixed condition number.

### Equivalent formulations

Aliases through function-value monotonicity, overshoot, restart, spectral polynomials, and semi-iterative recurrences were compared.

### Broader coverage

General nonmonotonicity does not imply the exact minimal-dimensional objective frontier.

### Exact database or table

A finite database cannot settle a theorem uniform in every condition number.

### Claim versus prior implication

The classical recurrence does not itself state the sharp dimensional barrier.

**Checked sources.** https://doi.org/10.1007/s10957-023-02261-w; https://web.stanford.edu/~boyd/papers/pdf/restart_fgm.pdf; published corpus search

**Residual risks.** Older semi-iterative or polynomial-acceleration literature may contain an equivalent observation under different terminology.

## Value — PASS

The theorem gives a sharp structural boundary for local objective descent under perfectly calibrated acceleration and isolates the exact interior-mode mechanism behind objective spikes.

**Checked sources.** Hagedorn--Jarre 2024; restart literature

**Residual risks.** It is a local monotonicity theorem, not a global-rate improvement.

## Limitations

- Exact arithmetic, exact spectral endpoints, classical constant momentum, and standard zero-momentum initialization are essential.
- The unbounded quantity is a local relative objective ratio, not divergence or absolute blow-up.
- Other accelerated, restarted, composite, stochastic, inexact, and time-varying schemes are outside scope.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
