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

The final claim was checked by an independent reconstruction of its algebraic proof from the definition. No computational certificate is required.

For finite \(I\), set \(A=\lVert x+y\rVert_1\) and \(B=\lVert x-y\rVert_1\). Splitting \(u_i=\min(|x_i|,|y_i|)\) by the sign of \(x_i y_i\) gives exact sums \(P\) and \(N\), from which
\[
A+B=4-2(P+N),\qquad |A-B|=2|P-N|
\]
and hence
\[
\min\{A,B\}=2-2\max\{P,N\}.
\]
If \(m(x)>0\), assuming both \(P<m(x)\) and \(N<m(x)\) forces \(u_i=|y_i|\) on every nonzero coordinate of \(y\), so \(1=P+N<2m(x)\le1\), a contradiction. Thus one shifted norm is at most \(2(1-m(x))\), while the other is at most \(2\). Monotonicity and symmetry of the generalized mean give the claimed upper bound, and \(y=\operatorname{sgn}(x_j)e_j\) at a minimum-modulus coordinate gives equality. The \(m(x)=0\) case is included by the same witness.

For infinite \(I\), every \(x\in\ell_1(I)\) has \(\inf_i|x_i|=0\). Coordinate-vector witnesses have shifted norms \(2\) and \(2(1-|x_i|)\), which approach \(2\) simultaneously; the triangle inequality supplies the matching universal upper bound.

The conventions at \(t=0\) and \(t=-\infty\) are checked directly. For finite negative \(t\), any zero shifted norm is handled by the continuous extension of the power mean; the maximizing witness itself has two positive shifted norms because \(|I|\ge2\) implies \(m(x)\le1/2\).

Limits: the proof is real-valued and does not establish the complex \(\ell_1\) analogue or any formula for general \(L_1\) spaces.
