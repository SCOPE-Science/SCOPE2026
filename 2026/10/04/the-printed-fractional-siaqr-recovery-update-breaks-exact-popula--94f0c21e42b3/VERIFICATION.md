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
The analytical conservation identity is exact:
\[
g_1+g_2+g_3+g_4+g_5=0.
\]

The numerical witness uses
\[
\gamma=\frac12,\qquad
\Delta t=1,\qquad
N=1,\qquad
\delta=\omega=\frac12,
\]
and the exact invariant history
\[
I=A=Q=0,\qquad S=1-R,
\qquad
R(t)=e^t\operatorname{erfc}(\sqrt t).
\]

At \(m=2\), the printed recurrence has correction coefficients
\[
C_2=\frac{4}{\Gamma(5/2)}
\]
and
\[
C_3=\frac{17}{2\Gamma(7/2)}.
\]
Because the erroneous recovery corrections are evaluated on \(Q=0\), the remaining total-population change is
\[
C_2(R_1-R_0)+C_3(R_2-2R_1+R_0).
\]

The bundled checker evaluates this expression at 80-digit precision and verifies
\[
\Delta N_3
\approx
-0.49207893684378897699,
\]
hence
\[
N_3
\approx
0.50792106315621102301.
\]

The checker is a replay of the explicit witness. The general cancellation and the source of its failure are established algebraically.
