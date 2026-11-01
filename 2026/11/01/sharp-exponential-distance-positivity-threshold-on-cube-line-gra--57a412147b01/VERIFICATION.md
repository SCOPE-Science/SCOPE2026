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

The embedded `verify.py` runs without third-party libraries. It constructs the cube line graph from edge-endpoint intersections, computes its distance matrix by independent breadth-first searches and verifies every displayed pairwise distance for dimensions 2–5.

For three exact rational kernel parameters, it verifies the full Walsh block action for every admissible frequency subset and direction. It checks the trace and squared-trace identities of the ordinary distance spectrum and exact rational intervals for the sharp root through dimension 14. The checker returned `EXACT_LINEGRAPH_KERNEL_SPECTRUM_OK 30368`.

The analytic proof, rather than enumeration, establishes the claims for all integer dimensions and all positive real kernel scales. No independent mathematical audit or external validation is asserted.
