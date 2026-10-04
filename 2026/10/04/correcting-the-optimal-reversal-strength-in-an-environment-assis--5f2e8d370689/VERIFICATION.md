---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The source formulas were independently reduced to
\[
C_3(y)=\frac{2r\sqrt y}{r+y},
\qquad
P_3(y)=\frac{r+y}{2},
\]
with
\[
r=1-d,
\qquad
y=1-q.
\]
The analytic derivative
\[
\frac{dC_3}{dy}
=
\frac{r(r-y)}{\sqrt y(r+y)^2}
\]
gives the unique maximum and the exact Pareto split.

`verify_scheme3_optimum.py` reconstructs the concurrence from the representative postselected \(X\)-state, checks the derivative sign on a deterministic grid, verifies the strict domination of the published point for representative damping strengths, and checks the closed Pareto formula. It prints `VERIFY_OK`.

The finite replay is supplementary. The general claim follows from the exact derivative and algebraic inequalities in `RESULT.md`.

The direct primary full text was inspected at the equations containing the claimed optimum. No independent audit has been performed.
