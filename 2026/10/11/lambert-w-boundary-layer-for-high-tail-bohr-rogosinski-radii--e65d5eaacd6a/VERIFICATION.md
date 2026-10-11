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

The cited sharp radius is the unique root of
\[
p\frac{1-r^m}{1+r^m}
=
\frac{2r^N}{1-r}.
\]

For fixed
\[
0<r<1,
\]
the left side decreases with \(r\), while
\[
r^N/(1-r)
\]
increases. Hence the root is unique and the defining function is strictly decreasing.

Increasing \(N\) decreases \(r^N\) at every fixed interior \(r\). Therefore the root increases strictly with \(N\). A limiting value below \(1\) contradicts the exact equation, so the roots tend to \(1\).

Writing
\[
\varepsilon=1-r,
\qquad
x=N\varepsilon,
\]
the exact equation gives
\[
(1-\varepsilon)^N
=
\frac{pm}{4}\varepsilon^2
\bigl(1+O(\varepsilon)\bigr).
\]
Taking logarithms before making any exponential approximation yields
\[
N[-\log(1-\varepsilon)]
=
2\log(1/\varepsilon)+O(1).
\]
This forces
\[
x\to\infty
\]
and
\[
x=O(\log N).
\]
Consequently,
\[
N\varepsilon^2
=
x^2/N
\to0.
\]

It is now justified to write
\[
(1-\varepsilon)^N=e^{-x}(1+o(1)).
\]
Thus
\[
x^2e^x
=
\frac{4N^2}{pm}(1+o(1)),
\]
and hence
\[
\frac{x}{2}e^{x/2}
=
\frac{N}{\sqrt{pm}}(1+o(1)).
\]
Inverting with the principal Lambert function gives
\[
x
=
2W\!\left(\frac{N}{\sqrt{pm}}\right)+o(1).
\]

Finally,
\[
W(y)=\log y-\log\log y+o(1)
\]
implies
\[
N(1-R_{m,N}^{(p)})
=
2\log N
-
2\log\log N
-
\log(pm)
+
o(1).
\]

The numerical checks performed during verification were consistency checks only; no finite computation is used to establish the infinite asymptotic statement.
