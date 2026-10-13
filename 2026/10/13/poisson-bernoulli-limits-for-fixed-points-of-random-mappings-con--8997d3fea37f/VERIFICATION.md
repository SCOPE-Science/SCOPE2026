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

The included `checker.py` needs only Python's standard library. Run `python checker.py` from the directory containing the supplied files. The expected final line is:

```
PASS: 278 exhaustive set-partition/injection cases; 1154 exact factorial-moment checks; 54 limit-profile moment comparisons
```

The enumerator lists all set partitions of domains up to six points and all injective assignments of their block targets. It calculates the count of fixed vertices directly from each assignment, then independently derives the factorial moments from the elementary symmetric polynomial of block sizes, checking exact equality with rational arithmetic. Supplementary finite comparisons address one- and two-macroscopic-fibre regimes.

The checker does **not** establish the all-size convergence, completeness of profiles, uniqueness of the Poisson regime, or historical originality. Those require the analytic argument in `RESULT.md` and the source comparisons. Independent audit is not performed.
