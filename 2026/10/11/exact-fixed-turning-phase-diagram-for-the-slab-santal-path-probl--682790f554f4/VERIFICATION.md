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

For
\[
S_p(w)=\sqrt{4p^2+w(1-w)^n},
\]
the optimized endpoint bound is
\[
F_n(a,p)
=
2p\log\frac1a+
\int_{-a}^{1}\frac{(1-w)^n}{S_p(w)+2p}\,dw.
\]
Differentiation gives
\[
\partial_pF_n(a,p)
=
2\log\frac1a
-
2\int_{-a}^{1}
\frac{(1-w)^n}{S_p(w)(S_p(w)+2p)}\,dw
=
2\Psi_n(a,p).
\]
The denominator in the last integral strictly increases with \(p\), so \(\Psi_n(a,p)\) strictly increases and \(F_n(a,p)\) is strictly convex.

The characteristic contact formulas are
\[
\rho(P_-)
=
-\frac12\Psi_n(a,p),
\qquad
\rho(P_+)
=
\frac12\Psi_n(a,p).
\]
Thus the unique post-threshold critical momentum makes both contacts equal to
\[
(\sqrt a,-\sqrt a),
\]
and calibration makes the bound sharp.

For the endpoint asymptotics, with
\[
L_a=\log\frac1a,
\qquad
C_a=\frac{(1+a)^{n+1}}{n+1},
\]
uniform expansion at large \(p\) gives
\[
\Psi_n(a,p)
=
L_a-\frac{C_a}{8p^2}+O(p^{-4})
\]
and
\[
F_n(a,p)
=
2pL_a+\frac{C_a}{4p}+O(p^{-3}).
\]
At the unique root, this yields the two limits in the finding.

The bundled checker uses only standard-library numerical quadrature. It samples separated dimensions and turning parameters, reconstructs the unique optimized momentum, checks monotonicity of \(\Psi_n\), checks the derivative identity by centered differences, and verifies convergence toward the analytic endpoint constants.

The numerical checks do not establish any infinite statement; they only replay representative consequences of the analytic proof.
