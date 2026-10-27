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

Run `python3 verify.py` using Python 3 and only its standard library. It independently constructs the fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_{11}\), directly computes multiplication and all idempotents for each tested weight vector, enumerates liftable cyclic rotations and their scalar choices, and compares predicted orbit classes against explicit finite-field isomorphism tests.

Covered configurations: all seven listed fields with \(1\le n\le3\), plus \(n=4\) in characteristics and field sizes \(q\in\{2,3,4,5,7\}\), for 26 configurations. This examines 3557 nonzero weighted coefficient vectors. The checker reports `ALL_CYCLIC_EVOLUTION_ARITHMETIC_CHECKS_PASSED 26 3557 32` when all assertions pass.

The calculation is exhaustive only for these cases; the universal isomorphism criterion, counting formula and joint distribution are established by the argument in RESULT.md. No independent audit has been carried out.
