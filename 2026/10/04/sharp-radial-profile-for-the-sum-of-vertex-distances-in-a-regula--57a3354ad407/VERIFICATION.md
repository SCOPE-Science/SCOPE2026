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

The universal claim is established analytically in `RESULT.md`. The finite checker `verify.py` is supplementary. It verifies the tetrahedral frame relations and direction reconstruction, checks both endpoint formulas on the extremal rays, and samples deterministic random directions on a radius grid spanning several orders of magnitude.

Finite floating-point sampling cannot certify the continuum of directions or radii. Those quantifiers come from the proof's critical-point classification, compactness, continuity, and connectedness.

Actual deterministic replay output:

```text
VERIFY_OK
checks=23496
frame_error=4.441e-16
reconstruction_error=1.110e-15
max_bound_violation=8.882e-16
endpoint_error=1.776e-15
```
