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
B=\|b\|_{A_1}<1
\]
and
\[
m=\widehat{|b|^2}(0).
\]
The \(SU(2)\) identity gives
\[
|a|^2
=
(1-m)(1+h),
\qquad
h
=
-\frac{|b|^2-m}{1-m}.
\]

Because the zero coefficient of \(|b|^2\) is \(m\ge0\),
\[
\||b|^2-m\|_{A_1}
=
\||b|^2\|_{A_1}-m.
\]
Using the Banach-algebra estimate
\[
\||b|^2\|_{A_1}\le B^2,
\]
one gets
\[
\|h\|_{A_1}
\le
\frac{B^2-m}{1-m}
\le B^2<1.
\]

Therefore
\[
\log(1+h)
\]
converges absolutely in \(A_1\), and
\[
\|\log|a|^2\|_{A_1}
\le
-\log(1-m)-\log(1-\|h\|_{A_1})
\le
-2\log(1-B^2).
\]

For the normalized outer factor,
\[
\|\log a\|_{A_1}
\le
2\|\log|a|\|_{A_1}
\le
-2\log(1-B^2).
\]
Hence
\[
\|a^{-1}\|_{A_1}
\le
\exp(\|\log a\|_{A_1})
\le
(1-B^2)^{-2}.
\]

The verified March 2026 proposition gives
\[
\|F\|_{\ell^1}
\lesssim
\varepsilon^{-1}\|b/a\|_{A_1}
\]
when
\[
B<1/\sqrt2-\varepsilon.
\]
Thus
\[
\|F\|_{\ell^1}
\lesssim
\frac{B}{\varepsilon(1-B^2)^2}.
\]

For every fixed
\[
\eta>0
\]
and
\[
B<1/\sqrt2-\eta,
\]
the right-hand side is bounded by a constant depending only on \(\eta\). This proves
\[
\tau\ge1/\sqrt2.
\]

No numerical computation or finite experiment is used.
