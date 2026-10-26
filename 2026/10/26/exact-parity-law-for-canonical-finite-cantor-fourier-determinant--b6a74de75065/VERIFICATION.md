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

The finite checker `verify.py` was executed with Python 3 using only the standard library. It computed log absolute determinants by complex Gaussian elimination for 35 base-depth combinations and verified 54 corresponding parity identities. The recorded result was `VERIFY_OK direct_determinants=35 parity_block_checks=54`.

The analytic proof, not the finite experiments, establishes all integer bases and all depths. The numerical tests use floating-point arithmetic, so they cannot establish exact identities by themselves. No independent audit was performed.
