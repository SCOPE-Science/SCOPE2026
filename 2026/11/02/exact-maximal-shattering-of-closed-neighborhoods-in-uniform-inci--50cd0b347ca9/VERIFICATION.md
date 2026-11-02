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

The standard-library Python program `verify_uniform_incidence_neighborhoods.py` builds literal closed-neighborhood incidence masks and counts exact Boolean traces, without using the asserted classification to determine whether a support is shattered.

Run:

```sh
python verify_uniform_incidence_neighborhoods.py
```

Observed tests:

- Every permitted rank for orders three through seven: exact maximum-support counts.
- All possible three-vertex supports for all these orders: independent trace computation against the structural criteria (36,582 tests).
- All supports one larger than the claimed dimension through order six: none shattered.
- Additional maximum-support counts at orders and ranks (8,3), (8,6), (9,2), (9,8).
- Exact version-space Littlestone recursion at rank two, orders three through eight.

The maximum-size census evaluates 256,813 support candidates across the tested cases. Terminal messages include `EXACT_SUPPORT_AND_TRIPLE_CENSUS_PASS`, `RANK_TWO_ONLINE_RECURRENCE_PASS`, and `ALL_UNIFORM_INCIDENCE_NEIGHBORHOOD_CHECKS_PASS`.

These are exact **finite** checks; none certifies an infinite parameter range. The universal proof in `RESULT.md` establishes the infinite statements by point/block incidence signatures, explicit witnesses, and the two-case online-tree argument. No formal proof assistant, external human audit, or independent certification has been used.
