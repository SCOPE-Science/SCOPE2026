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
The symbolic proof establishes the all-parameter statement. `artifacts/verify.py` independently reconstructs neighborhood complexes from common-neighbor sets, checks the exact cone decomposition on three base graphs, and computes mod-two homology for ten small \(K_r\vee(nK_m)\) examples. Replaying the packaged script must print `VERIFY_OK cone_identity_examples=3 clique_windmill_cases=10`.

The finite calculations do not certify cases beyond those enumerated and are not used to infer the theorem. No equivariant or simple-homotopy computation is claimed.
