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

Engine 1 generates all ternary prefixes whose factors have exponent at most \(\frac{20}{11}\) by testing every candidate period of each newly created suffix. Engine 2 independently computes the least period of each newly created suffix and applies the same exact integer threshold. The complete level sets must agree, ending with \(3042\) candidates at length \(22\).

All \(3042\) candidates are filtered by an exact doubled-word scan for circular factors above \(\frac{20}{11}\). Every one of the \(132\) survivors is then independently rescanned factor-by-factor over all rotations to confirm exact critical exponent \(\frac{20}{11}\). The verifier confirms six rotation classes, one orbit under alphabet permutations and reversal, and explicit critical factors of length \(20\) and period \(11\) in every stored representative.

The verification is finite and establishes only the stated length-\(22\) result. Independent audit has not been performed.
