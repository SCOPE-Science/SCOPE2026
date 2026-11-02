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

# Reproducibility and limits

Execute the embedded file `verify.py` with Python 3.11+ and no third-party libraries:

```sh
python verify.py
```

The program generates all idempotent set maps by choosing their fixed image points and freely assigning all remaining points to these roots. For each cycle-type representative on \(n\le8\), it then tests commutation \(f\sigma=\sigma f\) directly and accumulates exact image-rank counts. This procedure does not use the cycle-divisibility enumeration formula. It checks the closed polynomial, the minimum attainable rank and the size of its fiber, and the rank-refined average identity using permutation conjugacy-class weights. Run observations:

```
n=1 types=1 idempotents_tested_per_type=1 average_total=1 VERIFY_OK
n=2 types=2 idempotents_tested_per_type=3 average_total=2 VERIFY_OK
n=3 types=3 idempotents_tested_per_type=10 average_total=3 VERIFY_OK
n=4 types=5 idempotents_tested_per_type=41 average_total=5 VERIFY_OK
n=5 types=7 idempotents_tested_per_type=196 average_total=7 VERIFY_OK
n=6 types=11 idempotents_tested_per_type=1057 average_total=11 VERIFY_OK
n=7 types=15 idempotents_tested_per_type=6322 average_total=15 VERIFY_OK
n=8 types=22 idempotents_tested_per_type=41393 average_total=22 VERIFY_OK
ALL_VERIFY_OK
```

The terminal line is not an independent mathematical audit. Numerical verification is exhaustive only for these eight finite degrees. Unrestricted correctness follows from the mathematics in `RESULT.md`. No external expert check, formal proof assistant, or independent verification is claimed.
