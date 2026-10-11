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

Let
\[
M=\operatorname{span}\{e_1\}\subset\mathbb C^2,
\qquad
K=P_M,
\qquad
W_1=M,
\qquad
\omega_1=1,
\qquad
C=C'=I.
\]
For
\[
f=(f_1,f_2),
\]
one has
\[
\sum_i\omega_i^2\langle\pi_{W_i}Cf,\pi_{W_i}C'f\rangle
=
|f_1|^2
=
\|K^*f\|^2.
\]
Therefore the controlled \(K\)-fusion bounds are exactly
\[
A=B=1.
\]

The source coefficient space is
\[
M,
\]
and the analysis operator is
\[
T_{C,C'}=P_M:H\to M.
\]
For every \(x\in M\),
\[
\langle P_Mf,x\rangle_M=\langle f,x\rangle_H,
\]
so
\[
T_{C,C'}^*x=x.
\]
Hence
\[
R(T_{C,C'}^*)=M\ne H.
\]
The synthesis operator is not surjective, disproving the necessity direction of Theorem 10.

For the repair, the controlled lower frame inequality is
\[
A\|K^*f\|^2\le\|T_{C,C'}f\|^2,
\]
which is equivalent to
\[
A K K^*\le T_{C,C'}^*T_{C,C'}.
\]
Douglas range inclusion gives
\[
R(K)\subseteq R(T_{C,C'}^*).
\]
Conversely, this range inclusion gives the required operator domination and hence a positive lower controlled \(K\)-fusion bound.

The complete source theorem and proof, the operator definitions immediately preceding it, and the relevant primary range-inclusion literature were inspected. The earliest verified public version is arXiv:2007.05110v1, posted 9 July 2020.
