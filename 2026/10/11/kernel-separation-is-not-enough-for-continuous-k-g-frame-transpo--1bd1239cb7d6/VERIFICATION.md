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

The target journal PDF was inspected at the theorem statement and proof. The source assumes that \(U\) has closed range, \(UK=KU\), and \(R(K^*)\cap N(U^*)=\{0\}\), and then uses
\[
\|K^*f\|^2=\|UU^\dagger K^*f\|^2.
\]
Because \(UU^\dagger\) is the orthogonal projection onto \(R(U)\), this equality is valid for every \(f\) only when \(R(K^*)\subseteq R(U)\). The stated intersection condition does not imply that inclusion.

For the counterexample, every block is
\[
U_n=
\begin{pmatrix}
\lambda_n&a_n\\
0&0
\end{pmatrix},
\qquad
\lambda_n=\frac1{n+1},
\qquad
a_n=\sqrt{1-\lambda_n^2}.
\]
The block has singular values \(1\) and \(0\), and
\[
U_nU_n^*=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
Thus the direct sum is bounded with norm one and has closed range. Its adjoint sends the first coordinate unit vector to the unit vector
\[
v_n=\lambda_ne_n+a_nh_n
\]
and kills \(h_n\). The closed range \(R(U^*)\) is the orthogonal span of the \(v_n\), while \(N(U^*)\) is the orthogonal span of the \(h_n\); since every \(\lambda_n\) is positive, their intersection is zero.

With \(K=U\) and the one-point analysis operator \(\Lambda=K^*\),
\[
\|\Lambda f\|^2=\|K^*f\|^2\le\|f\|^2,
\]
so the original family is Parseval relative to \(K\). But
\[
(U^*)^2e_n=\lambda_nv_n,
\]
so
\[
\frac{\|(U^*)^2e_n\|^2}{\|K^*e_n\|^2}=\lambda_n^2\longrightarrow0.
\]
This proves failure of every positive lower bound without extrapolating from a finite computation.

For the repaired universal statement, define
\[
\delta(U,K)=\inf\{\|U^*x\|:x\in R(K^*),\ \|x\|=1\}.
\]
If \(\delta(U,K)>0\), the lower frame estimate follows from commutation. Conversely, universal preservation applied to the one-point family \(\Lambda=K^*\) forces exactly such a positive lower bound on \(U^*\) over \(R(K^*)\). The case \(K=0\) is trivial and was excluded only to avoid an empty unit-sphere infimum.
