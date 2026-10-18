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

Run `python3 verify.py` (Python 3 standard library). The program checks the CRT density counts exactly over one whole residue period for a diverse finite collection of parameters, compares defect indicators to independent exact reduced-fraction evaluations, checks that later defects are absent in sampled rigid parameters, and supplies explicit third-index witnesses in forbidden classes.

Expected successful output:

```
Residue classes checked: 155065
Direct rational checks: 2280
Longer recurrence checks in rigid class: 13101
Forbidden-class third-index witnesses: 8
VERIFY_OK
```

These bounded checks do not establish the infinite claim. The proof in `RESULT.md` supplies the reductions, local root counts, CRT argument, and full all-index rigidity induction. There has been no independent audit.
