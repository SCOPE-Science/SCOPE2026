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
A=F'(0)
=
[u_1\ \cdots\ u_k\ B]
\]
for an origin-preserving holomorphic map
\[
F:\Delta^k\times\mathbb B^m\to\mathbb B^{k+m}.
\]
The line Schwarz lemma gives
\[
\|A(z,w)\|_2
\le
\max\{\|z\|_\infty,\|w\|_2\}.
\]

For every unit vector \(v\in\mathbb C^m\), averaging
\[
\left\|
\sum_{j=1}^k\varepsilon_j u_j+\eta Bv
\right\|_2^2
\le1
\]
over independent unit phases gives exactly
\[
\sum_{j=1}^k\|u_j\|_2^2+\|Bv\|_2^2\le1.
\]
Thus, with
\[
s=\sum_{j=1}^k\|u_j\|_2^2,
\]
\[
\|B\|_{\mathrm{op}}^2\le1-s.
\]

Hadamard and AM-GM then give
\[
|\det A|^2
\le
\left(\frac{s}{k}\right)^k(1-s)^m.
\]
Differentiating the logarithm shows that the unique interior maximizer is
\[
s=\frac{k}{k+m},
\]
and substitution gives
\[
|\det A|^2
\le
\frac{m^m}{(k+m)^{k+m}}.
\]

The linear map
\[
L(z,w)
=
(k+m)^{-1/2}
(z_1,\ldots,z_k,\sqrt m\,w)
\]
maps the whole product into the Euclidean unit ball and has determinant squared exactly equal to the upper bound.

Finally,
\[
\mathbb B^{k+m}
\subset
\Delta^k\times\mathbb B^m
\subset
\Delta^{k+m}
\]
and the exact endpoint Kobayashi–Eisenman values are both \(1\), so the mixed-product value is \(1\) as well.

Every step is exact. No sampled determinant optimization, finite enumeration, or asymptotic extrapolation is used as proof.
