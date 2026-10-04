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

The proof is analytic. The exact finite identity follows from a support-distance lower bound and a permutation-equivariant minimal repair coupling. The log-free upper bounds use only multinomial variances and Cauchy--Schwarz. The asymptotic coefficient uses the multivariate central limit theorem with coordinatewise uniform integrability. The quantum step uses single-system classical-to-quantum data processing for the quantum Wasserstein distance of order one; equality for orthogonal signals follows from recovery of classical Hamming-Wasserstein distance on diagonal states.

`artifacts/verify.py` solves several complete finite optimal-transport linear programs rather than testing only the proposed repair map. It checks binary and ternary type classes against the claimed exact formula, verifies the balanced-binary closed form, and verifies the stated finite bounds. These computations are finite corroboration only; they are not used to infer the all-blocklength theorem.

No independent audit has been performed.
