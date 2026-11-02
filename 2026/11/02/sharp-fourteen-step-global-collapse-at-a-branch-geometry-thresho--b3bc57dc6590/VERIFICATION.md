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

# Reproduction

Run `python3 CHECK.py` with Python 3 standard library. The script exactly enumerates the nonempty sign-itinerary cells over the whole plane, computes their affine images using fractional vertices, and iterates the resulting convex polygons. It asserts the stage counts, singleton global fourteenth image, and explicit thirteenth-step witness. Every inequality uses exact rational arithmetic; this is not a floating-point grid test. The proof in RESULT.md supplies the recession-cone and homogeneous-nilpotence justifications that connect the finite computation to all real initial conditions.

The work has received self-review; independent scientific audit has not been performed.
