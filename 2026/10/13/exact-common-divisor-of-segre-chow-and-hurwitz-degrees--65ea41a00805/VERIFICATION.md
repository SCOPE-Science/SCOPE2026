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
Let
\[
d=a+b,
\qquad
C=\binom{d}{a}.
\]
The Segre intersection ring gives
\[
\deg(X)=C.
\]
Adjunction for a general curve section and the general Hurwitz-degree theorem give
\[
H=\frac{2ab}{d}C.
\]

If
\[
q=\frac{d}{\gcd(d,2ab)},
\]
then \(2ab/d\) has reduced denominator \(q\). Since \(H\) is integral,
\[
q\mid C,
\]
and therefore
\[
\gcd(C,H)=\frac{C}{q}
=
\frac{C\gcd(d,2ab)}{d}.
\]

For \(a=1\),
\[
(C,H)=(b+1,2b),
\]
so they are coprime exactly when \(b\) is even. If \(a,b\ge2\), then
\[
C\ge\binom d2>d\ge q,
\]
so \(C/q>1\).

The bundled checker evaluates these identities exactly for all
\[
1\le a,b\le200.
\]
Finite checks are not used as proof of the infinite theorem.
