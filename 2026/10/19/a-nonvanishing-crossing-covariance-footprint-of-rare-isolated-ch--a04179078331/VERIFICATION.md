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

The standard-library program `chord_cov_verify.py` independently enumerates \(146598\) perfect matchings with \(n=2,\ldots,7\), calculates exact rational expectations and covariances directly from pairing definitions, and checks against the mathematical identities. It passed all six sample sizes. General validity relies on the written conditioning proof, not finite enumeration. The large-\(n\) remainder bounds follow from the exact weight ratio and symmetric geometric tails; numerical testing does not prove the asymptotics. No independent audit has been performed.
