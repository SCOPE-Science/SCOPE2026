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
# Verification

The checker represents a divisor as its ten coefficients in the basis
\[
H,E_1,\ldots,E_9
\]
with intersection matrix
\[
\operatorname{diag}(1,-1,\ldots,-1).
\]
It defines
\[
\delta=3H-E_1-\cdots-E_9,
\qquad
\alpha=E_1-E_2,
\]
and replays the Kac translation
\[
T_\alpha(\lambda)=\lambda+(\lambda\cdot\delta)\alpha-
\left(\frac12(\lambda\cdot\delta)\alpha^2+\lambda\cdot\alpha\right)\delta.
\]

The script checks on the full basis that the translation with \(-\alpha\) is an integral inverse. It verifies by exact integer arithmetic, for a replay range, that iteration agrees with the closed formula
\[
T_\alpha^m(L)=L+4m\alpha+4m^2\delta,
\]
and with the coefficient formula in `RESULT.md`. It also checks
\[
L_m^2=20,
\qquad
L_m\cdot\delta=4,
\qquad
H\cdot L_m=9+12m^2.
\]

The finite replay is only a consistency check. The universal formula for all \(m\ge0\) is proved symbolically by induction in `RESULT.md`; the geometric ampleness and Seshadri arguments depend on the cited theorems and the countable very-general construction, not on enumeration.

The saved replay output ends in `VERIFY_OK`.
