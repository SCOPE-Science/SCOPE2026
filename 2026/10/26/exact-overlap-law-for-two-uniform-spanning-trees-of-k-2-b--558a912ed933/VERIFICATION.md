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

The accompanying `verify.py` reconstructs all spanning trees by the bridge-spoke bijection and enumerates all ordered pairs for each \(2\le b\le6\). It checks the overlap support, every probability using rational arithmetic, the exact mean and variance, and the total-variation identity. Run `python3 verify.py` with the Python standard library. The captured output is `verification_output.txt`.

The complete all-integer argument is proved in `RESULT.md`; finite checks are corroborative rather than an infinite certificate. A later revision of the primary comparison paper was accessible at abstract level but not as full text, so historical-priority verification is incomplete. No independent audit was performed.
