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

The proof is symbolic and does not depend on floating-point computation. The bundled `verify_lemoine_defect.py` performs deterministic Cartesian checks on several nondegenerate triangles and a grid of side parameters. It verifies the weighted normal equilibrium, the Lemoine barycentric coordinates, the exact defect decomposition, the pedal equality case, and the equilateral normalization.

The numerical replay is only a guard against algebraic or transcription mistakes. It is finite and therefore does not replace the universal proof. Historical originality likewise remains subject to the source-access limitations recorded in `AUDIT.json`.
