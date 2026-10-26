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

## Reproducible checks

- The standalone script reconstructs the remaining \(252\times381\) integer jet matrix.
- Its deterministic elimination over \(\mathbb F_{101}\) gives rank \(240\); the selected \(240\times240\) minor has determinant \(9\pmod{101}\).
- The five coordinate-point conditions have rank \(620\), so the full interpolation rank is at least \(860\).
- The script also verifies that the tangent fifth-power and six chord fifth-powers at a point of a standard rational normal quartic are independent: a selected \(7\times7\) minor has determinant \(11\pmod{101}\). This certifies the required nonempty open condition for independence of the curve relation from the line relations.
- The geometric relations give the matching upper bound \(860\) on the generic rank.

The modular certificates and geometric argument are complementary: the script does not certify the general geometric lemma. Independent audit has not been performed.
