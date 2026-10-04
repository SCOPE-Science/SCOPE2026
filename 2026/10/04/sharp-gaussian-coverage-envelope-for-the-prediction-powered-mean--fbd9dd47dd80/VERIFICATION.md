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

The proof is analytic. It checks the exact Gaussian decomposition, independence of the numerator and sample variances, strict concavity of \(h_z(q)=2\Phi(z\sqrt q)-1\), the coefficient-averaging convex-order argument for the upper endpoint, and the leave-one-out convex-order argument for the lower endpoint.

`verify.py` recomputes the numerical example from the Student distribution using a self-contained incomplete-beta implementation. It verifies the values \(0.9183555945395834\), \(0.9474279305425579\), and \(0.9500042097035590\) for \(n=10\), \(N=100\), and \(z=1.96\), and checks the balance-weight identity. Numerical replay does not certify the general theorem; the displayed proof does.

The theorem does not establish non-Gaussian coverage bounds, does not cover data-dependent predictors fitted on the same inference observations, and does not replace an independent audit.
