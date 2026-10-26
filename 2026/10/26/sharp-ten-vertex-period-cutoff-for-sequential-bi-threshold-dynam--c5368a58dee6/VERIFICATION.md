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

# Reproducible finite verification

Execute `python3 verify.py` from a directory containing that file; there are no optional libraries and no input data. The script constructs unlabelled trees recursively, reduces by complete center-rooted canonical codes, computes every state transition, and reports the entire periodic-orbit census through ten vertices. The output terminates in `VERIFY_OK` only after exact assertions on the known tree counts and computed maxima, the uniqueness and multiplicity of the ten-vertex extremizer, and all transitions of one exhibited orbit. The mathematical explanation of why this is exhaustive appears in `RESULT.md`.

Observed maximal periods by order were \((1,1,1,1,2,3,6,10,14,22)\). The last class consists of 106 distinct tree shapes, of which exactly one has primitive length \(22\), and its multiplicity is two. Separately implemented tree enumeration and orbit counting produced the same maxima and multiplicities.

This verification is an exact finite exhaustion, not an assertion about trees above ten vertices. The update-order reduction is attributed to the existing tree cycle-equivalence theorem and is not re-proved as a new theorem. No independent audit or external certification has been performed.
