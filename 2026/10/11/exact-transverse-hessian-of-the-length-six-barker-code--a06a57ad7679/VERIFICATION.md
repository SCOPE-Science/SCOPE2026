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

The verification target is the aperiodic base energy
\[
E(\theta)=\sum_{k=1}^{5}\left|\sum_{j=0}^{5-k}e^{i(\theta_{j+k}-\theta_j)}\right|^2
\]
at \(\theta_*=(0,0,\pi/3,\pi,0,4\pi/3)\).

`verify.py` uses only the Python standard library and exact arithmetic. It represents \(\mathbb Z[\zeta]\), where \(\zeta=e^{i\pi/3}\) and \(\zeta^2-\zeta+1=0\), as pairs \(a+b\zeta\). It checks that every nonzero aperiodic sidelobe has squared modulus \(1\), so \(E(\theta_*)=5\). It then evaluates the exact differentiated formulas for the gradient and Hessian, recovering
\[
\begin{pmatrix}
4&-6&-1&2&3&-2\\
-6&10&0&-3&-4&3\\
-1&0&4&-2&-3&2\\
2&-3&-2&4&0&-1\\
3&-4&-3&0&10&-6\\
-2&3&2&-1&-6&4
\end{pmatrix}.
\]
It verifies that the common-phase and linear-phase vectors span a two-dimensional kernel. Finally it expands \(\det(\lambda I-H)\) by an exact permutation determinant and checks
\[
\det(\lambda I-H)=\lambda^2(\lambda-1)(\lambda-5)(\lambda-9)(\lambda-21).
\]

No random search, floating-point eigenvalue computation, or finite sampling is used as proof. The local-minimum conclusion is analytic: the functional is smooth, invariant along the two kernel directions, and has positive-definite Hessian on their orthogonal complement. The verification does not address global optimality among all phase vectors.
