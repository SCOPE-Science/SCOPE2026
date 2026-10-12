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

Run `python3 verify.py` beside `certificate.json`.

The first engine extends every surviving binary prefix by both letters. A newly created cube must be a suffix; a newly created complementary-pair violation must involve the new length-\(6\) suffix. The second engine independently rescans every candidate for every cube factor and reconstructs its complete set of length-\(6\) factors.

The two engines are required to produce identical complete survivor sets at every length through \(51\). They give exactly \(16\) survivors at length \(50\) and none at length \(51\).

For each of the \(16\) boundary words, the verifier additionally checks complementary-factor avoidance directly for every factor length from \(6\) through \(50\), then recomputes the four reversal/complement orbits.

The verification proves only this finite equality classification. Independent audit has not been performed.
