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

The exact checker `verify_chord_pentagon.py` uses only Python's standard library and confirms the integer polygon is strictly convex and all its side lengths are integers. It integrates first and second moments along each edge and over the interior using polygon cross products, with exact `Fraction` arithmetic. It checks the resulting ratio against the independently implemented cap-removal/edge-replacement formulas and confirms the exact positive difference above \(2\).

The derivative formula for all nondegenerate rhombi is established analytically in `RESULT.md` by a first-order perturbation of normalized boundary second moment and a second-order bound for the interior moment. The finite rational parameter checks in the checker are finite tests, not a proof for all angles. No independent validation is claimed.
