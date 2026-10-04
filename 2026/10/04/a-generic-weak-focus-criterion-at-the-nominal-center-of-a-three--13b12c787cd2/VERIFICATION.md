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

The verification reconstructs the nonlinear local calculation from the published vector field.

Checks performed:

1. At \((a,b,c,d)=(5,50,-6,13)\), the shifted equilibrium is
\[
S_3=\left(50,0,-\frac{300}{13}\right).
\]

2. The exact shifted Jacobian is formed and its characteristic polynomial is checked to factor as
\[
(\lambda+13)\left(\lambda^2+\frac{109500}{169}\right),
\]
so
\[
\omega=\frac{10\sqrt{1095}}{13}.
\]

3. The quadratic bilinear form corresponding to \((-YZ,XZ,XY)\) is built directly. A center eigenvector \(q\) and adjoint eigenvector \(p\) are solved exactly and normalized by \(q_3=1\) and \(\langle p,q\rangle=1\).

4. The standard cubic center-manifold focal expression
\[
\frac{1}{2\omega}\operatorname{Re}\left\langle p,
-2B\!\left(q,A^{-1}B(q,\bar q)\right)
+B\!\left(\bar q,(2i\omega I-A)^{-1}B(q,q)\right)
\right\rangle
\]
is evaluated with exact symbolic arithmetic. The result is
\[
\ell=\frac{51590875683243\sqrt{1095}}{7747903716039146000}>0.
\]

5. The independent sign factor at the same parameter set,
\[
-abc(b^2-d^2),
\]
is checked to be positive, agreeing with the general factorization.

The bundled `verify.py` requires Python with SymPy and prints `VERIFY_OK` when all exact checks pass.

Limits: the checker verifies the source parameter example and the local normal-form calculation. It does not integrate trajectories, classify the remote two-scroll attractor, or resolve the exceptional cubic-degenerate surfaces \(a=0\) and \(b^2=d^2\).
