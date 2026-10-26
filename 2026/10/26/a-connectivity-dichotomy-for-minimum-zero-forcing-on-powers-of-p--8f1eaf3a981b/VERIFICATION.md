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

Run `python3 verify.py` with Python 3.9 or later. The program has no third-party dependencies and constructs the base graphs directly from their definitions. For each of 35 path and 15 cycle parameter pairs it independently enumerates all potential minimum-size blue sets, compares simultaneous and sequential forcing rules, and verifies agreement with the stated set families. It then builds the full minimum-set token-jumping graph and checks its vertex count, component decomposition, and, within scope, cycle edge count. Additional larger instances verify the closed formulas via the structural families.

Expected concluding output:

```text
PATH_EXHAUSTIVE_OK 35 parameter pairs, two independent forcing simulations
CYCLE_EXHAUSTIVE_OK 15 parameter pairs, two independent forcing simulations
k=2 n=20: path=4 states, components=[2, 2]; cycle=60 states, edges=180, components=1 STRUCTURAL_OK
k=3 n=25: path=6 states, components=[3, 3]; cycle=125 states, edges=500, components=1 STRUCTURAL_OK
k=4 n=30: path=8 states, components=[4, 4]; cycle=210 states, edges=1050, components=1 STRUCTURAL_OK
k=5 n=35: path=10 states, components=[5, 5]; cycle=315 states, edges=1890, components=1 STRUCTURAL_OK
k=6 n=40: path=12 states, components=[6, 6]; cycle=440 states, edges=3080, components=1 STRUCTURAL_OK
k=7 n=45: path=14 states, components=[7, 7]; cycle=585 states, edges=4680, components=1 STRUCTURAL_OK
ALL_VERIFY_OK
```

These finite computations cannot certify an infinite claim by themselves. The all-parameter proof in RESULT.md is the basis of correctness. No external audit or external formal proof certification has been performed.
