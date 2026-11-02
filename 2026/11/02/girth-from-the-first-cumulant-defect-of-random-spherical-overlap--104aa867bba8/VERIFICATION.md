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

# Reproducing the finite checks

Place `verify.py` beside this file and run:

```sh
python3 verify.py
```

The program uses only standard-library exact integer and rational arithmetic. It enumerates coordinate-index contractions in uniform spherical moments, then independently converts raw moments to cumulants. It checks 213 exact rational equalities in ambient dimensions 2, 3, and 4, eight finite graph families, short-cycle products up to length 7, a positively weighted triangle, and signed-weight cancellation. The accompanying `verification-output.txt` captures the actual output. These finite checks do not establish the all-graph theorem: the general proof is the leaf-elimination, cycle-integral, and joint-cumulant argument in `RESULT.md`. No separate external or independent audit was performed.
