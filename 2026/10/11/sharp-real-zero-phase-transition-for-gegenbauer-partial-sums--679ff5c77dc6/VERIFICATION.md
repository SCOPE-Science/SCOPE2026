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

Fix
\[
0<\alpha<1.
\]

For
\[
x=\cos\theta
\]
with \(\theta\) bounded away from
\[
0
\quad\text{and}\quad
\pi,
\]
the uniform ultraspherical expansion has leading amplitude
\[
b_k
=
\frac{(2\alpha)_k}{(\alpha+1)_k}.
\]
Its exact ratio is
\[
\frac{b_{k+1}}{b_k}
=
\frac{k+2\alpha}{k+\alpha+1}
<
1,
\]
and
\[
b_k\asymp k^{\alpha-1}\to0.
\]

Uniform Dirichlet summation therefore yields
\[
\sum_{k>n}
b_ke^{ik\theta}
=
O(n^{\alpha-1}).
\]
The asymptotic remainder sums to the same order because
\[
\sum_{k>n}k^{\alpha-2}
=
O(n^{\alpha-1}).
\]
Hence
\[
S_n^{(\alpha)}(x)
=
(2-2x)^{-\alpha}
+
O_K(n^{\alpha-1})
\]
uniformly on every compact
\[
K\subset(-1,1).
\]

The exact derivative identity is
\[
\left(S_n^{(\alpha)}\right)'
=
2\alpha S_{n-1}^{(\alpha+1)}.
\]
Since
\[
\alpha+1>1,
\]
the primary theorem puts all derivative zeros in
\[
(-1,1)
\]
for sufficiently large \(n\), and their normalized counting measures converge to
\[
\frac{dx}{\pi\sqrt{1-x^2}}.
\]

For any fixed
\[
\delta>0,
\]
the original polynomial is eventually positive on
\[
[-1+\delta,1-\delta].
\]
Rolle counting therefore gives
\[
R_n(\alpha)
\le
N_{n-1}^{(\alpha+1)}
\left(
(-1,-1+\delta)\cup(1-\delta,1)
\right)
+
3.
\]
The constant three accounts for the two connected edge intervals and at most one negative exterior root. There are no positive exterior roots.

Dividing by \(n\), using the arcsine zero-density theorem, and then letting
\[
\delta\downarrow0
\]
gives
\[
R_n(\alpha)/n\to0.
\]

No numerical sampling or finite-degree extrapolation is used.
