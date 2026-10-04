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

The proof is exact.

For a simple boundary zero \(a\), write
\[
p(z)=(z-a)Q(z).
\]
Then
\[
\frac{p''(a)}{p'(a)}
=
2\frac{Q'(a)}{Q(a)}
=
2\sum_k\frac1{a-z_k}.
\]
Factoring \(p'\) by its critical points also gives
\[
\frac{p''(a)}{p'(a)}
=
\sum_j\frac1{a-\zeta_j}.
\]
Multiplying by \(a\) and using \(|a|=1\) yields the exact real-part formula
\[
\operatorname{Re}\sum_j\frac{a}{a-\zeta_j}
=
n-1+
\sum_k\frac{1-|z_k|^2}{|a-z_k|^2}.
\]

Cauchy--Schwarz then gives
\[
\sum_j\frac1{|a-\zeta_j|^2}
\ge
\frac{(n-1+\Delta_a(p))^2}{n-1}.
\]

Equality in Cauchy--Schwarz and in the real-part-to-modulus step forces every reciprocal critical coordinate to be the same positive real number. Hence all critical points coincide, and integrating \(p'\) gives
\[
p(z)=C\left((z-(1-r)a)^n-(ra)^n\right).
\]
The roots have the form
\[
a((1-r)+r\omega),
\qquad \omega^n=1,
\]
and
\[
|(1-r)+r\omega|^2
=
1-2r(1-r)(1-\operatorname{Re}\omega).
\]
Thus every root is in the unit disk exactly when \(0<r\le1\).

The repeated critical point in this family is \((1-r)a\), so the left side is exactly \((n-1)/r^2\), confirming sharpness directly.

No finite computation, numerical fitting, or unproved limiting argument is used.
