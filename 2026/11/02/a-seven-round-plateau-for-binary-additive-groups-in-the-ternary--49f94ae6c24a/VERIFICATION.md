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

# Verification and limits

The included `verify_types.py` is an exact exhaustive enumerator of the row-space orbit recurrence. Run `python3 verify_types.py` and compare its complete stdout with `verify_types.out`; all exact partition assertions must pass, ending with `EXACT_ORBIT_RECURRENCE_OK`. The extension recurrence is justified by the linear-algebra orbit and projection lemmas in `RESULT.md`; the code alone does not establish those lemmas. `verify_direct.py` independently enumerates concrete tuples in groups of sizes two, four and eight and confirms the partitions through rank four; its complete stdout is `verify_direct.out`, ending in `DIRECT_VERIFY_OK`.

There is no experiment standing in for the infinite-dimensional step: the proof supplies the unconditional saturation argument for dimensions at least the number of rounds. Higher quantifier ranks, other primes, and independent scientific validation are outside the claim. No independent audit has been performed.
