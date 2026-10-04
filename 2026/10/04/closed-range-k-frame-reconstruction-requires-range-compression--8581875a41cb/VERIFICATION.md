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

The target is the closed-range reconstruction formula for a \(K\)-g-fusion-frame operator. The primary source defines
\[
S=\sum_jv_j^2P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}
\]
and states \(AKK^*\le S\). Its formula (2.10) applies \((S|_{R(K)})^{-1}\) directly to every \(f\in R(K)\).

The explicit check uses \(\mathcal H=\mathbb C^3\), \(K=P_{\operatorname{span}\{e_1\}}\), and two scalar analysis operators \(\Lambda_1x=x_1\), \(\Lambda_2x=x_1+x_2\). The coefficient energy is \(|x_1|^2+|x_1+x_2|^2\), so the lower \(K\)-bound is at least \(1\). The associated matrix is
\[
S=\begin{pmatrix}2&1&0\\1&1&0\\0&0&0\end{pmatrix},
\]
and therefore \(Se_1=2e_1+e_2\). Since \(R(K)=\operatorname{span}\{e_1\}\), the inverse of \(S|_{R(K)}:R(K)\to S(R(K))\) cannot be evaluated at \(e_1\).

For the corrected operator \(C=P_{R(K)}S|_{R(K)}\), the identity \((K^\dagger)^*K^*x=x\) for \(x\in R(K)\) gives
\[
\langle Cx,x\rangle\ge A\|K^*x\|^2\ge A\|K^\dagger\|^{-2}\|x\|^2.
\]
Thus \(C\) is positive, self-adjoint, onto, and boundedly invertible on \(R(K)\), with
\[
\|C^{-1}\|\le \|K^\dagger\|^2/A.
\]
Substitution verifies \(P_RSC^{-1}=I_R\) and \(C^{-1}P_RS|_R=I_R\).

Limits: the verification does not assert that \(S:R(K)\to S(R(K))\) fails to be invertible; later literature correctly states that range-to-range result. It also does not assert novelty over material unavailable to indexed search.
