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

The proof uses the published two-upper-facet formula
\[
f_n(x,y)
=
\frac{2}{n}y^2
-
(n+2)\sqrt{\frac{2}{n(n+1)}}xy
+
2x^2
\]
together with the published bounds
\[
\sqrt{\frac{n+1}{2n}}x
-
\sqrt{\frac{n-1}{2n}}\sqrt{1-x^2}
\le y\le
\sqrt{\frac{n}{2(n+1)}}x.
\]

For fixed \(x\), convexity in \(y\) reduces the maximum to the two endpoints.

The upper endpoint is exactly
\[
f_n=x^2
\]
and feasibility forces
\[
x^2\le1-\frac1{n^2}.
\]

At the lower endpoint, set
\[
y=\sin\phi,
\qquad
x=
\sqrt{\frac{n+1}{2n}}\sin\phi
+
\sqrt{\frac{n-1}{2n}}\cos\phi.
\]
Then
\[
f_n
=
\begin{pmatrix}\sin\phi&\cos\phi\end{pmatrix}
M_n
\begin{pmatrix}\sin\phi\\\cos\phi\end{pmatrix},
\]
with
\[
M_n=
\begin{pmatrix}
1/n & \frac12\sqrt{\frac{n-1}{n+1}}\\
\frac12\sqrt{\frac{n-1}{n+1}} & (n-1)/n
\end{pmatrix}.
\]
Its top eigenvalue is
\[
\lambda_n
=
\frac12+
\frac1{2n}
\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}.
\]

The exact comparison
\[
(2\lambda_n-1)^2-
\left(1-\frac2{n^2}\right)^2
=
\frac{(n-1)(n^2-2n-2)^2}{n^4(n+1)}
\]
shows that this lower branch dominates the upper endpoint for every \(n\ge3\).

The positive top eigenvector also satisfies the strict second-facet visibility inequality. The explicit supporting-normal construction in `RESULT.md` then shows that every remaining facet is non-upper, so the eigenvalue is attained inside the intended chamber.

The embedded `verify.py` was replayed from its actual package path. It checks these identities and inequalities numerically for dimensions \(3\) through \(400\), verifies the \(n=5\) published specialization, the \(n\ge5\) threshold for beating \(2n\), and the normalized asymptotic limit.

The replay output was:

`VERIFY_OK reflected simplex two-upper-facet benchmark`

Finite checks are consistency tests only; the continuum and all-dimensional statements are proved analytically.
