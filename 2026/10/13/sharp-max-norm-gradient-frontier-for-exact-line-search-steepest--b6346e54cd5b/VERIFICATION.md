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
The universal proof is analytic. The checker replays equality constructions and the concrete witness.

The sharp claimed factor is
\[
C_{n,\kappa}
=
\sqrt{n-1}\,
\frac{\kappa-1}{2\sqrt\kappa}.
\]
The max-norm safety boundary is
\[
\kappa_{\infty,n}
=
\frac{\sqrt n+1}{\sqrt n-1}.
\]

For equality, choose orthonormal vectors \(u,v\) with \(u\) flat and \(v\) the normalized projection of \(e_1\) onto \(u^\perp\). On their span use
\[
\frac1{\kappa+1}
\begin{pmatrix}
2\kappa&-\sqrt\kappa(\kappa-1)\\
-\sqrt\kappa(\kappa-1)&\kappa^2+1
\end{pmatrix},
\]
and use the identity on the orthogonal complement. The two-plane block has trace \(1+\kappa\) and determinant \(\kappa\), so its eigenvalues are \(1,\kappa\). Starting from \(g=u\), exact line search gives
\[
g^+
=
\frac{\kappa-1}{2\sqrt\kappa}v.
\]

The embedded `verify.py` checks this construction numerically at several \((n,\kappa)\), checks the boundary equation, and reconstructs the displayed \(n=3\), \(\kappa=4\) witness. It verifies
\[
\alpha=\frac58,
\qquad
\frac{\|g^+\|_2}{\|g\|_2}=\frac34,
\qquad
\frac{\|g^+\|_\infty}{\|g\|_\infty}
=
\frac{3\sqrt2}{4}>1.
\]

Finite replay is corroborative only. The all-\(n\) claim rests on the projection inequality and explicit equality construction.

Unproved limits include inexact line searches, finite precision, nonquadratic objectives, higher-step path maxima, and Hessian classes with additional sparsity or sign restrictions.
