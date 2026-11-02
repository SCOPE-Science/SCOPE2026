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

`python verify.py` uses only the Python standard library and compares exact rational multinomial enumerations to the binomial closed form for small dimensions and multiple tolerances. It additionally verifies the equal-leverage construction, stable-rank formula, all-row nonzeroness, arithmetic feasibility equivalence, explicitly forbidden and permitted sample counts, and the one-draw norm-sampler comparator. Recorded result: **PASS 9,371 exact-arithmetic checks**.

The reproducible script is included alongside the proof and has no network or external file dependencies. Its checks establish correctness of finite examples and implementation calculations, not the infinite theorem. The analytic proof covers every indicated dimension and sample budget. No independent audit has occurred.
