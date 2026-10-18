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

The exact algebraic proof is in `RESULT.md`. The separate standard-library script `verify.py` enumerates actual idempotents and their left-nested products and checks the full reachable/unreachable sets for eight representative finite-field quadratic forms (six ternary forms over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and two quaternary forms). The checker also verifies that each supposed generator is idempotent and that maximal shortest lengths are five or six as predicted.

For the exceptional \(81\)-element nonsplit ternary algebra over \(\mathbb F_3\), it independently evaluates the exact twelve-state transition quotient by signed permutations of coordinates, compares all ten reachable orbit types and their first-appearance lengths, and counts \(72\) reachable elements. The missing set consists of the scalar \(2\) and eight nonzero pure isotropic vectors.

Execute `python3 verify.py` with Python 3.8 or later. Observed output ends with `VERIFY_OK: finite-field BFS and exact exceptional orbit-transition certificate`. Computational checks are finite supplements, not evidence for all finite fields. The proof handles all field orders analytically. No external audit has occurred.
