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

For \(0<\alpha<1\), \(a>0\), and \(r\ge0\), the exact image distance is
\[
D_a(r)=\max\{r,a^{1-\alpha}r^\alpha\}.
\]
Thus the additive defect is \(E_a(r)=D_a(r)-r\). It is zero for \(r\ge a\), positive for \(0<r<a\), and its positive branch has derivative
\[
\alpha a^{1-\alpha}r^{\alpha-1}-1.
\]
The derivative vanishes once, at \(r_*=\alpha^{1/(1-\alpha)}a\), changes sign from positive to negative, and therefore gives the global maximum. Substitution yields
\[
E_a(r_*)=(1-\alpha)\alpha^{\alpha/(1-\alpha)}a.
\]
With \(a=\varepsilon/((1-\alpha)\alpha^{\alpha/(1-\alpha)})\), this equals \(\varepsilon\) and
\[
r_*=\frac{\alpha}{1-\alpha}\varepsilon.
\]
Representative numerical evaluations for several \(\alpha\) and \(\varepsilon\) values agree with the analytic maximizer and maximum.

The structural verification is theorem-based: the chosen gauge is nontrivial because \(\omega_\alpha(t)/t\to\infty\) as \(t\downarrow0\), so the associated free space is Schur; and any isometric embedding of a separable Banach source into a Banach target would force a linear isometric copy in that target. Since Schur is inherited by subspaces, a non-Schur \(X\) cannot embed isometrically into this target.

Limits: no independent audit has been performed; no claim is made outside separable real non-Schur sources or outside \(0<\alpha<1\).
