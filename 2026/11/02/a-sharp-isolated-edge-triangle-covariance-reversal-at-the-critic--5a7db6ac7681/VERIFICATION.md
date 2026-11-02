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

Run `python3 verify.py` with Python 3 and no third-party packages. The executable enumerates all 1,024 labeled simple graphs of order five and 32,768 of order six, compares the exact conditional-expectation covariance formula to direct sample covariance at every edge count, checks two independent-edge density identities, and checks the algebraic threshold formula plus adjacent-integer bounds for orders five through 104. The observed output is:

```
n=5: 1024 graphs, 11 exact covariance identities
n=6: 32768 graphs, 16 exact covariance identities
PASS: all exact finite checks, including 327 identity/inequality assertions
```

Exhaustive small-order checks are a regression test, not a proof of general correctness or uniqueness. The infinite identity and sparse asymptotics are established by the analytic argument in RESULT.md. Exact primary-literature priority outside the inspected material remains unresolved. No independent audit has been performed.
