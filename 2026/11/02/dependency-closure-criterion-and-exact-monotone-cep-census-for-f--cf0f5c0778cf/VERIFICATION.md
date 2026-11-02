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

Run the bundled `checker.py` with any Python 3.10+ interpreter: `python3 checker.py`. No third-party package, downloaded data, or network access is required. The script completely enumerates all \(20^3=8{,}000\) monotone unary operators on the eight-element Boolean algebra, checks CEP by independent direct congruence and graph/partition methods for every operator, and checks a seeded random selection of 500 additional unrestricted maps for consistency of the general decision methods.

The verified output is:

```text
MONOTONE_TOTAL 8000
CEP_PASS 5249
CEP_FAIL 2751
NORMAL_PASS_FAIL 4273 2586
NONADDITIVE_CEP 4520
ORBIT_TOTAL_FAIL 1440 492
FIXED_ALL (8000, 200, 200, 20, 20, 200)
FIXED_FAIL (2751, 65, 65, 3, 3, 65)
ALL_CHECKS_OK
```

The code enumerates all six Boolean atom permutations and independently checks orbit canonicalization against the Burnside fixed-point counts. It also checks the separate known \(45\)-closure-operator and \(13\)-failure totals. The universal finite-carrier graph theorem is proved in RESULT.md; finite tests do not establish universality. Historical priority has not been independently established. Independent audit has not been performed.
