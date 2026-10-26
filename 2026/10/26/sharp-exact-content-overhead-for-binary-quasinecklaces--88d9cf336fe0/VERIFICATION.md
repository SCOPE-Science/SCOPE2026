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

The universal proof is contained in `RESULT.md`. Running `python3 verify.py` checks the binary characterization against direct defining conditions, the two exact counts against brute enumeration, the orbit-multiplicity rule, and representative asymptotic ratios. Observed output:

```text
ALL_LENGTHS_THROUGH_15_OK 135
FIXED_Z 1 R 3000 RATIO 1.000000000
FIXED_Z 2 R 3000 RATIO 1.998667555
FIXED_Z 3 R 3000 RATIO 2.996002667
FIXED_Z 4 R 3000 RATIO 3.988023966
FIXED_Z 5 R 3000 RATIO 4.973428653
FIXED_Z 6 R 3000 RATIO 5.950269007
FIXED_Z 7 R 3000 RATIO 6.916631450
CYCLIC_ORBIT_COUNTS_OK 2587
VERIFY_OK
```

The finite experiment is not an infinite certificate. The asymptotic statement comes from bounded-composition polynomial degrees and Burnside's formula. The runtime-dependent output is reproducible with Python 3 standard library only. Independent audit was not performed.
