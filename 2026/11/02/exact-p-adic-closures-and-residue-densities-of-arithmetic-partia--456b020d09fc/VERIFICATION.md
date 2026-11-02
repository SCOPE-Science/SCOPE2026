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

# Verification evidence

Run `python3 verify.py` from the extracted package. The independent modular checker maintains the valuation and unit part of the derivative state modulo powers of the selected prime, and compares its complete finite state orbit with the theorem's independently constructed union of coset residues.

Actual successful execution: `{'checked_profiles': 6399, 'total_attained_residue_instances': 8480, 'nontrivial_cycle_examples': {2: (4, [4, 5], 5), 3: (9, [9, 10], 10), 5: (25, [25, 26], 26), 7: (49, [49, 50], 50)}, 'cycles_examined': 187, 'status': 'PASS'}`.

This is a finite sanity test, not a proof of the universal claim. The exact arithmetic lifting and orbit decomposition are proved in RESULT.md, using the externally established eventual valuation-periodicity theorem. Independent audit has not been performed.
