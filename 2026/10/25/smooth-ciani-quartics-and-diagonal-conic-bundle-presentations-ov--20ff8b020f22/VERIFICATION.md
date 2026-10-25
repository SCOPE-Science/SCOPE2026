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

The standalone `verify.py` uses only Python's standard library and directly counts the relevant finite-field parameter sets over prime fields. Running `python verify.py` yielded:

```text
basis 3 96 96 True
ciani 3 16 16 True
basis 5 6000 6000 True
ciani 5 800 800 True
basis 7 61824 61824 True
ciani 7 6624 6624 True
basis 11 1198560 1198560 True
F3_FIBERS_OK: 16 quartics, 48 forms each (24 projective presentations)
VERIFY_OK
```

The `basis` computation enumerates linearly independent triples of pairwise coprime squarefree projective binary quadratics. The independently structured `ciani` computation enumerates all scalar-normalized six-term coefficients and checks the necessary and sufficient nonsingularity conditions on their associated quadratic Gram forms. A further exhaustive raw nine-coefficient computation verifies the size of each presentation fiber over the smallest odd prime field. Exact finite enumeration is corroboration, not an infinite proof; the all-prime-power result relies on the involution count and the odd-dimensional similarity argument in `RESULT.md`. Neither mathematical originality nor independent validation is certified by this script.
