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

The verification is analytic.

1. The source Hamiltonian is invariant under the quarter-turn \(R\) and is decomposed into quasi-momentum fibers. The rotation unitary takes the fiber at \(k\) to the fiber at \(Rk\), giving exact spectral equality and hence \(E(U,Rk)=E(U,k)\).
2. Where \(E(U,\cdot)\) is \(C^2\), the chain rule yields \(R^{\mathsf T}\nabla E(U,Rk)=\nabla E(U,k)\) and \(R^{\mathsf T}H_U(Rk)R=H_U(k)\).
3. Orthogonality of \(R\) gives \(H_U(Rk)=R H_U(k)R^{\mathsf T}\); when the Hessian is nonsingular, inversion gives the identical covariance law for \(m_U\).
4. With \(A=\begin{pmatrix}a&b\\b&c\end{pmatrix}\), exact multiplication gives \(RAR^{\mathsf T}=\begin{pmatrix}c&-b\\-b&a\end{pmatrix}\). Therefore \((A+RAR^{\mathsf T})/2=(\operatorname{tr}A/2)I_2\).
5. The torus classes \(K_x=[(\pi,0)]\) and \(K_y=[(0,\pi)]\) satisfy \(K_y=RK_x\), so step 4 applies to their Hessians and, conditionally on invertibility, to their mass tensors.

Limits: differentiability is not asserted outside the source's regularity hypotheses; tensor masses are not asserted when the Hessian is singular; equal physical valley occupation and higher-order isotropy are not proved. No finite computation is used to infer any of these infinite or operator-level statements.
