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

At a source-defined regular-Coulomb minimum, let
\[
a=a_{L,\eta,n},
\qquad
y=y_{L,\eta}(a),
\qquad
\nu=L+\frac12.
\]
The exact source equations are
\[
b
=
\frac{1-\eta/a}{1+y}
\]
and
\[
ya^2-\eta(2y+1)a+(1+y)(y^2-\nu^2)=0.
\]

Set
\[
\varepsilon=1/a,
\qquad
y=\varepsilon Y.
\]
The algebraic equation becomes
\[
Y-\eta
-
2\eta\varepsilon Y
+
\varepsilon(1+\varepsilon Y)
(\varepsilon^2Y^2-\nu^2)
=
0.
\]
At
\[
\varepsilon=0
\]
the root is
\[
Y=\eta,
\]
and the derivative with respect to
\[
Y
\]
equals one. The implicit-function theorem therefore applies and gives
\[
Y
=
\eta
+
(2\eta^2+\nu^2)\varepsilon
+
O(\varepsilon^2).
\]
Thus
\[
y
=
\frac{\eta}{a}
+
\frac{2\eta^2+\nu^2}{a^2}
+
O(a^{-3}).
\]

Substitution in the exact formula for
\[
b
\]
gives
\[
1-b
=
\frac{2\eta}{a}
+
\frac{\nu^2}{a^2}
+
O(a^{-3}).
\]

The independently checked Coulomb zero phase satisfies
\[
x_{L,\eta,n}
=
\pi n+\eta\log n+O(1).
\]
Because the minimizer lies between consecutive positive zeros,
\[
a_{L,\eta,n}
=
\pi n+\eta\log n+O(1).
\]
Consequently
\[
1-b_{L,\eta,n}
=
\frac{2\eta}{\pi n}
-
\frac{2\eta^2}{\pi^2}
\frac{\log n}{n^2}
+
O(n^{-2}).
\]

No numerical experiment, finite enumeration, or empirical fit is used to prove either asymptotic statement.
