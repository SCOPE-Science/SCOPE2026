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

Running `python checker.py` from this package with Python 3 and SymPy 1.14.0 yielded:

```
PASS: polynomial identities, 28 high-seeding leading-term identities,
147 fully enumerated independent exact-rational epidemic expectations,
and two exact vaccine-allocation witnesses.
```

The checks reconstruct the stated expected-case identities, independently sum over directed edge configurations and initial seed subsets for all \(n\le3\) at 49 rational parameter pairs, and confirm the high-seeding coefficient for sizes 3–30. The proof of the continuum statement is analytic and appears in `RESULT.md`; checked finite values do not establish it by extrapolation. The model has not undergone independent audit or validation against epidemiological observations. Historical-priority verification is provisional because certain close household-allocation full texts were inaccessible.
