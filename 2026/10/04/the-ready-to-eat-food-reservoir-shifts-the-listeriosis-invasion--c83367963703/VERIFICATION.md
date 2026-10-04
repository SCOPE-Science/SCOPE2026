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
The primary model equations, food-total constraint, and disease-free proposition were checked against the published full text.

The general proof is symbolic. For \(q=p_f-\alpha_4F>0\), the characteristic cubic of the infected/environmental block is expanded explicitly and the Routh–Hurwitz conditions are verified algebraically from \(\mathcal R_F<1\). If \(\mathcal R_F>1\), the constant term is negative and continuity forces a positive real root.

The bundled verifier uses exact rational arithmetic for the concrete witness. It checks that the published zero-food point has nonzero food derivative, that the clean-food point satisfies the equilibrium equations, that the published and corrected thresholds are \(1/3\) and \(4/3\), respectively, and that the cubic is \(\lambda^3+5\lambda^2+6\lambda-1\).

No global-stability, endemic-equilibrium, or critical \(p_f=\alpha_4F\) assertion is verified or claimed.
