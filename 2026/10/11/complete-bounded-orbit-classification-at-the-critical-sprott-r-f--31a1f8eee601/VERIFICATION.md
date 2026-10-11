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

# Reproduction and limits

Run `python3 VERIFY.py` with Python 3 (standard library only). Successful execution prints `POLYNOMIAL_IDENTITIES_OK` and `ENDPOINT_ACTION_ALGEBRA_OK`. The checker performs exact polynomial-coefficient operations with rational numbers, not sampled floating-point tests. It verifies the global polynomial drift formula, the energy drift formula, and the endpoint action algebra.

The uniqueness of the bounded heteroclinic on each positive leaf is proved analytically using the planar reduction, the strict energy inequality, the saddle's one-dimensional unstable manifold, confinement on the left branch, and the impossibility of a bounded right branch. The script does not certify these infinite-time dynamical conclusions independently. No numerical trajectory is used as evidence for an infinite-time claim. The historical search may miss algebraically equivalent or unindexed results. Independent audit is not yet performed.
