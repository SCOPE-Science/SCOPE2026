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

Run `python3 checker.py` in a directory containing the packaged checker. Its Python standard-library implementation separately evaluates the constructive \(\Box\) and \(\Diamond\) clauses for all persistent truth sets and computes the threshold sequences. The exact local-family enumeration covers all nonempty families of nonempty subsets through four elements. Complete raw-frame enumeration occurs for one and two worlds; larger raw frames are tested by deterministic pseudorandom sampling (30,000 at three worlds; 8,000 at four). Every monotone sequence pair through four worlds is enumerated, its canonical raw realization is tested, and the exact N+P and D-valid counts are checked against the displayed binomial formulas. The disjoint-neighbourhood D-valid boundary example is checked.

Observed program output:

```
n=1 row_families=1 frames_tested=1 NP_types=1 NPD_types=1
n=2 row_families=7 frames_tested=49 NP_types=9 NPD_types=6
n=3 row_families=127 frames_tested=30000 NP_types=100 NPD_types=50
n=4 row_families=32767 frames_tested=8000 NP_types=1225 NPD_types=490
ALL_CHECKS_OK
```

This finite test does not constitute an exhaustive check of all raw frames for \(n\ge3\), or an independent proof for arbitrary \(n\). The unrestricted proof uses exact threshold equivalences and the classical two-row Jacobi--Trudi count. No external independent audit has been performed.
