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

The proof was checked symbolically from the displayed matrices.

For \(B=\begin{pmatrix}1&1\\0&1\end{pmatrix}\) and \(C=\begin{pmatrix}1&0\\1&0\end{pmatrix}\), characteristic \(2\) gives \([B,C]=B\). Hence their span is Lie closed.

For \(M(s,t)=\begin{pmatrix}s+t&s\\t&s\end{pmatrix}\) and \(v=(x,y)^{\mathsf T}\), the linear map \((s,t)\mapsto M(s,t)v\) has coefficient matrix \(\begin{pmatrix}x+y&x\\y&x\end{pmatrix}\) and determinant \(x^2\). Therefore all \(x\ne0\) directions are surjective, while the \(x=0\) direction has image \(k(1,1)^{\mathsf T}\). This proves the exact hull equation.

The matrices \(X=\begin{pmatrix}0&1\\0&1\end{pmatrix}\) and \(Y=\begin{pmatrix}0&0\\1&0\end{pmatrix}\) satisfy the hull equation, whereas \([X,Y]=\begin{pmatrix}1&0\\1&1\end{pmatrix}\) does not.

No computer enumeration is needed for the theorem. No claim is made for odd positive characteristic or for local derivation algebras of a specific algebra.
