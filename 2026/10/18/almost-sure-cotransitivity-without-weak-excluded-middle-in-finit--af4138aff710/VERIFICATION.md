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

The exact theorem follows from the proof in `RESULT.md`. The supplementary `verify_apartness.py` computes Heyting implication as the greatest upset satisfying the residuation inequality and then checks every cotransitivity triple. It also computes negation and weak excluded middle directly. No specialized software or external data is used.

Run `python3 verify_apartness.py` with Python 3 in the directory containing the script. The actual verification execution yielded:

```
m=1 elements=3 triples=27 cotrans_fail=0 wem_fail=0
m=2 elements=5 triples=125 cotrans_fail=14 wem_fail=2
m=3 elements=9 triples=729 cotrans_fail=66 wem_fail=6
m=4 elements=17 triples=4913 cotrans_fail=266 wem_fail=14
m=5 elements=33 triples=35937 cotrans_fail=1050 wem_fail=30
m=6 elements=65 triples=274625 cotrans_fail=4154 wem_fail=62
m=7 elements=129 triples=2146689 cotrans_fail=16506 wem_fail=126
VERIFY_OK cases=7 triples=2463045 direct_implication=YES WEM=YES
```

The program is a finite boundary and implementation check, not a substitute for the arbitrary-size proof. No independent external validation or publication-priority certification has been performed.
