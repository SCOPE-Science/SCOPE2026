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
`verify.py` uses exact rational arithmetic and no third-party packages. It implements the standard conjugate-gradient recurrence from \(x_0=0\), verifies the explicit witness
\[
A=
\begin{pmatrix}
5&-1&0\\
-1&2&-1\\
0&-1&2
\end{pmatrix},
\qquad
b=(1,0,7)^\mathsf T,
\]
and checks
\[
x_2=
(-5/751,\ 1324/751,\ 6881/1502)^\mathsf T,
\qquad
A^{-1}b=(10/13,\ 37/13,\ 64/13)^\mathsf T.
\]

The checker also evaluates the claimed rational formula for the first component of \(x_2\) on multiple rational values of \(a>2/3\) and \(B\ge0\), comparing it directly with recurrence output. It verifies the displayed inverse by exact matrix multiplication and checks representative parameters on both sides of \(a=4\).

Finite replay does not establish the universal threshold. The proof in RESULT.md does: \(Q_a(B)>0\) follows from a positive quadratic form, all coefficients of \(N_a(B)\) are nonnegative when \(a\le4\), and the leading coefficient is negative when \(a>4\). The dimension-minimality argument is likewise analytic.
