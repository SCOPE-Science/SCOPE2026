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

Run `python3 verify.py` with Python 3 and no external dependencies. It computes exactly all seven normalized odd-base modular residues, checks the even-base congruence and uses modular exponentiation and exact factorial division to verify 28 critical valuation witnesses for four parameter pairs. Actual verified output is:

```
CASE_OK 10 1 levels 9 initial_witnesses [(1, 7), (2, 13), (3, 25)]
CASE_OK 10 2 levels 7 initial_witnesses [(1, 7), (2, 13), (3, 25)]
CASE_OK 11 1 levels 7 initial_witnesses [(1, 7), (2, 13), (3, 25)]
CASE_OK 11 2 levels 5 initial_witnesses [(1, 7), (2, 13), (3, 25)]
CERTIFICATE_Q [(3, 573), (5, 415), (7, 374), (9, 1146), (11, 1355), (13, 1137), (15, 988)]
VERIFY_OK cases 4 total_levels 28
```

The unrestricted proof rests on the written 2-adic isometry, not on these examples. Independent mathematical audit is not yet performed.
