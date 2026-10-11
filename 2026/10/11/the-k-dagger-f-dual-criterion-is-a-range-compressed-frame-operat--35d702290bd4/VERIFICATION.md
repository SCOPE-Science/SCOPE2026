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

For a Bessel mapping \(F\), define
\[
S_Ff=
\int_\Omega \langle f,F(\omega)\rangle F(\omega)\,d\mu(\omega).
\]
If \(K\) has closed range, \(K^\dagger\) is bounded, so \(K^\dagger F\) is Bessel. Its reconstruction operator against \(F\) is
\[
f\longmapsto
\int_\Omega \langle f,K^\dagger F(\omega)\rangle F(\omega)\,d\mu(\omega)
=
S_F(K^\dagger)^*f.
\]
Thus it is a \(K\)-dual exactly when
\[
S_F(K^\dagger)^*=K.
\]

The Moore--Penrose identities give
\[
(K^\dagger)^*K^*=P_{R(K)}
\]
and
\[
K^*(K^\dagger)^*=P_{N(K)^\perp}.
\]
Therefore
\[
S_F(K^\dagger)^*=K
\]
implies
\[
S_FP_{R(K)}=KK^*.
\]
Conversely,
\[
S_FP_{R(K)}=KK^*
\]
implies
\[
S_F(K^\dagger)^*
=
KK^*(K^\dagger)^*
=
KP_{N(K)^\perp}
=
K.
\]

For the exact witness,
\[
H=\mathbb C,\qquad
K=\frac12I,\qquad
F(\omega_0)=1,
\]
on a one-point measure space of mass \(1\). Then
\[
\frac14\|f\|^2
=
\|K^*f\|^2
\le
\|f\|^2
=
\int_\Omega |\langle f,F(\omega)\rangle|^2\,d\mu(\omega),
\]
so the source's \(A=B=1\) inequalities hold. But
\[
K^\dagger=2I
\]
and
\[
S_F(K^\dagger)^*=2I\ne \frac12I=K.
\]

The publisher PDF was inspected as extracted text and as page images at Definition 2.2 and Lemma 3.2. The preprint was inspected independently. The later 2024 continuous \(K\)-frame paper was also inspected at its Parseval definition, where the stronger exact energy identity is explicitly stated.

No numerical experiment or finite enumeration is used.
