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
The bundled checker uses exact rational arithmetic.

For
\[
a=\frac{37}{2},\quad
b=\frac{19}{2},\quad
c=d=e=1,\quad
f=2,\quad
\alpha=2,\quad
\beta=1,
\]
it verifies
\[
(H^*,P^*)=(1,16),
\]
the weak-Allee inequality, and the source's sufficient coexistence inequalities.

It checks that both equilibrium exponents vanish exactly and reconstructs
\[
J^*
=
\begin{pmatrix}
-4&-\frac12\\
8&1
\end{pmatrix}.
\]
Hence
\[
T=-3,\qquad D=0,
\]
with exact characteristic polynomial
\[
\lambda(\lambda+3).
\]

The checker then verifies that the source's printed source alternative
\[
|T|>D+1
\]
is true, its printed saddle inequality is also true, the corrected saddle condition is true, and the corrected source condition is false.

The general trace-determinant classification is proved analytically in the report; the checker certifies the exact model-realizable witness.
