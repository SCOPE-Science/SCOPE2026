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

The primary source definition allows a semistability witness in any positive degree \(n\). In the example, \(x\) itself is the degree-\(m\) witness:
\[
\rho(x)=x\otimes\chi^m.
\]

Restriction to the ineffective kernel gives
\[
r_\Delta(\chi)=u,\qquad u^m=1,\qquad u\neq1.
\]
Thus the exact relation proved by the source argument,
\[
r_\Delta(\chi)^n=1,
\]
holds for \(n=m\) without the asserted stronger conclusion.

The full weight decomposition is
\[
A^{G,\chi^n}=
\begin{cases}
\mathbf Cx^d,&n=md,\\
0,&m\nmid n.
\end{cases}
\]
Therefore the semistable locus is exactly \(D(x)\), and the graded quotient ring is \(\mathbf C[x]\) with \(\deg x=m\), whose Proj is one point.

For the numerical condition, a one-parameter subgroup with exponent \(q\) yields
\[
x\longmapsto x\otimes t^{mq}.
\]
A polynomial coextension exists exactly when \(q\ge0\), and then
\[
\langle\chi,\lambda\rangle=q\ge0.
\]
Hence the example fails the stated criterion solely through the extra triviality requirement on \(r_\Delta(\chi)\).

No computational experiment or exhaustive enumeration is needed. The proof is uniform for every integer \(m\ge2\). It does not establish a complete replacement theorem for arbitrary superschemes.
