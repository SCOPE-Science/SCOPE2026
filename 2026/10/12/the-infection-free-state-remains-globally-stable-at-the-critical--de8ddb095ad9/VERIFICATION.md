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
The critical endpoint theorem is analytic.

Let
\[
a=d_2+pC_0>0,
\qquad
b=d_3+qA_0>0.
\]
At \(\mathcal R_0=1\), the infection characteristic equation is
\[
F(z)=(z+a)(z+b)-ab e^{-z\tau}.
\]
Then
\[
F(0)=0,
\]
and
\[
F'(0)=a+b+ab\tau>0.
\]
Hence zero is a simple characteristic root.

The bundled checker replays these identities with exact rational arithmetic for a positive witness and verifies the invariant-set chain
\[
T=T_0\text{ and }\dot T=0\Longrightarrow V=0,
\]
followed by
\[
V=0\text{ and }\dot V=0\Longrightarrow I=0.
\]

The finite checker does not establish the delay-system convergence. Global asymptotic stability follows from the source Lyapunov derivative together with the invariant-set proof in `RESULT.md`.
