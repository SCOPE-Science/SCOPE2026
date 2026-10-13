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

The exact proof uses the Kenyon--Prause small-\(r\) coexistence boundary
\[
s(R)=\frac1{m_1}\sum_i\frac{\alpha_i^2}{R+\alpha_i^2},\qquad
 t(R)=\frac1{m_2}\sum_j\frac{\beta_j^2R}{1+\beta_j^2R},
\]
and evaluates \(\frac12-\int_0^1T(s)\,ds\) after the monotone change of variables \(s=s(R)\). The pair integral is elementary and yields the closed formula in `RESULT.md`.

`verify.py` numerically integrates the published parametric boundary for three admissible higher-period parameter sets and compares it with the closed formula. It also checks the simply-periodic specialization against direct numerical integration of the published hyperbolic boundary. The numerical tolerances are intentionally much weaker than machine precision because the quadrature only corroborates the analytic proof.

Limits: finite numerical quadrature does not establish the theorem and is not used to infer originality. The theorem itself assumes every \(\alpha_i\beta_j<1\); no numerical or analytic claim is made here for products equal to or above \(1\).
