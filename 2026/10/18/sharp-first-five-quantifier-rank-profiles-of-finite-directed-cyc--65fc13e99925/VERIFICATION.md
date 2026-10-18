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

The recurrence in `verify_cycle_types.py` matches the complete finite-rank Ehrenfeucht--Fraïssé back-and-forth relation: each tuple records its full atomic diagram and the **set** of all possible one-point extension types. Global exact interning gives cross-model comparability, while rotation by any vertex is an automorphism and justifies anchoring the first selected point at 0.

Run `python3 verify_cycle_types.py` from the directory containing the script. It checks every size 1 through 32 and ranks 1 through 5, asserting the precise singleton-plus-final-class partitions. `certificate.json` contains the successful result of that computation. This checks all finite cases necessary for the theorem; the infinite tail follows independently from the directed-gap invariant in RESULT.md.

The computation does not enumerate cycles larger than 32, does not decide all ranks, and does not constitute independent external audit. The program and its reproducible output support one stated theorem only.
