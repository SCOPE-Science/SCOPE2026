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

# Verification record

Run `python verify.py` with standard Python 3. The included program independently enumerates every attachment sequence with exact rational weights for two and three roots in the declared finite test ranges; checks normalization, color-size probabilities, marginal means, mixed size-leaf and leaf-leaf moments, negative quadrant inequalities and strict covariance signs; and checks the three exact scalar moment recurrences for multiple positive weights through time 40. The recorded completed execution returned `PASS assertions= 1001  attachment_histories= 14779`.

The theorem applies to all positive real root weights and arbitrary forest sizes; finite calculation alone does not establish those quantifiers. The written monotone couplings, moment inductions and Dirichlet-mixture argument supply unrestricted proof. No independent audit has been performed.
