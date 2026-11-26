---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification and scope

The proof in `RESULT.md` is an exact substitution and sign comparison at two points, followed by the lift-iterate identity. It proves locking for both signs of the perturbation, not just the vanishing of a low-order drift coefficient. The unchanged accompanying `verify.py` includes finite numerical checks of the endpoint identity and half-translation conjugacy (lines 41–48), as well as diagnostics outside the stated endpoint claim. These diagnostics are not a proof of the endpoint theorem or a certification of rotation numbers from finite iterates.
