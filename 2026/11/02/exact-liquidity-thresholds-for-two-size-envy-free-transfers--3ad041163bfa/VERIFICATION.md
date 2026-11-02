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

The checker `verify.py` computes the proposed feasibility conditions with exact rational arithmetic and independently enumerates every final load vector obtained by distributing all goods in the test profiles. It validates the constructive large-first/unit-second allocation, internal budget balance, all pairwise envy inequalities and individual payment limits. It also tests a boundary profile in which the unit-good assumption is removed.

Executed with Python 3, exit status 0:

```
VERIFY_OK cases= 40800 load_vectors_checked= 5069616 constructive_allocations= 26145
BOUNDARY_OK 2+2+2+3 / capacities 3,3,3
```

The finite parameter suite uses `n` from 1 through 4, `r` from 2 through 5, item multiplicities from 0 through 5 with combined count at most 7, and independent budgets in `{0,1/3,1,2}`. This is not exhaustive over all real budgets or arbitrarily large numbers. The general conclusion follows from the analytic proof in `RESULT.md`, not from these finite checks. No independent assessment has been performed.
