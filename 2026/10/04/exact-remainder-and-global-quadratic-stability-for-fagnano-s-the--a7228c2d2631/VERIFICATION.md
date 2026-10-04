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

The universal proof is symbolic. The bundled `verify_fagnano_defect.py` checks the exact remainder and both stability inequalities on deterministic grids for several acute triangles and on 5000 seeded random acute triangles. It also verifies that the orthic side coordinates give zero deficit.

Replay output:

`PASS`

`worst exact identity error = 6.661e-15`

`minimum stability margin Q/(2D) = 1.509e-04`

`minimum weighted-coordinate stability margin = 1.509e-04`

These are finite numerical checks used only to detect algebraic or transcription errors; they are not a proof of the universal statement. Historical originality remains subject to the access risks recorded in `AUDIT.json`.
