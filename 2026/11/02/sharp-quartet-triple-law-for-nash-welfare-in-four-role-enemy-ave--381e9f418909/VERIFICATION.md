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

# Verification of the exact Nash-welfare claim

Run `python verify.py` with Python 3 and no third-party dependencies. The checked embedded script reported:

```
Optimal Nash products: PASS 730 ordered role-size profiles (n<=24)
Labeled optimal-partition counts: PASS 30 role-size profiles (n<=9)
Havel-Hakimi realizations: PASS 2000 seeded large profiles
Boundary and strict-exchange checks: PASS
```

One test enumerates all role-compatible non-singleton coalition arrangements by recursion on remaining class counts. A separate test enumerates labeled coalitions using bit masks and compares both the maximizing product and its multiplicity against coefficient extraction. A constructive incidence-matrix routine checks feasibility on seeded larger instances. All arithmetic is integral and the random seed is fixed. Proof of the infinite assertion requires the Gale–Ryser argument and the strict spectrum exchanges in `RESULT.md`, not these finite tests. Source originality is qualified and has not received independent scientific validation.
