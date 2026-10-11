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

Let \(\mathcal H=\ell^2(\mathbb N;\mathbb C)\), with orthonormal basis \((e_j)_{j\ge1}\), and set \(\Lambda_j f=\Gamma_j f=f_j\). Then
\[
\sum_j|\Lambda_j f|^2=\sum_j|\Gamma_j f|^2=\|f\|^2,
\qquad
\sum_j\Lambda_j^*\Gamma_jf=f.
\]
Thus \(\Lambda,\Gamma\) are alternate dual Parseval \(g\)-frames.

For every \(j\), use singleton local vectors \(\varphi_{j,1}=1/j\) and \(\phi_{j,1}=j\). Their optimal local frame bounds are \(j^{-2}\) and \(j^2\), and both local dual reconstruction identities hold exactly. Hence their block reconstruction operator is \(Q=I\), a bounded operator.

The induced vectors are
\[
\Lambda_j^*\varphi_{j,1}=e_j/j,
\qquad \Gamma_j^*\phi_{j,1}=j e_j.
\]
Testing \(e_N\) yields squared energies \(N^{-2}\) and \(N^2\), proving respectively the absence of a positive global lower bound and a finite Bessel upper bound. More strongly, \(f=(1/j)_{j\ge1}\in\ell^2\) gives
\[
\sum_j|\langle f,j e_j\rangle|^2=\infty.
\]
Formal scalar reconstruction remains valid, but two alternate dual *frames* do not exist.

Under common local upper bounds \(D_\varphi,D_\phi<\infty\), the induced sequences have Bessel bounds \(D_\varphi B_\Lambda,D_\phi B_\Gamma\). Their mixed synthesis/analysis composition coincides with \(\sum_j\Lambda_j^*\Gamma_j\). Hence the repaired equivalence holds.

For arbitrary positive scalars \(a_j\), testing coordinate basis vectors proves that both induced diagonal sequences \((a_j e_j)\) and \((a_j^{-1}e_j)\) are frames exactly when \(0<\inf_j a_j\le\sup_j a_j<\infty\). Truncated examples provide the exact finite bounds \(N^{-2}\) and \(N^2\), but the infinite conclusion follows from the quantified basis-vector argument and is not inferred from finite computation.

The target source was inspected directly at its definitions, Theorem 6.1, Corollary 6.2, and relevant proofs. Earlier common-local-bound frame-system theorems were compared separately. No independent audit has been performed.
