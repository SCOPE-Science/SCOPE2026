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

Starting from the primary-source formula,
\[
C_*(A)-L
=
\left(\frac73-\frac1A\right)
\log\frac{A}{A-1}
+
\frac{\log3-2\log2-2}{A},
\]
set
\[
x=1/A.
\]
Then
\[
C_*(A)-L
=
\left(\frac73-x\right)(-\log(1-x))
+x(\log3-2\log2-2).
\]
Using the absolutely convergent series for
\[
-\log(1-x)
\]
gives
\[
C_*(A)-L
=
\frac{c_*}{A}
+
\sum_{n=2}^{\infty}
\frac{4n-7}{3n(n-1)}A^{-n},
\]
with
\[
c_*=\frac13+\log\frac34.
\]

For
\[
n\ge2,
\]
all higher coefficients are positive and at most
\[
5/18.
\]
This gives the explicit geometric-tail bound and proves
\[
A(C_*(A)-L)\to c_*.
\]

Because the full coefficient satisfies
\[
C(A,B)\ge C_*(A),
\]
every admissible realization within tolerance \(\varepsilon\) has
\[
A\ge c_*/\varepsilon+O(1).
\]
Squares of ratios of odd positive integers are dense in the positive reals. Choosing such an \(A\) just above the continuous threshold and an admissible \(B\) sufficiently close to the continuous minimizer proves the matching upper asymptotic.

Finally,
\[
\cos\Phi_0=1-\frac2A
\]
gives
\[
\Phi_0=2\arcsin(A^{-1/2}),
\]
and direct Taylor expansion of the exact source formula for \(B_{\min}\) yields
\[
B_{\min}(A)
=
\frac{12}{\pi^2}
+
\frac{96}{\pi^3}A^{-1/2}
+
O(A^{-1}).
\]

All checks are symbolic. Decimal constants are evaluations of exact expressions and are not used to establish any infinite statement.
