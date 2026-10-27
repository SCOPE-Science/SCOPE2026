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

# Reproduction and scope

Run `python successor_run_checker.py` using a Python standard-library installation. The observed output is:

```text
SUCCESSOR_RUN_EXACT_OK 184884 588 [9120, 4392, 144, 168]
```

The program exhaustively compares all second permutations for every length from three through eight and each tested edge length, checks both exact first and binomial-second moments as rational equalities, checks independence-input invariance across reference permutations, and enumerates all triples of permutations on four labels for the two-edge indicator. The numbers are diagnostics, not complete formal certificates for arbitrary n. Infinite-domain asymptotics, Poisson approximation, the supercritical regime and overlap isolation are proved mathematically in `RESULT.md` and do not follow from finite enumeration.

Independent audit has not been performed.
