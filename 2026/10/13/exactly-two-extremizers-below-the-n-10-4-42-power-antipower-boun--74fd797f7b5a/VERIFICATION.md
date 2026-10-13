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

The first engine grows valid prefixes using only newly created suffixes. The second independently rescans every factor after every extension. Their complete levels through length \(42\) must agree.

The checker verifies the stored counts, exactly two length-\(41\) survivors, no length-\(42\) survivor, complement symmetry, palindromicity, and that both one-letter extensions of either extremizer are forbidden.

The scalar equality \(N(10,4)=42\) is published context and is independently reproduced only as a consistency check. Independent audit has not been performed.
