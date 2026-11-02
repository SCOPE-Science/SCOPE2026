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

The file `checker.py` is self-contained Python 3 standard-library code. Run it with `python checker.py` from a directory containing this file. It uses integer arithmetic throughout. It checks the original quantified definition of forward confluence against an independently stated structural criterion for every relation on six carriers of at most four worlds, and also counts their confluence instances. It independently sums admissible lower-source rows over upper-source rows for five further positive level-size pairs and compares against the closed formula. Finally it checks the exact rational relative-error inequality for all \(1\leq a,b\leq8\) by integer cross-multiplication.

The following outputs were obtained from the standalone packaged code before delivery:

```
BRUTE 1 1 11
BRUTE 1 2 185
BRUTE 2 1 281
BRUTE 1 3 10943
BRUTE 2 2 11401
BRUTE 3 1 33497
ROW_SUM 1 4 2547617
ROW_SUM 2 3 1252925
ROW_SUM 3 2 3771875
ROW_SUM 3 3 847519079
ROW_SUM 4 3 3223875731057
ALL_CHECKS_OK
```

These are bounded finite tests. They do not constitute an infinite proof. The proof in `RESULT.md` derives the exact formula and probability estimate for every positive \(a,b\), including all untested sizes. No independent audit has been performed.
