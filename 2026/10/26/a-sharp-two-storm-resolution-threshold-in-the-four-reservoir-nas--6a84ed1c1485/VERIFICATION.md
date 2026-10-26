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

# Reproducibility and scope

Run `python3 VERIFY.py` from this directory. The program uses only the Python standard library, fixes its pseudorandom seed, evaluates the cubic/derivative identity and discriminant factorization at 1,500 inputs each, brackets the unique root using 50-digit decimal arithmetic, and checks representative mode counts.

Observed output:

```
critical_dimensionless_separation= 2.9588081482438789725439156947328446553820823364814
1500 identity checks; 1500 discriminant checks; 4 mode-count checks PASSED
```

The analytic uniqueness proof of the cutoff uses the strict sign of \(G'(s)\) for every \(s\in(2,3)\). Neither the finite numerical checks nor a plot certifies an infinite-domain assertion. There is no independent audit of this claim.
