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

# Reproduction and boundaries

Run `python3 verify.py` with the attached `enumerate.cpp`, `independent.cpp`, and `spectrum.json` in the same directory. A C++17 compiler `g++` is needed. This invokes two independently coded exhaustive enumerations, validates all minimum-span vectors, compares exact candidate counts, checks every witness directly, and verifies the unique downward jump at eight points.

Actual output observed from the standalone verifier:

```
VERIFY_OK independent_enumerations=2 total_scanned=5563258 first_drop=k8_at_32_to_33 universal_N_2_8=34
```

The largest class has \(\binom{34}{7}=5{,}379{,}616\) normalized sets, all examined exactly. The exhaustive search is a finite proof because every potential improvement to the certified minimum must occur within the explicitly searched bound, after translation. Neither numerical approximation nor inference from a nonexhaustive sample is used. The result is restricted to set cardinalities two through eight and does not establish independent external verification or literature-priority certification.
