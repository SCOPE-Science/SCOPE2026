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

The proof uses an exact conditional identity and explicit monotonicity and asymptotic arguments. To reproduce the finite checks, run `python3 verify.py` with Python 3 standard library only. Observed output:

```text
PASS: 159 exact finite graph-case/threshold groups
PASS: 16 additional asymptotic/root checks
```

Checks independently sum exact rational probabilities of labelled graphs on four and five vertices (including nonuniform motif weights), then verify a number of threshold inequalities and asymptotic approximations. These are finite and numerical cross-checks; the proof of the all-\(n\) and all-\(p\) conclusions is in `RESULT.md`. Historical priority is provisional, notably because the complete older orthogonal-decomposition monograph could not be inspected. No independent audit has occurred.
