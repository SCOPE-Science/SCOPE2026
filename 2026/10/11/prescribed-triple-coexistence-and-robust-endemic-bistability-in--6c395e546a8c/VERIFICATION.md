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
# Reproducibility and limits

The proof is analytic: nullcline elimination factors the coexistence condition exactly; the Jacobian determinant and trace determine local type; a quadratic sign test gives exactly one positive disease-free equilibrium; nonzero determinants permit the implicit function theorem in all parameters. Those arguments apply for every triple and every choice satisfying the displayed strict inequalities.

Run `python3 verify.py` using Python 3 standard-library `fractions.Fraction`; it prints `CHECK_OK` when the original differential equations vanish at each of the three exact equilibria and all rational Jacobians, traces and determinants match. The checker also verifies the factored nullcline expression at several rational test values. The proof, not those finitely many tests, establishes the general identity and quantifiers.

Local asymptotic stability is proved; global basin classification, periodic orbit exclusion, stability after adding diffusion, and empirical calibration are unproved. Independent audit is not performed.
