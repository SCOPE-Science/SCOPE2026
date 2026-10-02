---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For the balanced-viscosity sheared Fourier Green system in the cited micropolar Couette problem, every fixed nonzero streamwise mode has an exact parabolic-cylinder fundamental matrix; both singular values have cubic decay exponent \(-A^2\xi^2/3\), while their ratio has an explicit quadratic-in-time exponential splitting. The streamwise-zero mode has the stated elementary hyperbolic formula.

## Correctness — PASS

Starting from the assigned source matrix \(B(t)=\begin{psmallmatrix}-q&q\\1&-q-2\end{psmallmatrix}\), the change \(y=e^Q\omega\), \(Q'=q+1\), gives \(y''=(q+1)y\). For \(\xi\ne0\), the quadratic \(q\) converts exactly to Weber's equation. The nonzero Wronskian gives a fundamental pair, reconstruction gives the displayed \(2\times2\) matrix, Liouville gives determinant \(e^{-2Q}\), and standard parabolic-cylinder asymptotics plus the determinant give the two singular-value laws. The actual verification script was inspected; its symbolic reduction, ODE comparisons and determinant checks corroborate but do not replace the proof.

**Checked sources.** Qi and Yu, arXiv:2609.20109v1, full primary text; assigned RESULT.md and actual verification script; NIST DLMF Chapter 12; Wang--Li 2026 DCDS-B; Tao 2026 Mathematical Methods in the Applied Sciences

**Residual risks.** Uniform frequency asymptotics are not proved. The related Couette papers were inspected at abstract/method level rather than line-by-line for every calculation.

## Originality — PASS

The primary source writes the same sheared coefficient matrix and derives the equivalent scalar second-order equation, but then explicitly treats its solution through a Volterra/Gronwall estimate rather than recognizing the quadratic coefficient as Weber's equation. Targeted corpus and literature searches found no earlier closed parabolic-cylinder Green matrix or the quadratic singular-value splitting for this micropolar mode.

### Equivalent formulations

The equivalent scalar ODE is prior, but the special-function solution and singular-value asymptotics are not the same statement and are not mechanically supplied by the source's estimates.

### Broader coverage

These broader stability theorems control norms and decay but the inspected material does not give the exact fixed-mode Green formula or condition-number asymptotic.

### Exact database or table

No numerical table is relevant; the comparison is theorem-level.

### Claim versus prior implication

The new claim is the source-specific exact identification and the derived matrix/singular-value theorem; standard special-function theory is an ingredient rather than prior coverage of that theorem.

**Checked sources.** https://arxiv.org/abs/2609.20109; https://doi.org/10.3934/dcdsb.2025124; https://doi.org/10.1002/mma.70878; https://dlmf.nist.gov/12

**Residual risks.** An equivalent special-function calculation could be hidden in less directly indexed older fluid literature, although targeted searches did not locate one.

## Value — PASS

The result supplies an exact benchmark for a coupled variable-coefficient Green system that the motivating paper can only bound, and separates common cubic enhanced dissipation from a quantitative nonnormal quadratic splitting. That is a natural structural refinement relevant to sharper frequency-localized analysis.

**Residual risks.** The theorem is diagnostic at fixed frequency rather than a new nonlinear stability theorem.

## Limitations

- The special-function formula is for the balanced-viscosity normalization and fixed sheared frequency labels.
- The sharp singular-value constants are not uniform as \(\xi\to0\), and the result does not itself improve the nonlinear threshold.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
