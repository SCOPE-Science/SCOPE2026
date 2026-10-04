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

The exact verifier `verify.py` reconstructs the published cubic, differentiates it symbolically, checks direct gradient vanishing on both claimed strata, verifies the algebra used in the exhaustive Jacobian case split, computes the Hessian rank certificate on the secondary plane, and verifies the diagonal normal-slice kernel and cubic coefficient. It terminates with `VERIFY_OK` when all assertions pass.

The analytic identification of the transverse germs uses the standard holomorphic splitting lemma. The calculation is specific to this cubic over \(\mathbb C\); lower-dimensional collision strata inside the diagonal plane are left unclassified.
