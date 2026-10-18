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

# Reproducibility and verification

The analytic claim is checked through the following identities: radial monomial diagonalization; the exact likelihood ratio \(d\mu_{k+1}/d\mu_k=r^2/m_k\); total-variation duality and its sign-threshold optimizer; strong concavity of the radial log-density; the local Gaussian expansion with curvature \(2\gamma+\gamma'\); and periodic phase inversion. Their details and quantifiers appear in RESULT.md.

Run the standalone standard-library checker with `python sensitivity_checker.py`. It uses centered Simpson quadrature for a nonconstant sinusoidal curvature tail and evaluates the sharp moment-law total-variation norm, then checks the predicted periodic coefficient and phase inversion. It reports 25 finite diagnostic groups. The actual global smooth cutoff is immaterial to these large-degree centered moments because the integration interval lies entirely inside the identical periodic tail; the omitted lower-radius contribution is exponentially negligible by the proved strong-concavity bound. Numerical agreement is supplementary evidence, not a substitute for the uniform asymptotic proof.

The checker does not validate all \(k\), all admissible curvature profiles, all bounded radial symbols, or scientific priority. The optimization over bounded symbols is proved by exact measure duality; full asymptotics are proved by estimates. Independent audit and external validation have not been performed.
